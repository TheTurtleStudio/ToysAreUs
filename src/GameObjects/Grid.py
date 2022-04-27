import math
import GameObjects
from GameObjects import GameObject
from MainEngine import Types #NEEDED. Mainly for Types.GameObject creation.
import pygame
class Grid(): #Change this to the name of your script
    
    def __init__(self, engine):
        self.gameObject = Types.GameObject(engine)
        #self.gameObject.renderEnabled = False
        self.engine = engine
        self.gridSize = Types.Vector2(20,15)
        self.gridMatrix = Types.Matrix2x2(self.gridSize.x, self.gridSize.y)
        self.demoWall = GameObjects.GameObject.Create(engine)
        self.engine.CreateNewObject(self.demoWall)

    def Update(self):
        if (self.engine.Input.TestFor.RIGHTMOUSEDOWN()):
            cellAtPos = self.GetGridCell(self.engine.Input.TestFor.MOUSEPOS())
            if ((type(cellAtPos) is Types.Cell) and (self.gridMatrix.CellExistsCheck(cellAtPos.cell))):
                cellToChange = self.gridMatrix.GetCell(cellAtPos.cell)
                cellToChange.cell = cellAtPos.cell
                cellToChange.position = cellAtPos.position
                cellToChange.size = cellAtPos.size
                self.engine.FindObject("PLACEHANDLER").obj.HANDLEPLACEMENT(self.gridMatrix.GetCell(cellAtPos.cell))
        else:
            cellAtPos = self.GetGridCell(self.engine.Input.TestFor.MOUSEPOS())
            if ((type(cellAtPos) is Types.Cell) and (self.engine.FindObject("PLACEHANDLER").obj.selectedPlaceObject != None) and (self.gridMatrix.CellExistsCheck(cellAtPos.cell))):
                cellToChange = self.gridMatrix.GetCell(cellAtPos.cell)
                cellToChange.cell = cellAtPos.cell
                cellToChange.position = cellAtPos.position
                cellToChange.size = cellAtPos.size
                self.engine.FindObject("PLACEHANDLER").obj.HANDLEDEMOPLACEMENT(self.gridMatrix.GetCell(cellAtPos.cell), self.demoWall)
            else:
                self.demoWall.gameObject.renderEnabled = False
                
            
    def GetGridCell(self, raycastPos):
        relative = Types.Vector3(raycastPos[0], raycastPos[1], 0) - self.gameObject.position
        gridCellSize = Types.Vector2(self.gameObject.size.x / self.gridSize.x, self.gameObject.size.y / self.gridSize.y)
        if (relative.x < 0 or relative.y < 0 or relative.x > self.gameObject.size.x or relative.y > self.gameObject.size.y):
            return None
        else: #If in the grid system do this
            cell = Types.Vector2(math.floor(relative.x / gridCellSize.x), math.floor(relative.y / gridCellSize.y))
            
            cellPos = Types.Vector2(cell.x * gridCellSize.x, cell.y * gridCellSize.y) + Types.Vector2(self.gameObject.position.x, self.gameObject.position.y)
            return Types.Cell(cellPos, gridCellSize, cell)




#Create needs to be defined for every script in this folder. Everything should be exactly the same except for what is commented below, read that.
class Create():
    def __init__(self, engine):
        self.obj = Grid(engine) #Replace Template with the name of your class
    @property
    def gameObject(self):
        return self.obj.gameObject