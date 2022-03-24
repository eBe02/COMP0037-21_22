import numpy as np

env_info = {"grid_height": 4, "grid_width": 12, "seed": 0}
agent_info = {"discount": 1, "step_size": 0.01, "seed": 0}

# The Safe Policy
# Hint: Fill in the array below (as done in the previous cell) based on the safe policy illustration
# in the environment diagram. This is the policy that strides as far as possible away from the cliff.
# We call it a "safe" policy because if the environment has any stochasticity, this policy would do a good job in
# keeping the agent from falling into the cliff (in contrast to the optimal policy shown before).
# BOILERPLATE:
policy = np.ones(shape=(env_info['grid_width'] * env_info['grid_height'], 4)) * 0.25

### START CODE HERE ###
h = env_info['grid_height']
w = env_info['grid_width']

for i in range(((h - 1) * w), 0, -w):
    policy[i] = [1, 0, 0, 0]

for i in range(0, w):
    policy[i] = [0, 0, 0, 1]

for i in range(w - 1, h * w - 1, w):
    policy[i] = [0, 0, 1, 0]

pass
### END CODE HERE ###