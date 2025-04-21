import os
import eel
import sys

# Import your custom assistant functions
from engine.features import *
from engine.command import *

def start():
    # Initialize Eel with your absolute path to the "www" folder
    eel.init(r"D:\PYTHON PROJECT\AI_assistant\www")
    
    # Play your assistant startup sound
    playAssistantSound()
    
    # OPTION 1: Launch as Chrome App Window (for standalone look)
    os.system('start chrome.exe --app="http://localhost:8000/index.html"')
    
    # Start Eel web server without opening a second browser window
    eel.start('index.html', mode="none", host='localhost')

    # ---------
    # If you prefer Eel to auto-open Chrome normally, then use this instead:
    # eel.start('index.html', mode="chrome", host='localhost')
    # and remove the os.system(...) line above
    # ---------

# Only run if this file is executed directly
if __name__ == "__main__":
    start()
