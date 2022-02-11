'''
Created on 4 Feb 2022

@author: ucacsjj
'''

from enum import IntEnum

# The battery state

class RobotBatteryState(IntEnum):
    DISCHARGED = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    NUMBER_OF_STATES = 4

# The robot actions

class RobotActions(IntEnum):
    TERMINATE = 0
    SEARCH = 1
    WAIT = 2
    RECHARGE = 3
    NUMBER_OF_ACTIONS = 4