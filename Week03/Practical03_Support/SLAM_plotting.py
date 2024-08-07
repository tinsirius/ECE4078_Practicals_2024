import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
import numpy as np
import pickle
import ipywidgets as widgets
from scipy.stats import norm
import time
from IPython.display import display

def createInitialPlot(x, y):
    fig, ax = plt.subplots()
    old_line, = ax.step(x, y, c='b', label='Current probability')
    line, = ax.step(x, y, c='g', label='Uncertainty after 5 steps')
    ax.legend()
    ax.set_xlabel("Robot's position along the 1D line")
    ax.set_ylabel("Probability of robot being at position x")
    return old_line, line

def createbtns():
    btn_move = widgets.Button(description='Move 5 steps',
                            layout=widgets.Layout(flex='1 1 0%', width='auto'),
                            button_style='success')
    btn_reset = widgets.Button(description='Reset',
                            layout=widgets.Layout(flex='1 1 0%', width='auto'),
                            button_style='success')
    display(widgets.HBox([btn_move, btn_reset]))
    return btn_move, btn_reset

def create_slam_plot(x, mu_k, sigma_k, true_state, sigma_R):
    y_pred = norm.pdf(x, loc=mu_k, scale=sigma_k)
    y_mes = norm.pdf(x, loc=true_state[0], scale=sigma_R)
    fig, ax = plt.subplots()
    hfig = display(fig, display_id=True)
    mes_line, = ax.step(x, y_pred, c='g')
    pred_line, = ax.step(x, y_mes, c='r')
    est_line, = ax.step([],[], c='orange')
    ax.set_xlabel("Robot's position along the 1D line")
    ax.set_ylabel("Probability of the robot's position")

    legend_elements = [Line2D([0], [0], color='g', lw=2, label='Model Uncertainty'),
                    Line2D([0], [0], color='r', lw=2, label='Measurement Uncertainty'),
                    Line2D([0], [0], color='orange', lw=2, label='KF Uncertainty'),
                    Line2D([0], [0], marker='o', color='w', label='True Position',
                            markerfacecolor='b', markersize=8)]

    ax.legend(handles=legend_elements, loc='upper right')
    return fig, ax, hfig

def update_slam_plot(fig, ax, hfig, x, true_state, y_pred, y_mes, y_est):
    ax.plot(x,y_pred,color='green')
    ax.plot(x, y_mes,color='red')
    ax.plot(x, y_est,color='orange')
    ax.scatter(true_state, 0, color='b')
    time.sleep(0.5)
    fig.canvas.draw()
    hfig.update(fig)