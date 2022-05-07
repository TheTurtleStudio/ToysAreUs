import SceneObjects
import threading
from MainEngine import Types
from MainEngine import Engine
class Globals:
  engine = None
  
  
class Main():
  def __init__(self):
    self._STARTENGINE()
    
  def _PRESTART(self):
    Globals.engine = Engine.Engine()
    settings = Engine.PregameSettings(Globals.engine)
    settings.SetScreenDimensions(Types.Vector2(SceneObjects.Injections.dimensions[0], SceneObjects.Injections.dimensions[1]))
    
  def _APPENDSCENEOBJECT(self, objectTuple):
    for _object in objectTuple:
      Globals.engine.CreateNewObject(_object)
      
  def _STARTENGINE(self):
    self._PRESTART()
    
  def _POSTSTART(self):
    Globals.engine.SetCaption(SceneObjects.Injections.caption) #Just change this to whatever
    for rawCode in SceneObjects.Injections.abstract:
      exec(rawCode)
    objects = SceneObjects.Objects(Globals.engine)
    self._APPENDSCENEOBJECT(objects.get())

if __name__ == "__main__":
  main = Main()
  Globals.engine.Start(main)