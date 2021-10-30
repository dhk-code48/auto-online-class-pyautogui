import pyautogui as bot
import os
import time
from datetime import datetime
import numpy as np
import webbrowser



# Getting Current Time
currentTime = datetime.now()
currentHour = currentTime.hour
currentMinute = currentTime.minute
currentDay = str(datetime.today().strftime("%A"))


# Openning Browser and waiting for class
webbrowser.open("https://pmss.mydynamicerp.com/Student/Accounts/Login?ReturnUrl=%2fStudent%2fStudent%2fCreation%2fLiveClass")
time.sleep(10)
bot.moveTo(x=977, y=456)
bot.click(x=977, y=456)
time.sleep(5)
bot.moveTo(x=128, y=225)
bot.click(x=128, y=225)


# Waiting for class to get started
if currentHour < 10 :
    remainingMinutesForClass = (59 - currentMinute) * 60
    print(remainingMinutesForClass)
    print(remainingMinutesForClass / 60)
    time.sleep(remainingMinutesForClass)


if currentDay == "Saturday":
    print("Happy Holiday Boss !")
else:
    print("Today's Routine \n")

    print("10 - 10:40 AM                 ||          C Math \n")
    
    if currentDay == "Sunday":
        print("10:50 - 11:30 AM              ||          HPE \n")
    else:
        print("10:50 - 11:30 AM              ||          Account \n")

    print("11:40 - 12:20 PM              ||          OPT Math \n")

    if currentDay == "Tuesday":
        print("12:30 - 1:10 PM               ||          HPE \n")
    else:
        print("12:30 - 1:10 PM               ||          English \n")

    print("1:40 - 2:20 PM                ||          Science \n")
    print("2:30 - 3:10 PM                ||          Social \n")
    print("3:20 - 4 PM                   ||          Nepali \n")
    
        



def openingLink() :
    bot.moveTo(x=1285, y=254)
    time.sleep(1)
    bot.click(x=1285, y=254)
    time.sleep(1)
    bot.moveTo(x=1285, y=254)
    bot.click(x=1285, y=254)
    time.sleep(5)
    bot.click(x=880, y=153)

def joiningClass():
    # Turn Off
    bot.moveTo(x=431, y=579)
    bot.click(x=431, y=579)

    # Turn Off Camera
    bot.moveTo(x=504, y=580)
    bot.click(x=504, y=580)

    # Ask To Join
    bot.moveTo(x=1014, y=445)
    bot.click(x=1014, y=445)


def endClass():
    bot.moveTo(x=828, y=723)
    bot.click(x=828, y=723)
    bot.hotKey("ctrl","w")


def classStuff():
    print("Time for class")
    mLocation = np.array(list(bot.locateAllOnScreen('my_screenshot.png',grayscale=False,confidence=0.8)))
    print(len(mLocation))
    if len(mLocation)>0:
        print("Joining Class")
        openingLink()
        # Waiting for google meet to open
        time.sleep(20)
        joiningClass()

        if currentHour == 10:
            remainingTime =  (40 - currentMinute) * 60
            print(remainingTime)
            time.sleep(remainingTime)
            if currentMinute == 40:
                endClass()
            if currentMinute >= 50:
                remainingTime = (59 - currentMinute) * 60
                print(remainingTime)
                time.sleep(remainingTime)
        if currentHour == 11:
            if currentMinute == 0:
                remainingTime =  30 * 60
                print(remainingTime)
                time.sleep(remainingTime)
            if currentMinute == 30:
                encClass()
                print("Ending Class")
            if currentMinute >= 40:
                remainingTime = (59 - currentMinute) * 60
                time.sleep(remainingTime)
        if currentHour == 12:
            
            if currentMinute == 20:
                endClass()
                print("Ending Class")
            if currentMinute >= 30:
                remainingTime = (59 - currentMinute) * 60
                print(remainingTime)
                time.sleep(remainingTime)
        if currentHour == 1:
            if currentMinute == 10:
                endClass()
                print("Ending Class")
            if currentMinute >= 20:
                remainingTime = (40 - currentMinute) * 60
                print(remainingTime)
                time.sleep(remainingTime)
        if currentHour == 2:
            if currentMinute == 20:
                endClass()
                print("Ending Class")
            if currentMinute >= 30:
                remainingTime = (59 - currentMinute) * 60
                print(remainingTime)
                time.sleep(remainingTime)
        if currentHour == 3:
            if currentMinute == 10:
                endClass()
                print("Ending Class")
                
        
                

        
        time.sleep(600)


if __name__ == "__main__":
    
    while True:
       
       if currentDay == "Saturday":
           break
       elif currentHour >= 16:
            bot.hotkey("win","d")
            bot.hotkey("alt","f4")
            time.sleep(1)
            bot.keyDown("enter")
            break
       else:
           classStuff()
           time.sleep(60)
            
            
            





