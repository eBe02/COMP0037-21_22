from enum import Enum

# The label which can be assigned to this cell

class CellLabel(Enum):
    UNVISITED=0
    DEAD=1
    ALIVE=2

# This class stores information about each cell - its coordinates in the grid,
# its label, and the path cost to reach it. It includes a few extra field which
# help with stuff like plotting as well.

class Cell(object):

    def __init__(self, coords, isOccupied):

        # Set coordinates
        self._coords = coords
        
        # The cell is initially given the label that it's not been visited.
        self._label = CellLabel.UNVISITED

        # Flag if the cell is obstructed
        if isOccupied > 0:
            self.isObstructed = True
        else:
            self.isObstructed = False

        # Initially the cell has no parents.
        self.parent = None

        # The initial path cost is infinite. For algorithms that need
        # it, this is the necessary initial condition.
        self.pathCost = float("inf")
        
        # Flags to show if the cell is at the start or the goal        
        self.isStart = False
        self.isGoal = False
        
        # These variables are used for plotting
        self.isOnPath = False
        self.parentChanged = False


    def coords(self):
        return self._coords

    # Get the cell label
    def label(self):
        return self._label

    # Revise the label        
    def setLabel(self, label):
        self._label = label
        
    # If it has changed, change the parent to this cell    
    def setParent(self, parent):
        
        # Nothing to do if the same
        if self.parent == parent:
            return 
        
        self.parent = parent
        self.parentChanged = True
        
    # Tie breaker; normally you'd make it random, but this is to 
    # give deterministic behaviour
    def __lt__(self, other):
        return True
    
        
    
