import numpy as np
import ipywidgets as widgets
import threading as thrd
import time
import meshcat
import meshcat.geometry as g
import meshcat.transformations as tf
from meshcat.animation import Animation

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import matplotlib.transforms as transforms
from matplotlib.lines import Line2D
from IPython.display import display

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
        
    def initialize(self, vis, bot, dt=0.02, max_iterations=60, realtime = False):
        self.lock = thrd.Lock()
        self.bot = bot
        self.initialized = False
        self.paused = True
        self.max_cycles = max_iterations
        self.dt = dt
        self.cur_frame = 0
        self.realtime = realtime
        self.finished_cycle = False
        self.vis = vis
        self.anim = Animation()
        
    def show_control_panel(self):
        self.btn_play = widgets.Button(
            description='Play/Pause', 
            layout=widgets.Layout(flex='1 1 0%', width='auto'), 
            button_style='success')
        
        self.btn_play.on_click(self.pause)
        
        self.btn_reset = widgets.Button(
            description='Reset', 
            layout=widgets.Layout(flex='1 1 0%', width='auto'), 
            button_style='success')

        self.frame_counter = widgets.IntText(
            description='Frame',
            layout=widgets.Layout(width='150px', height='80px'),
            disabled=True)

        self.btn_reset.on_click(self.reset)
              
        controls = widgets.HBox([self.btn_play, self.btn_reset, self.frame_counter])
                    
        display(controls)
        
    def spawn_robot(self):
        self.vis["bot"].set_object(g.triad(1))
#         (x, y, theta) = self.bot.get_state()
#         self.vis["bot"].set_transform(tf.translation_matrix([x, y, 0]) 
#                       @ tf.rotation_matrix(theta, [0, 0, 1]))
        self.render()
        
    def start_render_loop(self):
        if not self.is_alive():
            self.start()          
        self.initialized = True

    #Render Loop
    def run(self):
        while True:
            if self.paused == False:
                self.bot.drive(self.dt)
                
                # Determine frame to plot
                self.cur_frame += 1
                if self.cur_frame >= self.max_cycles:
                    self.pause()
                    self.finished_cycle = True
                    self.render()
                    self.frame_counter.value = self.cur_frame
                    self.vis.set_animation(self.anim, play = False)
                if self.initialized == True:
                    self.render()
                    self.frame_counter.value = self.cur_frame
            if self.realtime:
                time.sleep(self.dt)
            else:
                time.sleep(0.2)

            
    def render(self):
        self.lock.acquire()
        
        (x, y, theta) = self.bot.get_state()
        self.vis["bot"].set_transform(tf.translation_matrix([x, y, 0]) 
                                 @ tf.rotation_matrix(theta, [0, 0, 1]))
        self.anim.at_frame(self.vis, self.cur_frame)["bot"].set_transform(
            tf.translation_matrix([x, y, 0]) 
            @ tf.rotation_matrix(theta, [0, 0, 1]))

        trail = np.array(self.bot.states).transpose()
        trail[2, :] = np.zeros(len(trail[2, :]))
        self.vis["trail"].set_object(
            g.Line(g.PointsGeometry(trail), 
            g.LineBasicMaterial(color=0x0000ff)))

                        
        self.lock.release()
        
    def pause(self,b=None):
        if not self.finished_cycle:
            self.paused = not self.paused
        
    def reset(self, b=None):
        self.paused = True
        self.bot.reset()
        self.cur_frame = 0 
        self.spawn_robot()
        self.render()
        self.frame_counter.value = self.cur_frame
        self.finished_cycle = False
        self.anim = Animation()
        
class bot2D():
    def __init__(self):
        # Configuration of 2D robot in world frame, x,y = coordinates in world frame, theta=orientation
        self.x = 0
        self.y = 0
        self.theta = 0
        self.states = []
        
    def reset(self):
        first_state = self.states[0]
        self.x, self.y, self.theta = first_state
        del self.states[:]
        self.states = [first_state]
        
    def get_state(self):
        """Return the current bicycle state. The state is in (x,y,theta) format"""
        return (self.x, self.y, self.theta)
    
    def set_state(self,x=0,y=0,theta=0):
        """Sets the model new state"""
        self.x = x
        self.y = y
        self.theta = theta
        self.states.append([x, y, theta])
        
class traj_bot(bot2D):
    def __init__(self, traj):
        super().__init__()
        self.traj = traj
        self.counter = 0
        self.set_state(traj[0,0], traj[0,1], traj[0,2])
    
    def drive(self, dt):
        [next_x, next_y, next_theta] = self.traj[self.counter]
        self.counter += 1
        self.set_state(next_x, next_y, next_theta)
        
    def reset(self):
        super().reset()
        self.counter = 0

def display_traj(vis, trj, scale = 6):
    if trj.shape[1] != 3:
        print("ERROR: we are expecting trajectory of x, y and theta only")
        return
    else:
        bike = traj_bot(trj)
        rend = Renderer.Instance()
        rend.initialize(vis, bike, dt=1.0/30, max_iterations=trj.shape[0], realtime = True)
        rend.spawn_robot()
        rend.show_control_panel()
        rend.start_render_loop()
        
def display_bicycle_wheels(rear_wheel, front_wheel, theta):               
    # Initialize figure
    fig = plt.figure(figsize=(5, 5))
    ax = plt.gca()
    ax.set_xlim([0,4])
    ax.set_ylim([0,4])
    ax.tick_params(axis='both', which='major', labelsize=7)
    plt.title('Overhead View')
    plt.xlabel('X (m)',weight='bold')
    plt.ylabel('Y (m)',weight='bold')

    ax.plot(0,0)
  
    rear_wheel_x = FancyArrowPatch((0,0), (0.4,0),
                                        mutation_scale=8,color='red')
    rear_wheel_y = FancyArrowPatch((0,0), (0,0.4),
                                        mutation_scale=8,color='red')

    front_wheel_x = FancyArrowPatch((0,0), (0.4,0),
                                        mutation_scale=8,color='blue') 
    front_wheel_y = FancyArrowPatch((0,0), (0,0.4),
                                        mutation_scale=8,color='blue')

    custom_lines = [Line2D([0], [0], color='red', lw=4),
                    Line2D([0], [0], color='blue', lw=4)]
    
    # Apply translation and rotation as specified by current robot state
    cos_theta, sin_theta = np.cos(theta), np.sin(theta)
    Tw_rear = np.eye(3)
    Tw_rear[0:2,2] = rear_wheel
    Tw_rear[0:2,0:2] = [[cos_theta,-sin_theta],[sin_theta,cos_theta]]
    Tw_rear_obj = transforms.Affine2D(Tw_rear)

    Tw_front = np.eye(3)
    Tw_front[0:2,2] = front_wheel
    Tw_front[0:2,0:2] = [[cos_theta,-sin_theta],[sin_theta,cos_theta]]
    Tw_front_obj = transforms.Affine2D(Tw_front)

    ax_trans = ax.transData
    
    rear_wheel_x.set_transform(Tw_rear_obj+ax_trans)
    rear_wheel_y.set_transform(rear_wheel_x.get_transform())
    ax.add_patch(rear_wheel_x)
    ax.add_patch(rear_wheel_y)

    front_wheel_x.set_transform(Tw_front_obj+ax_trans)
    front_wheel_y.set_transform(front_wheel_x.get_transform())
    ax.add_patch(front_wheel_x)
    ax.add_patch(front_wheel_y)

    ax.legend(custom_lines, ['Rear Wheel', 'Front Wheel']) 
