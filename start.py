from pynput.keyboard import Key , Controller
import time

a=input(int("Choose any movie script :- \n 1. Test \n 2. Bee Movie \n 3. Pirates of the Carribean \n 4. Alien Vs Predator \n 5. Wall-E \n 6. Scary Movie \n 7. Titanic \n 8. Custom File "))

if(a==1):
    file = open('lorem.txt', 'r') 
else if (a==2):
    file = open('bee.txt', 'r')
else if (a==3):
    file = open('pirates.txt', 'r')
else if (a==4):
    file = open('pirates.txt', 'r')
else if (a==5):
    file = open('pirates.txt', 'r')
else if (a==6):
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
