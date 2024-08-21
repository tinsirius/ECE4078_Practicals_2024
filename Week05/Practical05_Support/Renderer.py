import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms
from ipywidgets import interact, widgets, Layout, Button, Box, VBox, IntSlider
import threading as thrd
import time

class Singleton:
    def __init__(self, cls):
        self._cls = cls

    def Instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._cls)

@Singleton
class Renderer(thrd.Thread):
    
    #Make singleton
    _instance = None
    
    def __init__(self):
        # Call the Thread class's init function
        thrd.Thread.__init__(self)

        
    def initialize(self, model_state, control_input, target_pose=np.zeros(3), dt_data=0.2):
        """
        Initialize renderer singleton
        :param model_state: Multidimensional array of dimensions 3 x T with sequence of T robot states (x, y, theta)
        :param control_input: Multidimensional array of dimensions 2 x T with sequence of T control inputs (v, w)
        :param target_pose: 3D vector that defines desired goal pose (x_d, y_d, theta_d)
        :param dt_data: Delta time
        """
        self.lock = thrd.Lock()

        self.initialized = False
        self.paused = False
        self.cur_frame = 0
        self.dt_data = dt_data
        self.dt_render = dt_data
        self.state = model_state
        
        if target_pose.shape[0] < 3:
            target_pose = np.hstack((target_pose, np.array([0])))
        
        self.target_pose = target_pose
        self.control_input = control_input
                
        # Initialize figure
        fig = plt.figure(constrained_layout=True, figsize=(14, 5))
        gs = fig.add_gridspec(2, 2)
        ax = fig.add_subplot(gs[:, 0])
        ax2 = fig.add_subplot(gs[0, 1])
        ax2.set_xlim([0, 3])
        ax2.set_ylim([np.min(self.control_input[:,0]), np.max(self.control_input[:,0])+1])
        ax2.set_title('Control - Linear Velocity')
        ax2.set_xlabel('Time')
        ax2.set_ylabel('m/s')
        ax3 = fig.add_subplot(gs[1, 1])
        ax3.set_title('Control - Angular Velocity')
        ax3.set_xlabel('Time')
        ax3.set_ylabel('radians/s')
        ax3.set_xlim([0, 3])
        ax3.set_ylim([np.min(self.control_input[:,1]), np.max(self.control_input[:,1])+1])

        ax.set_xlim([-2, 2])
        ax.set_ylim([-2, 2])
        ax.tick_params(axis='both', which='major', labelsize=7)
        ax.set_title('Overhead View')
        ax.set_xlabel('X (m)',weight='bold')
        ax.set_ylabel('Y (m)',weight='bold')

        self.figure = fig


        # Plot goal location
        self.goal_ax = []
        self.goal_ax.append(FancyArrowPatch((0,0), (0.3,0),
                                            mutation_scale=8,color='red'))
        self.goal_ax.append(FancyArrowPatch((0,0), (0,0.3),
                                            mutation_scale=8,color='green'))
        
        # Apply translation and rotation as specified by current robot state
        cos_theta, sin_theta = np.cos(self.target_pose[2]), np.sin(self.target_pose[2])
        Tw_r = np.eye(3)
        Tw_r[0:2,2] = self.target_pose[:2]
        Tw_r[0:2,0:2] = [[cos_theta,-sin_theta],[sin_theta,cos_theta]]
        Tw_r_obj = transforms.Affine2D(Tw_r)
        self.ax_trans = ax.transData
        self.goal_ax[0].set_transform(Tw_r_obj+self.ax_trans)
        self.goal_ax[1].set_transform(self.goal_ax[0].get_transform())
        ax.add_patch(self.goal_ax[0])
        ax.add_patch(self.goal_ax[1])

        
        # Plot current model state
        self.line, = ax.plot(self.state[0,0], self.state[0, 1], c='b', lw=1, label='Predicted state (model)')

        # Plot linear and angular velocities
        self.linear_v, = ax2.plot(0, self.control_input[0,0], c='g')
        self.angular_v, = ax3.plot(0, self.control_input[0,1], c='r')

        # Create Robot Axes 
        self.robot_ax = []
        self.robot_ax.append(FancyArrowPatch((0,0), (0.15,0),
                                            mutation_scale=8,color='red'))
        self.robot_ax.append(FancyArrowPatch((0,0), (0,0.15),
                                            mutation_scale=8,color='green'))
        
        # Apply translation and rotation as specified by current robot state
        cos_theta, sin_theta = np.cos(self.state[0,2]), np.sin(self.state[0,2])
        Tw_r = np.eye(3)
        Tw_r[0:2,2] = self.state[0,:2]
        Tw_r[0:2,0:2] = [[cos_theta,-sin_theta],[sin_theta,cos_theta]]
        Tw_r_obj = transforms.Affine2D(Tw_r)
        self.ax_trans = ax.transData
        self.robot_ax[0].set_transform(Tw_r_obj+self.ax_trans)
        self.robot_ax[1].set_transform(self.robot_ax[0].get_transform())
        ax.add_patch(self.robot_ax[0])
        ax.add_patch(self.robot_ax[1])

                
        btn_play = widgets.Button(description='Play/Pause', layout=Layout(flex='1 1 0%', width='auto'), button_style='success')
        btn_play.on_click(self.pause)
        
        btn_prev = widgets.Button(description='<<', layout=Layout(flex='0.3 1 0%', width='auto'), button_style='warning')
        btn_prev.on_click(self.prv)
        
        btn_next = widgets.Button(description='>>', layout=Layout(flex='0.3 1 0%', width='auto'), button_style='warning')
        btn_next.on_click(self.nxt)

        controls = [
            IntSlider(description='Frame: ', layout=Layout(flex='3 1 0%', width='auto'),min=0, max=(model_state.shape[0]-1)),
            btn_prev,
            btn_play,
            btn_next
         ]


        self.slider = controls[0]
        self.slider.observe(self.slider_change, names='value')
        
        box_layout = Layout(display='flex',
                            flex_flow='row',
                            align_items='stretch',
                            width='70%')
        display(Box(children=controls, layout=box_layout))
        
        if not self.is_alive():
            self.start()
            
        self.initialized = True
                            
    #Render Loop
    def run(self):
        while True:
            if self.paused == False:
                self.cur_frame = int(self.cur_frame + self.dt_render/self.dt_data)
                if self.cur_frame >= self.state.shape[0]:
                    self.cur_frame = 0
                if self.initialized == True:
                    self.render()
            time.sleep(0.05)

            
    def render(self):
        self.lock.acquire()
        self.figure.canvas.draw_idle()

        self.line.set_data(self.state[0:self.cur_frame,0],self.state[0:self.cur_frame,1])
        self.slider.value = self.cur_frame
        
        # Update robot position
        c, s = np.cos(self.state[self.cur_frame,2]), np.sin(self.state[self.cur_frame,2])
        Tw_r = np.eye(3)
        Tw_r[0:2,2] = [self.state[self.cur_frame,0],self.state[self.cur_frame,1]]
        Tw_r[0:2,0:2] = [[c,-s],[s,c]]
        Tw_r_obj = transforms.Affine2D(Tw_r)
        self.robot_ax[0].set_transform(Tw_r_obj+self.ax_trans)
        self.robot_ax[1].set_transform(self.robot_ax[0].get_transform())

        #Render position error
        t = np.arange(self.state[0:self.cur_frame].shape[0]) * self.dt_data

        self.linear_v.set_data(t, self.control_input[0:self.cur_frame, 0])
        self.angular_v.set_data(t, self.control_input[0:self.cur_frame, 1])
                   
        self.lock.release()
        
    def pause(self,b=None):
        self.paused = not self.paused
    
    def prv(self,b=None):
        self.paused = True
        self.cur_frame = int(self.cur_frame-1)
        self.slider.value = self.cur_frame
        if self.cur_frame < 0:
            self.cur_frame = 0
        self.render()
    
    def nxt(self,b=None):
        self.paused = True
        self.cur_frame = int(self.cur_frame + 1)
        self.slider.value = self.cur_frame
        if self.cur_frame >= self.state.shape[0]:
            self.cur_frame = self.state.shape[0]-1
        self.render()
    
    def slider_change(self,change):
        if self.paused == True:
            self.cur_frame = change['new']
            self.render()