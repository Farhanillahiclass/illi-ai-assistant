import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import subprocess
import time
import pyautogui
import glob
import psutil
import smtplib
import json
import winreg
from pathlib import Path

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    speak("Assalam o Alaikum Muhammad Farhan!")
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")   
    else:
        speak("Good Evening!")  
    speak("I am ILLI, your personal voice assistant. I was created by Muhammad Farhan. I am here to help you with all your needs!")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        r.dynamic_energy_threshold = True
        r.adjust_for_ambient_noise(source, duration=1)
        
        try:
            audio = r.listen(source)
        except Exception as e:
            print(f"Listen error: {e}")
            return "none"
    
    try:
        print("Recognizing...")
        query = ""
        attempts = ['en-in', 'en-US', 'en']
        
        for attempt in attempts:
            try:
                query = r.recognize_google(audio, language=attempt)
                if query.strip():
                    break
            except:
                continue
        
        if not query.strip():
            query = r.recognize_google(audio)
        
        print(f"User said: {query}")
        return query.lower()
        
    except sr.UnknownValueError:
        print("Could not understand audio...")
        return "none"
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return "none"
    except Exception as e:
        print(f"Error: {e}")
        return "none"

def launch_whatsapp():
    speak("Launching WhatsApp desktop app...")
    
    # Enhanced WhatsApp detection
    whatsapp_paths = [
        f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\WhatsApp\\WhatsApp.exe",
        f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\WhatsApp\\WhatsApp\\WhatsApp.exe",
        f"C:\\Program Files\\WindowsApps\\*\\WhatsApp.exe",
        f"C:\\Program Files (x86)\\WhatsApp\\WhatsApp.exe"
    ]
    
    for path in whatsapp_paths:
        try:
            matches = glob.glob(path)
            if matches:
                os.startfile(matches[0])
                speak("WhatsApp desktop app launched successfully!")
                return
        except:
            continue
    
    # Registry search
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Uninstall")
        for i in range(winreg.QueryInfoKey(key)[0]):
            try:
                subkey_name = winreg.EnumKey(key, i)
                if 'whatsapp' in subkey_name.lower():
                    subkey = winreg.OpenKey(key, subkey_name)
                    try:
                        install_location = winreg.QueryValueEx(subkey, "InstallLocation")[0]
                        whatsapp_exe = os.path.join(install_location, "WhatsApp.exe")
                        if os.path.exists(whatsapp_exe):
                            os.startfile(whatsapp_exe)
                            speak("WhatsApp desktop app launched successfully!")
                            winreg.CloseKey(subkey)
                            winreg.CloseKey(key)
                            return
                    except:
                        winreg.CloseKey(subkey)
            except:
                continue
        winreg.CloseKey(key)
    except:
        pass
    
    # Fallback to WhatsApp Web
    speak("WhatsApp desktop not found. Opening WhatsApp Web...")
    webbrowser.open("https://web.whatsapp.com")

def search_and_play_youtube(query):
    media_name = query.replace('play', '').strip()
    if media_name:
        speak(f"Searching YouTube for {media_name}")
        search_url = f"https://www.youtube.com/results?search_query={media_name}"
        webbrowser.open(search_url)
        time.sleep(4)
        
        speak("I found several videos. Which video would you like me to play? Please tell me the number: first, second, or third.")
        response = takeCommand()
        
        video_number = 1
        if 'first' in response or '1' in response:
            video_number = 1
        elif 'second' in response or '2' in response:
            video_number = 2
        elif 'third' in response or '3' in response:
            video_number = 3
        
        speak(f"Playing the {video_number} video...")
        try:
            # Navigate to the specified video
            pyautogui.press('tab', presses=8, interval=0.2)
            time.sleep(1)
            
            # Press down arrow to navigate to the specific video
            for _ in range(video_number - 1):
                pyautogui.press('down')
                time.sleep(0.5)
            
            pyautogui.press('enter')
            speak(f"Playing {media_name}")
        except Exception as e:
            print(f"Auto-play error: {e}")
            speak("Please manually select the video from search results")

def launch_app_by_name(app_name):
    speak(f"Trying to launch {app_name}")
    
    # Try common paths
    common_paths = [
        f"C:\\Program Files\\{app_name}\\{app_name}.exe",
        f"C:\\Program Files (x86)\\{app_name}\\{app_name}.exe",
        f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\{app_name}\\{app_name}.exe",
        f"C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\{app_name}\\{app_name}.exe"
    ]
    
    for path in common_paths:
        if os.path.exists(path):
            os.startfile(path)
            speak(f"{app_name} launched successfully!")
            return
    
    # Try searching
    search_paths = [
        f"C:\\Program Files\\**\\{app_name}*.exe",
        f"C:\\Program Files (x86)\\**\\{app_name}*.exe",
        f"C:\\Users\\{os.getlogin()}\\AppData\\**\\{app_name}*.exe"
    ]
    
    for search_path in search_paths:
        try:
            matches = glob.glob(search_path, recursive=True)
            if matches:
                os.startfile(matches[0])
                speak(f"{app_name} launched successfully!")
                return
        except:
            continue
    
    # Try 'where' command
    try:
        result = subprocess.run(["where", app_name], capture_output=True, text=True)
        if result.returncode == 0:
            subprocess.Popen([result.stdout.strip()])
            speak(f"{app_name} launched successfully!")
            return
    except:
        pass
    
    speak(f"Could not find {app_name}")

def who_created_me():
    speak("I was created by Muhammad Farhan. He is an amazing programmer who built me to help people with their daily tasks using voice commands!")

def show_help():
    speak("I am ILLI, your personal assistant. I can help you with:")
    speak("Open YouTube and play videos")
    speak("Launch WhatsApp and other applications")
    speak("Search Wikipedia for information")
    speak("Tell you the current time")
    speak("Take screenshots")
    speak("Control system functions")
    speak("And much more!")

if __name__ == "__main__":
    wishMe()
    
    while True:
        query = takeCommand()
        
        if not query or query == "none":
            continue
            
        print(f"Processing: {query}")
        
        # Introduction commands
        if 'who created you' in query or 'who made you' in query or 'who built you' in query:
            who_created_me()
            continue
        
        if 'who are you' in query or 'your name' in query:
            speak("I am ILLI, your personal voice assistant. I was created by Muhammad Farhan to help you with your daily tasks.")
            continue
        
        # YouTube commands
        if 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("youtube.com")
            continue
            
        if 'play' in query:
            search_and_play_youtube(query)
            continue
        
        # App commands
        if 'open whatsapp' in query or 'launch whatsapp' in query:
            launch_whatsapp()
            continue
            
        if 'open' in query:
            app_name = query.replace('open', '').strip()
            if app_name:
                launch_app_by_name(app_name)
                continue
        
        # Information commands
        if 'what is' in query:
            topic = query.replace('what is', '').strip()
            if topic:
                speak(f"Searching Wikipedia for {topic}")
                try:
                    results = wikipedia.summary(topic, sentences=2)
                    speak(f"According to Wikipedia, {results}")
                except:
                    speak(f"Could not find information about {topic}")
                continue
                
        if 'time' in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {current_time}")
            continue
            
        if 'help' in query:
            show_help()
            continue
        
        # System commands
        if 'shutdown' in query:
            speak("Are you sure you want to shutdown your computer?")
            response = takeCommand()
            if 'yes' in response or 'sure' in response:
                speak("Shutting down computer in 10 seconds")
                time.sleep(10)
                os.system("shutdown /s /t 1")
            else:
                speak("Shutdown cancelled")
            continue
            
        if 'restart' in query:
            speak("Are you sure you want to restart your computer?")
            response = takeCommand()
            if 'yes' in response or 'sure' in response:
                speak("Restarting computer in 10 seconds")
                time.sleep(10)
                os.system("shutdown /r /t 1")
            else:
                speak("Restart cancelled")
            continue
        
        # Fallback
        speak("I didn't understand that command. Say 'help' to see what I can do.")
        print(f"Unrecognized command: {query}")
