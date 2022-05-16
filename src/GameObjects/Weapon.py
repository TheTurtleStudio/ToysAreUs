import math
from GameObjects import GameObject
from GameObjects.Wall import Wall
from MainEngine import BMathL, Engine, Types #NEEDED. Mainly for Types.GameObject creation.
import pygame
class Weapon(): #Change this to the name of your script
    def __init__(self, engine):
        self.gameObject = Types.GameObject(engine)
        self.weaponType: Types.WeaponTypes._GENERIC = None
        self.oldWeaponType = None
        self.engine: Engine.Engine = engine
        self.creator = None
        self.cell = None
        self.maxHealth = None
        self.health = None
        self.hasBase = False
        self.baseGO = None
        self.placedRot = 0
        self.lastFired = 0
    def Destroy(self):
        self._UpdateLinkedMatrix()
        self.engine._Globals.sceneObjectsArray.remove(self.creator)
        if self.hasBase:
            self.engine._Globals.sceneObjectsArray.remove(self.baseGO)
            del self.baseGO
    def _UpdateLinkedMatrix(self):
        if (self.cell == None):
            return
        self.cell.weaponLink = None
    def Update(self):
        if self.engine.timeScale == 0:
            return
        if self.oldWeaponType != self.weaponType:
            self.lastFired = self.engine.GetTotalTime()
            self.oldWeaponType = self.weaponType
        if self.lastFired + self.weaponType.fireSpeed > self.engine.GetTotalTime():
            return
        fired = False
        enemyList = []
        if self.weaponType == Types.WeaponTypes.NerfGun:
            newSearchCells = self.weaponType.searchCells
            newSearchOffset = self.weaponType.searchOffset
            rot = self.placedRot
            if rot == 270:
                newSearchOffset = Types.Vector2(newSearchOffset.y, newSearchOffset.x)
                newSearchCells = Types.Vector2(newSearchCells.y, newSearchCells.x)
            if rot == 180:
                newSearchOffset = Types.Vector2(0, newSearchOffset.y)
            if rot == 90:
                newSearchOffset = Types.Vector2(newSearchOffset.y, 0)
                newSearchCells = Types.Vector2(newSearchCells.y, newSearchCells.x)
            
            for x in range(newSearchCells.x):
                for y in range(newSearchCells.y):
                    cellToSearch = newSearchOffset + Types.Vector2(x, y) + self.cell.cell
                    if self.engine.FindObject("GRID").obj.gridMatrix.CellExistsCheck(cellToSearch):
                        for enemy in self.engine.FindObject("GRID").obj.gridMatrix.GetCell(cellToSearch).enemyLinkDefinite:
                            if not enemy in enemyList:
                                enemyList.append(enemy)
            array = []
            linkedObjArray = []
            if (len(enemyList) != 0):
                for enemy in enemyList:
                    array.append((Types.Vector2(self.gameObject.position.x, self.gameObject.position.y) - Types.Vector2(enemy.gameObject.position.x, enemy.gameObject.position.y)).magnitude) #Add z component to array
                    linkedObjArray.append(enemy) #Add GameObject to array
                n = len(array)
                BMathL.Math.QuickSort.LinkedObject.QuickSort(array, linkedObjArray, 0, n-1) #Use our linked object quicksort algorithm
                V = (linkedObjArray[0].gameObject.position.x - self.gameObject.position.x, linkedObjArray[0].gameObject.position.y - self.gameObject.position.y)
                
                rotation = math.degrees(math.acos((V[1]) / ( ((V[0] ** 2) + (V[1] ** 2)) ** 0.5 )))
                
                self.gameObject.rotation = 90 - rotation - (180 if (linkedObjArray[0].gameObject.position.x - self.gameObject.position.x) > 0 else 0)
                self.gameObject.rotation = -self.gameObject.rotation if (linkedObjArray[0].gameObject.position.x - self.gameObject.position.x) > 0 else self.gameObject.rotation
                print(self.gameObject.rotation)
                linkedObjArray[0].Damage(self.weaponType.damage)
                fired = True
                
        enemyList.clear()
        del enemyList

        
        if fired:
            self.lastFired = self.engine.GetTotalTime()



#Create needs to be defined for every script in this folder. Everything should be exactly the same except for what is commented below, read that.
class Create():
    def __init__(self, engine):
        self.obj = Weapon(engine) #Replace Template with the name of your class
        self.obj.creator = self
    @property
    def gameObject(self):
        return self.obj.gameObject
