from GameObjects import GameObject
from MainEngine import Types #NEEDED. Mainly for Types.GameObject creation.
import pygame
from MainEngine.Engine import Engine


class PlaceWeapon(): #Change this to the name of your script
    def __init__(self, engine: Engine):
        self.gameObject = Types.GameObject(engine)
        self.engine = engine
        self.creator = None
        self.highlightedIndicator: GameObject.Create = None
        self.objectType: Types.WeaponTypes._GENERIC = None
        self.infoBox: GameObject.Create = None

    def Update(self): #This is called every rendercycle
        if self.engine.timeScale == 0:
            return
        if (self.engine.Input.TestFor.RIGHTMOUSEDOWN()):
            if (self.gameObject.sprite.rect in self.engine.Collisions.PointCollide(self.engine.Input.TestFor.MOUSEPOS(), [Types.CollisionLayer.UI])):
                if (self.engine.FindObject("PLACEHANDLER").obj.selectedPlaceObject != None):
                    self.engine.FindObject("PLACEHANDLER").obj.selectedPlaceObject.highlightedIndicator.gameObject.renderEnabled = False
                self.engine.FindObject("GRID").obj.placeRotation = 0
                self.engine.FindObject("PLACEHANDLER").obj.selectedPlaceObject = self if (self.engine.FindObject("PLACEHANDLER").obj.selectedPlaceObject != self) else None
                self.highlightedIndicator.gameObject.renderEnabled = (self.engine.FindObject("PLACEHANDLER").obj.selectedPlaceObject == self)
                
                self.engine.FindObject("PLACEHANDLER").obj.removingTile = False
                self.engine.FindObject("TRASHCANBUTTON").obj.UpdateImage()
                self.engine.PlaySound("Assets\\Sounds\\place.mp3")
        if (self.gameObject.sprite.rect in self.engine.Collisions.PointCollide(self.engine.Input.TestFor.MOUSEPOS(), [Types.CollisionLayer.UI])):
            if not self.infoBox.gameObject.renderEnabled:
                self.infoBox.gameObject.renderEnabled = True
        else:
            if self.infoBox.gameObject.renderEnabled:
                self.infoBox.gameObject.renderEnabled = False



#Create needs to be defined for every script in this folder. Everything should be exactly the same except for what is commented below, read that.
class Create():
    def __init__(self, engine):
        self.obj: PlaceWeapon = PlaceWeapon(engine) #Replace Template with the name of your class
        self.obj.creator = self
    @property
    def gameObject(self) -> Types.GameObject:
        return self.obj.gameObject