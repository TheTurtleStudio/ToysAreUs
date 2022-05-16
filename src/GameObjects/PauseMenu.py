from MainEngine import Types #NEEDED. Mainly for Types.GameObject creation.
import pygame
from MainEngine import Engine

class PauseMenu(): #Change this to the name of your script
    def __init__(self, engine):
        self.gameObject = Types.GameObject(engine)
        self.engine: Engine.Engine = engine
        self.creator = None
        self.pausedState = False
        self.elements = [self]

    def Start(self):
        self.gameObject.image = "40PERCENTTRANS"
        for element in self.elements:
            element.gameObject.renderEnabled = False

    def Update(self):
        if self.engine.GetUniversal("STARTED") == False:
            return
        if self.engine.Input.TestFor._testFor(768)[0] is True and (self.engine.FindObject("GAMEOVER").obj.active == False):
            self.pausedState = not self.pausedState
            if self.pausedState is True:
                for element in self.elements:
                    element.gameObject.renderEnabled = True
                self.engine.timeScale = 0
            else:
                for element in self.elements:
                    element.gameObject.renderEnabled = False
                self.engine.timeScale = 1
            #self.engine.Reload()


#Create needs to be defined for every script in this folder. Everything should be exactly the same except for what is commented below, read that.
class Create():
    def __init__(self, engine):
        self.obj: PauseMenu = PauseMenu(engine) #Replace Template with the name of your class
        self.obj.creator = self
    @property
    def gameObject(self):
        return self.obj.gameObject
