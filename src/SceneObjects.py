from GameObjects import GameObject
from GameObjects import Button
from GameObjects import Draggable
from GameObjects import Grid
from GameObjects import PlaceWall
from GameObjects import PlaceHandler
from MainEngine import Types
import pygame, random

class Objects():
    def __init__(self, engine):
        self.ObjectList = []
        BackGround = GameObject.Create(engine)
        BackGround.gameObject.size = engine._Globals._display
        BackGround.gameObject.color = (106,181,102)
        BackGround.gameObject.name = "BackGround"
        self.ObjectList.append(BackGround)
        BaseWall = GameObject.Create(engine)
        BaseWall.gameObject.size = (75, engine._Globals._display[1]-140)
        BaseWall.gameObject.color = (50,50,50)
        BaseWall.gameObject.position = Types.Vector3(engine._Globals._display[0]-75, 120, 1)
        BaseWall.gameObject.name = "BaseWall"
        
        
        self.ObjectList.append(BaseWall)
        TopBar = GameObject.Create(engine)
        TopBar.gameObject.size = (engine._Globals._display[0], 100)
        TopBar.gameObject.color = (200,200,200)
        TopBar.gameObject.position = Types.Vector3(0, 0, 4096)
        self.ObjectList.append(TopBar)
        WaveTitle = GameObject.Create(engine)
        
        WaveTitle.gameObject.size = (60, 60)
        WaveTitle.gameObject.position = Types.Vector3((engine._Globals._display[0]/2) - (WaveTitle.gameObject.size.x / 2), 0, 4097)
        WaveTitle.gameObject.color = TopBar.gameObject.color
        WaveTitle.gameObject.text = "WAVE"
        WaveTitle.gameObject.fontSize = 30
       
        
        self.ObjectList.append(WaveTitle)
        tepmColorIndex = [(255,0,0), (255,0,0), (255,0,0), (128,128,128), (255,0,0), (255,0,0), (255,0,0), (0,0,0), (0,255,0), (128,0,128), (0,0,0), (255,255,0)]
        for buttonNum in range(3): #Red ("button"), Gray ("Garbage"), Black ("Nothing/Space") Green ("Start Button") Purple ("Money text and stuff") Yellow ("HealthBar")
            MyButton = PlaceWall.Create(engine)
            MyButton.gameObject.size = (60, 60)
            MyButton.gameObject.color = tepmColorIndex[buttonNum]
            MyButton.gameObject.position = Types.Vector3((buttonNum * 60) + ((buttonNum + 1) * 20), 5, 4097)
            MyButton.gameObject.collisionLayer = engine._Globals.CollisionLayer.UI
            MyButton.obj.assignedNumber = buttonNum
            self.ObjectList.append(MyButton)
        BoardGrid = Grid.Create(engine)
        BoardGrid.gameObject.name = 'GRID'
        BoardGrid.gameObject.size = ((engine._Globals._display[0]-BaseWall.gameObject.size.x) * 0.7, BaseWall.gameObject.size.y-10)
        BoardGrid.gameObject.position = ((engine._Globals._display[0]-BaseWall.gameObject.size.x) * 0.3,BaseWall.gameObject.position.y+5,8192)
        BoardGrid.gameObject.color = (96, 171, 92)
        self.ObjectList.append(BoardGrid)
        PlaceObjectHandler = PlaceHandler.Create(engine)
        PlaceObjectHandler.gameObject.name = "PLACEHANDLER"
        self.ObjectList.append(PlaceObjectHandler)

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