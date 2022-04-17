from MainEngine import Types #NEEDED. Mainly for Types.GameObject creation.
import pygame
class GameObject(): #Change this to the name of your script
    def __init__(self, engine):
        self.gameObject = Types.GameObject(engine)
        self.engine = engine
        self.Start()

    def Start(self): #Called when the object is added to the scene.
        self.speed = 20
        self.sizeIncrease = 0

    def Update(self): #This is called every rendercycle
        #Below is some example code that moves the square. The attached GameObject.
        left = -1 if self.engine.Input.TestFor.KEYDOWN(pygame.K_a) else 0
        right = 1 if self.engine.Input.TestFor.KEYDOWN(pygame.K_d) else 0
        up = -1 if self.engine.Input.TestFor.KEYDOWN(pygame.K_w) else 0
        down = 1 if self.engine.Input.TestFor.KEYDOWN(pygame.K_s) else 0
        self.gameObject.position += self.speed * Types.Vector3((left+right), (up+down), 0) * self.engine.GetDeltaTime()
#Create needs to be defined for every script in this folder. Everything should be exactly the same except for what is commented below, read that.
class Create():
    def __init__(self, engine):
        self.obj = GameObject(engine) #Replace Template with the name of your class
    @property
    def gameObject(self):
        return self.obj.gameObject