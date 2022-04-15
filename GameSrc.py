import Engine as PyE
import threading, time


class Globals:
  engine = None
  player = PyE.GameObject()
  
  
class Main:
  def __init__(self):
    self._STARTENGINE()
    
  def _PRESTART(self):
    settings = PyE.PregameSettings()
    settings.SetScreenDimensions(PyE.Types.Vector2(512,512))
    
  def _DEFSTARTINGOBJ(self):
    Globals.player.position = PyE.Types.Vector3(0,0,2)
    self.BackGround = PyE.GameObject()
    self.gm2 = PyE.GameObject()
    self.gm2.position = PyE.Types.Vector3(15,5,1) #Maybe call update everytime a property changes?
    self.gm2.sprite.image.fill((58,192,18))
    self._APPENDSCENEOBJECT(Globals.player, self.gm2)
    
  def _APPENDSCENEOBJECT(self, *args):
    for _object in args:
      PyE.Globals.sceneObjectsArray.append(_object)
      
  def _STARTENGINE(self):
    self._PRESTART()
    self._DEFSTARTINGOBJ()
    Globals.engine = PyE.Engine()
    self.GameThread()
    
  class GameThread():
    def __init__(self):
      self.gameThread = threading.Thread(target=self.ThreadTarget)
      self.gameThread.start()
      
    def ThreadTarget(self):
      i = 0
      while self.gameThread.is_alive():
        i += 1
        if (i % 1 == 0):
          print(Globals.engine.GetDeltaTime())
        Globals.player.position += PyE.Types.Vector3(0.2 * Globals.engine.GetDeltaTime(),0,0)

    
    
main = Main()
