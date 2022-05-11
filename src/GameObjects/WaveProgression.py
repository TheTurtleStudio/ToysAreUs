import random
from GameObjects import Enemy
from MainEngine import Engine, Types #NEEDED. Mainly for Types.GameObject creation.
import pygame
class WaveProgression(): #Change this to the name of your script
    def __init__(self, engine):
        self.gameObject = Types.GameObject(engine)
        self.engine: Engine.Engine = engine
        self.creator = None
        self.wave = 0
        self.spawnInterval = 0
        self.lastSpawnTime = 0
        self.grid = None

    def Update(self):
        if self.engine.timeScale == 0 or (self.spawnInterval <= 0):
            return
        self.WaveStep()
    
    def WaveStep(self):
        if (self.lastSpawnTime + self.spawnInterval) <= self.engine.GetTotalTime():
            self.lastSpawnTime = self.engine.GetTotalTime()
            enemy = Enemy.Create(self.engine)
            enemy.obj.enemyType = random.choice([Types.EnemyTypes.TeddyBear, Types.EnemyTypes.ToyCar, Types.EnemyTypes.ToySoldier])
            enemy.gameObject.size = Types.Vector2(self.grid.gameObject.size.y / self.grid.obj.gridSize.y, self.grid.gameObject.size.y / self.grid.obj.gridSize.y)
            self.engine.CreateNewObject(enemy)

    def ProgressWave(self):
        self.wave += 1
        self.engine.FindObject("MONEYMANAGEMENT").obj.money += 50
        self.StartWave(self.wave)

    def StartWave(self, wave: int):
        print(f"Starting wave {wave}")
        self.lastSpawnTime = 0
        self.spawnInterval = 1 / (wave * 0.09)
        self.engine.FindObject("WAVEINDICATOR").obj.gameObject.text = str(wave)
        self.EndWave()

    def EndWave(self):
        self.engine.FindObject("WAVESTARTBUTTON").obj.gameObject.image = "PLAYCLICKABLE"
        self.engine.FindObject("WAVESTARTBUTTON").obj.activated = False
        
#Create needs to be defined for every script in this folder. Everything should be exactly the same except for what is commented below, read that.
class Create():
    def __init__(self, engine):
        self.obj: WaveProgression = WaveProgression(engine) #Replace Template with the name of your class
        self.obj.creator = self
    @property
    def gameObject(self):
        return self.obj.gameObject
