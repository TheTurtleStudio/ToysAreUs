from MainEngine import Types #NEEDED. Mainly for Types.GameObject creation.
import pygame
class PlaceWall(): #Change this to the name of your script
    def __init__(self, engine):
        self.gameObject = Types.GameObject(engine)
        self.engine = engine
        self.creator = None
        self.highlightedIndicator = None

    def Update(self): #This is called every rendercycle
        if (self.engine.Input.TestFor.RIGHTMOUSEDOWN()):
            if (self.gameObject.sprite.rect in self.engine.Collisions.PointCollide(self.engine.Input.TestFor.MOUSEPOS(), [self.engine._Globals.CollisionLayer.UI])):
                if (self.engine.FindObject("PLACEHANDLER").obj.selectedPlaceObject != None):
                    self.engine.FindObject("PLACEHANDLER").obj.selectedPlaceObject.highlightedIndicator.gameObject.renderEnabled = False
                self.engine.FindObject("PLACEHANDLER").obj.selectedPlaceObject = self if (self.engine.FindObject("PLACEHANDLER").obj.selectedPlaceObject != self) else None
                self.highlightedIndicator.gameObject.renderEnabled = (self.engine.FindObject("PLACEHANDLER").obj.selectedPlaceObject == self)
                
                self.engine.FindObject("PLACEHANDLER").obj.removingTile = False
                self.engine.FindObject("TRASHCANBUTTON").obj.UpdateImage()



#Create needs to be defined for every script in this folder. Everything should be exactly the same except for what is commented below, read that.
class Create():
    def __init__(self, engine):
        self.obj = PlaceWall(engine) #Replace Template with the name of your class
        self.obj.creator = self
    @property
    def gameObject(self):
        return self.obj.gameObject