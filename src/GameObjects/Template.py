from MainEngine import Types #NEEDED. Mainly for Types.GameObject creation.
class Template(): #Change this to the name of your script
    def __init__(self, engine):
        self.gameObject = Types.GameObject(engine)
        self.engine = engine
        self.Start()

    def Start(self): #Called when the object is added to the scene.
        self.speed = 0
        self.sizeIncrease = 0

    def Update(self): #This is called every rendercycle
        #Below is some example code that moves the square. The attached GameObject.
        self.gameObject.position += Types.Vector3(self.speed * self.engine.GetDeltaTime(), self.speed * self.engine.GetDeltaTime(), 0)
        self.gameObject.size += Types.Vector2(self.sizeIncrease * self.engine.GetDeltaTime(), self.sizeIncrease * self.engine.GetDeltaTime())
        print(id(self.gameObject))
        
#Create needs to be defined for every script in this folder. Everything should be exactly the same except for what is commented below, read that.
class Create():
    def __init__(self, engine):
        self.obj = Template(engine) #Replace Template with the name of your class
    @property
    def gameObject(self):
        return self.obj.gameObject