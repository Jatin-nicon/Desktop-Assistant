import speech_recognition as sr
import keyboard
import pyttsx3
import time
from os import system


r = sr.Recognizer()


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.2)
    engine.stop() 

def execute_command(command):
    if "play" in command:
        speak("Playing media")
        time.sleep(0.2)
        keyboard.press_and_release('space')
    elif "volume" in command:
        if "increase" in command:
            speak("Increasing volume")
            for _ in range(5):
                keyboard.press_and_release('volume up')
                time.sleep(0.1)
        elif "decrease" in command:
            speak("Decreasing volume")
            for _ in range(5):
                keyboard.press_and_release('volume down')
                time.sleep(0.1)
        elif "mute" in command:
            speak("Muting volume")
            keyboard.press_and_release('volume mute')
        elif "unmute" in command:
            speak("Unmuting volume")
            keyboard.press_and_release('volume mute')
        elif "maximum" in command or "max" in command:
            speak("Setting volume to maximum")
            for _ in range(20):
                keyboard.press_and_release('volume up')
                time.sleep(0.05)
        

    elif "pause" in command:
        speak("Pausing media")
        keyboard.press_and_release('space')

    elif "forward" in command:
        speak("Skipping forward")
        keyboard.press_and_release('right')

    elif "back" in command:
        speak("Rewinding")
        keyboard.press_and_release('left')

    elif "new tab" in command:
        speak("Opening a new tab")
        keyboard.press_and_release('ctrl+t')

    elif "close" in command:
        if "tab" in command:
            speak("Closing tab")
            keyboard.press_and_release('ctrl+w')
        elif "you" in command:
            speak("Thak you for using me sir.... Goodbye")
            exit()
        elif "window" in command:
            speak("Closing window")
            keyboard.press_and_release('alt+f4')

    elif "refresh" in command:
        speak("Refreshing page")
        keyboard.press_and_release('f5')
    
    elif "scroll" in command:
        if "down" in command:
            speak("Scrolling down")
            keyboard.press_and_release('pagedown')
        elif "up" in command:
            speak("Scrolling up")
            keyboard.press_and_release('pageup')

    elif "search" in command:
        speak("What do you want to search?")
        search_query()

    elif "go" in command and "to" in command and "tab" in command:
        if "first" in command:
            speak("Going to first tab")
            keyboard.press_and_release('ctrl+1')
        elif "second" in command:
            speak("Going to second tab")
            keyboard.press_and_release('ctrl+2')
        elif "third" in command:
            speak("Going to third tab")
            keyboard.press_and_release('ctrl+3')
        elif "fourth" in command:
            speak("Going to fourth tab")
            keyboard.press_and_release('ctrl+4')
        elif "fifth" in command:
            speak("Going to fifth tab")
            keyboard.press_and_release('ctrl+5')
        elif "last" in command:
            speak("Going to last tab")
            keyboard.press_and_release('ctrl+9')
        elif "next" in command:
            speak("Going to next tab")
            keyboard.press_and_release('ctrl+tab')
        elif "previous" in command:
            speak("Going to previous tab")
            keyboard.press_and_release('ctrl+shift+tab')
        
    elif "open" in command:
        if "tor" in command:
            
            speak("Opening Tor Browser")
            keyboard.press("windows")
            time.sleep(0.3)  # allow Start Menu to open
            keyboard.release("windows")

            time.sleep(0.3)  # small wait so typing is not lost

            keyboard.write("tor")
            time.sleep(0.3)

            keyboard.press_and_release("enter")
        elif "chrome" in command:
            speak("Opening Google Chrome")
            keyboard.press("windows")
            time.sleep(0.3)  # allow Start Menu to open
            keyboard.release("windows")

            time.sleep(0.3)  # small wait so typing is not lost

            keyboard.write("chrome")
            time.sleep(0.3)

            keyboard.press_and_release("enter")
            time.sleep(1)
            keyboard.press_and_release("tab")
            time.sleep(0.3)
            keyboard.press_and_release("enter")
        
        elif "brave" in command:
            speak("Opening Brave Browser")
            keyboard.press("windows")
            time.sleep(0.3)  # allow Start Menu to open
            keyboard.release("windows")

            time.sleep(0.3)  # small wait so typing is not lost

            keyboard.write("Brave")
            time.sleep(0.3)

            keyboard.press_and_release("enter")
            time.sleep(1)
            keyboard.press_and_release("tab")
            time.sleep(0.3)
            keyboard.press_and_release("enter")


    elif "phone" in command:
         if "torch" in command:
            if "off" in command:
                speak("Turning off the phone's torch")
                keyboard.write("termux-torch off")
                keyboard.press_and_release("enter")
             
            elif "on" in command:
                speak("Turning on the phone's torch")
                keyboard.press("windows")
                time.sleep(0.3)  # allow Start Menu to open
                keyboard.release("windows")

                time.sleep(0.3)  # small wait so typing is not lost

                keyboard.write("terminal")
                time.sleep(0.3)

                keyboard.press_and_release("enter")
                time.sleep(1)
                keyboard.write("ssh u0_a405@192.168.1.109 -p 8022")
                keyboard.press_and_release("enter")
                time.sleep(1)
                keyboard.write("yes")
                keyboard.press_and_release("enter")
                time.sleep(1)

                keyboard.write("fighternicon")
                keyboard.press_and_release("enter")

                time.sleep(2)
                keyboard.write("termux-torch on")
                keyboard.press_and_release("enter")

           




    else:
        print("Command not recognized")


def search_query():
    with sr.Microphone() as source:
        print("Listening query...")
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio).lower()
        print("Searching:", query)
        keyboard.write(query)
        keyboard.press_and_release('enter')

    except Exception:
        print("Search failed")


def listen():
    with sr.Microphone() as source:
        print("Listening for commands...")
        # Adjust noise detection
        r.adjust_for_ambient_noise(source, duration=0.4)
        audio = r.listen(source, phrase_time_limit=4)  # STOP after you finish speaking

    try:
        command = r.recognize_google(audio).lower()
        print("Recognized:", command)

        execute_command(command)

    except Exception as e:
        print(e)

first_run = True

speak("Initializing assistant")
while True:
    if first_run:
        speak("I am here sir")
        first_run = False
    listen()
