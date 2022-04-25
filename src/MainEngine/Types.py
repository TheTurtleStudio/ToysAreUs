import pygame

class Vector2():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.whole = (self.x, self.y) # don't know if the variables are pointers or not, python is weird as hell
    def __add__(self, other):
        try:
            if (type(other) == tuple):
                other = Vector2(other[0], other[1])
            return Vector2(self.x + other.x, self.y + other.y)
        except Exception:
            print("Can only add Vector2's with themselves or tuples of 2 elements or more.")
    def __abs__(self, exclude=[]):
        returnVal = Vector2(abs(self.x), abs(self.y))
        if ("x" in exclude):
            returnVal.x = self.x
        if ("y" in exclude):
            returnVal.y = self.y
        return returnVal
    def __mul__(self, other):
        return Vector2(self.x * other, self.y * other)
    def __eq__(self, other):
        try:
            return self.whole == other.whole
        except:
            return False
    def __sub__(self, other):
        try:
            if (type(other) == tuple):
                other = Vector2(other[0], other[1])
            return Vector2(self.x - other.x, self.y - other.y)
        except Exception:
            print("Can only subtract Vector2's from themselves or tuples of 2 elements or more.")
class Vector3():
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        self.whole = (self.x, self.y, self.z) # don't know if the variables are pointers or not, python is weird as hell
    def __add__(self, other):
        try:
            if (type(other) == tuple):
                other = Vector3(other[0], other[1], other[2])
            return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
        except Exception:
            print("Can only add Vector3's with themselves or tuples of 3 elements or more.")
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
    def __eq__(self, other):
        try:
            return self.whole == other.whole
        except:
            return False
    def __sub__(self, other):
        try:
            if (type(other) == tuple):
                other = Vector3(other[0], other[1], other[2])
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        except Exception:
            print("Can only subtract Vector3's from themselves or tuples of 3 elements or more.")
class Matrix2x2:
    def __init__(self, dim1, dim2):
        self.dimensions = Vector2(dim1, dim2)
        self.matrix = []
        for potCell in range(dim1*dim2):
            self.matrix.append(Cell())
    def GetCell(self, position):
        if not (type(position) == tuple or type(position) == Vector2):
            raise ValueError
        if (type(position) == tuple):
            position = Vector2(position[0], position[1])
        if (position.x < 1 or position.y < 1 or position.x > self.dimensions.x or position.y > self.dimensions.y):
            raise IndexError
        
        return self.matrix[(position.y * self.dimensions.x) + position.x - 1]
    def SetCell(self, position, replacement):
        if not (type(position) == tuple or type(position) == Vector2):
            raise ValueError
        if (type(position) == tuple):
            position = Vector2(position[0], position[1])
        if (position.x < 0 or position.y < 0 or position.x >= self.dimensions.x or position.y >= self.dimensions.y):
            raise IndexError
        
        self.matrix[(position.y * self.dimensions.x) + position.x] = replacement
class Cell():
    def __init__(self, _position=Vector3(0,0,0), _size=Vector2(0,0), _cell=Vector2(0,0)):
        self.position = _position
        self.size = _size
        self.center = Vector2(_position.x + (_size.x / 2), _position.y + (_size.y / 2))
        self.cell = _cell
class GameObject:
    def __init__(self, master): #Can optimize Update function to only call explicitly here
        self._master = master
        self.sprite = Sprite()
        self.position = Vector3() #Default is (0,0,0)
        self._size = Vector2(1,1)
        self.color = (255,255,255)
        self.name = "New GameObject"
        self._image = None
        self.isImage = False
        self.collisionLayer = master._Globals.CollisionLayer.GENERIC_GAMEOBJECT
        self.renderEnabled = True
    @property
    def image(self):
        return self._image
    @image.setter
    def image(self, value):
        if (value is None):
            self._image = None
            self.sprite.ORIGINALIMAGE = pygame.Surface(self._size[0], self._size[1])
            self._syncOriginalImage()
            self.isImage = False
            self.position = self._position
        elif (type(value) is str):
            self._image = pygame.image.load(value)
            self.sprite.ORIGINALIMAGE = self._image
            self._syncOriginalImage()
            self.isImage = True
            self.position = self._position
        else:
            print(f"Provided image is expected to be a file path. Given {type(value)} instead.")
            return
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
            self.sprite.rect.x = self._position.x + self._positionOffset.x
            self.sprite.rect.y = self._position.y + self._positionOffset.y
        except:
            self.sprite.rect.x = self._position.x
            self.sprite.rect.y = self._position.y
        self.sprite.rect.x, self.sprite.rect.y = (self.position.x, self.position.y)
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
            self.sprite.rect = self.sprite.image.get_rect()
            self.position = self._position
            self._updateColor()
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, value):
        if ((type(value) == tuple) and (len(value) == 3)):
            self._color = (value[0], value[1], value[2])
            self._syncOriginalImage()
        else:
            raise Exception("Can only change colors to tuples of length 3! RGB values!")
    @color.getter
    def color(self):
        return self._color
    def setOriginalColor(self, color):
        self.sprite.ORIGINALIMAGE.fill(color, special_flags=pygame.BLEND_MULT)
    def _updateColor(self):
        self.sprite.image.fill(self._color, special_flags=pygame.BLEND_MULT)
    def _syncOriginalImage(self):
        self.sprite.image = self.sprite.ORIGINALIMAGE
        self._updateColor
        self.position = self._position
        self.sprite.rect = self.sprite.image.get_rect()
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
class CollisionLayer():
    NONE = "NONE"
    ALL = "ALL"
    BACKGROUND = "BACKGROUND"
    WALL = "WALL"
    GENERIC_GAMEOBJECT = "GENERIC_GAMEOBJECT"
    UI = "UI"

