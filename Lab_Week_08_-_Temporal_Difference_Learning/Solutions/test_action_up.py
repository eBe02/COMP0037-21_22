from env import CliffWalkEnvironment

def test_action_up():
    env = CliffWalkEnvironment()
    env.env_init({"grid_height": 4, "grid_width": 12})
    env.agent_loc = (0, 0)
    env.env_step(0)
    assert (env.agent_loc == (0, 0))

    env.agent_loc = (1, 0)
    env.env_step(0)
    assert (env.agent_loc == (0, 0))


test_action_up()
