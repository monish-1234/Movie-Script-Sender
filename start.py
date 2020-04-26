from pynput.keyboard import Key , Controller
import time

keyboard = Controller()
file = open('pirates.txt', 'r') 
time.sleep(4) 
while 1: 
      
    # read by character 
    char = file.read(1)           
    if not char:  
        break
          
    print(char)
    if (char==" "):
        time.sleep(0.2)
        keyboard.press(Key.enter)
    keyboard.press(char)
    keyboard.release(char)
    
  
file.close() 
