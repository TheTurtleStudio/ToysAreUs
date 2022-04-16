from GameObjects import Template


class Objects():
    def __init__(self, engine):
        self.test1 = Template.Create(engine)
        self.test1.gameObject.position = (4,3,2)
        self.test1.obj.speed = 20
        self.test1.obj.sizeIncrease = 20
        self.test1.gameObject.color = (255, 0, 0)

        self.test2 = Template.Create(engine)
        self.test2.gameObject.position = (2,1,1)
        self.test2.gameObject.size = (50,50)
        self.test2.obj.speed = 3
        self.test2.obj.sizeIncrease = 3
        self.test2.gameObject.color = (0, 255, 0)

        self.test3 = Template.Create(engine)
        self.test3.gameObject.position = (540,670,0)
        self.test3.obj.speed = -14
        self.test3.obj.sizeIncrease = 9
        self.test3.gameObject.color = (0, 0, 255)
    def get(self):
        return (self.test1, self.test2, self.test3)
class Injections():
    def __init__(self):
        self.caption = "ToysWereUs"
        self.abstract = [
            "#This is raw code to be after all other injections are made. Yes, I know this is vulnerable to ACE and very unsafe in general. No, I don't care. Why? Because I'm a thug.",
            "#Also this is an array/list... Idk man I hate python. I have no idea what the brackets are, they just seem like an array, maybe it's a list.",
            "#You can really just delete all this, just needed to explain somewhat what the hell this is.",
            "print(\"Injections complete\") #This is for debugging though!"
        ]