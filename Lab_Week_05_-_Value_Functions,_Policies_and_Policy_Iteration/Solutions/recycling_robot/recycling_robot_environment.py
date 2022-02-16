'''
Created on 4 Feb 2022

@author: ucacsjj
'''

import random
from enum import Enum
import numpy as np

from gym import Env, spaces

from .robot_states_and_actions import *

# This environment affords a much lower level control of the robot than the
# battery environment. It is partially inspired by the AI Gymn Frozen Lake
# example.

class RecyclingRobotEnvironment(Env):

    def __init__(self):

        # The action space
        self.action_space = spaces.Discrete(RobotActions.NUMBER_OF_ACTIONS)
        
        self.observation_space = spaces.Discrete(RobotBatteryState.NUMBER_OF_STATES)
        
        # Values
        
        # Probability of discharging high => medium
        self._alpha = 0.4
        
        # Probability of discharging medium => low
        self._beta = 0.1
        
        # Probability of discharging low  => discharged
        self._gamma = 0.1
        
        # Probability of charging up a level low => medium, medium => high
        self._delta = 0.9

        self._r_search = 10
        self._r_wait = 5
        self._r_charge = 0
        self._r_discharged = -20
        
        # State transition table. The dictionary consists of (s, a) values. The
        # value is a tuple which is the conditional value of the probabilities of
        # DISCHARGED, LOW, MEDIUM, HIGH, conditioned on s and a. 
        
        self._state_transition_table = {

            # New state when a=SEARCH
            (RobotBatteryState.HIGH, RobotActions.SEARCH) : \
                (0, self._alpha / 3, 2 * self._alpha / 3, 1 - self._alpha),
                     
            (RobotBatteryState.MEDIUM, RobotActions.SEARCH) : \
                (0, self._beta, 1 - self._beta, 0),

            (RobotBatteryState.LOW, RobotActions.SEARCH) : \
                (self._gamma, 1 - self._gamma, 0 , 0),

            (RobotBatteryState.DISCHARGED, RobotActions.SEARCH) : \
                (0, 0, 0, 0),
                
            # a = WAIT
             (RobotBatteryState.HIGH, RobotActions.WAIT) : \
                (0, 0, 0, 1),
                                
            (RobotBatteryState.MEDIUM, RobotActions.WAIT) : \
                (0, 0 ,1, 0),
                
            (RobotBatteryState.LOW, RobotActions.WAIT) : \
                (0, 1, 0, 0),
                
            (RobotBatteryState.DISCHARGED, RobotActions.WAIT) : \
                (0, 0, 0, 0),
                               
            # a = RECHARGE
             (RobotBatteryState.HIGH, RobotActions.RECHARGE) : \
                (0, 0, 0, 1),
                                
            (RobotBatteryState.MEDIUM, RobotActions.RECHARGE) : \
                (0, 0, 1 - self._delta, self._delta),
                
            (RobotBatteryState.LOW, RobotActions.RECHARGE) : \
                (0, 1 - self._delta, self._delta, 0),
                
            (RobotBatteryState.DISCHARGED, RobotActions.RECHARGE) : \
                (0, 0, 0, 0)
            }
        
        # The rewards. In this case, they are only a function of the actions
        # and not the state.
        
        self._action_reward_table = {
            RobotActions.SEARCH : self._r_search,
            RobotActions.WAIT: self._r_wait,
            RobotActions.RECHARGE: self._r_charge,
            RobotActions.TERMINATE: self._r_discharged
            }
        
        # Reset to the initial state
        self.reset()
        
    # Reset the scenario to the initial state
    def reset(self):
        self._battery_state = RobotBatteryState.HIGH
        
    # Reset the initial value function
    def initial_value_function(self):
        
        v_initial = np.zeros(RobotBatteryState.NUMBER_OF_STATES)
        v_initial[RobotBatteryState.DISCHARGED] = self._r_discharged
        
        return v_initial
        
    # An initial random policy under consideration
    def initial_policy(self):
        pi_initial = {
            RobotBatteryState.HIGH: (0, 1/3, 1/3, 1/3),
            RobotBatteryState.MEDIUM: (0, 1/3, 1/3, 1/3),
            RobotBatteryState.LOW: (0, 1/3, 1/3, 1/3)}
        
        return pi_initial
        
    def step(self, action):
        
        # From the (s, a) pair, get the appropriate row in the table
        transition_key = (self._battery_state, action)
        
        # Sanity check
        assert transition_key in self._state_transition_table

        # Get the state transition probabilities and rewards        
        p = self._state_transition_table[transition_key]
        r = self._reward_table[transition_key]
        
        print(str(self._battery_state) + ":" + str(p) + str(r))
        
        # Work out the state transition
        sample = random.random()
        
        done = False
        
        # Probability of transitioning to high state
        if sample < p[0]:
            self._battery_state = RobotBatteryState.HIGH
            reward = r[0]
        elif sample < p[0] + p[1]:
            self._battery_state = RobotBatteryState.MEDIUM
            reward = r[1]
        elif sample < p[0] + p[1] + p[2]:
            self._battery_state = RobotBatteryState.LOW
            reward = r[2]                 
        if sample < p[0] + p[1] + p[2] + p[3]:
            self._battery_state = RobotBatteryState.DISCHARGED
            reward = r[3]
            done = True
        return self._battery_state, reward, done, {}
    
    # Return the state, reward and probability distributions
    def next_state_and_reward_distribution(self, state, action):
        
                # From the (s, a) pair, get the appropriate row in the table
        transition_key = (state, action)
        
        # Sanity check
        #print(transition_key)
        
        assert transition_key in self._state_transition_table
        
        s_prime = [RobotBatteryState.DISCHARGED, RobotBatteryState.LOW, \
                   RobotBatteryState.MEDIUM, RobotBatteryState.HIGH]

        # Get the state transition probabilities and rewards        
        p = self._state_transition_table[transition_key]
        #r = self._reward_table[transition_key]
        r = self._action_reward_table[action]

        return s_prime, r, p
        

        
