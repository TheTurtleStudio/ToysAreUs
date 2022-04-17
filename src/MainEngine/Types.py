import math
import pygame
from sympy import false, true


class Vector2():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.whole = (self.x, self.y) # don't know if the variables are pointers or not, python is weird as hell
    def __add__(self, other):
        if (type(other) == type(self)):
            return Vector2(self.x + other.x, self.y + other.y)
        else:
            raise Exception("Can only add Vector2 to Vector2!")
    def __abs__(self, exclude=[]):
        returnVal = Vector2(abs(self.x), abs(self.y))
        if ("x" in exclude):
            returnVal.x = self.x
        if ("y" in exclude):
            returnVal.y = self.y
        return returnVal
    def __mul__(self, other):
        return Vector2(self.x * other, self.y * other)
    def __rmul__(self, other):
        return self.__mul__(other)
    def __eq__(self, other):
        try:
            return self.whole == other.whole
        except:
            return False
class Vector3():
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        self.whole = (self.x, self.y, self.z) # don't know if the variables are pointers or not, python is weird as hell
    def __add__(self, other):
        if (type(other) == type(self)):
            return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise Exception("Can only add Vector3 to Vector3!")
    def __abs__(self, exclude=[]):
        returnVal = Vector3(abs(self.x), abs(self.y), abs(self.z))
        if ("x" in exclude):
            returnVal.x = self.x
        if ("y" in exclude):
            returnVal.y = self.y
        if ("z" in exclude):
            returnVal.z = self.z
        return returnVal
    def __mul__(self, other):
        return Vector3(self.x * other, self.y * other, self.z * other)
    def __rmul__(self, other):
        return self.__mul__(other)
    def __eq__(self, other):
        try:
            return self.whole == other.whole
        except:
            return False
class GameObject:
    def __init__(self, master): #Can optimize Update function to only call explicitly here
        self._master = master
        self.sprite = Sprite()
        self.position = Vector3() #Default is (0,0,0)
        self._size = Vector2(1,1)
        self.color = (255,255,255)
        self.name = "New GameObject"
        self.renderEnabled = True
    @property
    def position(self):
        return self._position
    @position.setter
    def position(self, value):
        if (type(value) == tuple):
            self._position = Vector3(value[0], value[1], value[2])
        else:
            self._position = value
        
        try:
            self.sprite.rect.x = self.position.x + self._positionOffset.x
            self.sprite.rect.y = self.position.y + self._positionOffset.y
        except:
            self.sprite.rect.x = self.position.x
            self.sprite.rect.y = self.position.y
    @position.getter
    def position(self):
        return self._position
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, value):
        newValue = value
        self._setSize(newValue)
    @size.getter
    def size(self):
        return self._size
    def _setSize(self, value, forceChange=False):
        valueAsV2 = value
        shouldScale = not (self._size == valueAsV2)
        if (type(value) == tuple):
            valueAsV2 = Vector2(value[0], value[1])
        shouldScale = (not (self._size == valueAsV2)) or forceChange
        self._size = valueAsV2
        print(value)
        horizontalFlip = (valueAsV2.x < 0)
        verticalFlip = (valueAsV2.y < 0)
        if shouldScale:
            if (horizontalFlip or verticalFlip):
                self.sprite.image = pygame.transform.flip(self.sprite.ORIGINALIMAGE, horizontalFlip, verticalFlip)
                try:
                    self._positionOffset
                except:
                    self._positionOffset = Vector2()
                if horizontalFlip:
                    self._positionOffset.x = self._size.x
                if verticalFlip:
                    self._positionOffset.y = self._size.y
                self.position = self._position
                tempSize = abs(valueAsV2).whole

                self.sprite.image = pygame.transform.scale(self.sprite.image, tempSize)
            else:
                self.sprite._flippedH, self.sprite._flippedV = False, False
                self.sprite.image = pygame.transform.scale(self.sprite.ORIGINALIMAGE, abs(valueAsV2).whole)
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, value):
        if ((type(value) == tuple) and (len(value) == 3)):
            self._color = (value[0], value[1], value[2])
            self.sprite.ORIGINALIMAGE.fill(self._color)
            self._syncOriginalImage()
        else:
            raise Exception("Can only change colors to tuples of length 3! RGB values!")
    @color.getter
    def color(self):
        return self._color
    def _syncOriginalImage(self):
        self.sprite.image = self.sprite.ORIGINALIMAGE
        self.position = self._position
        self._setSize(self._size, forceChange=True)
    def Destroy(self, engine):
        try:
            engine.Globals.sceneObjectsArray.remove(self)
        except ValueError:
            pass
        del self
class Sprite(pygame.sprite.Sprite):
    def __init__(self, dimensions=(32,32), color=(255,255,255)):
        if not (type(dimensions) == tuple):
            dimensions = dimensions.whole
        super().__init__()
        self.image = pygame.Surface(dimensions)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.ORIGINALIMAGE = self.image
