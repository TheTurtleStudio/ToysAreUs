from MainEngine import Types #NEEDED. Mainly for Types.GameObject creation.
import pygame
class PlaceWall(): #Change this to the name of your script
    def __init__(self, engine):
        self.gameObject = Types.GameObject(engine)
        self.engine = engine

    def Start(self):
        self.pressed = False
        self.offset = None
        self.canDrag = False

    def Update(self): #This is called every rendercycle
        if (self.engine.Input.TestFor.RIGHTMOUSEDOWN()):
            if (self.gameObject.sprite.rect in self.engine.Collisions.PointCollide(self.engine.Input.TestFor.MOUSEPOS(), [self.engine._Globals.CollisionLayer.UI])):
                if (self.engine.FindObject("PLACEHANDLER").obj.selectedPlaceObject is not None):
                    self.engine.FindObject("PLACEHANDLER").obj.selectedPlaceObject.gameObject.color = (255,255,255)
                self.engine.FindObject("PLACEHANDLER").obj.selectedPlaceObject = self if (self.engine.FindObject("PLACEHANDLER").obj.selectedPlaceObject != self) else None
                self.gameObject.color = (105,0,0) if (self.engine.FindObject("PLACEHANDLER").obj.selectedPlaceObject != self) else (255,255,255)



#Create needs to be defined for every script in this folder. Everything should be exactly the same except for what is commented below, read that.
class Create():
    def __init__(self, engine):
        self.obj = PlaceWall(engine) #Replace Template with the name of your class
    @property
    def gameObject(self):
        return self.obj.gameObject