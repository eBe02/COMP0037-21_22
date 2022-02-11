from .cell import Cell

class SearchGrid(object):

    # This class stores the state of a search grid to illustrate forward search

    def __init__(self, width, height, resolution):
        self._width = width
        self._height = height
        self._resolution = resolution

    # Construct the class using an occupancy grid object
    @classmethod
    def fromOccupancyGrid(cls, occupancyGrid):

        (self) = cls(occupancyGrid.width(), occupancyGrid.height(), occupancyGrid.resolution())

        # Populate the search grid from the occupancy grid
        self.setFromOccupancyGrid(occupancyGrid)
        
        return (self)

    # Reset the state of the search grid to the value of the occupancy grid
    def setFromOccupancyGrid(self, occupancyGrid):
        self.grid = [[Cell((x, y), occupancyGrid.cell(x,y)) for y in range(self._height)] \
                     for x in range(self._width)]

    def cellFromCoords(self, coords):
        return self.grid[coords[0]][coords[1]]

    def width(self):
        return self._width

    def height(self):
        return self._height
