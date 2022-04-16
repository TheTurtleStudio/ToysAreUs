from MainEngine import Types
class Template():
    def __init__(self, engine):
        self.gameObject = Types.GameObject(engine)
        self.engine = engine
        self.Start()

    def Start(self):
        self.speed = 0
        self.sizeIncrease = 0

    def Update(self):
        self.gameObject.position += Types.Vector3(self.speed * self.engine.GetDeltaTime(), self.speed * self.engine.GetDeltaTime(), 0)
        self.gameObject.size += Types.Vector2(self.sizeIncrease * self.engine.GetDeltaTime(), self.sizeIncrease * self.engine.GetDeltaTime())
        
class Create():
    def __init__(self, engine):
        self.obj = Template(engine)
    @property
    def gameObject(self):
        return self.obj.gameObject