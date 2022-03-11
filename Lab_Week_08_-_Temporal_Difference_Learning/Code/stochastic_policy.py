from td_agent import *

# A Near Optimal Stochastic Policy
# Now, we try a stochastic policy that deviates a little from the optimal policy seen above.
# This means we can get different results due to randomness.
# We will thus average the value function estimates we get over multiple runs.
# This can take some time, upto about 5 minutes from previous testing.

env_info = {"grid_height": 4, "grid_width": 12}
agent_info = {"discount": 1, "step_size": 0.01}

policy = np.ones(shape=(env_info['grid_width'] * env_info['grid_height'], 4)) * 0.25
policy[36] = [0.9, 0.1/3., 0.1/3., 0.1/3.]

for i in range(24, 35):
    policy[i] = [0.1/3., 0.1/3., 0.1/3., 0.9]

policy[35] = [0.1/3., 0.1/3., 0.9, 0.1/3.]
agent_info.update({"policy": policy})
agent_info.update({"step_size": 0.01})