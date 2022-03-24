from td_agent import *

def test_td_updates():
    # The following test checks that the TD check works for a case where the transition
    # garners reward -1 and does not lead to a terminal state. This is in a simple two state setting
    # where there is only one action. The first state's current value estimate is 0 while the second is 1.
    # Note the discount and step size if you are debugging this test.
    agent = TDAgent()
    policy_list = np.array([[1.], [1.]])
    agent.agent_init({"policy": np.array(policy_list), "discount": 0.99, "step_size": 0.1})
    agent.values = np.array([0., 1.])
    agent.agent_start(0)
    reward = -1
    next_state = 1
    agent.agent_step(reward, next_state)
    assert (np.isclose(agent.values[0], -0.001) and np.isclose(agent.values[1], 1.))

    # The following test checks that the TD check works for a case where the transition
    # garners reward -100 and lead to a terminal state. This is in a simple one state setting
    # where there is only one action. The state's current value estimate is 0.
    # Note the discount and step size if you are debugging this test.
    agent = TDAgent()
    policy_list = np.array([[1.]])
    agent.agent_init({"policy": np.array(policy_list), "discount": 0.99, "step_size": 0.1})
    agent.values = np.array([0.])
    agent.agent_start(0)
    reward = -100
    next_state = 0
    agent.agent_end(reward)
    assert (np.isclose(agent.values[0], -10))


test_td_updates()
