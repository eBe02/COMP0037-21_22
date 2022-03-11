from env import CliffWalkEnvironment

def test_state():
    env = CliffWalkEnvironment()
    env.env_init({"grid_height": 4, "grid_width": 12})
    coords_to_test = [(0, 0), (0, 11), (1, 5), (3, 0), (3, 9), (3, 11)]
    true_states = [0, 11, 17, 36, 45, 47]
    output_states = [env.state(coords) for coords in coords_to_test]
    print(output_states)
    assert(output_states == true_states)


test_state()
