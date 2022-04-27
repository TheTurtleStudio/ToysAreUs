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
            print("link")
            print(self.engine.FindObject("GRID").obj.gridMatrix.GetCell(cell.cell).objectLink)
            if (cell.objectLink == None):
                wall = Wall.Create(self.engine)
                self.engine.CreateNewObject(wall)
                wall.gameObject.size = cell.size
                pos = self.engine.FindObject("GRID").obj.gridMatrix.GetCell(cell.cell).position
                wall.gameObject.position = Types.Vector3(pos.x, pos.y, 400000)
                cell.objectLink = wall
                self.engine.FindObject("GRID").obj.gridMatrix.SetCell(cell.cell, cell)
                print(self.engine.FindObject("GRID").obj.gridMatrix.GetCell(cell.cell).objectLink)


                print("i totally just made that wall")
            else:
                print("can't do that man, es illegal")

#Create needs to be defined for every script in this folder. Everything should be exactly the same except for what is commented below, read that.
class Create():
    def __init__(self, engine):
        self.obj = PlaceWall(engine) #Replace Template with the name of your class
    @property
    def gameObject(self):
        return self.obj.gameObject