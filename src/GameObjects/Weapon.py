from MainEngine import Types #NEEDED. Mainly for Types.GameObject creation.
import pygame
class Weapon(): #Change this to the name of your script
    def __init__(self, engine):
        self.gameObject = Types.GameObject(engine)
        self.engine = engine
        self.creator = None
        self.cell = None
        self.maxHealth = None
        self.health = None
    def DestroyWall(self):
        self._UpdateLinkedMatrix()
        self.engine._Globals.sceneObjectsArray.remove(self.creator)
        del self
    def _UpdateLinkedMatrix(self):

        if (self.cell == None):
            return
        if (self.engine.FindObject("GRID").obj.gridMatrix.CellExistsCheck(self.cell.cell + Types.Vector2(0, -1))):
            self.engine.FindObject("GRID").obj.gridMatrix.GetCell(self.cell.cell + Types.Vector2(0, -1)).belowCell_OL = None
        
        if (self.engine.FindObject("GRID").obj.gridMatrix.CellExistsCheck(self.cell.cell + Types.Vector2(0, 1))):
            self.engine.FindObject("GRID").obj.gridMatrix.GetCell(self.cell.cell + Types.Vector2(0, 1)).aboveCell_OL = None

        if (self.engine.FindObject("GRID").obj.gridMatrix.CellExistsCheck(self.cell.cell + Types.Vector2(1, 0))):
            self.engine.FindObject("GRID").obj.gridMatrix.GetCell(self.cell.cell + Types.Vector2(1, 0)).leftCell_OL = None

        if (self.engine.FindObject("GRID").obj.gridMatrix.CellExistsCheck(self.cell.cell + Types.Vector2(-1, 0))):
            self.engine.FindObject("GRID").obj.gridMatrix.GetCell(self.cell.cell + Types.Vector2(-1, 0)).rightCell_OL = None
        self.cell.objectLink = None
#Create needs to be defined for every script in this folder. Everything should be exactly the same except for what is commented below, read that.
class Create():
    def __init__(self, engine):
        self.obj = Weapon(engine) #Replace Template with the name of your class
        self.obj.creator = self
    @property
    def gameObject(self):
        return self.obj.gameObject
