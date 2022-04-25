import math
import GameObjects
from MainEngine import Types #NEEDED. Mainly for Types.GameObject creation.
import pygame
class Grid(): #Change this to the name of your script
    gridSize = Types.Vector2(30,15)
    #gridMatrix = WHATEVER
    #Need to have this grid matrix be composed of a shit ton of Cells, each containing their own data. The matrix will have dimensions equal to that of gridSize.
    #Basically we just need a place to get all the information about cells. What's in them, their adjacent cells, etc. 
    def __init__(self, engine):
        self.gameObject = Types.GameObject(engine)
        self.gameObject.renderEnabled = False
        self.engine = engine

    def Update(self):
        if (self.engine.Input.TestFor.RIGHTMOUSEDOWN()):
            cell = self.GetGridCell(self.engine.Input.TestFor.MOUSEPOS())
            if (type(cell) is Cell):
                new = GameObjects.GameObject.GameObject(self.engine)
                new.gameObject.size = cell.size
                new.gameObject.position = Types.Vector3(cell.position.x, cell.position.y, 600000)
                self.engine.CreateNewObject(new)

            
    def GetGridCell(self, raycastPos):
        relative = Types.Vector3(raycastPos[0], raycastPos[1], 0) - self.gameObject.position
        gridCellSize = Types.Vector2(self.gameObject.size.x / self.gridSize.x, self.gameObject.size.y / self.gridSize.y)
        if (relative.x < 0 or relative.y < 0 or relative.x > self.gameObject.size.x or relative.y > self.gameObject.size.y):
            return None
        else: #If in the grid system do this
            cellPos = Types.Vector2(math.floor(relative.x / gridCellSize.x) * gridCellSize.x, math.floor(relative.y / gridCellSize.y) * gridCellSize.y) + Types.Vector2(self.gameObject.position.x, self.gameObject.position.y)
            return Cell(cellPos, gridCellSize)


class Cell():
    def __init__(self, _position, _size):
        self.position = _position
        self.size = _size
        self.center = Types.Vector2(_position.x + (_size.x / 2), _position.y + (_size.y / 2))

#Create needs to be defined for every script in this folder. Everything should be exactly the same except for what is commented below, read that.
class Create():
    def __init__(self, engine):
        self.obj = Grid(engine) #Replace Template with the name of your class
    @property
    def gameObject(self):
        return self.obj.gameObject