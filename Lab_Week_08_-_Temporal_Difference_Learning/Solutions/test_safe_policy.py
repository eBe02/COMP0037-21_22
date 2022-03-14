from run_experiment import *
from safe_policy import *

agent_info.update({"policy": policy})
v = run_experiment(env_info, agent_info,
               experiment_name="Policy Evaluation On Safe Policy",
               num_episodes=5000, plot_freq=500, gifname='safe_policy.gif')