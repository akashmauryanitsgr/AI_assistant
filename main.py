import os
import eel
import sys
#sys.path.append(os.path.dirname(os.path.abspath('D:\\endterm\\jarvis\\main.py')))

from engine.features import *
from engine.command import *
    
def start():
    
  eel.init("www")

  playAssistantSound()
  os.system('start chrome.exe --app=" http://127.0.0.1:5501/jarvis/www/index.html"')
  
  eel.start('index.html', mode="chrome", host='localhost')
 
  

    
