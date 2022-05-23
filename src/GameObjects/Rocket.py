from MainEngine import Engine, Types #NEEDED. Mainly for Types.GameObject creation.
import pygame
class Rocket(): #Change this to the name of your script
    def __init__(self, engine):
        self.gameObject = Types.GameObject(engine)
        self.engine: Engine.Engine = engine
        self.creator = None
        self.enemy = None
        self.speed = 500
        self.startSequenceFinished = False
        self.flipped = False

    def Destroy(self):
        self.engine._Globals.sceneObjectsArray.remove(self.creator)
        self.gameObject.sprite.kill()
        del self.gameObject
        self.engine = None
        del self.creator
        self.creator = None

    def Update(self):
        if self.enemy.exists is False:
            self.Destroy()
        if self.startSequenceFinished is False:
            self.gameObject.position.y -= self.speed * self.engine.GetDeltaTime() * 0.85
            if self.gameObject.position.y <= -self.speed * 0.85:
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
        
        
            

#Create needs to be defined for every script in this folder. Everything should be exactly the same except for what is commented below, read that.
class Create():
    def __init__(self, engine):
        self.obj: Rocket = Rocket(engine) #Replace Template with the name of your class
        self.obj.creator = self

    @property
    def gameObject(self):
        return self.obj.gameObject
