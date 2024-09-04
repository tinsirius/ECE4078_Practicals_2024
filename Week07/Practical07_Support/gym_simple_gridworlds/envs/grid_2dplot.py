from matplotlib import pyplot as plt
import numpy as np
import matplotlib.colors


def plot_grid_world(grid_env):
    """
    Generate plot of a grid world environment
    :param grid_env: Environment to be displayed
    :return (fig, ax): Matplotlib objects on which plot is defined
    """
    colors = {'wall': 'black', 'final_positive': 'green', 'final_negative': 'red',
              'cell': 'lightblue'
              }

    height, width = grid_env.grid.shape

    fig, ax = plt.subplots(figsize=(4, 4))

    # Draw grid outline
    for col in range(width + 1):
        ax.axvline(col, ymin=0, ymax=height)

    for row in range(height + 1):
        ax.axhline(row)

    for i in range(height):
        for j in range(width):
            y = (height - 1) - i
            if grid_env.is_obstacle(i, j):
                wall = plt.Rectangle((j, y), width=1.0, height=1.0, color=colors['wall'])
                ax.add_artist(wall)
            elif grid_env.is_terminal_state(i, j):
                s_idx = int(grid_env.grid[i, j])
                color = 'final_positive' if grid_env.immediate_rewards[s_idx] > 0 else 'final_negative'
                target = plt.Rectangle((j, y), width=1.0, height=1.0, color=colors[color])
                ax.add_artist(target)
            else:
                cell = plt.Rectangle((j, y), width=1.0, height=1.0, color=colors['cell'])
                ax.add_artist(cell)

    ax.set_xticks(np.arange(0.5, width))
    ax.set_xticklabels(np.arange(0, width), fontsize=8)
    ax.set_yticks(np.arange(0.5, height))
    ax.set_yticklabels(np.arange(0, height), fontsize=8)

    ax.set_ylim(0, height)
    ax.set_xlim(0, width)

    return fig, ax


def get_state_to_plot(env):
    x, y = env.cur_state
    h, _ = env.grid.shape
    return y, (h - 1) - x


def plot_value_function(grid_env, value_function, ax=None):
    """
    Generate plot of a given value function for a grid world environment
    :param grid_env: Environment
    :param value_function: Value function to be displayed
    :return (fig, ax): Matplotlib objects on which plot is defined
    """
    cmap = plt.cm.coolwarm
    norm = matplotlib.colors.Normalize(vmin=-1, vmax=1)

    height, width = grid_env.grid.shape

    if ax is None:
        fig, ax = plt.subplots(figsize=(4, 4))

    # Draw grid outline
    for col in range(width + 1):
        ax.axvline(col, ymin=0, ymax=height)

    for row in range(height + 1):
        ax.axhline(row)

    for i in range(height):
        for j in range(width):
            y = (height - 1) - i
            if grid_env.is_obstacle(i, j):
                wall = plt.Rectangle((j, y), width=1.0, height=1.0, color='k')
                ax.add_artist(wall)
            elif grid_env.is_terminal_state(i, j):
                s_idx = int(grid_env.grid[i, j])
                color = cmap(norm(grid_env.immediate_rewards[s_idx]))
                target = plt.Rectangle((j, y), width=1.0, height=1.0, color=color)
                ax.text(j + 0.3, y + 0.5, "%0.2f" % grid_env.immediate_rewards[s_idx], fontsize=10)
                ax.add_artist(target)
            else:
                s_idx = int(grid_env.grid[i, j])
                color = cmap(norm(value_function[s_idx]))
                cell = plt.Rectangle((j, y), width=1.0, height=1.0, color=color)
                ax.text(j+0.3, y+0.5, "%0.2f" % value_function[s_idx], fontsize=10)
                ax.add_artist(cell)

    ax.set_xticks(np.arange(0.5, width))
    ax.set_xticklabels(np.arange(0, width), fontsize=8)
    ax.set_yticks(np.arange(0.5, height))
    ax.set_yticklabels(np.arange(0, height), fontsize=8)

    ax.set_ylim(0, height)
    ax.set_xlim(0, width)

    return ax

def plot_action_value_function(grid_env, value_function, ax=None):
    """
    Generate plot of a given state-action value function for a grid world environment
    :param grid_env: Environment
    :param value_function: Value function to be displayed
    :return (fig, ax): Matplotlib objects on which plot is defined
    """
    cmap = plt.cm.coolwarm
    norm = matplotlib.colors.Normalize(vmin=-1, vmax=1)

    states = grid_env.get_states()
    actions = ["Up", "Down", "Left", "Right"]
    
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 5))

    v_transpose = np.transpose(value_function)
    
    im = ax.imshow(v_transpose, cmap=cmap)
    # Show all ticks and label them with the respective list entries
    ax.set_xticks(np.arange(len(states)), labels=states)
    ax.set_yticks(np.arange(len(actions)), labels=actions)
    
    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), ha="right",
             rotation_mode="anchor")
    
    # Loop over data dimensions and create text annotations.
    for i in range(len(actions)):
        for j in range(len(states)):
            text = ax.text(j, i, "%0.2f" % v_transpose[i, j],
                           ha="center", va="center", color="w")
    
    ax.set_title("Action-value function")
    return ax

def plot_policy(grid_env, policy):
    """
    Generate plot of a given policy for a grid world environment
    :param grid_env: Environment
    :param policy: Policy to be displayed
    :return (fig, ax): Matplotlib objects on which plot is defined
    """

    colors = {'wall': 'black', 'final_positive': 'green', 'final_negative': 'red',
              'cell': 'lightblue'
              }

    height, width = grid_env.grid.shape

    fig, ax = plt.subplots(figsize=(4, 4))

    # Draw grid outline
    for col in range(width + 1):
        ax.axvline(col, ymin=0, ymax=height)

    for row in range(height + 1):
        ax.axhline(row)

    def get_annotation_coordinates(a, x, y):
        a_origin, a_end = (0, 0), (0, 0)
        if a == 0:
            a_origin = (x + 0.5, y + 0.2)
            a_end = (x + 0.5, y + 0.8)
        elif a == 1:
            a_origin = (x + 0.5, y + 0.8)
            a_end = (x + 0.5, y + 0.2)
        elif a == 2:
            a_origin = (x + 0.8, y + 0.5)
            a_end = (x + 0.2, y + 0.5)
        elif a == 3:
            a_origin = (x + 0.2, y + 0.5)
            a_end = (x + 0.8, y + 0.5)
        else:
            pass

        return a_origin, a_end

    for i in range(height):
        for j in range(width):
            y = (height - 1) - i
            if grid_env.is_obstacle(i, j):
                wall = plt.Rectangle((j, y), width=1.0, height=1.0, color=colors['wall'])
                ax.add_artist(wall)
            elif grid_env.is_terminal_state(i, j):
                s_idx = int(grid_env.grid[i, j])
                color = 'final_positive' if grid_env.immediate_rewards[s_idx] > 0 else 'final_negative'
                target = plt.Rectangle((j, y), width=1.0, height=1.0, color=colors[color])
                ax.add_artist(target)
            else:
                cell = plt.Rectangle((j, y), width=1.0, height=1.0, color=colors['cell'])
                ax.add_artist(cell)
                origin, end = get_annotation_coordinates(policy[i,j], j, y)

                ax.annotate("", ha='center', va='center', xytext=origin,
                            xy=end, arrowprops={'color': 'black', 'arrowstyle': "->",
                                                 "linewidth": 2})

    ax.set_xticks(np.arange(0.5, width))
    ax.set_xticklabels(np.arange(0, width), fontsize=8)
    ax.set_yticks(np.arange(0.5, height))
    ax.set_yticklabels(np.arange(0, height), fontsize=8)

    ax.set_ylim(0, height)
    ax.set_xlim(0, width)

    return fig, ax
