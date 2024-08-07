import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import time


def generate_measurements(steps=20, a=1, b=1, u=20, c=1, true_move_noise=2, true_mes_noise=10):

	#Our true state
	true_state = np.zeros((steps,1))
	#Our measurements
	measurements = np.zeros((steps,1))

	for i in range(1,steps):
		true_state[i] = a*true_state[i-1]+b*u+np.random.randn(1,1)*true_move_noise
		measurements[i] = c*true_state[i]+np.random.randn(1,1)*true_mes_noise

	return true_state, measurements