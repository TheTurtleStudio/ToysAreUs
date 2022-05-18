from MainEngine import Engine, Types #NEEDED. Mainly for Types.GameObject creation.
import pygame
class Rocket(): #Change this to the name of your script
    def __init__(self, engine):
        self.gameObject = Types.GameObject(engine)
        self.engine: Engine.Engine = engine
        self.creator = None
        self.enemy = None
        self.speed = 0

    def Update(self):
        if self.enemy == None:
            return

        self.gameObject.position.x = self.enemy.gameObject.position.x
        self.gameObject.position.y += self.speed * self.engine.GetDeltaTime()

#Create needs to be defined for every script in this folder. Everything should be exactly the same except for what is commented below, read that.
class Create():
    def __init__(self, engine):
        self.obj: Rocket = Rocket(engine) #Replace Template with the name of your class
        self.obj.creator = self

    @property
    def gameObject(self):
        return self.obj.gameObject
