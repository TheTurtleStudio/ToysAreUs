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
        engine.AddImageAsset("TRASH_CLOSED", "Assets\\trashcanClosed.png")
        engine.AddImageAsset("TRASH_OPEN", "Assets\\trashcanOpen.png")
        engine.AddImageAsset("SELECT_FRAME", "Assets\\selectedFrame.png")
        engine.AddImageAsset("FLOOR", "Assets\\floor.png")


        self.ObjectList = []
        BackGround = GameObject.Create(engine)
        BackGround.gameObject.size = engine._Globals._display
        BackGround.gameObject.image = "FLOOR"
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
        TopBar.gameObject.color = (69,10,30)
        TopBar.gameObject.position = Types.Vector3(0, 0, 4083)
        TopBarBorder = GameObject.Create(engine)
        TopBarBorder.gameObject.size = TopBar.gameObject.size + Types.Vector2(0, 3)
        TopBarBorder.gameObject.position = TopBar.gameObject.position - Types.Vector3(0, 0, 1)
        TopBarBorder.gameObject.color = (35, 6, 15)
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
        for buttonNum in range(8): #Red ("button"), Gray ("Garbage"), Black ("Nothing/Space") Green ("Start Button") Purple ("Money text and stuff") Yellow ("HealthBar")
            if buttonNum < 3:
                WallButton = PlaceWall.Create(engine)
                WallButtonHighlight = GameObject.Create(engine)
                WallButton.gameObject.size = (60, 60)
                WallButtonHighlight.gameObject.size = WallButton.gameObject.size + Types.Vector2(4, 4)
                WallButton.gameObject.color = (255,255,255)
                WallButtonHighlight.gameObject.color = (255,255,255)
                WallButton.gameObject.position = Types.Vector3((buttonNum * 60) + ((buttonNum + 1) * 20), TopBar.gameObject.size.y-WallButton.gameObject.size.y-10, 4097)
                WallButtonHighlight.gameObject.position = WallButton.gameObject.position - Types.Vector3(2, 2, -1)
                WallButton.gameObject.collisionLayer = engine._Globals.CollisionLayer.UI
                WallButtonHighlight.gameObject.renderEnabled = False
                WallButton.obj.highlightedIndicator = WallButtonHighlight
                WallButtonHighlight.gameObject.image = "SELECT_FRAME"
                if buttonNum == 1:
                    WallsTitle.gameObject.size = (60, 60)
                    WallsTitle.gameObject.position = WallButton.gameObject.position + Types.Vector3(0,-WallButton.gameObject.position.y,-5)
                    WallsTitle.gameObject.color = TopBar.gameObject.color
                    WallsTitle.gameObject.text = "WALLS"
                    WallsTitle.gameObject.fontSize = 20
                    self.ObjectList.append(WallsTitle)
                self.ObjectList.append(WallButton)
                self.ObjectList.append(WallButtonHighlight)
            if buttonNum == 3:
                DestroyWallButton = RemoveTile.Create(engine)
                DestroyWallButton.gameObject.size = (64, 64)
                DestroyWallButton.gameObject.color = (255,255,255)
                DestroyWallButton.gameObject.position = Types.Vector3((buttonNum * 60) + ((buttonNum + 1) * 20) - 0, TopBar.gameObject.size.y-WallButton.gameObject.size.y - 16, 4097)
                DestroyWallButton.gameObject.collisionLayer = engine._Globals.CollisionLayer.UI
                DestroyWallButton.gameObject.image = "TRASH_CLOSED"
                DestroyWallButton.gameObject.name = "TRASHCANBUTTON"
            if buttonNum >= 4:
                WeaponsButton = PlaceWall.Create(engine)
                WeaponsButtonHighlight = GameObject.Create(engine)
                WeaponsButton.gameObject.size = (60, 60)
                WeaponsButtonHighlight.gameObject.size = WeaponsButton.gameObject.size + Types.Vector2(4, 4)
                WeaponsButton.gameObject.color = (255,255,255)
                WeaponsButtonHighlight.gameObject.color = (255,255,255)
                WeaponsButton.gameObject.position = Types.Vector3((buttonNum * 60) + ((buttonNum + 1) * 20), TopBar.gameObject.size.y-WeaponsButton.gameObject.size.y-10, 4097)
                WeaponsButtonHighlight.gameObject.position = WeaponsButton.gameObject.position - Types.Vector3(2, 2, -1)
                WeaponsButton.gameObject.collisionLayer = engine._Globals.CollisionLayer.UI
                WeaponsButtonHighlight.gameObject.renderEnabled = False
                WeaponsButton.obj.highlightedIndicator = WeaponsButtonHighlight
                WeaponsButtonHighlight.gameObject.image = "SELECT_FRAME"
                if buttonNum == 6:
                    WeaponsTitle = GameObject.Create(engine)
                    WeaponsTitle.gameObject.size = (100, 60)
                    WeaponsTitle.gameObject.position = WeaponsButton.gameObject.position + Types.Vector3(0,-WeaponsButton.gameObject.position.y,-5)
                    WeaponsTitle.gameObject.color = TopBar.gameObject.color
                    WeaponsTitle.gameObject.text = "WEAPONS"
                    WeaponsTitle.gameObject.fontSize = 20
                    self.ObjectList.append(WeaponsTitle)
                self.ObjectList.append(WeaponsButton)
                self.ObjectList.append(WeaponsButtonHighlight)
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