from pynput.keyboard import Key , Controller
import time

a= int(input("Choose any movie script :- \n 1. Test Script \n 2. Bee Movie \n 3. Pirates of the Carribean \n 4. Alien Vs Predator \n 5. Wall-E \n 6. Scary Movie \n 7. Titanic \n 8. Custom File \n \n"))

if(a==1):
    file = open('lorem.txt', 'r') 
elif (a==2):
    file = open('bee.txt', 'r')
elif (a==3):
    file = open('pirates.txt', 'r')
elif (a==4):
    file = open('alien.txt', 'r')
elif (a==5):
    file = open('walle-e.txt', 'r')
elif (a==6):
    file = open('scarymovie.txt', 'r')
elif (a==7):
    file = open('titanic.txt', 'r')
elif (a==8):
    custom=input("Enter .txt file Name and/or Location \n ")
    file = open(custom, 'r')


print ("--------------------DISCLAIMER--------------------DISCLAIMER--------------------DISCLAIMER--------------------\n \n \n \t This Script does not stop automatically untill the entire script is finished so , you cannot use your computer untill the script is finished. \n \n Press Ctrl+C / Ctrl+Z in the shell to stop the script. \n \n Do not indulge in any illegal activities using this script \n \n The Developer IS NOT RESPONSIBLE for whatever way you choose to use this \n \n The script will start running in .... \n 14")
time.sleep(2)
print (" \n 12....")
time.sleep(2)
print (" \n 10....")
time.sleep(2)
print (" \n 8....")
time.sleep(1)
print (" \n 7....")
time.sleep(7) 
keyboard=Controller()
while 1: 
      
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
