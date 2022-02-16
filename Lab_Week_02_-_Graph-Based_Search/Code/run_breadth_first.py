#!/usr/bin/env python3

from grid_search.occupancy_grid import OccupancyGrid
from grid_search.breadth_first_planner import BreadthFirstPlanner

# Create the occupancy grid
occupancyGrid = OccupancyGrid(21, 21, 0.5)

# Q3c:
# Change to range(1, 20) for the simpler example
for y in range(0, 20):
    occupancyGrid.setCell(11, y, 1)

start = (0, 20)
goal = (20, 0)

planner = BreadthFirstPlanner(occupancyGrid)

planner.setPauseTime(0)
planner.updateGraphicsEachIteration(True)


planner.plan(start, goal)
    
# Pause
planner.gridDrawer.waitForKeyPress()
    
# Show the path
planner.extractPathToGoal()
planner.gridDrawer.waitForKeyPress()


