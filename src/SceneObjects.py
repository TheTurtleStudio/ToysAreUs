from GameObjects import GameObject
import pygame, random

class Objects():
    def __init__(self, engine):
        self.ObjectList = []
        BackGround = GameObject.Create(engine)
        BackGround.gameObject.size = engine._Globals._display
        BackGround.gameObject.color = (106,181,102)
        self.ObjectList.append(BackGround)
        Wall = GameObject.Create(engine)
        Wall.gameObject.size = (50, engine._Globals._display[0])
        Wall.gameObject.color = (50,50,50)
        self.ObjectList.append(Wall)
    def get(self):
        #return (self.test1, self.test2, self.test3, self.test4)
        return tuple(self.ObjectList)
class Injections():
    def __init__(self):
        self.caption = "ToysWereUs"
        self.abstract = [
            "#This is raw code to be after all other injections are made. Yes, I know this is vulnerable to ACE and very unsafe in general. No, I don't care. Why? Because I'm a thug.",
            "#It's pretty intuitive, just put every piece of code encapsulated in a string as a new item in the array.",
            "#You can really just delete all this, just needed to explain somewhat what the hell this is.",
            "print(\"Injections complete\") #This is for debugging though!"
        ]