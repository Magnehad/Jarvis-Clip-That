from wykrywAudio import mow, google
import pyttsx3
from pynput.keyboard import Key, Controller
import pygetwindow as gw
import webbrowser as web

keyboard = Controller()
engine = pyttsx3.init()
engine.say("Good morning, Sir.")
engine.runAndWait()

while True:
    tekst = mow()
    if "jarvis" in tekst or "Jarvis" in tekst or "Doravis" in tekst or "Jervis" in tekst or "Charlie's" in tekst or "Journey" in tekst or "Jaravis" in tekst or "Jar" in tekst:
        if "clip" in tekst or "Clip" in tekst or "keep" in tekst or "Keep" in tekst or "creep" in tekst or "Calipadat" in tekst or "calipadat" in tekst or "Klee" in tekst or "Alipidat" in tekst:
            try:
                rivals=gw.getWindowsWithTitle('Marvel Rivals')[0]
                rivals.minimize()
                keyboard.press(Key.ctrl)
                keyboard.press(Key.alt)
                keyboard.press("]")
                keyboard.release(Key.ctrl)
                keyboard.release(Key.alt)
                keyboard.release("]")
                engine.say("Clipped those fools")
                engine.runAndWait()
                rivals.restore()
            except IndexError:
                engine.say("Marvel: Rivals is not on")
                engine.runAndWait()

        elif "google" in tekst or "googol" in tekst or "Google" in tekst:
            url= "https://www.google.com/search?q=" + str(google(tekst))
            wypowiedz="Googling " + str(google(tekst)) + " , Sir."
            engine.say(wypowiedz)
            engine.runAndWait()
            web.open(url)

        elif "exit" in tekst or "stop" in tekst or "end" in tekst or "Exit" in tekst or "Stop" in tekst or "End" in tekst: 
            engine.say("Goodbye, sir.")
            engine.runAndWait()
            break
        elif "test" in tekst or "Test" in tekst:
            engine.say("TEST")
            engine.runAndWait()
        else:
            engine.say("Hello, Sir.")
            engine.runAndWait()
        
        
            








