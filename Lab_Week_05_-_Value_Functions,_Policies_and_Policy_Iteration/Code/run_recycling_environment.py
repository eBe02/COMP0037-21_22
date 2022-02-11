#!/usr/bin/env python3


'''
Created on 4 Feb 2022

@author: ucacsjj
'''

from recycling_robot.robot_states_and_actions import *
from recycling_robot.policy_evaluator import PolicyEvaluator
from recycling_robot.recycling_robot_environment import RecyclingRobotEnvironment

if __name__ == '__main__':
    
    # Create the recycling robot
    rre = RecyclingRobotEnvironment()
    
    # Create the policy evaluate
    policyEvaluator = PolicyEvaluator(rre)

    # Initialize the evaluator for the given policy    
    policyEvaluator.initialize(rre.initial_policy(), rre.initial_value_function())
    
    # Now evaluate it; note that you can call this repeatedly
    policyEvaluator.evaluate_policy()
