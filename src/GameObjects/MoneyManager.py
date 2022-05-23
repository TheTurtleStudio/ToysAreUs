import math
from MainEngine import Engine, Types #NEEDED. Mainly for Types.GameObject creation.
import pygame

class MoneyManager(): #Change this to the name of your script
    def __init__(self, engine):
        self.gameObject = Types.GameObject(engine)
        self.engine: Engine.Engine = engine
        self.creator = None
        self._money = 0

    def Start(self):
        self._money = 150

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, value):
        oldMoney = self._money + 0
        self._money = value
        if self._money > 5000:
            self._money = 5000
        self.engine.FindObject("MONEY").obj.gameObject.text = self.formatMoneyText(self._money)

    def formatMoneyText(self, textToFormat: str):
        return "${:,}".format(math.floor(int(textToFormat)))

#Create needs to be defined for every script in this folder. Everything should be exactly the same except for what is commented below, read that.
class Create():
    def __init__(self, engine):
        self.obj: MoneyManager = MoneyManager(engine) #Replace Template with the name of your class
        self.obj.creator = self
    @property
    def gameObject(self):
        return self.obj.gameObject
