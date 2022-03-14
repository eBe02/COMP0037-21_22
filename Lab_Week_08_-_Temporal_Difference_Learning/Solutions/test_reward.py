from env import CliffWalkEnvironment

def test_reward():
    env = CliffWalkEnvironment()
    env.env_init({"grid_height": 4, "grid_width": 12})
    env.agent_loc = (0, 0)
    reward_state_term = env.env_step(0)
    assert (reward_state_term[0] == -1 and reward_state_term[1] == env.state((0, 0)) and
            reward_state_term[2] == False)

    env.agent_loc = (3, 1)
    reward_state_term = env.env_step(2)
    assert (reward_state_term[0] == -100 and reward_state_term[1] == env.state((3, 0)) and
            reward_state_term[2] == False)

    env.agent_loc = (2, 11)
    reward_state_term = env.env_step(2)
    assert (reward_state_term[0] == -1 and reward_state_term[1] == env.state((3, 11)) and
            reward_state_term[2] == True)


test_reward()
