from GameObjects import GameObject
from GameObjects.Wall import Wall
from MainEngine import Types #NEEDED. Mainly for Types.GameObject creation.
import pygame
class Weapon(): #Change this to the name of your script
    def __init__(self, engine):
        self.gameObject = Types.GameObject(engine)
        self.engine = engine
        self.creator = None
        self.cell = None
        self.maxHealth = None
        self.health = None
        self.hasBase = None
        self.baseGO = None
    def Destroy(self):
        self._UpdateLinkedMatrix()
        self.engine._Globals.sceneObjectsArray.remove(self.creator)
        if self.self.hasBase:
            self.engine._Globals.sceneObjectsArray.remove(self.baseGO)
    def _UpdateLinkedMatrix(self):
        if (self.cell == None):
            return
        self.cell.weaponLink = None
    def Update(self):
        if self.engine.timeScale == 0:
            return
        pass #Do the firing and killing enemies here


#Create needs to be defined for every script in this folder. Everything should be exactly the same except for what is commented below, read that.
class Create():
    def __init__(self, engine):
        self.obj = Weapon(engine) #Replace Template with the name of your class
        self.obj.creator = self
    @property
    def gameObject(self):
        return self.obj.gameObject
