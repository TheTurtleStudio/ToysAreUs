import GameObjects
from MainEngine import Types #NEEDED. Mainly for Types.GameObject creation.
from GameObjects import GameObject
import pygame
class Healthbar(): #Change this to the name of your script
    def __init__(self, engine):
        self.gameObject = Types.GameObject(engine)
        self.engine = engine
        self.creator = None
        self._health = -1
        self._maxHealth = -1
        self._fullnessBar = GameObject.Create(engine)
        self.engine.CreateNewObject(self._fullnessBar)

    @property
    def health(self):
        return self._health
    @health.setter
    def health(self, value: float):
        self._health = self._maxHealth if (value > self._maxHealth) else value
        self._health = 0 if (value < 0) else value
        self._UpdateBar()
    @property
    def maxHealth(self):
        return self._maxHealth
    @health.setter
    def maxHealth(self, value: float):
        self._maxHealth = value
        self._UpdateBar()

    def _UpdateBar(self):
        if self._health < 0: #Maximize health if it wasn't set
            self._health = self._maxHealth
        if self._maxHealth <= 0:
            return
        
        self._fullnessBar.gameObject.size = Types.Vector2(self.gameObject.size.x * (self._health / self._maxHealth), self._fullnessBar.gameObject.size.y)
        
#Create needs to be defined for every script in this folder. Everything should be exactly the same except for what is commented below, read that.
class Create():
    def __init__(self, engine):
        self.obj = Healthbar(engine) #Replace Template with the name of your class
        self.obj.creator = self
    @property
    def gameObject(self):
        return self.obj.gameObject
