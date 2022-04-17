import pygame
from sympy import true


class InputHandler():
    def __init__(self, engine):
        self.events = []
        self.engine = engine
        self.TestFor = self._TestFor(self)
    def _getEvents(self):
        return self.events
    def postEvents(self, events):
        self.events = events
    def clearEvents(self):
        self.events.clear()
    class _TestFor():
        def __init__(self, handler):
            self._InputHandler = handler
        def QUIT(self):
            return self._testFor(pygame.QUIT)[0]
        def KEYDOWN_ANY(self):
            return self._testFor(pygame.KEYDOWN)[0]
        def KEYDOWN(self, key):
            keys = pygame.key.get_pressed()
            if (keys[key]):
                return True
            return False
        def _testFor(self, typeOf):
            for i in self._InputHandler._getEvents():
                if i.type == typeOf:
                    return (True, i)
            return (False, None)