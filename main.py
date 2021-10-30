# Importing necessary modules
import pyautogui as bot
import time
from datetime import datetime
import numpy as np
import webbrowser

# Getting Current Date and Time
currentTime = datetime.now()
currentHour = currentTime.hour
currentMinute = currentTime.minute
currentDay = str(datetime.today().strftime("%A"))




# Opening Link
def openingLink() :
    bot.moveTo(x=1285, y=254)
    time.sleep(1)
    bot.click(x=1285, y=254)
    time.sleep(1)
    bot.moveTo(x=1285, y=254)
    bot.click(x=1285, y=254)
    time.sleep(2)
    bot.click(x=880, y=153)

# Joining Class
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

# Ending Class
def endClass():
    bot.moveTo(x=828, y=723)
    bot.click(x=828, y=723)
    bot.hotkey("ctrl","w")






if __name__ == "__main__":

    while True:
        currentTime = datetime.now()
        currentHour = currentTime.hour
        currentMinute = currentTime.minute
        currentDay = str(datetime.today().strftime("%A"))
        print(currentHour)
        print(currentMinute)
        # Befor 10 AM
        if currentHour < 10 :

            # Opening Browser and waiting for class
            webbrowser.open("https://pmss.mydynamicerp.com/Student/Accounts/Login?ReturnUrl=%2fStudent%2fStudent%2fCreation%2fLiveClass")
            time.sleep(10)
            bot.moveTo(x=977, y=456)
            bot.click(x=977, y=456)
            time.sleep(10)
            bot.moveTo(x=128, y=225)
            bot.click(x=128, y=225)

            # Waiting for class to get started
            remainingMinutesForClass = (59 - currentMinute) * 60
            print(remainingMinutesForClass)
            print(remainingMinutesForClass / 60)
            time.sleep(remainingMinutesForClass)

        
        if currentDay == "Saturday":
           break
        elif currentHour > 16:
            bot.hotkey("win","d")
            bot.hotkey("alt","f4")
            time.sleep(1)
            bot.keyDown("enter")
            break
        else:
            if currentHour == 10:
                if currentMinute < 40:
                    mLoc = len(np.array(list(bot.locateAllOnScreen('my_screenshot.png',grayscale=False,confidence=0.9))))
                    print(f"mLocation {mLoc}")
                    print("Time for first class")
                    if mLoc >= 1:
                        openingLink()
                        time.sleep(10)
                        joiningClass()
                        print("Joined First Class")
                        remainingTime = (35 - currentMinute) * 60
                        print("Sleeping for {} s".format(remainingTime))
                        time.sleep(remainingTime)
                        endClass()
                        time.sleep(600)
                    else:
                        time.sleep(60)
                if currentMinute > 50:
                    mLoc = len(np.array(list(bot.locateAllOnScreen('my_screenshot.png',grayscale=False,confidence=0.9))))
                    print(f"mLocation {mLoc}")
                    print("Time for second class")
                    if mLoc >= 1:
                        openingLink()
                        time.sleep(10)
                        joiningClass()
                        print("JOined Second Class")
                        remainingTime = ((60 - currentMinute) + 25 )* 60
                        print("Sleeping for {} s".format(remainingTime))
                        time.sleep(remainingTime)
                        endClass()
                        time.sleep(600)
                    else:
                        time.sleep(60)
            if currentHour == 11:
                if currentMinute >= 40 :
                    mLoc = len(np.array(list(bot.locateAllOnScreen('my_screenshot.png',grayscale=False,confidence=0.9))))
                    print(f"mLocation {mLoc}")
                    print("Time for third class")
                    if mLoc >= 1:
                        openingLink()
                        time.sleep(10)
                        joiningClass()
                        print("JOined Third Class")
                        remainingTime = ((60 - currentMinute) + 15)*60
                        print("Sleeping for {} s".format(remainingTime))
                        time.sleep(remainingTime)
                        endClass()
                        time.sleep(600)
                    else:
                        time.sleep(60)

            if currentHour == 12:
                if currentMinute < 30:
                    mLoc = len(np.array(list(bot.locateAllOnScreen('my_screenshot.png',grayscale=False,confidence=0.9))))
                    print(f"mLocation {mLoc}")
                    
                    if mLoc >= 1:
                        print("Time for fourth class")
                        openingLink()
                        time.sleep(10)
                        joiningClass()
                        print("JOined Fourth Class")
                        remainingTime = ((60 - currentMinute) + 5) * 60
                        print("Sleeping for {} s".format(remainingTime))
                        time.sleep(remainingTime)
                        endClass()
                        time.sleep(1800)
                    else:
                        time.sleep(60)
            if currentHour == 13:
                if currentMinute >= 40:
                    mLoc = len(np.array(list(bot.locateAllOnScreen('my_screenshot.png',grayscale=False,confidence=0.9))))
                    print(f"mLocation {mLoc}")
                    print("Time for fifth class")
                    if mLoc >= 1:
                        openingLink()
                        time.sleep(10)
                        joiningClass()
                        print("JOined Fifth Class")
                        remainingTime = ((60 - currentMinute) + 15) * 60
                        print("Sleeping for {} s".format(remainingTime))
                        time.sleep(remainingTime)
                        endClass()
                        time.sleep(600)
                    else:
                        time.sleep(60)
            if currentHour == 14:
                if currentMinute >= 30:
                    mLoc = len(np.array(list(bot.locateAllOnScreen('my_screenshot.png',grayscale=False,confidence=0.9))))
                    print(f"mLocation {mLoc}")
                    print("Time for Sixth class")
                    if mLoc >= 1:
                        openingLink()
                        time.sleep(10)
                        joiningClass()
                        print("JOined Sixth Class")
                        remainingTime = ((60 - currentMinute) + 5) * 60
                        print("Sleeping for {} s".format(remainingTime))
                        time.sleep(remainingTime)
                        endClass()
                        time.sleep(600)
                    else:
                        time.sleep(60)
            if currentHour == 15:
                print("YEs")
                if currentMinute < 40:
                    print("YEs")
                    mLoc = len(np.array(list(bot.locateAllOnScreen('my_screenshot.png',grayscale=False,confidence=0.9))))
                    print(f"mLocation {mLoc}")
                    print("Time for Seventh class")
                    if mLoc >= 1:
                        openingLink()
                        time.sleep(10)
                        joiningClass()
                        print("JOined Seventh Class")
                        remainingTime = (55 - currentMinute) * 60
                        print("Sleeping for {} s".format(remainingTime))
                        time.sleep(remainingTime)
                        endClass()
                        time.sleep(600)
                    else:
                        time.sleep(60)
        print("OUT")
        time.sleep(30)
            
                    
                
                    
            
            
        
