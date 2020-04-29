from pynput.keyboard import Key , Controller #Importing "pynput" module for simultaing key press
import time #Importing "time" module for delay

a= int(input("Choose any movie script :- \n 1. Bee Movie \n 2. Pirates of the Carribean \n 3. Alien Vs Predator \n 4. Wall-E \n 5. Scary Movie \n 6. Titanic \n 7. Test Script \n 8. Custom File \n \n"))

#list of existing movie scripts
if(a==1):
    file = open('bee.txt', 'r')
elif (a==2):
    file = open('pirates.txt', 'r')
elif (a==3):
    file = open('alien.txt', 'r')
elif (a==4):
    file = open('walle-e.txt', 'r')
elif (a==5):
    file = open('scarymovie.txt', 'r')
elif (a==6):
    file = open('titanic.txt', 'r')
elif (a==7):
    file = open('lorem.txt', 'r') 
elif (a==8):
    custom=input("Enter .txt file Name and/or Location \n ")
    file = open(custom, 'r') #opening custom file


print ("--------------------DISCLAIMER--------------------DISCLAIMER--------------------DISCLAIMER--------------------\n \n \n \t This Script does not stop automatically untill the entire script is finished so , you cannot use your computer untill the script is finished. \n \n Press Ctrl+C / Ctrl+Z in the shell to stop the script. \n \n Do not indulge in any illegal activities using this script \n \n The Developer IS NOT RESPONSIBLE for whatever way you choose to use this \n \n The script will start running in .... \n 14")
time.sleep(2)#Delay to select the output window.
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
      
    char = file.read(1) #reading one character
    if not char: #if cannot read(end of file), stop program.
        break
          
    print(char) #output each character to python console
    if (char==" "): #if character empty, delay for 0.2 seconds and send (press enter)
        time.sleep(0.2) 
        keyboard.press(Key.enter)
    keyboard.press(char) #Simulate character key press - start
    keyboard.release(char) #Simulate character key press - end
    
  
file.close() 

#Programmed by https://github.com/monish-1234/