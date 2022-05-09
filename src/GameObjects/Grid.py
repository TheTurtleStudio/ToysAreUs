import math
import GameObjects
from GameObjects import Wall
from GameObjects import GameObject
from MainEngine import Types #NEEDED. Mainly for Types.GameObject creation.
import pygame

from MainEngine.Engine import Engine
class Grid(): #Change this to the name of your script
    
    def __init__(self, engine):
        self.gameObject = Types.GameObject(engine)
        self.engine: Engine = engine
        self.creator = None
        self.gridSize = Types.Vector2(17,12)
        self.gridMatrix: Types.Matrix2x2 = Types.Matrix2x2(self.gridSize.x, self.gridSize.y)
        self.demoPlacement = GameObjects.GameObject.Create(engine)
        self.engine.CreateNewObject(self.demoPlacement)
        self.dragStart = None
        self.dragging = False

    def Start(self):
        self.ConfigureAllCells()
        self.demoPlacement.gameObject.transparency = 60

    def Update(self):
        if self.engine.timeScale == 0:
            return
        if (self.engine.Input.TestFor.RIGHTMOUSESTATE()): #Did the player click to place something this frame?
            cellAtPos = self.GetGridCell(self.engine.Input.TestFor.MOUSEPOS()) #Convert their mouse position to a cell position
            if ((type(cellAtPos) is Types.Cell) and (self.gridMatrix.CellExistsCheck(cellAtPos.cell))): #Checks if the cell they clicked even exists, is it in our cell matrix? (Just math to figure it out, not a search algorithm)
                if (self.dragging is False):
                    self.dragStart = self.engine.GetTotalTime()
                self.dragging = True
                elapsedSinceDrag = self.engine.GetTotalTime() - self.dragStart
                if self.engine.Input.TestFor.RIGHTMOUSEDOWN() or (elapsedSinceDrag > 0.15):
                    cellToChange = self.gridMatrix.GetCell(cellAtPos.cell) #Get the actual cell now that we know it exists
                    if (not self.engine.FindObject("PLACEHANDLER").obj.removingTile): #If we're meant to be placing a tile, this doesn't know what type of tile yet though.
                        self.engine.FindObject("PLACEHANDLER").obj.HANDLEDEMOPLACEMENT(cellToChange, self.demoPlacement)
                        self.engine.FindObject("PLACEHANDLER").obj.HANDLEPLACEMENT(cellToChange) #Tell our handler to do it, this is in SRC\GameObjects\PlaceHandler.py
                    else: #Are we removing the tile?
                        self.DestroyWallChain(cellToChange) #Attempt to the cell as well as any now floating artifacts once attached to it.
        else:
            cellAtPos = self.GetGridCell(self.engine.Input.TestFor.MOUSEPOS())
            if self.gridMatrix.CellExistsCheck(cellAtPos.cell):
                self.dragging = False
                self.dragStart = None
            if ((type(cellAtPos) is Types.Cell) and (self.engine.FindObject("PLACEHANDLER").obj.selectedPlaceObject != None) and (self.gridMatrix.CellExistsCheck(cellAtPos.cell))):
                cellToChange = self.gridMatrix.GetCell(cellAtPos.cell)
                cellToChange.cell = cellAtPos.cell
                cellToChange.position = cellAtPos.position
                cellToChange.size = cellAtPos.size
                self.engine.FindObject("PLACEHANDLER").obj.HANDLEDEMOPLACEMENT(self.gridMatrix.GetCell(cellAtPos.cell), self.demoPlacement)
                
            else:
                self.demoPlacement.gameObject.renderEnabled = False
    def DestroyWallChain(self, rootWall: Wall.Create):
        if (rootWall.objectLink != None):
            initialPairs = [rootWall.aboveCell_OL, rootWall.belowCell_OL, rootWall.rightCell_OL, rootWall.leftCell_OL]
            rootWall.objectLink.obj.Destroy()
            for stem in initialPairs:
                if (stem != None):
                    if (stem != None):
                        self.DestroyFloatingWalls(stem)
    def DestroyFloatingWalls(self, initialStem: Wall.Create):
        queue = [initialStem]
        visited = []
        foundWallConnection = False
        while queue:
            current = queue.pop(0)
            if (current.objectLink == None):
                return
            if not (current in visited):
                visited.append(current)
                if (current.cell.x == self.gridSize.x - 1):
                    foundWallConnection = True
                    break
                if (current.aboveCell_OL != None): #If the above cell exists
                    if (current.aboveCell_OL.objectLink != None):
                        queue.append(current.aboveCell_OL)
                if (current.belowCell_OL != None): #If the below cell exists
                    if (current.belowCell_OL.objectLink != None):
                        queue.append(current.belowCell_OL)
                if (current.rightCell_OL != None): #If the right cell exists
                    if (current.rightCell_OL.objectLink != None):
                        queue.append(current.rightCell_OL)
                if (current.leftCell_OL != None): #If the left cell exists
                    if (current.leftCell_OL.objectLink != None):
                        queue.append(current.leftCell_OL)
        if not foundWallConnection:
            for cell in visited:
                cell.objectLink.obj.Destroy()
    
    def ConfigureAllCells(self):
        for x in range(self.gridSize.x):
            for y in range(self.gridSize.y):
                setCell = self.gridMatrix.GetCell((x,y))
                setCell.cell = Types.Vector2(x,y)
                setCell.position = self.CellToPosition((x,y))
                setCell.size = Types.Vector2(self.gameObject.size.x / self.gridSize.x, self.gameObject.size.y / self.gridSize.y)

    def GetGridCellFULL(self, raycastPos: Types.Vector2):
        if (type(raycastPos) == Types.Vector2):
            raycastPos = (raycastPos.x, raycastPos.y)
        relative = Types.Vector3(raycastPos[0], raycastPos[1], 0) - self.gameObject.position
        gridCellSize = Types.Vector2(self.gameObject.size.x / self.gridSize.x, self.gameObject.size.y / self.gridSize.y)
        if (relative.x < 0 or relative.y < 0 or relative.x > self.gameObject.size.x or relative.y > self.gameObject.size.y):
            return None
        else: #If in the grid system do this
            cell = Types.Vector2(math.floor(relative.x / gridCellSize.x), math.floor(relative.y / gridCellSize.y))
            return self.gridMatrix.GetCell((cell.x, cell.y))

    def GetGridCell(self, raycastPos: Types.Vector2):
        if (type(raycastPos) == Types.Vector2):
            raycastPos = (raycastPos.x, raycastPos.y)
        relative = Types.Vector3(raycastPos[0], raycastPos[1], 0) - self.gameObject.position
        gridCellSize = Types.Vector2(self.gameObject.size.x / self.gridSize.x, self.gameObject.size.y / self.gridSize.y)
        if (relative.x < 0 or relative.y < 0 or relative.x > self.gameObject.size.x or relative.y > self.gameObject.size.y):
            return None
        else: #If in the grid system do this
            cell = Types.Vector2(math.floor(relative.x / gridCellSize.x), math.floor(relative.y / gridCellSize.y))
            
            cellPos = Types.Vector2(cell.x * gridCellSize.x, cell.y * gridCellSize.y) + Types.Vector2(self.gameObject.position.x, self.gameObject.position.y)
            return Types.Cell(cellPos, gridCellSize, cell)

    def CellToPosition(self, cellGridPosition: Types.Vector2):
        if type(cellGridPosition) == tuple:
            cellGridPosition = Types.Vector2(cellGridPosition[0], cellGridPosition[1])

        gridCellSize = Types.Vector2(self.gameObject.size.x / self.gridSize.x, self.gameObject.size.y / self.gridSize.y)
        return Types.Vector2(cellGridPosition.x * gridCellSize.x, cellGridPosition.y * gridCellSize.y) + Types.Vector2(self.gameObject.position.x, self.gameObject.position.y)

    def PositionToCell(self, position: Types.Vector2):
        if (type(position) == Types.Vector3):
            position = (position.x, position.y)
        if (type(position) == Types.Vector2):
            position = (position.x, position.y)
        relative = Types.Vector3(position[0], position[1], 0) - self.gameObject.position
        gridCellSize = Types.Vector2(self.gameObject.size.x / self.gridSize.x, self.gameObject.size.y / self.gridSize.y)
        return Types.Vector2(math.floor(relative.x / gridCellSize.x), math.floor(relative.y / gridCellSize.y))


#Create needs to be defined for every script in this folder. Everything should be exactly the same except for what is commented below, read that.
class Create():
    def __init__(self, engine):
        self.obj = Grid(engine) #Replace Template with the name of your class
        self.obj.creator = self
    @property
    def gameObject(self):
        return self.obj.gameObject