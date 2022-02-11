'''
Created on 29 Jan 2022

@author: ucacsjj
'''

import copy

import numpy as np

# This class implements the policy evaluation algorithm.

from .robot_states_and_actions import *

class PolicyEvaluator:

    def __init__(self, environment):
        
        # The environment the system works with        
        self._environment = environment

        # The discount factor        
        self._gamma = 1
        
        # Threshold on maximum change in the value function to test
        # for convergence in policy evaluation
        self._theta = 1e-3
        
        # Flag to show if initialized
        self._initialized = False
        
        # Working scratch variables for the current value function
        self._v= None

        # The maximum number of times the policy evaluation algorithm
        # will be run before the for loop is exited.
        self._max_policy_evaluation_steps = 5000

    def initialize(self, pi, initial_v):
        self._pi = copy.deepcopy(pi)
        self._v = copy.deepcopy(initial_v)
        print(f'initial_v={initial_v}')

    def evaluate_policy(self):

        # Get the environment
        environment = self._environment

        # Execute the loop at least once
        
        for iteration in range(self._max_policy_evaluation_steps):
            
            delta = 0

            for s in range(RobotBatteryState.NUMBER_OF_STATES):
               
                # Special case: discharged always goes to the terminal state, so skip it
                if s == RobotBatteryState.DISCHARGED:
                    continue
                
                # Get the action distribution
                pia = self._pi.get(s)

                # Store the old value of the state value function to test for
                # convergence
                old_v = self._v[s]
                
                new_v = 0
                
                # Q2: Insert policy evaluation code here.

                self._v[s] = new_v
                                    
                # Update the maximum deviation
                delta = max(delta, abs(old_v-new_v))
            
            # Terminate the loop if either the change was very small
            if delta < self._theta:
                    break

        print(f'Terminated after {iteration} iterations')
        print(f'converged_v={self._v}')
        
        return self._v
     