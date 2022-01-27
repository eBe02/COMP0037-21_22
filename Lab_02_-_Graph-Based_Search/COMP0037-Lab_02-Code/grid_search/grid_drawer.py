import random
from .graphics import *
from .search_grid import SearchGrid
from .cell import CellLabel

class GridDrawer(object):

    def __init__(self, searchGrid, maximumGridDrawerWindowHeightInPixels, drawParentArrows = True):

        self._searchGrid = searchGrid;
        self._drawParentArrows = drawParentArrows
        
        width = searchGrid.width();
        height = searchGrid.height();

        # Make sure that the height of the window is less than the specified maximum
        self._cellSize = max(20, maximumGridDrawerWindowHeightInPixels / height)

        # Create the window
        self._win = GraphWin("Graphics", width * self._cellSize , height * self._cellSize, autoflush = False)
        
        # Allocate the cells
        self._rectangles = [[Rectangle(Point(i * self._cellSize, (height - j - 1) * self._cellSize), \
                                      Point((i+1) * self._cellSize, (height - j) * self._cellSize)) \
                            for i in range(width)] \
                           for j in range(height)]

        for i in range(width):
            for j in range(height):
                self._rectangles[j][i].draw(self._win)
                
        if (self._drawParentArrows is True):
            self.parentArrows = {}
                
    def update(self):

        ### Figure out the width and height
        width = self._searchGrid.width();
        height = self._searchGrid.height();

        for i in range(width):
            for j in range(height):
                
                # First update the grid cell
                cell = self._searchGrid.cellFromCoords((i, j))
                cellLabel = cell.label()
                if cell.isObstructed is True:
                    color = 'purple'
                elif cell.isStart is True:
                    color = 'red'
                elif cell.isGoal is True:
                    color = 'green'
                elif cell.isOnPath is True:
                    color = 'yellow'
                elif cellLabel == CellLabel.UNVISITED:
                    color = 'gray'
                elif cellLabel == CellLabel.DEAD:
                    color = 'black'
                else:
                    color = 'white'
                self._rectangles[j][i].setFill(color);
                
                # Now handle drawing the parent arrow if required
                if (self._drawParentArrows is False):
                    continue
                
                # If we have no parent continue
                if (cell.parent is None):
                    continue

                # Get the coordinates
                cellCoords = cell.coords()
                parentCellCoords = cell.parent.coords()

                # If we have a parent object, and the parent has changed, redraw the arrow
                # Note that the graphics doesn't have an API to do this, so had to hack it
                if (cell in self.parentArrows):
                    parentArrow = self.parentArrows[cell]
                    if (cell.parentChanged is True):
                        parentArrow.undraw()
                        parentArrow.p2 = Point((parentCellCoords[0] + 0.5)* self._cellSize, \
                                               (height - parentCellCoords[1] - 0.5) * self._cellSize)
                        cell.parentChanged = False
                        parentArrow.setOutline('red')
                        parentArrow.draw(self._win)
                        
                    else:
                        parentArrow.setOutline('cyan')

                    continue
                
                # Create a new parent arrow and draw it
                parentArrow = Line(Point((cellCoords[0] + 0.5)* self._cellSize, \
                                         (height - cellCoords[1] - 0.5) * self._cellSize), \
                                   Point((parentCellCoords[0] + 0.5)* self._cellSize, \
                                         (height - parentCellCoords[1] - 0.5) * self._cellSize))
                
                parentArrow.setArrow('last')
                parentArrow.setOutline('red')
                self.parentArrows[cell] = parentArrow
                parentArrow.draw(self._win)                

        # Flush the drawing right at the very end for speed
        self._win.flush()
                    
    def waitForKeyPress(self):
        self._win.getKey()
