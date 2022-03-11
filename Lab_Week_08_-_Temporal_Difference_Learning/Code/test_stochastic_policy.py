from tqdm import tqdm
from run_experiment import *
from stochastic_policy import *

arr = []

for i in tqdm(range(30)):

    env_info['seed'] = i
    agent_info['seed'] = i
    v = run_experiment(env_info, agent_info, experiment_name="Policy Evaluation On Optimal Policy", num_episodes=5000,
                       plot_freq=10000, gifname=None)
    arr.append(v)
average_v = np.array(arr).mean(axis=0)
