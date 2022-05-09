import pygame, threading
from MainEngine import BMathL
from MainEngine import Input
from MainEngine import Types
from MainEngine import Collision
from MainEngine import ImageManipulation
import Main


class PregameSettings():
    def __init__(self, engine):
        self.engine = engine
    def SetScreenDimensions(self, dimensions: Types.Vector2):
        self.engine._Globals.screen = pygame.display.set_mode(dimensions.whole)
        self.engine._Globals.display = dimensions.whole  
class Engine():
    def __init__(self, initialStart=True):
        if initialStart is True:
            pygame.init() #Initialize pygame duh
            pygame.mixer.pre_init(44100, 16, 2, 4096) #Audio mixer settings
        self._Globals: self.Globals = self.Globals()
        
    @property
    def timeScale(self):
        return self._Globals.timeScale
    @timeScale.setter
    def timeScale(self, value):
        if (type(value) == float) or (type(value) == int):
            self._Globals.timeScale = value
        else:
            print("Can't set timeScale to an arbitrary value; only integers and floats allowed.")

    def Start(self, main: Main.Main): #Start the main gameloop
        self._Globals.clock = pygame.time.Clock()
        self.Input = Input.InputHandler(self)
        self.Collisions = Collision.Collision(self)
        main._POSTSTART()
        self.mainReference = main
        while True:
            self.FrameEvents()
    
    def SetUniversal(self, key: str, value):
        self._Globals.Universals[key] = value

    def GetUniversal(self, key: str):
        return self._Globals.Universals[key]

    def FindObject(self, name: str):
        for subscriber in self._Globals.sceneObjectsArray:
            if subscriber.gameObject.name == name:
                return subscriber
        return None

    def FrameEvents(self):
        self._Globals.clock.tick()
        self._PostEventsToInput()
        self._Globals._totalTime += self.GetDeltaTime()
        self._UpdateSubscribers() #Tell every GameObject to call their Update function.
        if (self.Input.TestFor.QUIT()):
            quit()
        self.Input.clearEvents()
        self.Render() #Call a render update
    
    def CreateNewObject(self, _object):
        try:
            self._Globals.sceneObjectsArray.append(_object)
            _object.obj.Start()
        except AttributeError:
            pass

    def _PostEventsToInput(self):
        self.Input.postEvents(pygame.event.get())

    def _UpdateSubscribers(self):
        for subscriber in self._Globals.sceneObjectsArray:
            try:
                subscriber.obj.Update()
            except AttributeError:
                pass

    def GetDeltaTime(self): #Seconds since last frame
        return ((self._Globals.lastRenderTime - self._Globals.currentRenderTime) / 1000) * self._Globals.timeScale

    def GetTotalTime(self):
        return self._Globals._totalTime

    def CalculateRenderOrder(self):
        array = []
        linkedObjArray = []
        sOA_copy = self._Globals.sceneObjectsArray.copy()
        if (len(sOA_copy) != 0):
            for obj in sOA_copy:
                if (obj.gameObject.renderEnabled):
                    array.append(obj.gameObject.position.z) #Add z component to array
                    linkedObjArray.append(obj) #Add GameObject to array
            n = len(array)
            linkedObjectQuicksort = BMathL.Math.QuickSort.LinkedObject()
            linkedObjectQuicksort.QuickSort(array, linkedObjArray, 0, n-1) #User our linked object quicksort algorithm
            return (linkedObjArray, array)
        del array, linkedObjArray, sOA_copy
        return None

    def Reload(self):
        for item in self._Globals.sceneObjectsArray.copy():
            self._Globals.sceneObjectsArray.remove(item)
            del item
        del self.Input
        del self.Collisions
        del self._Globals
        self.mainReference.Reload()

    def Render(self): #Note that the render function has literally no culling. Everything in the scene will be rendered no matter if it's even on the screen or not.
        self._Globals.currentRenderTime = pygame.time.get_ticks()
        self._Globals._screen.fill((0,0,0)) #Background, can remove.
        renderOrderReturnVal = self.CalculateRenderOrder()
        if (renderOrderReturnVal == None):
            return
        array = renderOrderReturnVal[0]
        for i in array:
            self._Globals.screen.blit(i.gameObject.sprite.image, (i.gameObject.position.x, i.gameObject.position.y))
        pygame.display.update()
        self._Globals.lastRenderTime = pygame.time.get_ticks()

    def AddImageAsset(self, key: str, value: str or list, transparency=True):
        if type(value) == str:
            self._Globals.Assets[key] = pygame.image.load(value).convert_alpha() if transparency else pygame.image.load(value)
        elif type(value) == list:
            self._Globals.Assets[key] = [(img.convert_alpha() if transparency else img) for img in value]
        elif type(value) == pygame.Surface:
            self._Globals.Assets[key] = value.convert_alpha() if transparency else value
        else:
            print("Can only import lists of paths or paths.")

    def GetImageAsset(self, key: str or pygame.Surface) -> pygame.Surface:
        try:
            return self._Globals.Assets[key]
        except KeyError:
            return None

    def AddAnimation(self, key: str, sequence: list, framerate: float, loop=True):
        self._Globals.Animations[key] = Types.Animation(sequence, framerate, loop)

    def GetAnimation(self, key: str) -> Types.Animation:
        try:
            return self._Globals.Animations[key]
        except KeyError:
            return None

    def SetCaption(self, value: str):
        pygame.display.set_caption(value)

    def SetIcon(self, value: str):
        pygame.display.set_icon(pygame.image.load(value))

    class Globals():
        _totalTime = 0
        Assets = {}
        Animations = {}
        sceneObjectsArray = []
        _display = (512, 512)
        clock = None
        lastRenderTime = pygame.time.get_ticks()
        currentRenderTime = pygame.time.get_ticks()

        _screen = pygame.display.set_mode(_display)
        timeScale = 1
        @property
        def display(self):
            return self._display
        @display.setter
        def display(self, value):
            if (type(value) == tuple):
                self._display = value
            else:
                self._display = value.whole

            self._screen = pygame.display.set_mode(self._display)
            
