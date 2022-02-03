import time
import math
from collections import deque

from .occupancy_grid import OccupancyGrid
from .search_grid import SearchGrid
from .grid_drawer import GridDrawer
from .cell import CellLabel
from .planned_path import PlannedPath

# This class implements the basic components of the forward search
# planning algorithm in LaValle's book and the lecture slides. The
# same general framework can be used to implement a wide array of
# algorithms, including depth first search, breadth first search,
# greedy (shortest distance first) search, Dijkstra and A*. The code
# here is written to be easy to understand and is not optimised in any
# way.

# The code includes a number of hooks which do not appear in LaValle's
# description, but are useful when implementing some techniques. In
# addition, the code can optionally use a graphics library to draw the
# grid cells.

# The planner itself takes an occupancy map as an input. This
# specifies the structure of the environment - basically how big is
# it, which cells are blocked and which cells are open. The planner
# internally constructs a SearchGrid. This contains the nodes and
# edges from the planner and the labels associated with them.

class PlannerBase(object):

    # Construct a new planner object and set defaults.
    def __init__(self, occupancyGrid):
        self.occupancyGrid = occupancyGrid
        self.searchGrid=None

        # All these variables are used for controlling the graphics output
        self.pauseTimeInSeconds = 0.05
        self.pathPauseTimeInSeconds = 0.05
        self.showGraphics=True
        self.showGraphicsEachIteration=False
        self.goalReached=None
        self.gridDrawer=None
        self.maximumGridDrawerWindowHeightInPixels = 800
        self.drawParentArrows=True

    # This method pushes a cell onto the queue Q. Its implementation
    # depends upon the type of search algorithm used. If necessary,
    # (self) could also do things like update path costs as well.
    # This used in lines 2 and 11 of the pseudocode    
    def pushCellOntoQueue(self, cell):
        raise NotImplementedError()

    # This method returns a boolean - true if the queue is empty,
    # false if it still has some cells on it. Its implementation
    # depends upon the the type of search algorithm used.
    # This is used in line 3 of the pseudocode    
    def isQueueEmpty(self):
        raise NotImplementedError()

    # Handle the case that a cell has been visited already. This is
    # used by some algorithms to rewrite paths to identify the
    # shortest path.
    # This corresponds to line 13 of the pseudocode    
    def resolveDuplicate(self, cell, parentCell):
        raise NotImplementedError()

    # This method finds the first cell (at the head of the queue),
    # removes it from the queue, and returns it. Its implementation
    # depends upon the the type of search algorithm used.
    # This corresponds to line 4 of the pseudocode    
    def popCellFromQueue(self):
        raise NotImplementedError()

    # This method determines if the goal has been reached.
    # This corresponds to line 5 of the pseudocode    
    def hasGoalBeenReached(self, cell):
        return cell == self.goal

    # Compute the additive cost of performing a step from the parent to the
    # current cell. This calculation is carried out the same way no matter
    # what heuristics, etc. are used
    def computeLStageAdditiveCost(self, parentCell, cell):
        
        
        # If the parent is empty, this is the start of the path and the
        # cost is 0.
        if (parentCell is None):
            return 0

        # Q2b:
        # Complete the implementation
        
        # Cost is the Cartesian distance
        cellCoords = cell.coords()
        parentCellCoords = parentCell.coords()
        dX = cellCoords[0] - parentCellCoords[0]
        dY = cellCoords[1] - parentCellCoords[1]
        L = math.sqrt(dX * dX + dY * dY)
        
        return L

    # This method gets the list of cells which potentially could be
    # visited next. Each candidate position has to be tested
    # separately.
    # This corresponds to line 7 of the pseudocode    
    def nextCellsToBeVisited(self, cell):

        # This stores the set of valid actions / cells
        cells = list()

        #Q3b
        # Modify so that the cells are visited in a different sequence.
        # Investigate the impact of changing the search order on the computed path

        # Go through all the neighbours and add the cells if they
        # don't fall outside the grid and they aren't the cell we
        # started with. The order has been manually written down to
        # create a spiral.

        # The swapped order video transposed the last four transitions first
        self.pushBackCandidateCellIfValid(cell, cells, 0, -1)
        self.pushBackCandidateCellIfValid(cell, cells, 1, -1)
        self.pushBackCandidateCellIfValid(cell, cells, 1, 0)
        self.pushBackCandidateCellIfValid(cell, cells, 1, 1)
        self.pushBackCandidateCellIfValid(cell, cells, 0, 1)
        self.pushBackCandidateCellIfValid(cell, cells, -1, 1)
        self.pushBackCandidateCellIfValid(cell, cells, -1, 0)
        self.pushBackCandidateCellIfValid(cell, cells, -1, -1)

        return cells

    # This helper method checks if the robot, at cell.coords, can move
    # to cell.coords+(offsetX, offsetY). Reasons why it can't do (self)
    # include falling off the edge of the map or running into an
    # obstacle.
    def pushBackCandidateCellIfValid(self, cell, cells, offsetX, offsetY):
        cellCoords = cell.coords()
        newX = cellCoords[0] + offsetX
        newY = cellCoords[1] + offsetY
        if ((newX >= 0) & (newX < self.occupancyGrid.width()) \
            & (newY >= 0) & (newY < self.occupancyGrid.height())):
            newCoords = (newX, newY)
            newCell = self.searchGrid.cellFromCoords(newCoords)
            if newCell.isObstructed is False:
                cells.append(newCell)

    # This method determines whether a cell has been visited already.
    # This corresponds to line 9 of the pseudocode    
    def hasCellBeenVisitedAlready(self, cell):
        return cell.label() != CellLabel.UNVISITED

    # Mark that the cell has been visited. Also note the parent, which
    # is used to extract the path later on.
    # This corresponds to line 10 of the pseudocode    
    def markCellAsVisitedAndRecordParent(self, cell, parentCell):
        cell.setLabel(CellLabel.ALIVE)
        cell.setParent(parentCell)

    # Mark that a cell is dead. A dead cell is one in which all of its
    # immediate neighbours have been visited.
    # This corresponds to line 14 of the pseudocode    
    def markCellAsDead(self, cell):
        cell.setLabel(CellLabel.DEAD)
        
    # The main search routine. Given the input startCoords (x,y) and
    # goalCoords (x,y), compute a plan. Note that the coordinates
    # index from 0 and refer to the cell number.
    def plan(self, startCoords, goalCoords):

        # Empty the queue. This is needed to make sure everything is reset
        while (self.isQueueEmpty() == False):
            self.popCellFromQueue()
        
        # Create the search grid from the occupancy grid and seed
        # unvisited and occupied cells.
        if (self.searchGrid is None):
            self.searchGrid = SearchGrid.fromOccupancyGrid(self.occupancyGrid)
        else:
            self.searchGrid.setFromOccupancyGrid(self.occupancyGrid)

        # Get the start cell object and label it as such. Also set its
        # path cost to 0.
        self.start = self.searchGrid.cellFromCoords(startCoords)
        self.start.isStart=True
        self.start.pathCost = 0

        # Get the goal cell object and label it.
        self.goal = self.searchGrid.cellFromCoords(goalCoords)
        self.goal.isGoal=True

        # If required, set up the grid drawer and show the initial state
        if (self.showGraphics == True):
            if (self.gridDrawer is None):
                self.gridDrawer = GridDrawer(self.searchGrid, self.maximumGridDrawerWindowHeightInPixels)
            self.drawCurrentState()
            self.gridDrawer.waitForKeyPress()

        # Insert the start on the queue to start the process going.
        self.markCellAsVisitedAndRecordParent(self.start, None)
        self.pushCellOntoQueue(self.start)

        # Reset the count
        self.numberOfCellsVisited = 0

        # Indicates if we reached the goal or not
        self.goalReached=False
        
        # Iterate until we have run out of live cells to try or we reached the goal
        # This corresponds to lines 3-15 of the pseudocode
        while (self.isQueueEmpty() == False):
            cell = self.popCellFromQueue()
            if (self.hasGoalBeenReached(cell) == True):
                self.goalReached=True
                break
            cells = self.nextCellsToBeVisited(cell)
            for nextCell in cells:
                if (self.hasCellBeenVisitedAlready(nextCell) == False):
                    self.markCellAsVisitedAndRecordParent(nextCell, cell)
                    self.pushCellOntoQueue(nextCell)
                    self.numberOfCellsVisited = self.numberOfCellsVisited + 1
                else:
                    self.resolveDuplicate(nextCell, cell)

            # Now that we've checked all the actions for (self) cell,
            # mark it as dead
            self.markCellAsDead(cell)

            # Draw the update if required
            if (self.showGraphicsEachIteration == True):
                self.drawCurrentState()

        # Draw the final results if required
        self.drawCurrentState()

        if (self.goalReached == True):
            print (f'Reached the goal after visiting {self.numberOfCellsVisited} cells')
        else:
            print (f'Could not reach the goal after visiting {self.numberOfCellsVisited} cells')
            
        return self.goalReached


    # This method extracts a path from the pathEndCell to the start
    # cell. The path is a list actually sorted in the order:
    # cell(x_I), cell(x_1), ... , cell(x_K), cell(x_G). You can use
    # (self) method to try to find the path from any end cell. However,
    # depending upon the planner used, the results might not be
    # valid. In (self) case, the path will probably not terminate at the
    # start cell.
    def extractPath(self, pathEndCell):

        # Construct the path object and mark if the goal was reached
        path = PlannedPath()
        path.goalReached = self.goalReached
        
        # Initial condition - the goal cell
        path.waypoints.append(pathEndCell)
               
        # Start at the goal and find the parent
        cell = pathEndCell.parent
        
        # Q2a:
        # Complete the implementation of the code to extract the full path.
        
        # Iterate back through and extract each parent in turn and add
        # it to the path. To work out the travel length along the
        # path, you'll also have to add (self) at (self) stage.
        while (cell is not None):
            path.waypoints.appendleft(cell)
            if (cell.isStart is False) and (cell.isGoal is False):
                cell.isOnPath=True

            if (self.showGraphics == True):
                self.gridDrawer.update()
                time.sleep(self.pathPauseTimeInSeconds)

            cell = cell.parent

        # Return the path
        return path

    # Extract the path between the start and goal.
    def extractPathToGoal(self):
        path = self.extractPath(self.goal)
        return path
    
    # Draw the output and sleep for the pause time.
    def drawCurrentState(self):
        if (self.showGraphics == True):
            self.gridDrawer.update()
            time.sleep(self.pauseTimeInSeconds)

    # Set the pause time
    def setPauseTime(self, pauseTimeInSeconds):
        self.pauseTimeInSeconds = pauseTimeInSeconds
        
    # Set the pause time for showing the path
    def setPathPauseTime(self, pathPauseTimeInSeconds):
        self.pathPauseTimeInSeconds = pathPauseTimeInSeconds
        
    def showParentArrows(self, drawParentArrows):    
        self.drawParentArrows = drawParentArrows
    
    # Specify if we show graphics on each iteration
    def updateGraphicsEachIteration(self, updateGraphicsEachIteration):
        self.showGraphicsEachIteration = updateGraphicsEachIteration
