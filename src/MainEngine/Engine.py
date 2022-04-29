import pygame, threading
from MainEngine import BMathL
from MainEngine import Input
from MainEngine import Types
from MainEngine import Collision


class PregameSettings():
    def __init__(self, engine):
        self.engine = engine
    def SetScreenDimensions(self, dimensions, gridDimension=None): #We expect dimensions to be a type Types.Vector2 but python is implicit (yucky) so we can't specify this.
        if (gridDimension == None):
            gridDimension = dimensions
        self.engine._Globals.screen = pygame.display.set_mode(dimensions.whole)
        self.engine._Globals.display = dimensions.whole
    
class Engine:
    def __init__(self):
        pygame.mixer.pre_init(44100, 16, 2, 4096) #Audio mixer settings
        self._Globals = self.Globals()
        
    def Start(self, main): #Start the main gameloop
        pygame.init() #Initialize pygame duh
        pygame.key.set_repeat(1, 1)
        self._Globals.clock = pygame.time.Clock()
        self.Input = Input.InputHandler(self)
        self.Collisions = Collision.Collision(self)
        main._POSTSTART()
        while True:
            self.FrameEvents()
    
    def FindObject(self, name):
        for subscriber in self._Globals.sceneObjectsArray:
            if subscriber.gameObject.name == name:
                return subscriber
        return None

    def FrameEvents(self):
        self._Globals.clock.tick()
        self._PostEventsToInput()
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
        return self._Globals.clock.get_rawtime() / 1000 * self._Globals.timeScale

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

    def Render(self): #Note that the render function has literally no culling. Everything in the scene will be rendered no matter if it's even on the screen or not.
        self._Globals._screen.fill((0,0,0)) #Background, can remove.
        renderOrderReturnVal = self.CalculateRenderOrder()
        if (renderOrderReturnVal == None):
            return
        array = renderOrderReturnVal[0]
        #to_render = pygame.sprite.Group()
        for i in array:
            self._Globals.screen.blit(i.gameObject.sprite.image, (i.gameObject.position.x, i.gameObject.position.y))
            #to_render.add(i.gameObject.sprite)
        #to_render.draw(self._Globals.screen) 
        #del to_render
        pygame.display.update()

    def SetCaption(self, value):
        pygame.display.set_caption(value)

    class Globals():
        CollisionLayer = Types.CollisionLayer()
        _display = (512, 512)
        _gridDimensions = (32,32)
        clock = None
        sceneObjectsArray = []
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
        @display.getter
        def display(self):
            return self._display
        @property
        def gridDimensions(self):
            return self._gridDimensions
        @gridDimensions.setter
        def gridDimensions(self, value):
            if (type(value) == tuple):
                self._gridDimensions = value
            else:
                self._gridDimensions = value.whole
        @gridDimensions.getter
        def gridDimensions(self):
            return self._gridDimensions
            
