import SceneObjects
from MainEngine import Types
from MainEngine import Engine
class Globals:
  engine = None
  
  
class Main():
  def __init__(self):
    self._STARTENGINE()
    
  def _PRESTART(self):
    settings = Engine.PregameSettings()
    settings.SetScreenDimensions(Types.Vector2(800, 800))
    
  def _APPENDSCENEOBJECT(self, objectTuple):
    for _object in objectTuple:
      Globals.engine.Globals.sceneObjectsArray.append(_object)
      
  def _STARTENGINE(self):
    self._PRESTART()
    Globals.engine = Engine.Engine()

main = Main()
Globals.engine.Start()
injections = SceneObjects.Injections()
Globals.engine.SetCaption(injections.caption) #Just change this to whatever
objects = SceneObjects.Objects(Globals.engine)
main._APPENDSCENEOBJECT(objects.get())