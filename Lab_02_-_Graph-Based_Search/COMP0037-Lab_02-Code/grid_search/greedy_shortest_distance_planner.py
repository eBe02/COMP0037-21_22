from math import sqrt
from queue import PriorityQueue

from .planner_base import PlannerBase

class GreedyShortestDistancePlanner(PlannerBase):

    # Q4a:
    # Add queue definition
    def __init__(self, occupancyGrid):
        PlannerBase.__init__(self, occupancyGrid)
        raise NotImplementedError()

    # Q4a:
    # Implement computing the search key and add to the priority queue
    def pushCellOntoQueue(self, cell):
        raise NotImplementedError()
    
    # Q4a:
    # Check the queue size is zero
    def isQueueEmpty(self):
        raise NotImplementedError()
        
    # Q4a:
    # Simply pull from the front of the list
    def popCellFromQueue(self):

    def resolveDuplicate(self, cell, parentCell):
        # Nothing to do in this case
        pass
