from MainEngine import Types #NEEDED. Mainly for Types.GameObject creation.
from GameObjects import Wall
import pygame
class PlaceWall(): #Change this to the name of your script
    def __init__(self, engine):
        self.gameObject = Types.GameObject(engine)
        self.engine = engine
        self.creator = None
        self.selectedPlaceObject = None
        self.removingTile = False
        self.gameObject.renderEnabled = False

    def HANDLEPLACEMENT(self, cell):
        if (self.engine.FindObject("GRID").obj.gridMatrix.CellExistsCheck(cell.cell)):
            if (self.selectedPlaceObject != None):
                if self.CHECKIFCANPLACE(cell):
                    wall = Wall.Create(self.engine)
                    wall.obj.cell = cell
                    self.engine.CreateNewObject(wall)
                    wall.gameObject.size = cell.size
                    pos = cell.position
                    wall.gameObject.position = Types.Vector3(pos.x, pos.y, 40000)
                    cell.objectLink = wall
                    self.UpdateLinkedMatrix(cell)
                    
                    self.engine.FindObject("GRID").obj.gridMatrix.SetCell(cell.cell, cell)
    def UpdateLinkedMatrix(self, cell):
        if (self.engine.FindObject("GRID").obj.gridMatrix.CellExistsCheck(cell.cell + Types.Vector2(0, -1))):
            cell.aboveCell_OL = self.engine.FindObject("GRID").obj.gridMatrix.GetCell(cell.cell + Types.Vector2(0, -1))
            self.engine.FindObject("GRID").obj.gridMatrix.GetCell(cell.cell + Types.Vector2(0, -1)).belowCell_OL = cell
        else:
            cell.aboveCell_OL = None
        
        if (self.engine.FindObject("GRID").obj.gridMatrix.CellExistsCheck(cell.cell + Types.Vector2(0, 1))):
            cell.belowCell_OL = self.engine.FindObject("GRID").obj.gridMatrix.GetCell(cell.cell + Types.Vector2(0, 1))
            self.engine.FindObject("GRID").obj.gridMatrix.GetCell(cell.cell + Types.Vector2(0, 1)).aboveCell_OL = cell
        else:
            cell.belowCell_OL = None

        if (self.engine.FindObject("GRID").obj.gridMatrix.CellExistsCheck(cell.cell + Types.Vector2(1, 0))):
            cell.rightCell_OL = self.engine.FindObject("GRID").obj.gridMatrix.GetCell(cell.cell + Types.Vector2(1, 0))
            self.engine.FindObject("GRID").obj.gridMatrix.GetCell(cell.cell + Types.Vector2(1, 0)).leftCell_OL = cell
        else:
            cell.rightCell_OL = None

        if (self.engine.FindObject("GRID").obj.gridMatrix.CellExistsCheck(cell.cell + Types.Vector2(-1, 0))):
            cell.leftCell_OL = self.engine.FindObject("GRID").obj.gridMatrix.GetCell(cell.cell + Types.Vector2(-1, 0))
            self.engine.FindObject("GRID").obj.gridMatrix.GetCell(cell.cell + Types.Vector2(-1, 0)).rightCell_OL = cell
        else:
            cell.leftCell_OL = None
    def HANDLEDEMOPLACEMENT(self, cell, demoObj):
        if (self.engine.FindObject("GRID").obj.gridMatrix.CellExistsCheck(cell.cell)):
            if (self.selectedPlaceObject != None):
                demoObj.gameObject.renderEnabled = True
                demoObj.gameObject.color = (255,255,255)
                demoObj.gameObject.size = cell.size
                pos = cell.position
                demoObj.gameObject.position = Types.Vector3(pos.x, pos.y, 400000)
                if self.CHECKIFCANPLACE(cell):
                    demoObj.gameObject.color = (0, 128, 0)
                else:
                    demoObj.gameObject.color = (128, 0, 0)

    def CHECKIFCANPLACE(self, cell):
        condition1 = cell.objectLink == None
        condition2 = False
        cellOffsets = [Types.Vector2(0,1), Types.Vector2(0,-1), Types.Vector2(1,0), Types.Vector2(-1,0)]
        for i in range(4):
            if (self.engine.FindObject("GRID").obj.gridMatrix.CellExistsCheck(cell.cell + cellOffsets[i])):
                if (self.engine.FindObject("GRID").obj.gridMatrix.GetCell(cell.cell + cellOffsets[i]).objectLink != None):
                    condition2 = True
            else:
                if (i == 2):
                    condition2 = True
        return (condition1 and condition2)

#Create needs to be defined for every script in this folder. Everything should be exactly the same except for what is commented below, read that.
class Create():
    def __init__(self, engine):
        self.obj = PlaceWall(engine) #Replace Template with the name of your class
        self.obj.creator = self
    @property
    def gameObject(self):
        return self.obj.gameObject