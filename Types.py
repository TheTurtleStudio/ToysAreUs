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
