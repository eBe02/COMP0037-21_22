#!/usr/bin/env python3

from grid_search.occupancy_grid import OccupancyGrid
from grid_search.depth_first_planner import DepthFirstPlanner
from grid_search.depth_first_planner import DepthFirstPlanner

# Create the occupancy grid
occupancyGrid = OccupancyGrid(21, 21, 0.5)

start = (10, 10)
goal = (10, 0)

planner = DepthFirstPlanner(occupancyGrid)

planner.setPauseTime(0.5)
planner.updateGraphicsEachIteration(True)


planner.plan(start, goal)
    
# Pause
planner.gridDrawer.waitForKeyPress()
    
# Show the path
planner.extractPathToGoal()
planner.gridDrawer.waitForKeyPress()

