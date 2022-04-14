import Engine as PyE
import threading


class Globals:
  engine = null
  
  
class Main:
  def __init__(self):
    self._STARTENGINE()
    
  def _PRESTART(self):
    settings = PyE.PregameSettings()
    settings.SetScreenDimensions(Types.Vector2(512,512))
    
  def _DEFSTARTINGOBJ(self):
    gm1 = PyE.GameObject()
    gm1.position = Types.Vector3(0,0,2)
    gm1.Update()
    gm2 = PyE.GameObject()
    gm2.position = PyE.Types.Vector3(15,5,1) #Maybe call update everytime a property changes?
    gm2.Update()
    gm2.sprite.image.fill((58,192,18))
    self._APPENDSCENEOBJECT(gm1, gm2)
    
  def _APPENDSCENEOBJECT(self, *args _objects):
    for _object in _objects:
      PyE.Globals.sceneObjectsArray.append(_object)
      
  def _STARTENGINE(self)
    self._PRESTART()
    Globals.engine = PyE.Engine()
    
    
    
main = Main()
