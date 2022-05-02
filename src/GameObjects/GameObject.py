from MainEngine import Types #NEEDED. Mainly for Types.GameObject creation.
import pygame
class GameObject(): #Change this to the name of your script
    def __init__(self, engine):
        self.gameObject = Types.GameObject(engine)
        self.engine = engine
        self.creator = None

#Create needs to be defined for every script in this folder. Everything should be exactly the same except for what is commented below, read that.
class Create():
    def __init__(self, engine):
        self.obj: GameObject = GameObject(engine) #Replace Template with the name of your class
        self.obj.creator = self
    @property
    def gameObject(self):
        return self.obj.gameObject
