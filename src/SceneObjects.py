from GameObjects import GameObject, PlaceWeapon
from GameObjects import Button
from GameObjects import Grid
from GameObjects import PlaceWall
from GameObjects import PlaceHandler
from GameObjects import RemoveTile
from GameObjects import Enemy
from GameObjects import Healthbar

from MainEngine import ImageManipulation
from MainEngine import Types
from MainEngine.Engine import Engine
import pygame, random

class Objects():
    def __init__(self, engine: Engine):
        self.ObjectList = []
        engine.AddImageAsset("NOTEXTURE", "_ROOT\\NOTEXTURE.png") #WILL POSSIBLY MOVE TO DIFFERENT FILE LATER, AS OF RIGHT NOW DO NOT REMOVE THIS
        engine.AddAnimation("NOTEXTURE", ["NOTEXTURE"], framerate=1, loop=False) #WILL POSSIBLY MOVE TO DIFFERENT FILE LATER, AS OF RIGHT NOW DO NOT REMOVE THIS
        

        engine.AddImageAsset("TRASH_CLOSED", "Assets\\trashcanClosed.png")
        engine.AddImageAsset("TRASH_OPEN", "Assets\\trashcanOpen.png")
        engine.AddImageAsset("SELECT_FRAME", "Assets\\selectedFrame.png")
        engine.AddImageAsset("FLOOR", "Assets\\floor.png")
        

        engine.AddAnimation("ATTACK_TEMP", ImageManipulation.Sheets.Disect("Assets\\attackingAnimation.png", (32, 32), 4), framerate=2, loop=False) #Spritesheet

        engine.AddAnimation("WALK_TEMP", ImageManipulation.Sheets.Disect("Assets\\movingAnimation.png", (32, 32), 4), framerate=4, loop=True)

        


        
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

        HealthBar = Healthbar.Create(engine)
        HealthBar.gameObject.size = Types.Vector2(TopBar.gameObject.size.x * 0.35 - 20, 60)
        HealthBar.gameObject.position = Types.Vector3(TopBar.gameObject.size.x * 0.65, TopBar.gameObject.size.y-70, 4097)
        HealthBar.gameObject.color = (200, 60, 60)
        HealthBar.obj._fullnessBar.gameObject.color = (100, 185, 115)
        HealthBar.obj._fullnessBar.gameObject.position = HealthBar.gameObject.position + Types.Vector3(0, 0, 1)
        HealthBar.obj._fullnessBar.gameObject.size = HealthBar.gameObject.size
        HealthBar.obj.maxHealth = 500
        HealthBar.gameObject.name = "HEALTHBAR"
        
        HealthTitle = GameObject.Create(engine)
        HealthTitle.gameObject.size = (HealthBar.gameObject.size.x, 60)
        HealthTitle.gameObject.position = Types.Vector3(HealthBar.gameObject.position.x, 0, 4097)
        HealthTitle.gameObject.color = TopBar.gameObject.color
        HealthTitle.gameObject.text = "WALL HEALTH"
        HealthTitle.gameObject.fontSize = 20

        self.ObjectList.append(HealthBar)
        
        self.ObjectList.append(WaveTitle)

        self.ObjectList.append(HealthTitle)
        WallsTitle = GameObject.Create(engine)
        walls = [Types.WallTypes.Domino, Types.WallTypes.LincolnLog, Types.WallTypes.Lego]
        weapons = [Types.WeaponTypes.ToothpickTrap, Types.WeaponTypes.NerfGun, Types.WeaponTypes.BottleRocket, Types.WeaponTypes.BarrelOfMonkeys]
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
                WallButton.gameObject.collisionLayer = Types.CollisionLayer.UI
                WallButtonHighlight.gameObject.renderEnabled = False
                WallButton.obj.highlightedIndicator = WallButtonHighlight
                WallButtonHighlight.gameObject.image = "SELECT_FRAME"
                WallButton.obj.objectType = walls[buttonNum]
                WallButton.gameObject.image = walls[buttonNum]._UITexture
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
                DestroyWallButton.gameObject.position = Types.Vector3((buttonNum * 60) + ((buttonNum + 1) * 20) - 2, TopBar.gameObject.size.y-WallButton.gameObject.size.y - 12, 4097)
                DestroyWallButton.gameObject.collisionLayer = Types.CollisionLayer.UI
                DestroyWallButton.gameObject.image = "TRASH_CLOSED"
                DestroyWallButton.gameObject.name = "TRASHCANBUTTON"
            if buttonNum >= 4:
                WeaponsButton: PlaceWeapon.Create = PlaceWeapon.Create(engine)
                WeaponsButtonHighlight = GameObject.Create(engine)
                WeaponsButton.gameObject.size = (60, 60)
                WeaponsButtonHighlight.gameObject.size = WeaponsButton.gameObject.size + Types.Vector2(4, 4)
                WeaponsButton.gameObject.color = (255,255,255)
                WeaponsButtonHighlight.gameObject.color = (255,255,255)
                WeaponsButton.gameObject.position = Types.Vector3((buttonNum * 60) + ((buttonNum + 1) * 20), TopBar.gameObject.size.y-WeaponsButton.gameObject.size.y-10, 4097)
                WeaponsButtonHighlight.gameObject.position = WeaponsButton.gameObject.position - Types.Vector3(2, 2, -1)
                WeaponsButton.gameObject.collisionLayer = Types.CollisionLayer.UI
                WeaponsButtonHighlight.gameObject.renderEnabled = False
                WeaponsButton.obj.highlightedIndicator = WeaponsButtonHighlight
                WeaponsButtonHighlight.gameObject.image = "SELECT_FRAME"
                WeaponsButton.obj.objectType = weapons[buttonNum - 4]
                WeaponsButton.gameObject.image = weapons[buttonNum - 4]._UITexture
                if buttonNum == 5:
                    WeaponsTitle = GameObject.Create(engine)
                    WeaponsTitle.gameObject.size = (100, 60)
                    WeaponsTitle.gameObject.position = WeaponsButton.gameObject.position + Types.Vector3(20,-WeaponsButton.gameObject.position.y,-5)
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
        


        #CREATE ENEMY
        enemy = Enemy.Create(engine)
        enemy.obj.enemyType = Types.EnemyTypes.TeddyBear
        enemy.gameObject.size = Types.Vector2(50,50)
        enemy.gameObject.position = Types.Vector3(0,320,500000)
        #enemy.gameObject.rotation = 0
        self.ObjectList.append(enemy)
        #END CREATE ENEMY
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