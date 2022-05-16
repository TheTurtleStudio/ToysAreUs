from MainEngine import Types #NEEDED. Mainly for Types.GameObject creation.
import pygame
from MainEngine import Engine
from GameObjects import GameObject

class GameOverScreen(): #Change this to the name of your script
    def __init__(self, engine):
        self.gameObject = Types.GameObject(engine)
        self.engine: Engine.Engine = engine
        self.creator = None
        self.elements = [self]
        self.active = False
        self.trans = 255

    def Start(self):
        self.gameObject.image = "40PERCENTTRANS"
        for element in self.elements:
            element.gameObject.renderEnabled = False

    def Update(self):
        if self.engine.GetUniversal("STARTED") == False:
            return
        if self.active and (self.trans != 0):
            self.trans -= 1020 * self.engine.GetDeltaTimeRAW()
            if self.trans < 0:
                self.trans = 0
            for element in self.elements:
                element.gameObject.transparency = self.trans

    def Indicate(self):
        for element in self.elements:
            self.engine.timeScale = 0
            element.gameObject.transparency = 255
            element.gameObject.renderEnabled = True
        self.active = True


#Create needs to be defined for every script in this folder. Everything should be exactly the same except for what is commented below, read that.
class Create():
    def __init__(self, engine):
        self.obj: GameOverScreen = GameOverScreen(engine) #Replace Template with the name of your class
        self.obj.creator = self
    @property
    def gameObject(self):
        return self.obj.gameObject
