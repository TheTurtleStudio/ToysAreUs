from MainEngine import Types #NEEDED. Mainly for Types.GameObject creation.
import pygame
class Draggable(): #Change this to the name of your script
    def __init__(self, engine):
        self.gameObject = Types.GameObject(engine)
        self.engine = engine
        self.creator = None

    def Start(self): #Called when the object is added to the scene.
        self.pressed = False
        self.offset = None
        self.canDrag = False

    def Update(self): #This is called every rendercycle
        if (self.engine.Input.TestFor.RIGHTMOUSEDOWN()): #Is this the frame the mousebutton was initially pressed?
            self.canDrag = True
        elif ((self.pressed is False) and (self.engine.Input.TestFor.RIGHTMOUSEDOWN() is False)): #Is the mousebutton not pressed and the mouse was not pressed initially on this frame?
            self.canDrag = False
        if self.canDrag: #Can we drag this?
            if (self.engine.Input.TestFor.RIGHTMOUSESTATE()): #Is the mouse state down? (Is it currently being pressed?)
                if (self.gameObject.sprite.rect in self.engine.Collisions.PointCollide(self.engine.Input.TestFor.MOUSEPOS(), [self.engine._Globals.CollisionLayer.UI])): #Is the mouse colliding with our sprite?
                    if (self.pressed == False):
                        mousepos = self.engine.Input.TestFor.MOUSEPOS()
                        self.offset = (self.gameObject.position.x - mousepos[0], self.gameObject.position.y - mousepos[1]) #Positional modification stuff
                    self.pressed = True
                if self.pressed and (not (self.offset == None)): #If the mouse is pressed and there's an offset to the mouse (pressed shouldn't be true if there's no offset, this is a failsafe.)
                    mousepos = self.engine.Input.TestFor.MOUSEPOS()
                    self.gameObject.position = Types.Vector3(mousepos[0] + self.offset[0], mousepos[1] + self.offset[1], self.gameObject.position.z) #Change position of draggable
            elif self.pressed:
                self.pressed = False
                self.offset = None
                self.canDrag = False
            
#Create needs to be defined for every script in this folder. Everything should be exactly the same except for what is commented below, read that.
class Create():
    def __init__(self, engine):
        self.obj = Draggable(engine) #Replace Template with the name of your class
        self.obj.creator = self
    @property
    def gameObject(self):
        return self.obj.gameObject