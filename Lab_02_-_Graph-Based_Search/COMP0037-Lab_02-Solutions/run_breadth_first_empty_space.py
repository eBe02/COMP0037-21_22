#!/usr/bin/env python3

from grid_search.occupancy_grid import OccupancyGrid
from grid_search.breadth_first_planner import BreadthFirstPlanner

# Create the occupancy grid
# Q1b:
# Modify the occupancy grid size
occupancyGrid = OccupancyGrid(31, 31, 0.5)

# Q1c:
# Add obstacles to the occupancy grid
occupancyGrid.setCell(7, 2, 1)

# Q1a:
# Set the start and end values to the specifed 
start = (20, 20)
goal = (0, 0)

planner = BreadthFirstPlanner(occupancyGrid)

planner.setPauseTime(0)
planner.updateGraphicsEachIteration(True)


planner.plan(start, goal)
    
# Pause
planner.gridDrawer.waitForKeyPress()
    
# Show the path
planner.extractPathToGoal()
planner.gridDrawer.waitForKeyPress()

