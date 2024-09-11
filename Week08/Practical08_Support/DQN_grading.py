import torch
import torch.nn as nn
import numpy as np
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class DQN(nn.Module):
    def __init__(self):
        super(DQN, self).__init__()
        self.layers = None
        
    def forward(self, x):
        return self.layers(x)
    
class DQNAgent(object):
    
    def __init__(self):

        self.action_value_net = DQN().to(device)
                     
    def obtain_action(self, state, action_space_dim, epsilon):
        with torch.no_grad():
            cur_q = self.action_value_net(torch.from_numpy(state).float().to(device))
        q_value, action = torch.max(cur_q, axis=0)
        action = action if torch.rand(1,).item() > epsilon else torch.randint(0, action_space_dim, (1,)).item()
        action = torch.tensor([action]).to(device)
        return action
    
    def get_next_q(self, state):
        return None
    
    def optimize(self, batch):
        return None
    
    def transfer_parameters(self):
        return None