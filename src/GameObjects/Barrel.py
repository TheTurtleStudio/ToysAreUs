import math
from GameObjects import GameObject
from MainEngine import Engine, Types #NEEDED. Mainly for Types.GameObject creation.
import pygame
class Barrel(): #Change this to the name of your script
    def __init__(self, engine):
        self.gameObject = Types.GameObject(engine)
        self.engine: Engine.Engine = engine
        self.creator = None
        self.enemies = None
        self.speed = 400
        self.startSequenceFinished = False
        self.elapsedRotation = 0
        self.arm: GameObject.Create = None

    def Destroy(self):
        self.engine._Globals.sceneObjectsArray.remove(self.creator)
        self.gameObject.sprite.kill()
        self.arm.gameObject.sprite.kill()
        del self.arm
        del self.gameObject
        self.engine = None
        del self.creator
        self.creator = None

    def Update(self):
        if self.elapsedRotation >= 360:
            for i in self.enemies:
                self.enemies.remove(i)
                i.Stunned = False
                i.Damage(Types.WeaponTypes.BarrelOfMonkeys.damage)
            self.arm.obj.Destroy()
            self.Destroy()
        
        self.arm.gameObject.position = self.gameObject.position + Types.Vector3(self.arm.gameObject.size.x / 2, 0) + (Types.Vector3(math.cos(math.radians(-self.elapsedRotation - 90)), math.sin(math.radians(-self.elapsedRotation - 90)), 0.1) * self.gameObject.size.y)

        self.elapsedRotation += self.speed * self.engine.GetDeltaTime()
        self.arm.gameObject.rotation = self.elapsedRotation
        '''if self.startSequenceFinished is False:
            self.gameObject.position.y -= self.speed * self.engine.GetDeltaTime()
            if self.gameObject.position.y <= -self.speed:
                self.startSequenceFinished = True
            return
        elif self.gameObject.position.y >= self.enemy.gameObject.position.y:
            self.enemy.Targeted = False
            self.enemy.Damage(Types.WeaponTypes.BottleRocket.damage)
            self.Destroy()
        if self.flipped is False:
            self.flipped = True
            self.gameObject.rotation = 180
        self.gameObject.position.x = self.enemy.gameObject.position.x
        self.gameObject.position.y += self.speed * self.engine.GetDeltaTime()
        if self.enemy == None:
            self.Destroy()'''
        
            

#Create needs to be defined for every script in this folder. Everything should be exactly the same except for what is commented below, read that.
class Create():
    def __init__(self, engine):
        self.obj: Barrel = Barrel(engine) #Replace Template with the name of your class
        self.obj.creator = self

    @property
    def gameObject(self):
        return self.obj.gameObject
