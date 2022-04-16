import pygame, threading
from MainEngine import BMathL



class PregameSettings:
        def SetScreenDimensions(self, dimensions, gridDimension=None): #We expect dimensions to be a type Types.Vector2 but python is implicit (yucky) so we can't specify this.
            if (gridDimension == None):
                gridDimension = Engine.Globals.display
            Engine.Globals.screen = pygame.display.set_mode(dimensions.whole)
            Engine.Globals.display = gridDimension
    
class Engine:
    def __init__(self):
        pygame.mixer.pre_init(44100, 16, 2, 4096) #Audio mixer settings
        
    def Start(self, main): #Start the main gameloop
        pygame.init() #Initialize pygame duh
        self.Globals.clock = pygame.time.Clock()
        main._POSTSTART()
        while True:
            for event in pygame.event.get():
                self.EventHandler(event)
            self.Globals.clock.tick()
            self._UpdateSubscribers() #Tell every GameObject to call their Update function.
            self.Render() #Call a render update


    def _UpdateSubscribers(self):
        for subscriber in self.Globals.sceneObjectsArray:
            try:
                subscriber.obj.Update()
            finally:
                pass

    def GetDeltaTime(self): #Seconds since last frame
        return self.Globals.clock.get_rawtime() / 1000 * self.Globals.timeScale
    
    def EventHandler(self, event):
        if event.type == pygame.QUIT:
            quit()

    def CalculateRenderOrder(self):
        array = []
        linkedObjArray = []
        sOA_copy = self.Globals.sceneObjectsArray.copy()
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
        self.Globals._screen.fill((0,0,0)) #Background, can remove.
        renderOrderReturnVal = self.CalculateRenderOrder()
        if (renderOrderReturnVal == None):
            return
        array = renderOrderReturnVal[0]
        to_render = pygame.sprite.Group()
        for i in array:
            to_render.add(i.gameObject.sprite)
        to_render.draw(self.Globals.screen) 
        to_render.update()
        del to_render
        pygame.display.update()

    def SetCaption(self, value):
        pygame.display.set_caption(value)


    class Globals():
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
                _display = value
            else:
                _display = value.whole

            self._screen = self._screen = pygame.display.set_mode(_display)
        @property
        def gridDimensions(self):
            return self._gridDimensions
        @gridDimensions.setter
        def gridDimensions(self, value):
            if (type(value) == tuple):
                self._gridDimensions = value
            else:
                self._gridDimensions = value.whole
            