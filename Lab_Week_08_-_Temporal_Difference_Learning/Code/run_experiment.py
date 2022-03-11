import matplotlib.pyplot as plt

from td.rl_glue import RLGlue
from td.manager import Manager
from env import CliffWalkEnvironment
from td_agent import TDAgent
import numpy as np
import imageio

def run_experiment(env_info, agent_info, num_episodes=5000, experiment_name=None, plot_freq=100, true_values_file=None,
                   value_error_threshold=1e-8,gifname=None):

    env = CliffWalkEnvironment
    agent = TDAgent
    rl_glue = RLGlue(env, agent)

    rl_glue.rl_init(agent_info, env_info)
    manager = Manager(env_info, agent_info, true_values_file=true_values_file, experiment_name=experiment_name)
    images = []

    for episode in range(1, num_episodes + 1):
        rl_glue.rl_episode(0)  # no step limit
        if episode % plot_freq == 0:
            values = rl_glue.agent.agent_message("get_values")
            fig = manager.visualize(values, episode)

            image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
            images.append(image.reshape(3342, 2500, 3)) ## Y×X

    if gifname is not None:
        imageio.mimsave(gifname, images, fps=1)

    values = rl_glue.agent.agent_message("get_values")
    if true_values_file is not None:
        # Grading: The Manager will check that the values computed using your TD agent match
        # the true values (within some small allowance) across the states. In addition, it also
        # checks whether the root mean squared value error is close to 0.
        manager.run_tests(values, value_error_threshold)

    return values