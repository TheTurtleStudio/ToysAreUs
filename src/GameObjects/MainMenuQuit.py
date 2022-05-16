from MainEngine import Types #NEEDED. Mainly for Types.GameObject creation.
import pygame
from MainEngine import Engine

class MainMenuQuit(): #Change this to the name of your script
    def __init__(self, engine):
        self.gameObject = Types.GameObject(engine)
        self.engine: Engine.Engine = engine
        self.creator = None
        self.pausedState = False
        self.elements = [self]


    def Update(self):
        if self.engine.GetUniversal("STARTED") == True:
            return
        if (self.engine.Input.TestFor.RIGHTMOUSEDOWN()):
            if (self.gameObject.sprite.rect in self.engine.Collisions.PointCollide(self.engine.Input.TestFor.MOUSEPOS(), [Types.CollisionLayer.UI])):
                self.engine.Quit()


#Create needs to be defined for every script in this folder. Everything should be exactly the same except for what is commented below, read that.
class Create():
    def __init__(self, engine):
        self.obj: MainMenuQuit = MainMenuQuit(engine) #Replace Template with the name of your class
        self.obj.creator = self
    @property
    def gameObject(self):
        return self.obj.gameObject
