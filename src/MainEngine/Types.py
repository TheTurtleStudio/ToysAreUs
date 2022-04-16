import pygame


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
class GameObject:
    def __init__(self, master): #Can optimize Update function to only call explicitly here
        self._master = master
        self.sprite = Sprite()
        self.position = Vector3() #Default is (0,0,0)
        self.size = Vector2(1,1)
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
            
        self.sprite.rect.x = self.position.x
        self.sprite.rect.y = self.position.y
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, value):
        if (type(value) == tuple):
            self._size = Vector2(value[0], value[1])
        else:
            self._size = value
        self.sprite.image = pygame.transform.scale(self.sprite.image, self._size.whole) 
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, value):
        if ((type(value) == tuple) and (len(value) == 3)):
            self._color = (value[0], value[1], value[2])
            self.sprite.image.fill(self._color)
        else:
            raise Exception("Can only change colors to tuples of length 3! RGB values!")
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