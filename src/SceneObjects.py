from GameObjects import GameObject
from GameObjects import Button
from GameObjects import Draggable
from GameObjects import Grid
from GameObjects import PlaceWall
from GameObjects import PlaceHandler
from GameObjects import RemoveTile
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
        TopBar.gameObject.color = (128,128,128)
        TopBar.gameObject.position = Types.Vector3(0, 0, 4083)
        TopBarBorder = GameObject.Create(engine)
        TopBarBorder.gameObject.size = TopBar.gameObject.size + Types.Vector2(0, 1)
        TopBarBorder.gameObject.position = TopBar.gameObject.position - Types.Vector3(0, 0, 1)
        TopBarBorder.gameObject.color = (20,20,20)
        self.ObjectList.append(TopBar)
        self.ObjectList.append(TopBarBorder)
        
        WaveTitle = GameObject.Create(engine)
        
        WaveTitle.gameObject.size = (60, 60)
        WaveTitle.gameObject.position = Types.Vector3((engine._Globals._display[0]/2) - (WaveTitle.gameObject.size.x / 2), 0, 4097)
        WaveTitle.gameObject.color = TopBar.gameObject.color
        WaveTitle.gameObject.text = "WAVE"
        WaveTitle.gameObject.fontSize = 30
       
        
        self.ObjectList.append(WaveTitle)
        WallsTitle = GameObject.Create(engine)
        for buttonNum in range(3): #Red ("button"), Gray ("Garbage"), Black ("Nothing/Space") Green ("Start Button") Purple ("Money text and stuff") Yellow ("HealthBar")
            WallButton = PlaceWall.Create(engine)
            WallButtonHighlight = GameObject.Create(engine)
            WallButton.gameObject.size = (60, 60)
            WallButtonHighlight.gameObject.size = WallButton.gameObject.size + Types.Vector2(6, 6)
            WallButton.gameObject.color = (255,255,255)
            WallButtonHighlight.gameObject.color = (20,20,20)
            WallButton.gameObject.position = Types.Vector3((buttonNum * 60) + ((buttonNum + 1) * 20), TopBar.gameObject.size.y-WallButton.gameObject.size.y-10, 4097)
            WallButtonHighlight.gameObject.position = WallButton.gameObject.position - Types.Vector3(3, 3, 1)
            WallButton.gameObject.collisionLayer = engine._Globals.CollisionLayer.UI
            WallButtonHighlight.gameObject.renderEnabled = False
            WallButton.obj.highlightedIndicator = WallButtonHighlight
            if buttonNum == 1:
                WallsTitle.gameObject.size = (60, 60)
                WallsTitle.gameObject.position = WallButton.gameObject.position + Types.Vector3(0,-WallButton.gameObject.position.y,-5)
                WallsTitle.gameObject.color = TopBar.gameObject.color
                WallsTitle.gameObject.text = "WALLS"
                WallsTitle.gameObject.fontSize = 20
                self.ObjectList.append(WallsTitle)
            self.ObjectList.append(WallButton)
            self.ObjectList.append(WallButtonHighlight)
        
        DestroyWallButton = RemoveTile.Create(engine)
        DestroyWallButton.gameObject.size = (60, 60)
        DestroyWallButton.gameObject.color = (255,255,255)
        DestroyWallButton.gameObject.position = Types.Vector3(300, TopBar.gameObject.size.y-WallButton.gameObject.size.y-10, 4097)
        DestroyWallButton.gameObject.collisionLayer = engine._Globals.CollisionLayer.UI
        DestroyWallButton.gameObject.image = "Assets\\trashcanClosed.png"
        DestroyWallButton.gameObject.name = "TRASHCANBUTTON"
        self.ObjectList.append(DestroyWallButton)
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