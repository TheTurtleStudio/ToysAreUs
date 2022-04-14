import pygame, threading
import Types #Our own types! Woot woot!
import BMathL
import time

class Globals():
    screen = pygame.display.set_mode((512,512)) #Default before PregameSettings change
    screenGridCellCount = (32,32)
    clock = None
    sceneObjectsArray = []


class PregameSettings:
    def SetScreenDimensions(self, dimensions, gridDimension=Globals.screenGridCellCount): #We expect dimensions to be a type Types.Vector2 but python is implicit (yucky) so we can't specify this.
        Globals.screen = pygame.display.set_mode(dimensions.whole)
        Globals.screenGridCellCount = gridDimension

    
class Engine:
    def __init__(self):
        pygame.mixer.pre_init(44100, 16, 2, 4096) #Audio mixer settings
        
        pygame.init() #Initialize pygame duh
        Globals.clock = pygame.time.Clock()
        self.MainThread = threading.Thread(target = self.StartMain) #Start main game loop in its own thread.
        self.MainThread.start()
        
    def StartMain(self): #Start the main gameloop
        while True:  
            for event in pygame.event.get():  
                self.EventHandler(event)
            self.Render() #Call a render update
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
            return linkedObjArray
        return None

    
    def Render(self): #Note that the render function has literally no culling. Everything in the scene will be rendered no matter if it's even on the screen or not.
        array = self.CalculateRenderOrder()
        to_render = pygame.sprite.Group()
        if (array == None):
            return
        for i in array:
            to_render.add(i.sprite)
        to_render.draw(Globals.screen)
        to_render.update()
        pygame.display.update()


class GameObject:
    def __init__(self):
        self.position = Types.Vector3() #Default is (0,0,0)
        self.size = Types.Vector2(1,1)
        self.name = "GameObject"
        self.sprite = Sprite()
        self.Update()
        pass
    def Update(self):
        self.sprite.rect.x = self.position.x
        self.sprite.rect.y = self.position.y
    def Destroy(self):
        try:
            Globals.sceneObjectsArray.remove(self)
        except ValueError:
            pass
        del self


class Sprite(pygame.sprite.Sprite):
    def __init__(self, height=32, width=32, color=(255,255,255)):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()

settings = PregameSettings()
settings.SetScreenDimensions(Types.Vector2(512,512))
#Z order testing START
gm1 = GameObject()
gm1.position = Types.Vector3(0,0,2)
gm1.Update()
gm2 = GameObject()
gm2.position = Types.Vector3(15,5,1) #Maybe call update everytime a property changes?
gm2.Update()
gm2.sprite.image.fill((58,192,18))
#Z order testing END
engine = Engine()
Globals.sceneObjectsArray.append(gm1)
Globals.sceneObjectsArray.append(gm2)





