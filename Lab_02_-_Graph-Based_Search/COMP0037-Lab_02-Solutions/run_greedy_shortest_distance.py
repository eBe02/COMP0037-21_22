#!/usr/bin/env python3

from grid_search.occupancy_grid import OccupancyGrid
from grid_search.greedy_shortest_distance_planner \
    import GreedyShortestDistancePlanner

# Create the occupancy grid
occupancyGrid = OccupancyGrid(21, 21, 0.5)

# Change to range(1, 20) for the simpler example
for y in range(0, 20):
    occupancyGrid.setCell(11, y, 1)

start = (0, 20)
goal = (20, 0)

planner = GreedyShortestDistancePlanner(occupancyGrid)

planner.setPauseTime(0.1)
planner.updateGraphicsEachIteration(True)


planner.plan(start, goal)
    
# Pause
planner.gridDrawer.waitForKeyPress()
    
# Show the path
planner.extractPathToGoal()
planner.gridDrawer.waitForKeyPress()

