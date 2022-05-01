from MainEngine import Types
import pygame
from MainEngine.Engine import Engine


class Sheets():
    def __init__(self, _engine: Engine):
        self.engine = _engine
    def Disect(self, sheetPath: str, spriteDimensions: Types.Vector2, amount: int):
        #Convert whatever it is to Vector2
        if (type(spriteDimensions) == Types.Vector3):
            spriteDimensions = Types.Vector2(spriteDimensions.x, spriteDimensions.y)
        if (type(spriteDimensions) == tuple):
            spriteDimensions = Types.Vector2(spriteDimensions[0], spriteDimensions[1])

        sheet = pygame.image.load(sheetPath).convert_alpha()
        spriteList = []
        sheetRect = sheet.get_rect()
        rows = sheetRect.size[0] / spriteDimensions.x
        collumns = sheetRect.size[1] / spriteDimensions.y

        if not (rows.is_integer() and collumns.is_integer()):
            print(f"CANNOT CONVERT \"{sheetPath}\" TO SPRITES, INVALID DIMENSIONS")
            return []

        rows = int(rows)
        collumns = int(collumns)
            
        for y in range(collumns):
            for x in range(rows):
                if ((y * rows) + x) >= amount:
                    break
                image = pygame.Surface(spriteDimensions.whole).convert_alpha()
                image.blit(sheet, (0, 0), pygame.Rect(x * spriteDimensions.x, y * spriteDimensions.y, 32, 32))
                print(pygame.Rect(x * spriteDimensions.x, y * spriteDimensions.y, 32, 32))
                spriteList.append(image)
        return spriteList
