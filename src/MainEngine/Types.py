import math
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
        if (position.x < 0 or position.y < 0 or position.x >= self.dimensions.x or position.y >= self.dimensions.y):
            raise IndexError
        return self.matrix[(position.y * self.dimensions.x) + position.x]
    def SetCell(self, position, replacement):
        if not (type(position) == tuple or type(position) == Vector2):
            raise ValueError
        if (type(position) == tuple):
            position = Vector2(position[0], position[1])
        if (position.x < 0 or position.y < 0 or position.x >= self.dimensions.x or position.y >= self.dimensions.y):
            raise IndexError

        self.matrix[(position.y * self.dimensions.x) + position.x] = replacement
    def CellExistsCheck(self, position):
        if not (type(position) == tuple or type(position) == Vector2):
            raise ValueError
        if (type(position) == tuple):
            position = Vector2(position[0], position[1])
        if (position.x < 0 or position.y < 0 or position.x >= self.dimensions.x or position.y >= self.dimensions.y):
            return False
        else:
            return True
class Cell():
    def __init__(self, _position=Vector3(0,0,0), _size=Vector2(0,0), _cell=Vector2(-1,-1), _objectLink=None, _enemyLink=None):
        self.position = _position
        self.size = _size
        self._center = None
        self.cell = _cell
        self.objectLink: Wall.Create = _objectLink
        self.enemyLink = _enemyLink
        self.aboveCell_OL = None
        self.belowCell_OL = None
        self.rightCell_OL = None
        self.leftCell_OL = None
    @property
    def center(self):
        self._center = Vector2(self.position.x + (self.size.x / 2), self.position.y + (self.size.y / 2))
        return self._center
class GameObject():
    def __init__(self, master):
        self._master = master
        self.sprite = Sprite()
        self.position = Vector3() #Default is (0,0,0)
        self._size = Vector2(1,1)
        self._rotation = 0
        self._transparency = 0
        self.color = (255,255,255)
        self.name = "New GameObject"
        
        
        self._image = None
        self._textFont = pygame.font.Font("Assets\\gameFont.ttf",  30)
        self._text = None
        self._textRender = None
        self._fontSize = 30
        self.isImage = False
        self.collisionLayer = CollisionLayer.GENERIC_GAMEOBJECT
        self.renderEnabled = True
    

    @property
    def transparency(self):
        return self._transparency
    @transparency.setter
    def transparency(self, value):
        self._transparency = value
        self._syncOriginalImage()
    @property
    def fontSize(self):
        return self._fontSize
    @fontSize.setter
    def fontSize(self, value):
        if (type(value) == int):
            self._textFont = pygame.font.Font("Assets\\gameFont.ttf",  value)
            self.text = self._text
            self._fontSize = value
    @property
    def text(self):
        return self._text
    @text.setter
    def text(self, value):
        if (type(value) == str):
            self._text = value
            self._textRender = self._textFont.render(self._text, True, (255,255,255))
            self._syncOriginalImage()
        else:
            self._text = None
            self._textRender = None
            self._syncOriginalImage()
    @property
    def rotation(self):
        return self._rotation
    @rotation.setter
    def rotation(self, value):
        if (self._rotation != value):
            self._rotation = value
            self._syncOriginalImage()
    @property
    def image(self):
        return self._image
    @image.setter
    def image(self, value: str or pygame.Surface):
        if (value is None):
            self._image = None
            self.sprite.ORIGINALIMAGE = pygame.Surface(self._size.x, self._size.y)
            self._syncOriginalImage()
            self.isImage = False
            self.position = self._position
        elif (type(value) is str) or (type(value) is pygame.Surface):
            self._image = self._master.GetImageAsset(value) if (type(value) is str) else value
            self.sprite.ORIGINALIMAGE = self._image
            self._syncOriginalImage()
            self.isImage = True
            self.position = self._position
        else:
            print(f"Provided image is expected to be a file path or Surface object. Given {type(value)} instead.")
            return
    @property
    def position(self) -> Vector3:
        return self._position
    @position.setter
    def position(self, value: Vector3):
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
    @property
    def size(self) -> Vector2:
        return self._size
    @size.setter
    def size(self, value: str):
        newValue = value
        self._setSize(newValue)
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
        try:
            self.sprite.image.blit(self._textRender, self._textRender.get_rect(center=(self.size.x/2, self._textRender.get_rect().height/2)))
        except Exception:
            pass
        
        
        self.sprite.image = pygame.transform.rotate(self.sprite.image, self._rotation)
        
        
        
    def Destroy(self, engine):
        try:
            engine.Globals.sceneObjectsArray.remove(self)
        except ValueError:
            pass
        del self
class Animation:
    def __init__(self, p_collection: list, p_framerate: float, p_loop=True):
        self.collection = p_collection
        self.framerate = p_framerate
        self.loop = p_loop
class Animator:
    def __init__(self, gameObject: GameObject):
        self.animStates = {}
        self.currentlyPlaying = None #Is type Animation
        self.currentFrame = 0
        self.lastRefreshTime = -1
        self.lastCycleTime = -1
        self.effector = gameObject
        self.firstIteration = True
        self.finished = False

    def GetRawAnimationData(self, name: str) -> list: #Grabs the images
        return self.effector._master.GetAnimation(name)

    def _PlayAnimation(self, name: str): #Will restart animation every time it is called
        self.currentFrame = -1
        self.currentlyPlaying = self.GetRawAnimationData(name=name)
        self.firstIteration = True
        self.lastCycleTime = self.effector._master.GetTotalTime()
        self.finished = False

    def ResetAnimationState(self): #Makes it so you can play two non-loop animations back to back.
        self.currentlyPlaying: Animation = None
        self.finished = True

    def AnimationStep(self, name: str, restart=False): #Continues the animation cycle, doing nothing if a non-looped animation has completed
        if (restart):
            self.ResetAnimationState()
        if self.currentlyPlaying != self.GetRawAnimationData(name=name):
            self._PlayAnimation(name=name)
        if not self.finished:
            self._Refresh()
    
    def _CalculateFrame(self):
        elapsedTimeSinceCycle = self.effector._master.GetTotalTime() - self.lastCycleTime
        return math.floor(elapsedTimeSinceCycle * self.currentlyPlaying.framerate)

    def _Refresh(self):
        oldFrame = self.currentFrame + 0
        toReset = False
        if (self.currentlyPlaying == None):
            return
        if (not self.currentlyPlaying.loop) and (not self.firstIteration):
            self.finished = True
            return
        
        if self.currentlyPlaying.framerate <= 0: #Fix invalid framerame to be 0
            self.currentlyPlaying.framerate = 0
        else:
            calculatedFrame = self._CalculateFrame()
            self.currentFrame = calculatedFrame % len(self.currentlyPlaying.collection) #Set the current frame according to time. If overflow, restart from beginning of sequence.
            if (calculatedFrame != self.currentFrame) or (len(self.currentlyPlaying.collection) <= 1):
                self.firstIteration = False
                toReset = True
        if (not self.firstIteration and not self.currentlyPlaying.loop) or (self.currentlyPlaying.framerate == 0): 
            self.effector.image = self.currentlyPlaying.collection[-1]
            self.finished = True
            return
        else:
            if toReset: #Reset cycletime
                self.lastCycleTime = self.effector._master.GetTotalTime()
            if (self.currentFrame != oldFrame): #Only redraw if it's a new image from the animation
                self.effector.image = self.currentlyPlaying.collection[self.currentFrame]
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

class PlacementType():
    health = 1
    methodReference = None
    _UITexture = "NOTEXTURE"
    _FieldTexture = "NOTEXTURE"
from GameObjects import Wall
from GameObjects import Weapon
class WallTypes():
    class _GENERIC(PlacementType):
        methodReference = Wall
    class Domino(_GENERIC): #Weak
        health = 50
        _FieldTexture = "TRASH_CLOSED"
        _UITexture = "TRASH_OPEN"
    class LincolnLog(_GENERIC): #Medium
        health = 100
        _FieldTexture = "LLW"
    class Lego(_GENERIC): #Strong
        health = 150
        _UITexture = "LEGOWALLS_UI"
        _FieldTexture = "LEGOWALLS"
class WeaponTypes():
    class _GENERIC(PlacementType):
        methodReference = Weapon
        damage = 1
        canPlace_ROOT = True
        canPlace_ABOVE = False
        canPlace_BELOW = False
        canPlace_LEFT = False
        canPlace_RIGHT = False
    class NerfGun(_GENERIC): #Long range
        pass
    class ToothpickTrap(_GENERIC): #Short range
        pass
    class BottleRocket(_GENERIC): #Overshot mortar
        pass
    class BarrelOfMonkeys(_GENERIC): #Trap
        pass

class EnemyTypes():
    class _GENERIC():
        health = 1
        damage = 1
        speed = 100
        _WalkingAnimation = ["NOTEXTURE"]
        _AttackAnimation = ["NOTEXTURE"]
        _AttackAnimationAttackFrame = 0
    class ToyCar(_GENERIC): #Fast and weak
        damage = 20
        speed = 250
        _WalkingAnimation = ["CAR1_WALK", "CAR2_WALK", "CAR3_WALK"]
        _AttackAnimation = "ATTACK_TEMP"
        _AttackAnimationAttackFrame = 2
    class ToySoldier(_GENERIC): #Basic, medium speed and medium strength
        damage = 40
        speed = 120
        _WalkingAnimation = ["SOLDIER1_WALK", "SOLDIER2_WALK", "SOLDIER3_WALK"]
        _AttackAnimation = "ATTACK_TEMP"
        _AttackAnimationAttackFrame = 2
    class TeddyBear(_GENERIC): #Slow and strong
        damage = 75
        speed = 60
        _WalkingAnimation = ["TEDDYBEAR1_WALK", "TEDDYBEAR2_WALK", "TEDDYBEAR3_WALK"]
        _AttackAnimation = "ATTACK_TEMP"
        _AttackAnimationAttackFrame = 2
    