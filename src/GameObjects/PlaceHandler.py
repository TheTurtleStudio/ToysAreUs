import random
from GameObjects.PlaceWall import PlaceWall
from GameObjects.PlaceWeapon import PlaceWeapon
from MainEngine import Types #NEEDED. Mainly for Types.GameObject creation.
from GameObjects import Wall
from GameObjects import Weapon
from GameObjects import GameObject
import pygame

from MainEngine.Engine import Engine
class PlaceHandler(): #Change this to the name of your script
    def __init__(self, engine):
        self.gameObject = Types.GameObject(engine)
        self.engine: Engine = engine
        self.creator = None
        self.selectedPlaceObject = None
        self.removingTile = False
        self.gameObject.renderEnabled = False

    def HANDLEPLACEMENT(self, cell):
        if (self.selectedPlaceObject != None): #Kinda far in the process but check if we even are placing anything
            if self.CHECKIFCANPLACE(cell): #Check if we can place the tile
                cell: Types.Cell = cell
                objectType: Types.PlacementType = self.selectedPlaceObject.objectType
                placeObject = objectType.methodReference.Create(self.engine)
                placeObject.obj.maxHealth = objectType.health
                placeObject.obj.health = objectType.health
                images = self.engine.GetImageAsset(objectType._FieldTexture)
                toPlugin = None 
                if (type(images) == pygame.Surface):
                    toPlugin = objectType._FieldTexture
                else:
                    toPlugin = (self.engine.GetImageAsset(objectType._FieldTexture)[random.randint(0, len(self.engine.GetImageAsset(objectType._FieldTexture)) - 1)])
                placeObject.gameObject.image = toPlugin
                placeObject.obj.cell = cell
                self.engine.CreateNewObject(placeObject)
                placeObject.gameObject.size = cell.size
                pos = cell.position
                placeObject.gameObject.position = Types.Vector3(pos.x, pos.y, 40000)
                if objectType.__bases__[0] == Types.WallTypes._GENERIC:
                    cell.objectLink = placeObject
                elif objectType.__bases__[0] == Types.WeaponTypes._GENERIC:
                    cell.weaponLink = placeObject
                self.UpdateLinkedMatrix(cell)
                    
                self.engine.FindObject("GRID").obj.gridMatrix.SetCell(cell.cell, cell)
    def UpdateLinkedMatrix(self, cell):
        if (self.engine.FindObject("GRID").obj.gridMatrix.CellExistsCheck(cell.cell + Types.Vector2(0, -1))):
            cell.aboveCell_OL = self.engine.FindObject("GRID").obj.gridMatrix.GetCell(cell.cell + Types.Vector2(0, -1))
            self.engine.FindObject("GRID").obj.gridMatrix.GetCell(cell.cell + Types.Vector2(0, -1)).belowCell_OL = cell
        else:
            cell.aboveCell_OL = None
        
        if (self.engine.FindObject("GRID").obj.gridMatrix.CellExistsCheck(cell.cell + Types.Vector2(0, 1))):
            cell.belowCell_OL = self.engine.FindObject("GRID").obj.gridMatrix.GetCell(cell.cell + Types.Vector2(0, 1))
            self.engine.FindObject("GRID").obj.gridMatrix.GetCell(cell.cell + Types.Vector2(0, 1)).aboveCell_OL = cell
        else:
            cell.belowCell_OL = None

        if (self.engine.FindObject("GRID").obj.gridMatrix.CellExistsCheck(cell.cell + Types.Vector2(1, 0))):
            cell.rightCell_OL = self.engine.FindObject("GRID").obj.gridMatrix.GetCell(cell.cell + Types.Vector2(1, 0))
            self.engine.FindObject("GRID").obj.gridMatrix.GetCell(cell.cell + Types.Vector2(1, 0)).leftCell_OL = cell
        else:
            cell.rightCell_OL = None

        if (self.engine.FindObject("GRID").obj.gridMatrix.CellExistsCheck(cell.cell + Types.Vector2(-1, 0))):
            cell.leftCell_OL = self.engine.FindObject("GRID").obj.gridMatrix.GetCell(cell.cell + Types.Vector2(-1, 0))
            self.engine.FindObject("GRID").obj.gridMatrix.GetCell(cell.cell + Types.Vector2(-1, 0)).rightCell_OL = cell
        else:
            cell.leftCell_OL = None
    def HANDLEDEMOPLACEMENT(self, cell, demoObj: GameObject.Create):    #This
        if (self.engine.FindObject("GRID").obj.gridMatrix.CellExistsCheck(cell.cell)):
            if (self.selectedPlaceObject != None):
                if self.engine.Input.TestFor.LEFTMOUSEDOWN() and (type(self.selectedPlaceObject) == PlaceWeapon) and self.selectedPlaceObject.objectType.canRotate:
                    demoObj.gameObject.rotation -= 90
                    demoObj.gameObject.rotation %= 360
                demoObj.gameObject.renderEnabled = True
                demoObj.gameObject.image = self.selectedPlaceObject.objectType._GRAYTexture
                demoObj.gameObject.color = (255,255,255)
                demoObj.gameObject.size = cell.size
                pos = cell.position
                demoObj.gameObject.position = Types.Vector3(pos.x, pos.y, 400000)
                if self.CHECKIFCANPLACE(cell):
                    demoObj.gameObject.color = (0, 255, 0)
                else:
                    demoObj.gameObject.color = (255, 0, 0)

    def CHECKIFCANPLACE(self, cell):
        condition1 = False
        condition3 = True
        if (type(self.selectedPlaceObject) == PlaceWall):
            condition3 = cell.objectLink == None
            cellOffsets = [Types.Vector2(0,1), Types.Vector2(0,-1), Types.Vector2(1,0), Types.Vector2(-1,0)]
            for i in range(4):
                if (self.engine.FindObject("GRID").obj.gridMatrix.CellExistsCheck(cell.cell + cellOffsets[i])):
                    current = self.engine.FindObject("GRID").obj.gridMatrix.GetCell(cell.cell + cellOffsets[i])
                    if current.objectLink != None:
                        condition1 = True
                else:
                    if (i == 2): #If neighboring the main wall
                        condition1 = True
        elif (type(self.selectedPlaceObject) == PlaceWeapon):
            condition3 = cell.weaponLink == None
            if self.selectedPlaceObject.objectType.canPlace_ROOT:
                if (self.engine.FindObject("GRID").obj.gridMatrix.CellExistsCheck(cell.cell)):
                    current = self.engine.FindObject("GRID").obj.gridMatrix.GetCell(cell.cell)
                    if (current.objectLink != None) and (type(current.objectLink) == Wall.Create) and (current.weaponLink == None):
                        condition1 = True
            if self.selectedPlaceObject.objectType.canPlace_SIDE:
                cellOffsets = [Types.Vector2(0,1), Types.Vector2(0,-1), Types.Vector2(1,0), Types.Vector2(-1,0)]
                for i in range(4):
                    if (self.engine.FindObject("GRID").obj.gridMatrix.CellExistsCheck(cell.cell + cellOffsets[i])):
                        current = self.engine.FindObject("GRID").obj.gridMatrix.GetCell(cell.cell + cellOffsets[i])
                        if (current.objectLink != None) and (type(current.objectLink) == Wall.Create):
                            condition1 = True
        condition2 = cell.enemyLink == None
        return (condition1 and condition2 and condition3)

#Create needs to be defined for every script in this folder. Everything should be exactly the same except for what is commented below, read that.
class Create():
    def __init__(self, engine):
        self.obj: PlaceHandler = PlaceHandler(engine) #Replace Template with the name of your class
        self.obj.creator = self
    @property
    def gameObject(self):
        return self.obj.gameObject
