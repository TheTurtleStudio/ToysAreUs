from math import floor
from GameObjects import GameObject, GoToMainMenu, MainMenuQuit, MainMenuStart, MoneyManager, PlaceWeapon, ProgressWaveButton, StartButtonFunctionality, WaveProgression
from GameObjects import Button
from GameObjects import Grid
from GameObjects import PlaceWall
from GameObjects import PlaceHandler
from GameObjects import RemoveTile
from GameObjects import Enemy
from GameObjects import Healthbar
from GameObjects import PauseMenu
from GameObjects import GameOverScreen

from MainEngine import ImageManipulation
from MainEngine import Types
from MainEngine.Engine import Engine
import pygame, random

class Objects():
    def __init__(self, engine: Engine):
        self.ObjectList = []
        engine.SetUniversal("STARTED", False)
        engine.AddImageAsset("NOTEXTURE", "_ROOT\\NOTEXTURE.png") #WILL POSSIBLY MOVE TO DIFFERENT FILE LATER, AS OF RIGHT NOW DO NOT REMOVE THIS
        engine.AddImageAsset("NOTEXTURE_GRAYSCALE", "_ROOT\\NOTEXTUREGRAYSCALE.png") #WILL POSSIBLY MOVE TO DIFFERENT FILE LATER, AS OF RIGHT NOW DO NOT REMOVE THIS
        engine.AddAnimation("NOTEXTURE", ["NOTEXTURE"], framerate=1, loop=False) #WILL POSSIBLY MOVE TO DIFFERENT FILE LATER, AS OF RIGHT NOW DO NOT REMOVE THIS
        

        engine.AddImageAsset("TRASH_CLOSED", "Assets\\Common\\trashcanClosed.png")
        engine.AddImageAsset("TRASH_OPEN", "Assets\\Common\\trashcanOpen.png")
        engine.AddImageAsset("SELECT_FRAME", "Assets\\Common\\selectedFrame.png")
        engine.AddImageAsset("FLOOR", "Assets\\Common\\floor.png")
        engine.AddImageAsset("RUG", "Assets\\Common\\rug.png")
        engine.AddImageAsset("_PLUGWALK", "Assets\\Common\\enemyWalk.png")
        engine.AddImageAsset("_ENEMYATTACK", "Assets\\Common\\enemyAttack.png")
        engine.AddImageAsset("WEAPONBASE", "Assets\\Common\\weaponBase.png")

        engine.AddImageAsset("DICEWALLS", ImageManipulation.Sheets.Disect(engine, "Assets\\Dice\\diceWalls.png", (64, 64), 6))
        engine.AddImageAsset("DICEWALLS_UI", "Assets\\Dice\\diceWallsUI.png")
        engine.AddImageAsset("DICEWALLS_UI_GRAYSCALE", "Assets\\Dice\\diceWallsUIGRAYSCALE.png")
        engine.AddImageAsset("LEGOWALLS", ImageManipulation.Sheets.Disect(engine, "Assets\\Lego\\legoWalls.png", (32, 32), 6))
        engine.AddImageAsset("LEGOWALLS_UI", "Assets\\Lego\\legoWallsUI.png")
        engine.AddImageAsset("LEGOWALLS_UI_GRAYSCALE", "Assets\\Lego\\legoWallsUIGRAYSCALE.png")
        engine.AddImageAsset("BLOCKWALLS", ImageManipulation.Sheets.Disect(engine, "Assets\\Woodblocks\\blockWalls.png", (64, 64), 3))
        engine.AddImageAsset("BLOCKWALLS_UI", "Assets\\WoodBlocks\\blockWallsUI.png")
        engine.AddImageAsset("BLOCKWALLS_UI_GRAYSCALE", "Assets\\WoodBlocks\\blockWallsUIGRAYSCALE.png")
        engine.AddImageAsset("TOOTHPICKTRAPSTATIONARY", ImageManipulation.Sheets.Disect(engine, "Assets\\Common\\toothpickTrap.png", (64, 64), 1))

        
        engine.AddImageAsset("ARROW", "Assets\\Common\\arrow.png")

        engine.AddAnimation("SOLDIER1_WALK", ImageManipulation.Sheets.Disect(engine, "_PLUGWALK", (64, 64), 4), framerate=5, loop=True)
        engine.AddAnimation("SOLDIER2_WALK", ImageManipulation.Sheets.Disect(engine, "_PLUGWALK", (64, 64), 4, 4), framerate=5, loop=True)
        engine.AddAnimation("SOLDIER3_WALK", ImageManipulation.Sheets.Disect(engine, "_PLUGWALK", (64, 64), 4, 8), framerate=5, loop=True)
        engine.AddAnimation("TEDDYBEAR1_WALK", ImageManipulation.Sheets.Disect(engine, "_PLUGWALK", (64, 64), 6, 12), framerate=5, loop=True)
        engine.AddAnimation("TEDDYBEAR2_WALK", ImageManipulation.Sheets.Disect(engine, "_PLUGWALK", (64, 64), 6, 18), framerate=5, loop=True)
        engine.AddAnimation("TEDDYBEAR3_WALK", ImageManipulation.Sheets.Disect(engine, "_PLUGWALK", (64, 64), 6, 24), framerate=5, loop=True)
        engine.AddAnimation("CAR1_WALK", ImageManipulation.Sheets.Disect(engine, "_PLUGWALK", (64, 64), 4, 30), framerate=5, loop=True)
        engine.AddAnimation("CAR2_WALK", ImageManipulation.Sheets.Disect(engine, "_PLUGWALK", (64, 64), 4, 34), framerate=5, loop=True)
        engine.AddAnimation("CAR3_WALK", ImageManipulation.Sheets.Disect(engine, "_PLUGWALK", (64, 64), 4, 38), framerate=5, loop=True)
        
        #Can optimize this
        engine.AddAnimation("SOLDIER1_ATTACK", ImageManipulation.Sheets.Disect(engine, "_ENEMYATTACK", (64, 64), 8), framerate=8, loop=False)
        engine.AddAnimation("SOLDIER2_ATTACK", ImageManipulation.Sheets.Disect(engine, "_ENEMYATTACK", (64, 64), 8, 8), framerate=8, loop=False)
        engine.AddAnimation("SOLDIER3_ATTACK", ImageManipulation.Sheets.Disect(engine, "_ENEMYATTACK", (64, 64), 8, 16), framerate=8, loop=False)
        engine.AddAnimation("TEDDYBEAR1_ATTACK", ImageManipulation.Sheets.Disect(engine, "_ENEMYATTACK", (64, 64), 6, 24), framerate=8, loop=False)
        engine.AddAnimation("TEDDYBEAR2_ATTACK", ImageManipulation.Sheets.Disect(engine, "_ENEMYATTACK", (64, 64), 6, 30), framerate=8, loop=False)
        engine.AddAnimation("TEDDYBEAR3_ATTACK", ImageManipulation.Sheets.Disect(engine, "_ENEMYATTACK", (64, 64), 6, 36), framerate=8, loop=False)
        engine.AddAnimation("CAR1_ATTACK", ImageManipulation.Sheets.Disect(engine, "_ENEMYATTACK", (64, 64), 12, 42), framerate=12, loop=False)
        engine.AddAnimation("CAR2_ATTACK", ImageManipulation.Sheets.Disect(engine, "_ENEMYATTACK", (64, 64), 12, 54), framerate=12, loop=False)
        engine.AddAnimation("CAR3_ATTACK", ImageManipulation.Sheets.Disect(engine, "_ENEMYATTACK", (64, 64), 12, 66), framerate=12, loop=False)
        engine.AddAnimation("toothpickTrap", ImageManipulation.Sheets.Disect(engine, "Assets\\Common\\toothpickTrap.png", (64, 64), 5), framerate=6, loop=False)
        engine.AddAnimation("deathCloud", ImageManipulation.Sheets.Disect(engine, "Assets\\Common\\deathCloud.png", (64, 64), 6), framerate=8, loop=False)

        engine.AddImageAsset("TURRET", ImageManipulation.Sheets.Disect(engine, "Assets\\Common\\turret.png", (64, 64), 1)[0])
        engine.AddImageAsset("TURRETUI", ImageManipulation.Sheets.Disect(engine, "Assets\\Common\\turretUI.png", (64, 64), 1)[0])
        engine.AddImageAsset("TURRETUIGRAYSCALE", ImageManipulation.Sheets.Disect(engine, "Assets\\Common\\turretUIGRAYSCALE.png", (64, 64), 1)[0])
        engine.AddImageAsset("BOTTLEROCKETPROJECTILE", ImageManipulation.Sheets.Disect(engine, "Assets\\Common\\bottleRocket.png", (64, 64), 6)[5])
        engine.AddImageAsset("BOTTLEROCKETUI", ImageManipulation.Sheets.Disect(engine, "Assets\\Common\\bottleRocketUI.png", (64, 64), 1)[0])
        
        engine.AddImageAsset("MONKEYBARREL", "Assets\\Common\\monkeyBarrel.png")
        engine.AddImageAsset("MONKEYBARRELBROKEN", "Assets\\Common\\monkeyBarrelBROKEN.png")
        engine.AddImageAsset("MONKEYBARRELUI", ImageManipulation.Sheets.Disect(engine, "Assets\\Common\\monkeyBarrelUI.png", (64, 64), 1)[0])
        engine.AddImageAsset("MONKEYBARRELUIGRAYSCALE", "Assets\\Common\\monkeyBarrelUIGRAYSCALE.png")
        engine.AddImageAsset("MONKEYARM", "Assets\\Common\\monkeyHand.png")

        engine.AddImageAsset("TOOTHPICKTRAPUI", "Assets\\Common\\toothpickTrapUI.png")


        engine.AddImageAsset("PLAYCLICKABLE", "Assets\\Common\\playButtonClickable.png")
        engine.AddImageAsset("PLAYNOTCLICKABLE", "Assets\\Common\\playButtonUnclickable.png")
        engine.AddImageAsset("40PERCENTTRANS", "Assets\\Common\\40PERCENTTRANS.png")
        engine.AddImageAsset("100PERCENTTRANS", "Assets\\Common\\100PERCENTTRANS.png")

        engine.AddImageAsset("MAINWALL", "Assets\\Common\\wall.png")
        

        

        MainMenu = GameObject.Create(engine)
        MainMenu.gameObject.size = engine._Globals._display
        MainMenu.gameObject.position = Types.Vector3(0, 0, 6413607225314159)
        MainMenu.gameObject.color = (218,218,218)
        MainMenu.gameObject.name = "MAINMENU"
        self.ObjectList.append(MainMenu)

        MainMenuTitle = GameObject.Create(engine)
        MainMenuTitle.gameObject.size = engine._Globals._display
        MainMenuTitle.gameObject.position = Types.Vector3(0, 0, MainMenu.gameObject.position.z + 1)
        MainMenuTitle.gameObject._textColor = (20,20,20)
        MainMenuTitle.gameObject.fontSize = floor(80 / 1600 * engine._Globals._display[0])
        MainMenuTitle.gameObject.text = "ToysWarUs "
        MainMenuTitle.gameObject.image = "100PERCENTTRANS"
        MainMenuTitle.gameObject.name = "MAINMENUTITLE"
        self.ObjectList.append(MainMenuTitle)
        
        StartButtonMain = MainMenuStart.Create(engine)
        StartButtonMain.gameObject.size = ((300 / 1600 * engine._Globals._display[0]), (80 / 900 * engine._Globals._display[1]))
        StartButtonMain.gameObject.color = (127,127,127)
        StartButtonMain.gameObject.position = Types.Vector3((engine._Globals._display[0] / 2) - (StartButtonMain.gameObject.size.x / 2), (engine._Globals._display[1] / 2) - (StartButtonMain.gameObject.size.y / 2), MainMenu.gameObject.position.z + 2)
        StartButtonMain.gameObject.collisionLayer = Types.CollisionLayer.UI
        StartButtonMain.gameObject.name = "MAINMENUSTART"
        StartButtonMain.gameObject._textColor = (20,20,20)
        StartButtonMain.gameObject.textFormat = 0
        StartButtonMain.gameObject.fontSize = floor(50 / 1600 * engine._Globals._display[0])
        StartButtonMain.gameObject.text = "START"
        self.ObjectList.append(StartButtonMain)

        QuitButtonMain = MainMenuQuit.Create(engine)
        QuitButtonMain.gameObject.size = ((300 / 1600 * engine._Globals._display[0]), (80 / 900 * engine._Globals._display[1]))
        QuitButtonMain.gameObject.color = (127,127,127)
        QuitButtonMain.gameObject.position = Types.Vector3((engine._Globals._display[0] / 2) - (QuitButtonMain.gameObject.size.x / 2), (engine._Globals._display[1] / 2) - (QuitButtonMain.gameObject.size.y / 2) + (StartButtonMain.gameObject.size.y * 1.1), MainMenu.gameObject.position.z + 2)
        QuitButtonMain.gameObject.collisionLayer = Types.CollisionLayer.UI
        QuitButtonMain.gameObject.name = "MAINMENUQUIT"
        QuitButtonMain.gameObject._textColor = (20,20,20)
        QuitButtonMain.gameObject.textFormat = 0
        QuitButtonMain.gameObject.fontSize = floor(50 / 1600 * engine._Globals._display[0])
        QuitButtonMain.gameObject.text = "QUIT"
        self.ObjectList.append(QuitButtonMain)

        BackGround = GameObject.Create(engine)
        BackGround.gameObject.size = engine._Globals._display
        BackGround.gameObject.image = "FLOOR"
        BackGround.gameObject.name = "BackGround"
        self.ObjectList.append(BackGround)
        BaseWall = GameObject.Create(engine)
        BaseWall.gameObject.size = ((75 / 1600 * engine._Globals._display[0]), engine._Globals._display[1]-(120 / 900 * engine._Globals._display[1]))
        BaseWall.gameObject.color = (128,128,128)
        BaseWall.gameObject.position = Types.Vector3(engine._Globals._display[0]-(75 / 1600 * engine._Globals._display[0]), (110 / 900 * engine._Globals._display[1]), 1)
        BaseWall.gameObject.name = "BaseWall"
        BaseWall.gameObject.image = "MAINWALL"
        
        
        self.ObjectList.append(BaseWall)
        TopBar = GameObject.Create(engine)
        TopBar.gameObject.size = (engine._Globals._display[0], (100 / 900 * engine._Globals._display[1]))
        TopBar.gameObject.color = (69,10,30)
        TopBar.gameObject.position = Types.Vector3(0, 0, 4093)
        TopBarBorder = GameObject.Create(engine)
        TopBarBorder.gameObject.size = TopBar.gameObject.size + Types.Vector2(0, (3 / 900 * engine._Globals._display[1]))
        TopBarBorder.gameObject.position = TopBar.gameObject.position - Types.Vector3(0, 0, 1)
        TopBarBorder.gameObject.color = (35, 6, 15)
        self.ObjectList.append(TopBar)
        self.ObjectList.append(TopBarBorder)
        
        WaveTitle = GameObject.Create(engine)
        
        WaveTitle.gameObject.size = ((60 / 1600 * engine._Globals._display[0]), (60 / 900 * engine._Globals._display[1]))
        WaveTitle.gameObject.position = Types.Vector3((engine._Globals._display[0] / 2) - (WaveTitle.gameObject.size.x / 2), 0, 4097)
        WaveTitle.gameObject.color = TopBar.gameObject.color
        WaveTitle.gameObject.text = "WAVE"
        WaveTitle.gameObject.fontSize = floor(30 / 1600 * engine._Globals._display[0])

        WaveIndicator = GameObject.Create(engine)
        
        WaveIndicator.gameObject.size = ((120 / 1600 * engine._Globals._display[0]), (60 / 900 * engine._Globals._display[1]))
        WaveIndicator.gameObject.position = Types.Vector3((engine._Globals._display[0] / 2) - (WaveIndicator.gameObject.size.x / 2), WaveTitle.gameObject.size.y / 2, 4098)
        WaveIndicator.gameObject.color = TopBar.gameObject.color
        WaveIndicator.gameObject.text = "0"
        WaveIndicator.gameObject.image = "100PERCENTTRANS"
        WaveIndicator.gameObject.fontSize = floor(60 / 1600 * engine._Globals._display[0])
        WaveIndicator.gameObject.name = "WAVEINDICATOR"

        GameOver = GameOverScreen.Create(engine)
        GameOver.gameObject.size = engine._Globals._display
        GameOver.gameObject.position = Types.Vector3(0,0,65536)
        GameOver.gameObject.color = (0, 0, 0)
        GameOver.gameObject.name = "GAMEOVER"
        GameOverTitle = GameObject.Create(engine)
        GameOverTitle.gameObject.size = ((900 / 1600 * engine._Globals._display[0]), (100 / 900 * engine._Globals._display[1]))
        GameOverTitle.gameObject.position = Types.Vector3((engine._Globals._display[0] / 2) - (GameOverTitle.gameObject.size.x / 2), GameOverTitle.gameObject.size.y / 2, GameOver.gameObject.position.z + 1)
        GameOverTitle.gameObject.image = "100PERCENTTRANS"
        GameOverTitle.gameObject.textFormat = 0
        GameOverTitle.gameObject.fontSize = 100
        GameOverTitle.gameObject.text = "GAME OVER"
        GameOver.obj.elements.append(GameOverTitle)
        GameOverRestart = StartButtonFunctionality.Create(engine)
        GameOverRestart.gameObject.size = ((150 / 1600 * engine._Globals._display[0]), (50 / 900 * engine._Globals._display[1]))
        GameOverRestart.gameObject.position = Types.Vector3((engine._Globals._display[0] / 2) - (GameOverRestart.gameObject.size.x / 2), engine._Globals._display[1] / 2, GameOver.gameObject.position.z + 1)
        GameOverRestart.gameObject.color = (50, 50, 50)
        GameOverRestart.gameObject.collisionLayer = Types.CollisionLayer.UI
        GameOverRestart.gameObject.textFormat = 0
        GameOverRestart.gameObject.fontSize = 30
        GameOverRestart.gameObject.text = "MAIN MENU"

        GameOver.obj.elements.append(GameOverRestart)
        self.ObjectList.append(GameOverTitle)
        self.ObjectList.append(GameOverRestart)
        self.ObjectList.append(GameOver)

        

        HealthBar = Healthbar.Create(engine)
        HealthBar.gameObject.size = Types.Vector2(TopBar.gameObject.size.x * 0.25 - (20 / 1600 * engine._Globals._display[0]), (60 / 900 * engine._Globals._display[1]))
        HealthBar.gameObject.position = Types.Vector3(TopBar.gameObject.size.x * 0.75, TopBar.gameObject.size.y-(70 / 900 * engine._Globals._display[1]), 4097)
        HealthBar.gameObject.color = (200, 60, 60)
        HealthBar.obj._fullnessBar.gameObject.color = (100, 185, 115)
        HealthBar.obj._fullnessBar.gameObject.position = HealthBar.gameObject.position + Types.Vector3(0, 0, 1)
        HealthBar.obj._fullnessBar.gameObject.size = HealthBar.gameObject.size
        HealthBar.obj.maxHealth = 100
        HealthBar.gameObject.name = "HEALTHBAR"
        
        HealthTitle = GameObject.Create(engine)
        HealthTitle.gameObject.size = (HealthBar.gameObject.size.x, (60 / 900 * engine._Globals._display[1]))
        HealthTitle.gameObject.position = Types.Vector3(HealthBar.gameObject.position.x, 0, 4097)
        HealthTitle.gameObject.color = TopBar.gameObject.color
        HealthTitle.gameObject.text = "WALL HEALTH"
        HealthTitle.gameObject.fontSize = floor(20 / 1600 * engine._Globals._display[0])

        self.ObjectList.append(HealthBar)
        
        self.ObjectList.append(WaveTitle)
        self.ObjectList.append(WaveIndicator)

        self.ObjectList.append(HealthTitle)

        
   

        WallsTitle = GameObject.Create(engine)
        walls = [Types.WallTypes.Dice, Types.WallTypes.LetterBlock, Types.WallTypes.Lego]
        weapons = [Types.WeaponTypes.NerfGun, Types.WeaponTypes.BottleRocket, Types.WeaponTypes.ToothpickTrap, Types.WeaponTypes.BarrelOfMonkeys]
        for buttonNum in range(8):
            if buttonNum < 3:
                WallButton = PlaceWall.Create(engine)
                WallButtonHighlight = GameObject.Create(engine)
                
                WallButton.gameObject.size = ((60 / 1600 * engine._Globals._display[0]), (60 / 900 * engine._Globals._display[1]))
                WallButtonHighlight.gameObject.size = WallButton.gameObject.size + Types.Vector2((4 / 1600 * engine._Globals._display[0]), (4 / 900 * engine._Globals._display[1]))
                
                WallButton.gameObject.color = (255,255,255)
                WallButtonHighlight.gameObject.color = (255,255,255)
                
                WallButton.gameObject.position = Types.Vector3((buttonNum * (60 / 1600 * engine._Globals._display[0])) + ((buttonNum + 1) * (20 / 1600 * engine._Globals._display[0])), TopBar.gameObject.size.y-WallButton.gameObject.size.y-(10 / 900 * engine._Globals._display[1]), 4097)
                WallButtonHighlight.gameObject.position = WallButton.gameObject.position - Types.Vector3((2 / 1600 * engine._Globals._display[0]), (2 / 900 * engine._Globals._display[1]), -1)
                
                WallButton.gameObject.collisionLayer = Types.CollisionLayer.UI
                WallButtonHighlight.gameObject.renderEnabled = False

                WallButtonInfoBox = GameObject.Create(engine)
                WallButtonInfoBox.gameObject.size = WallButton.gameObject.size
                WallButtonInfoBox.gameObject.color = (128,128,128)
                WallButtonInfoBox.gameObject.position = WallButton.gameObject.position + Types.Vector3(0, 0, 0.5)
                WallButtonInfoBox.gameObject.renderEnabled = False
                WallButtonInfoBox.gameObject.fontSize = floor(30 / 1600 * engine._Globals._display[0])
                WallButtonInfoBox.gameObject.textFormat = 0
                WallButtonInfoBox.gameObject.image = "40PERCENTTRANS"
                WallButtonInfoBox.gameObject.text = f"${walls[buttonNum].cost}"
                WallButton.obj.infoBox = WallButtonInfoBox
                self.ObjectList.append(WallButtonInfoBox)

                WallButton.obj.highlightedIndicator = WallButtonHighlight
                WallButtonHighlight.gameObject.image = "SELECT_FRAME"
                WallButton.obj.objectType = walls[buttonNum]
                
                WallButton.gameObject.image = walls[buttonNum]._UITexture
                if buttonNum == 1:
                    WallsTitle.gameObject.size = ((60 / 1600 * engine._Globals._display[0]), (60 / 900 * engine._Globals._display[1]))
                    WallsTitle.gameObject.position = WallButton.gameObject.position + Types.Vector3(0,-WallButton.gameObject.position.y,-0.01)
                    WallsTitle.gameObject.color = TopBar.gameObject.color
                    WallsTitle.gameObject.text = "WALLS"
                    WallsTitle.gameObject.fontSize = floor(20 / 1600 * engine._Globals._display[0])
                    self.ObjectList.append(WallsTitle)
                self.ObjectList.append(WallButton)
                
                self.ObjectList.append(WallButtonHighlight)
            if buttonNum == 3:
                DestroyWallButton = RemoveTile.Create(engine)
                DestroyWallButton.gameObject.size = ((64 / 1600 * engine._Globals._display[0]), (64 / 900 * engine._Globals._display[1]))
                DestroyWallButton.gameObject.color = (255,255,255)
                DestroyWallButton.gameObject.position = Types.Vector3((buttonNum * (60 / 1600 * engine._Globals._display[0])) + ((buttonNum + 1) * (20 / 1600 * engine._Globals._display[0])) - (2 / 1600 * engine._Globals._display[0]), TopBar.gameObject.size.y-WallButton.gameObject.size.y - (12 / 900 * engine._Globals._display[1]), 4097)
                DestroyWallButton.gameObject.collisionLayer = Types.CollisionLayer.UI
                DestroyWallButton.gameObject.image = "TRASH_CLOSED"
                DestroyWallButton.gameObject.name = "TRASHCANBUTTON"
            if buttonNum >= 4:
                WeaponsButton: PlaceWeapon.Create = PlaceWeapon.Create(engine)
                WeaponsButtonHighlight = GameObject.Create(engine)
                WeaponsButton.gameObject.size = ((60 / 1600 * engine._Globals._display[0]), (60 / 900 * engine._Globals._display[1]))
                WeaponsButtonHighlight.gameObject.size = WeaponsButton.gameObject.size + Types.Vector2((4 / 1600 * engine._Globals._display[0]), (4 / 900 * engine._Globals._display[1]))
                WeaponsButton.gameObject.color = (255,255,255)
                WeaponsButtonHighlight.gameObject.color = (255,255,255)
                WeaponsButton.gameObject.position = Types.Vector3((buttonNum * (60 / 1600 * engine._Globals._display[0])) + ((buttonNum + 1) * (20 / 1600 * engine._Globals._display[0])), TopBar.gameObject.size.y-WeaponsButton.gameObject.size.y-(10 / 900 * engine._Globals._display[1]), 4097)
                WeaponsButtonHighlight.gameObject.position = WeaponsButton.gameObject.position - Types.Vector3((2 / 1600 * engine._Globals._display[0]), (2 / 900 * engine._Globals._display[1]), -1)
                WeaponsButton.gameObject.collisionLayer = Types.CollisionLayer.UI
                WeaponsButtonHighlight.gameObject.renderEnabled = False
                WeaponsButton.obj.highlightedIndicator = WeaponsButtonHighlight
                WeaponsButtonHighlight.gameObject.image = "SELECT_FRAME"
                WeaponsButton.obj.objectType = weapons[buttonNum - 4]
                WeaponsButton.gameObject.image = weapons[buttonNum - 4]._UITexture

                WeaponsButtonInfoBox = GameObject.Create(engine)
                WeaponsButtonInfoBox.gameObject.size = WeaponsButton.gameObject.size
                WeaponsButtonInfoBox.gameObject.color = (128,128,128)
                WeaponsButtonInfoBox.gameObject.position = WeaponsButton.gameObject.position + Types.Vector3(0, 0, 0.5)
                WeaponsButtonInfoBox.gameObject.renderEnabled = False
                WeaponsButtonInfoBox.gameObject.fontSize = floor(30 / 1600 * engine._Globals._display[0])
                WeaponsButtonInfoBox.gameObject.textFormat = 0
                WeaponsButtonInfoBox.gameObject.image = "40PERCENTTRANS"
                WeaponsButtonInfoBox.gameObject.text = f"${weapons[buttonNum - 4].cost}"
                WeaponsButton.obj.infoBox = WeaponsButtonInfoBox
                self.ObjectList.append(WeaponsButtonInfoBox)

                if buttonNum == 5:
                    WeaponsTitle = GameObject.Create(engine)
                    WeaponsTitle.gameObject.size = ((100 / 1600 * engine._Globals._display[0]), (60 / 900 * engine._Globals._display[1]))
                    WeaponsTitle.gameObject.position = WeaponsButton.gameObject.position + Types.Vector3((20 / 1600 * engine._Globals._display[0]),-WeaponsButton.gameObject.position.y,-0.01)
                    WeaponsTitle.gameObject.color = TopBar.gameObject.color
                    WeaponsTitle.gameObject.text = "WEAPONS"
                    WeaponsTitle.gameObject.fontSize = floor(20 / 1600 * engine._Globals._display[0])
                    self.ObjectList.append(WeaponsTitle)
                self.ObjectList.append(WeaponsButton)
                self.ObjectList.append(WeaponsButtonHighlight)
        self.ObjectList.append(DestroyWallButton)


        WaveProgressionObj = WaveProgression.Create(engine)
        WaveProgressionObj.gameObject.name = "WAVEPROGRESSION"
        WaveProgressionObj.gameObject.renderEnabled = False
        self.ObjectList.append(WaveProgressionObj)

        ProgressWave = ProgressWaveButton.Create(engine)
        ProgressWave.gameObject.size = ((64 / 1600 * engine._Globals._display[0]), (64 / 900 * engine._Globals._display[1]))
        ProgressWave.gameObject.position = Types.Vector3((WaveTitle.gameObject.position.x + WaveTitle.gameObject.size.x) + (40 / 1600 * engine._Globals._display[0]), (TopBar.gameObject.size.y / 2) - (ProgressWave.gameObject.size.y / 2), 4097)
        ProgressWave.gameObject.collisionLayer = Types.CollisionLayer.UI
        ProgressWave.gameObject.name = "WAVESTARTBUTTON"
        self.ObjectList.append(ProgressWave)

        CurrencyTitle = GameObject.Create(engine)
        CurrencyTitle.gameObject.text = "MONEY"
        CurrencyTitle.gameObject.position = Types.Vector3((WaveTitle.gameObject.position.x + WaveTitle.gameObject.size.x) + (140 / 1600 * engine._Globals._display[0]), 0, WaveTitle.gameObject.position.z)
        CurrencyTitle.gameObject.size = WaveTitle.gameObject.size + Types.Vector2(100, 0)
        CurrencyTitle.gameObject.color = TopBar.gameObject.color
        CurrencyTitle.gameObject.fontSize = floor(25 / 1600 * engine._Globals._display[0])
        self.ObjectList.append(CurrencyTitle)

        

        CurrencyHolder = GameObject.Create(engine)
        CurrencyHolder.gameObject.name = "MONEY"
        CurrencyHolder.gameObject.text = "N\A"
        
        CurrencyHolder.gameObject.size = WaveTitle.gameObject.size + Types.Vector2(100, 0)
        CurrencyHolder.gameObject.position = Types.Vector3((WaveTitle.gameObject.position.x + WaveTitle.gameObject.size.x) + (140 / 1600 * engine._Globals._display[0]), (TopBar.gameObject.size.y / 2) - (CurrencyHolder.gameObject.size.y / 2) + (10 / 900 * engine._Globals._display[1]), WaveTitle.gameObject.position.z)
        CurrencyHolder.gameObject.color = TopBar.gameObject.color
        CurrencyHolder.gameObject.fontSize = floor(20 / 1600 * engine._Globals._display[0])
        self.ObjectList.append(CurrencyHolder)

        MoneyManagement = MoneyManager.Create(engine)
        MoneyManagement.gameObject.renderEnabled = False
        MoneyManagement.gameObject.name = "MONEYMANAGEMENT"
        self.ObjectList.append(MoneyManagement)

        BoardGrid = Grid.Create(engine)
        BoardGrid.gameObject.name = 'GRID'
        BoardGrid.gameObject.size = ((1088 / 1600 * engine._Globals._display[0]), (768 / 900 * engine._Globals._display[1]))
        BoardGrid.gameObject.image = "RUG"
        BoardGrid.gameObject.position = (BaseWall.gameObject.position.x - BoardGrid.gameObject.size.x, BaseWall.gameObject.position.y + ((BaseWall.gameObject.size.y - BoardGrid.gameObject.size.y) / 2),8192)
        BoardGrid.gameObject.color = (96, 171, 92)
        WaveProgressionObj.obj.grid = BoardGrid
        self.ObjectList.append(BoardGrid)
        PlaceObjectHandler = PlaceHandler.Create(engine)
        PlaceObjectHandler.gameObject.name = "PLACEHANDLER"
        self.ObjectList.append(PlaceObjectHandler)
        
        Pause = PauseMenu.Create(engine)
        Pause.gameObject.size = engine._Globals._display
        Pause.gameObject.position = Types.Vector3(0,0,6553600)
        Pause.gameObject.color = (0, 0, 0)
        PauseTitle = GameObject.Create(engine)
        PauseTitle.gameObject.size = ((900 / 1600 * engine._Globals._display[0]), (100 / 900 * engine._Globals._display[1]))
        PauseTitle.gameObject.position = Types.Vector3((engine._Globals._display[0] / 2) - (PauseTitle.gameObject.size.x / 2), PauseTitle.gameObject.size.y / 2, Pause.gameObject.position.z + 1)
        PauseTitle.gameObject.image = "100PERCENTTRANS"
        PauseTitle.gameObject.textFormat = 0
        PauseTitle.gameObject.fontSize = 100
        PauseTitle.gameObject.text = "PAUSED"
        Pause.obj.elements.append(PauseTitle)
        PauseRestart = StartButtonFunctionality.Create(engine)
        PauseRestart.gameObject.size = ((200 / 1600 * engine._Globals._display[0]), (50 / 900 * engine._Globals._display[1]))
        PauseRestart.gameObject.position = Types.Vector3((engine._Globals._display[0] / 2) - (PauseRestart.gameObject.size.x / 2), engine._Globals._display[1] / 2, Pause.gameObject.position.z + 1)
        PauseRestart.gameObject.color = (50, 50, 50)
        PauseRestart.gameObject.collisionLayer = Types.CollisionLayer.UI
        PauseRestart.gameObject.textFormat = 0
        PauseRestart.gameObject.fontSize = 30
        PauseRestart.gameObject.text = "EXIT TO MENU"
        Pause.obj.elements.append(PauseRestart)

        self.ObjectList.append(Pause)
        self.ObjectList.append(PauseTitle)
        self.ObjectList.append(PauseRestart)


    def get(self):
        return tuple(self.ObjectList)
class Injections():
    caption = "ToysWarUs"
    dimensions = (1600, 900)
    icon = "Assets\\Common\\icon.png"
    abstract = [
        "#This is raw code to be after all other injections are made. Yes, I know this is vulnerable to ACE and very unsafe in general. No, I don't care. Why? Because I'm a thug.",
        "#It's pretty intuitive, just put every piece of code encapsulated in a string as a new item in the array.",
        "#You can really just delete all this, just needed to explain somewhat what the hell this is.",
        "print(\"Injections complete\") #This is for debugging though!",
    ]