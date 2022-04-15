import pygame, threading
import Types #Our own types! Woot woot!
import BMathL
import time

class Globals():
    _display = (512, 512)
    _gridDimensions = (32,32)
    clock = None
    sceneObjectsArray = []
    _screen = pygame.display.set_mode(_display)
    @property
    def display(self):
        return display;
    @display.setter
    def display(self, value):
        if (type(value) == tuple):
            _display = value
        else:
            _display = value.whole

        _screen = _screen = pygame.display.set_mode(_display)
    @property
    def gridDimensions(self):
        return _gridDimensions
    @gridDimensions.setter
    def gridDimensions(self, value):
        if (type(value) == tuple):
            _gridDimensions = value
        else:
            _gridDimensions = value.whole


class PregameSettings:
    def SetScreenDimensions(self, dimensions, gridDimension=Globals.display): #We expect dimensions to be a type Types.Vector2 but python is implicit (yucky) so we can't specify this.
        Globals.screen = pygame.display.set_mode(dimensions.whole)
        Globals.display = gridDimension

    
class Engine:
    def __init__(self):
        pygame.mixer.pre_init(44100, 16, 2, 4096) #Audio mixer settings
        pygame.init() #Initialize pygame duh
        Globals.clock = pygame.time.Clock()
        self.MainThread = threading.Thread(target=self.StartMain) #Start main game loop in its own thread.
        self.MainThread.start()
        
    def StartMain(self): #Start the main gameloop
        while True:  
            for event in pygame.event.get():  
                self.EventHandler(event)
            Globals.clock.tick()
            self.Render() #Call a render update

    def GetDeltaTime(self): #Seconds since last frame
        return Globals.clock.get_rawtime() / 1000 #
    
    def EventHandler(self, event):
        if event.type == pygame.QUIT:
            quit()

    def CalculateRenderOrder(self):
        array = []
        linkedObjArray = []
        sOA_copy = Globals.sceneObjectsArray
        if (len(sOA_copy) != 0):
            for i in range(len(sOA_copy)):
                array.append(sOA_copy[i].position.z) #Add z component to array
                linkedObjArray.append(sOA_copy[i]) #Add GameObject to array
            n = len(array)
            linkedObjectQuicksort = BMathL.Math.QuickSort.LinkedObject()
            linkedObjectQuicksort.QuickSort(array, linkedObjArray, 0, n-1) #User our linked object quicksort algorithm
            return (linkedObjArray, array)
        return None

    
    def Render(self): #Note that the render function has literally no culling. Everything in the scene will be rendered no matter if it's even on the screen or not.
        Globals._screen.fill((0,0,0))
        renderOrderReturnVal = self.CalculateRenderOrder()
        if (renderOrderReturnVal == None):
            return
        array = renderOrderReturnVal[0]
        to_render = pygame.sprite.Group()
        for i in array:
            to_render.add(i.sprite)
        to_render.draw(Globals.screen)
        to_render.update()
        pygame.display.update()


class GameObject:
    def __init__(self): #Can optimize Update function to only call explicitly here
        self._position = Types.Vector3() #Default is (0,0,0)
        self._size = Types.Vector2(1,1)
        self.name = "New GameObject"
        self.sprite = Sprite()
    @property
    def position(self):
        return self._position
    @position.setter
    def position(self, value):
        if (type(value) == tuple):
            self._position = Types.Vector3(value[0], value[1], value[2])
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
            self._size = Types.Vector2(value[0], value[1])
        else:
            self._size = value
            
        #Change size here
    def Destroy(self):
        try:
            Globals.sceneObjectsArray.remove(self)
        except ValueError:
            pass
        del self


class Sprite(pygame.sprite.Sprite):
    def __init__(self, dimensions=(50,50), color=(255,255,255)):
        if not (type(dimensions) == tuple):
            dimensions = dimensions.whole
        super().__init__()
        self.image = pygame.Surface(dimensions)
        self.image.fill(color)
        self.rect = self.image.get_rect()
    
