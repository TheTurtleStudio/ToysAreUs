import math
from GameObjects import GameObject
from MainEngine import Engine, Types #NEEDED. Mainly for Types.GameObject creation.
import pygame
class ToothpickTrap(): #Change this to the name of your script
    def __init__(self, engine):
        self.gameObject = Types.GameObject(engine)
        self.engine: Engine.Engine = engine
        self.creator = None
        self.enemies = None
        self.speed = 700
        self.startSequenceFinished = False
        self.timer = 0
        self.initialTime = 0
        self.elapsedRotation = 0
        self.arm: GameObject.Create = None
        self.Animator = Types.Animator(self.gameObject)
        self.initial = True
        self.trapCreator = None

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
        if self.initial is True:
            self.initial = False
            for i in self.enemies.copy():
                i.Stunned = True
        if self.startSequenceFinished is False:
            self.Animator.AnimationStep("toothpickTrap")
            if self.Animator.finished:
                self.engine.PlaySound("Assets\\Sounds\\toothpick_shoot.mp3")
                for i in self.enemies.copy():
                    i.Stunned = False
                    i.Damage(Types.WeaponTypes.BarrelOfMonkeys.damage)
                self.startSequenceFinished = True
        else:
            self.Destroy()
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
        self.obj: ToothpickTrap = ToothpickTrap(engine) #Replace Template with the name of your class
        self.obj.creator = self

    @property
    def gameObject(self):
        return self.obj.gameObject
