from MainEngine import Types #NEEDED. Mainly for Types.GameObject creation.
import pygame
class GameObject(): #Change this to the name of your script
    def __init__(self, engine):
        self.gameObject = Types.GameObject(engine)
        self.engine = engine
        self.Start()

    def Start(self): #Called when the object is added to the scene.
        pass

    def Update(self): #This is called every rendercycle
        pass
#Create needs to be defined for every script in this folder. Everything should be exactly the same except for what is commented below, read that.
class Create():
    def __init__(self, engine):
        self.obj = GameObject(engine) #Replace Template with the name of your class
    @property
    def gameObject(self):
        return self.obj.gameObject
