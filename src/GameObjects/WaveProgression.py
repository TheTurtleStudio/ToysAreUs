from MainEngine import Types #NEEDED. Mainly for Types.GameObject creation.
import pygame
class WaveProgression(): #Change this to the name of your script
    def __init__(self, engine):
        self.gameObject = Types.GameObject(engine)
        self.engine = engine
        self.creator = None
        self.wave = 0

    def Update(self):
        if self.engine.timeScale == 0:
            return
    
    def ProgressWave(self):
        self.wave += 1
        self.engine.FindObject("MONEYMANAGEMENT").obj.money += 50
        self.StartWave(self.wave)

    def StartWave(self, wave):
        print(f"Starting wave {wave}")
        self.EndWave()

    def EndWave(self):
        self.engine.FindObject("WAVESTARTBUTTON").obj.gameObject.renderEnabled = True
#Create needs to be defined for every script in this folder. Everything should be exactly the same except for what is commented below, read that.
class Create():
    def __init__(self, engine):
        self.obj: WaveProgression = WaveProgression(engine) #Replace Template with the name of your class
        self.obj.creator = self
    @property
    def gameObject(self):
        return self.obj.gameObject
