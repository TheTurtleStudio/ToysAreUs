from GameObjects import GameObject
from GameObjects import Button
from MainEngine import Types
import pygame, random

class Objects():
    def __init__(self, engine):
        self.ObjectList = []
        BackGround = GameObject.Create(engine)
        BackGround.gameObject.size = engine._Globals._display
        BackGround.gameObject.color = (106,181,102)
        self.ObjectList.append(BackGround)
        BaseWall = GameObject.Create(engine)
        BaseWall.gameObject.size = (50, engine._Globals._display[1])
        BaseWall.gameObject.position = Types.Vector3(engine._Globals._display[0]-50, 0, 0)
        BaseWall.gameObject.color = (50,50,50)
        self.ObjectList.append(BaseWall)
        TopBar = GameObject.Create(engine)
        TopBar.gameObject.size = (engine._Globals._display[0], 100)
        TopBar.gameObject.color = (50,50,50)
        TopBar.gameObject.position = Types.Vector3(0, 0, 4096)
        self.ObjectList.append(TopBar)
        for buttonNum in range(3):
            MyButton = Button.Create(engine)
            MyButton.gameObject.size = (60, 60)
            MyButton.gameObject.color = (255,0,0)
            MyButton.gameObject.position = Types.Vector3((buttonNum * 60) + ((buttonNum + 1) * 20), 20, 4097)
            MyButton.gameObject.collisionLayer = engine._Globals.CollisionLayer.UI
            MyButton.obj.assignedNumber = buttonNum
            self.ObjectList.append(MyButton)

    def get(self):
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