from MainEngine import Types #NEEDED. Mainly for Types.GameObject creation.
from GameObjects import Wall
from GameObjects import GameObject
import random
import pygame
class Enemy(): #Change this to the name of your script
    def __init__(self, engine):
        self.gameObject = Types.GameObject(engine)
        self.engine = engine
        self.creator = None
        self.speed = 300 #Pixels per second
        self._oldCurrentCell1 = None
        self._oldCurrentCell2 = None
        self.Animator = Types.Animator(self.gameObject)
    def Start(self):
        self.gridAccessor = self.engine.FindObject("GRID")
        yPos = self.gridAccessor.obj.CellToPosition((0, random.randint(1, self.gridAccessor.obj.gridSize.y - 2))).y
        self.gameObject.position = Types.Vector3(-self.gameObject.size.x - 1, yPos, 500000)
        self._destination = None

    def Update(self):
        if (self._destination != None):
            currentCell = self.gridAccessor.obj.GetGridCellFULL(Types.Vector2(self.gameObject.position.x + (self.gameObject.size.x / 2), self.gameObject.position.y + (self.gameObject.size.y / 2)))
            yCellOffset = -(currentCell.cell.y - self._destination.y) #-1=up, 1=down
            yChange = ((1 if (yCellOffset > 0) else -1) * self.speed * self.engine.GetDeltaTime())
            checkPos = Types.Vector2(self.gameObject.position.x + (self.gameObject.size.x / 2), self.gameObject.position.y + (self.gameObject.size.y if (yCellOffset > 0) else 0) + yChange)
            if (not self.gridAccessor.obj.gridMatrix.CellExistsCheck(self.gridAccessor.obj.PositionToCell(checkPos))):
                self.gameObject.position = Types.Vector3(self.gameObject.position.x, self.gridAccessor.obj.CellToPosition(currentCell.cell).y, self.gameObject.position.z)
                self.UpdateLink(False)
                self._destination = None
                return
            futureCell = self.gridAccessor.obj.GetGridCellFULL(checkPos)
            if (futureCell.cell.y == self._destination.y):
                self.gameObject.position = Types.Vector3(self.gameObject.position.x, self.gridAccessor.obj.CellToPosition(currentCell.cell).y, self.gameObject.position.z)
                
                self._destination = None
            else:
                self.gameObject.position += Types.Vector3(0, yChange, 0)
            self.UpdateLink(False)
            
        else:
            move = True
            currentCell = None
            futureCell = None
            tempPos = Types.Vector2(self.gameObject.position.x + (self.gameObject.size.x / 2), self.gameObject.position.y + (self.gameObject.size.y / 2))
            if self.gridAccessor.obj.gridMatrix.CellExistsCheck(self.gridAccessor.obj.PositionToCell(tempPos)):
                currentCell = self.gridAccessor.obj.GetGridCellFULL(tempPos)
            tempPos = Types.Vector2(self.gameObject.position.x + self.gameObject.size.x + self.speed * self.engine.GetDeltaTime(), self.gameObject.position.y + (self.gameObject.size.y / 2))
            if self.gridAccessor.obj.gridMatrix.CellExistsCheck(self.gridAccessor.obj.PositionToCell(tempPos)):
                futureCell = self.gridAccessor.obj.GetGridCellFULL(tempPos)
            
            if (futureCell != None) and (type(futureCell.objectLink) == Wall.Create):
                self.gameObject.position = Types.Vector3(self.gameObject.position.x, self.gridAccessor.obj.CellToPosition(currentCell.cell).y, self.gameObject.position.z)
                move = False

            if move:
                if (currentCell != None) and (currentCell.cell.x == self.gridAccessor.obj.gridSize.x - 1) and (futureCell == None): #If they've reached the main wall
                    self.HandleBaseWallDamage()
                else:
                    self.gameObject.position += Types.Vector3(self.speed * self.engine.GetDeltaTime(), 0, 0)
                self.UpdateLink()
                
            else: #If there's something in the way (a wall)
                immediateAbove = None
                immediateBelow = None
                encounteredWallAbove = None
                encounteredWallBelow = None
                if (currentCell.aboveCell_OL):
                    immediateAbove = currentCell.aboveCell_OL.objectLink
                if (currentCell.belowCell_OL):
                    immediateBelow = currentCell.belowCell_OL.objectLink
                if (futureCell.aboveCell_OL):
                    encounteredWallAbove = futureCell.aboveCell_OL.objectLink
                if (futureCell.belowCell_OL):
                    encounteredWallBelow = futureCell.belowCell_OL.objectLink
                current = self.gridAccessor.obj.PositionToCell(self.gameObject.position)
                canGoAbove = (immediateAbove == None) and (encounteredWallAbove == None) and self.gridAccessor.obj.gridMatrix.CellExistsCheck((current.x, current.y - 1))
                canGoBelow = (immediateBelow == None) and (encounteredWallBelow == None) and self.gridAccessor.obj.gridMatrix.CellExistsCheck((current.x, current.y + 1))
                if (canGoAbove or canGoBelow):
                    if (canGoAbove and canGoBelow):
                        goAbove = bool(random.getrandbits(1))
                    else:
                        goAbove = canGoAbove
                    self._destination = currentCell.cell + Types.Vector2(0, -2 if goAbove else 2)
                else:
                    self.gridAccessor.obj.DestroyWallChain(futureCell)


    def HandleBaseWallDamage(self):
        self.Animator.AnimationStep("temp")
        if (self.Animator.finished):
            self.Animator.ResetAnimationState()
            self.engine.FindObject("HEALTHBAR").obj.health -= 50
            #self.Start()
                
    def GetEndPoints(self, horizontal=True):
        if (horizontal):
            position1 = (self.gameObject.position.x + self.gameObject.size.x, self.gameObject.position.y + (self.gameObject.size.y / 2))
            position2 = (self.gameObject.position.x, self.gameObject.position.y + (self.gameObject.size.y / 2))
        else:
            position1 = (self.gameObject.position.x + (self.gameObject.size.x / 2), self.gameObject.position.y + self.gameObject.size.y)
            position2 = (self.gameObject.position.x + (self.gameObject.size.x / 2), self.gameObject.position.y)
        return (position1, position2)
    def UpdateLink(self, horizontal=True):
        position1, position2 = self.GetEndPoints(horizontal=horizontal)
        if self._oldCurrentCell1:
            self._oldCurrentCell1.enemyLink = None
        if self._oldCurrentCell2:
            self._oldCurrentCell2.enemyLink = None
        if self.gridAccessor.obj.gridMatrix.CellExistsCheck(self.gridAccessor.obj.PositionToCell(position1)): #Check if the first cell position exists
            newCurrentCell = self.gridAccessor.obj.GetGridCellFULL(Types.Vector2(position1[0], position1[1]))
            newCurrentCell.enemyLink = self
            self._oldCurrentCell1 = newCurrentCell
        if self.gridAccessor.obj.gridMatrix.CellExistsCheck(self.gridAccessor.obj.PositionToCell(position2)): #Check if the first cell position exists
            newCurrentCell = self.gridAccessor.obj.GetGridCellFULL(Types.Vector2(position2[0], position2[1]))
            newCurrentCell.enemyLink = self
            self._oldCurrentCell2 = newCurrentCell
        
            

#Create needs to be defined for every script in this folder. Everything should be exactly the same except for what is commented below, read that.
class Create():
    def __init__(self, engine):
        self.obj = Enemy(engine) #Replace Template with the name of your class
        self.obj.creator = self
    @property
    def gameObject(self):
        return self.obj.gameObject
