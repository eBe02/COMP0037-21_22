from .helpers import clamp

# This class stores the occupancy grid. This is a "chessboard-like"
# representation of the environment. The environment is represented by
# a set of square cells. Each cell encodes whether that bit of the
# environment is free, or whether it is blocked. A "0" says that a
# cell is free and so the robot can travel over it. A "1" means that
# it is blocked and the robot cannot travel over it.

class OccupancyGrid(object):

    # Construct a new occupancy grid with a given width and
    # height. The resolution says the lenght of the side of each cell
    # in metres. By default, all the cells are set to "0" which means
    # that there are no obstacles.
    def __init__(self, width, height, resolution):
        self._width = width
        self._height = height
        self._resolution = resolution
        self._data = [[0 for x in range(width)] for y in range(height)]

    # The width of the occupancy map in cells                
    def width(self):
        return self._width

    # The height of the occupancy map in cells                
    def height(self):
        return self._height

    # The resolution of each cell (the length of its side in metres)
    def resolution(self):
        return self._resolution

    # Get the status of a cell.
    def cell(self, x, y):
        return self._data[y][x]

    # Set the status of a cell.
    def setCell(self, x, y, c):
        self._data[y][x] = c
    
    # Take a position in world coordinates (i.e., m) and turn it into
    # cell coordinates. Clamp the value so that it always falls within
    # the grid. The conversion uses integer rounding.
    def getCellCoordinatesFromWorldCoordinates(self, worldCoords):

        cellCoords = (clamp(int(worldCoords[0] / self._resolution), 0, self._width - 1), \
                      clamp(int(worldCoords[1] / self._resolution), 0, self._height - 1))
        
        return cellCoords
    
    # Convert a position in cell coordinates to world coordinates. The
    # conversion uses the centre of a cell, hence the mysterious 0.5
    # addition. No clamping is currently done.
    def getWorldCoordinatesFromCellCoordinates(self, cellCoords):

        worldCoords = ((cellCoords[0] + 0.5) * self._resolution, \
                      (cellCoords[1] + 0.5) * self._resolution)

        return worldCoords
