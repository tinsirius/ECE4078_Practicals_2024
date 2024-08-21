import numpy as np

class PenguinPi(object):

    """Implementation of a differential drive robot

    """
    
    def __init__(self, init_state=np.zeros(3), max_v=20, max_omega=np.pi):

        """
        Initialize a new PenguinPi robot
        :param init_state: Initial state of the robot
        :param max_omega: Maximum angular velocity that can applied to the robot
        :param max_v: Maximum linear velocity that can applied to the robot
        """
        
        # Robot state
        self.x = init_state[0]
        self.y = init_state[1]
        self.theta = init_state[2]
                        
        # Control input bounds
        self.max_linear_velocity = max_v
        self.max_angular_velocity = max_omega
                                 
    def drive(self, v=0, omega=0, dt=0.02):
        """
        Update the PenguiPi state
        :param v: Linear velocity (m/s)
        :param omega: Angular velocity (radians/s)
        :param dt: Delta time, i.e., time elapse since last state update
        """        
        
        # Set control signals within admisible bounds
        v = np.clip(v, -self.max_linear_velocity, self.max_linear_velocity)
        omega = np.clip(omega, -self.max_angular_velocity, self.max_angular_velocity)


        if omega == 0:
            next_x = self.x + np.cos(self.theta)*v*dt
            next_y = self.y + np.sin(self.theta)*v*dt
            next_theta = self.theta
        else:
            R = v / omega
            next_theta = self.theta + omega*dt
            next_theta = (next_theta + np.pi) % (2 * np.pi) - np.pi # clamp theta to [-pi, pi]
            next_x = self.x + R * (-np.sin(self.theta) + np.sin(next_theta))
            next_y = self.y + R * (np.cos(self.theta) - np.cos(next_theta))
       
        # Make next state our current state
        self.set_state(next_x, next_y, next_theta)        
        
           
    def reset(self):
        """
        Set robot state back to zero
        """
        self.x, self.y, self.theta = 0, 0, 0
    
    def get_state(self):
        """Return the current robot state. The state is in (x,y,theta) format"""
        return np.array([self.x, self.y, self.theta])
    
    def set_state(self,x=0,y=0,theta=0):
        """Define the new model state"""
        self.x = x
        self.y = y
        self.theta = theta


class Robot1D(object):

    """
    A simple implementation of a 1D robot in state-space form
    The constant MAX_CONTROL bounds the magnitude of the control signal that can be applied to the robot 
    """

    MAX_CONTROL = 500
    
    def __init__(self, A=np.eye(2), B=np.array([[0],[0]]), C=np.array([0, 0]), initial_state=np.array([[10],[0]])):
        
        """
        Initialize a new model. 
        :param A: nxn state matrix, where n = state dimensionality
        :param B: nx1 input matrix, where n = state dimensionality
        :param C: 1xn input matrix, where n = state dimensionality
        :param initial_state: 2x1 vector with the initial state of our system
        """
        self.A = A
        self.B = B
        self.C = C
        self.state = initial_state
                
    def drive(self, control_u=10):
        """
        Update the system's state given a new control input
        :param control_u: Control input
        """
        # Make sure control signal is within -MAX_CONTROL < control_u < MAX_CONTROL
        clip_control = np.clip(control_u, -self.MAX_CONTROL, self.MAX_CONTROL)
        state_t1 = self.A @ self.state + self.B * clip_control
        self.state = state_t1
            
    def get_state(self):
        """
        Get the system's current state
        """
        return self.state
    
    def get_output(self):
        """
        Get the system's ouput (position of the robot along the 1D line)
        """
        return np.array(self.C @ self.state)
                
    def get_error(self, desired_x):
        """
        This method measures the error (scalar) between the current robot's state and the desired state
        :param desired_x: Desired state (i.e., position) on the 1D line
        """
        return np.array(desired_x - self.state)