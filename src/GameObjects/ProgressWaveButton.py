from GameObjects.WaveProgression import WaveProgression
from MainEngine import Types #NEEDED. Mainly for Types.GameObject creation.
import pygame

from MainEngine import Engine
class Button(): #Change this to the name of your script
    def __init__(self, engine):
        self.gameObject = Types.GameObject(engine)
        self.engine: Engine.Engine = engine
        self.creator = None
        self.activated = False

    def Start(self):
        self.waveProgressionRef: WaveProgression = self.engine.FindObject("WAVEPROGRESSION").obj
        self.gameObject.image = "PLAYCLICKABLE"

    def Update(self): #This is called every rendercycle
        if self.engine.timeScale == 0:
            return
        if (self.engine.Input.TestFor.RIGHTMOUSEDOWN()):
            if (self.gameObject.sprite.rect in self.engine.Collisions.PointCollide(self.engine.Input.TestFor.MOUSEPOS(), [Types.CollisionLayer.UI])) and (self.engine.FindObject("GAMEOVER").obj.active == False):
                if not self.activated:
                    self.activated = True
                    self.gameObject.image = "PLAYNOTCLICKABLE"
                    self.waveProgressionRef.ProgressWave()
                
                

#Create needs to be defined for every script in this folder. Everything should be exactly the same except for what is commented below, read that.
class Create():
    def __init__(self, engine):
        self.obj = Button(engine) #Replace Template with the name of your class
        self.obj.creator = self
    @property
    def gameObject(self):
        return self.obj.gameObject