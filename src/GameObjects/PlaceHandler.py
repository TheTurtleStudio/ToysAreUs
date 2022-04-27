from MainEngine import Types #NEEDED. Mainly for Types.GameObject creation.
from GameObjects import Wall
import pygame
class PlaceWall(): #Change this to the name of your script
    def __init__(self, engine):
        self.gameObject = Types.GameObject(engine)
        self.engine = engine
        self.selectedPlaceObject = None
        self.gameObject.renderEnabled = False
    def HANDLEPLACEMENT(self, cell):
        if (self.selectedPlaceObject != None):
            if (cell.objectLink == None):
                wall = Wall.Create(self.engine)
                self.engine.CreateNewObject(wall)
                wall.gameObject.size = cell.size
                pos = cell.position
                wall.gameObject.position = Types.Vector3(pos.x, pos.y, 40000)
                cell.objectLink = wall
                self.engine.FindObject("GRID").obj.gridMatrix.SetCell(cell.cell, cell)
            else:
                print("Can't place!")
    def HANDLEDEMOPLACEMENT(self, cell, demoObj):
        if (self.selectedPlaceObject != None):
            demoObj.gameObject.renderEnabled = True
            demoObj.gameObject.color = (255,255,255)
            demoObj.gameObject.size = cell.size
            pos = cell.position
            demoObj.gameObject.position = Types.Vector3(pos.x, pos.y, 400000)
            if (cell.objectLink == None):
                demoObj.gameObject.color = (0, 128, 0)
            else:
                demoObj.gameObject.color = (128, 0, 0)

#Create needs to be defined for every script in this folder. Everything should be exactly the same except for what is commented below, read that.
class Create():
    def __init__(self, engine):
        self.obj = PlaceWall(engine) #Replace Template with the name of your class
    @property
    def gameObject(self):
        return self.obj.gameObject