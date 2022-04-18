import pygame


class Collision():
    def __init__(self, engine):
        self.engine = engine
        self.CollisionLayersRef = self.engine._Globals.CollisionLayer
    def RectCollide(self, obj, layers=None):
        if (layers == None):
            layers = [self.CollisionLayersRef.NONE]
        return pygame.Rect.collidelistall(obj.gameObject.sprite.rect, self._GrabList(layers))
    def PointCollide(self, point, layers=None):
        if (layers == None):
            layers = [self.CollisionLayersRef.NONE]
        collisionList = []
        for potentialCollision in self._GrabList(layers):
            if pygame.Rect.collidepoint(potentialCollision, point):
                collisionList.append(potentialCollision)
        return collisionList
    def _GrabList(self, layers):
        returnList = []
        for obj in self.engine._Globals.sceneObjectsArray:
            if (obj.gameObject.collisionLayer in layers):
                returnList.append(obj.gameObject.sprite.rect)
        return returnList
