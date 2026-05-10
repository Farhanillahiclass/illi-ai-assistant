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
import winreg
import psutil
import shutil
import smtplib
import json
import hashlib
import base64
import webbrowser
from pathlib import Path
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import win32gui
import win32con
import win32process
import win32api
import random

# Initialize text-to-speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    print(f"ILLI: {text}")
    engine.say(text)
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
    speak("I am ILLI, your working virtual assistant created by Muhammad Farhan. I can help you with everything!")

def takeCommand():
    """Working voice recognition"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # Working settings
        r.pause_threshold = 1.0
        r.energy_threshold = 300
        r.dynamic_energy_threshold = False
        r.adjust_for_ambient_noise(source, duration=2)
        
        try:
            audio = r.listen(source, timeout=15, phrase_time_limit=8)
        except sr.WaitTimeoutError:
            print("Listening timeout...")
            return "none"
        except Exception as e:
            print(f"Listen error: {e}")
            return "none"
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        
        if not query or len(query.strip()) == 0:
            query = r.recognize_google(audio)
        
        if query and len(query.strip()) > 0:
            print(f"You said: {query}")
            return query.lower()
        else:
            return "none"
            
    except sr.UnknownValueError:
        print("Could not understand")
        return "none"
    except sr.RequestError as e:
        print(f"Request error: {e}")
        return "none"
    except Exception as e:
        print(f"Error: {e}")
        return "none"

# ==================== APP LAUNCHER ====================
def launch_whatsapp():
    """Launch WhatsApp"""
    speak("Opening WhatsApp")
    
    whatsapp_paths = [
        f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\WhatsApp\\WhatsApp.exe",
        f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\WhatsApp\\WhatsApp\\WhatsApp.exe",
        f"C:\\Users\\{os.getlogin()}\\Desktop\\WhatsApp.lnk"
    ]
    
    for path in whatsapp_paths:
        try:
            matches = glob.glob(path)
            if matches:
                os.startfile(matches[0])
                speak("WhatsApp launched successfully!")
                return True
        except:
            continue
    
    # Fallback to web
    webbrowser.open("https://web.whatsapp.com")
    return False

def launch_instagram():
    """Launch Instagram"""
    speak("Opening Instagram")
    
    instagram_paths = [
        f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Instagram\\Instagram.exe",
        f"C:\\Users\\{os.getlogin()}\\Desktop\\Instagram.lnk"
    ]
    
    for path in instagram_paths:
        try:
            matches = glob.glob(path)
            if matches:
                os.startfile(matches[0])
                speak("Instagram launched successfully!")
                return True
        except:
            continue
    
    # Fallback to web
    webbrowser.open("https://www.instagram.com")
    return False

def launch_chrome():
    """Launch Chrome"""
    speak("Opening Chrome")
    
    chrome_paths = [
        f"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
        f"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    ]
    
    for path in chrome_paths:
        if os.path.exists(path):
            os.startfile(path)
            speak("Chrome launched successfully!")
            return True
    
    speak("Chrome not found")
    return False

def launch_vscode():
    """Launch VS Code"""
    speak("Opening VS Code")
    
    vscode_path = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    if os.path.exists(vscode_path):
        os.startfile(vscode_path)
        speak("VS Code launched successfully!")
        return True
    
    speak("VS Code not found")
    return False

# ==================== YOUTUBE MODULE ====================
def play_youtube_video(query):
    """Play YouTube video"""
    search_term = query.replace("play", "").strip()
    if not search_term:
        speak("Please tell me what to play")
        return False
    
    speak(f"Searching YouTube for {search_term}")
    search_url = f"https://www.youtube.com/results?search_query={search_term}"
    webbrowser.open(search_url)
    time.sleep(10)
    
    speak("Playing first video...")
    try:
        pyautogui.moveTo(400, 300, duration=1)
        pyautogui.click()
        time.sleep(3)
        pyautogui.press('space')
        speak(f"Playing {search_term}")
        return True
    except Exception as e:
        print(f"Auto-play error: {e}")
        speak("Please manually select first video")
        return False

def open_youtube():
    speak("Opening YouTube")
    webbrowser.open("https://www.youtube.com")

# ==================== EMAIL MODULE ====================
def send_email(recipient, subject, message):
    """Send email"""
    try:
        sender_email = "farhanhomeschooling519@gmail.com"
        sender_password = "dzpn aork haur hxtm"
        
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient, msg.as_string())
        server.quit()
        
        speak(f"Email sent successfully to {recipient}")
        return True
    except Exception as e:
        print(f"Email error: {e}")
        speak(f"Could not send email to {recipient}")
        return False

# ==================== WHATSAPP MESSAGING ====================
def send_whatsapp_message(contact_name, message):
    """Send WhatsApp message"""
    try:
        speak(f"Opening WhatsApp to send message to {contact_name}")
        
        # Launch WhatsApp
        launch_whatsapp()
        time.sleep(8)
        
        # Search for contact
        pyautogui.hotkey('ctrl', 'f')
        time.sleep(2)
        pyautogui.typewrite(contact_name)
        time.sleep(3)
        pyautogui.press('enter')
        time.sleep(3)
        
        # Type and send message
        pyautogui.typewrite(message)
        time.sleep(2)
        pyautogui.press('enter')
        
        speak(f"Message sent to {contact_name}")
        return True
        
    except Exception as e:
        print(f"WhatsApp error: {e}")
        speak(f"Could not send message to {contact_name}")
        return False

# ==================== UTILITY MODULES ====================
def get_time():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Current time is {strTime}")
    return True

def search_wikipedia(topic):
    speak(f"Searching Wikipedia for {topic}")
    try:
        results = wikipedia.summary(topic, sentences=2)
        speak(f"According to Wikipedia: {results}")
        return True
    except Exception as e:
        print(f"Wikipedia error: {e}")
        speak(f"Could not find information about {topic}")
        return False

def who_created_me():
    speak("I was created by Muhammad Farhan. He is an amazing programmer!")

def show_help():
    speak("I am ILLI, your working virtual assistant. I can help you with:")
    speak("Launch apps: WhatsApp, Instagram, Chrome, VS Code")
    speak("Send emails and WhatsApp messages")
    speak("Search and play YouTube videos")
    speak("Search Wikipedia for information")
    speak("Tell you current time")
    speak("System controls")
    speak("I was created by Muhammad Farhan")

def cleanup_project():
    """Clean up unnecessary project files"""
    try:
        speak("Cleaning up unnecessary project files...")
        
        project_path = "g:/Virtual Assistant"
        unnecessary_files = []
        
        # Define unnecessary file types
        file_types = {
            '.tmp': 'Temporary files',
            '.log': 'Log files',
            '.bak': 'Backup files',
            '.cache': 'Cache files',
            '.pyc': 'Python compiled files',
            '.pyo': 'Python optimized files',
            '__pycache__': 'Python cache directories',
            '.DS_Store': 'macOS system files',
            'Thumbs.db': 'Windows thumbnail cache'
        }
        
        # Find unnecessary files
        for root, dirs, files in os.walk(project_path):
            for file in files:
                file_path = os.path.join(root, file)
                file_ext = os.path.splitext(file)[1].lower()
                
                for ext, description in file_types.items():
                    if file.endswith(ext) or file == ext:
                        unnecessary_files.append({
                            'path': file_path,
                            'type': description,
                            'size': os.path.getsize(file_path)
                        })
                        break
            
            # Check for unnecessary directories
            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                if dir_name in file_types:
                    try:
                        total_size = 0
                        for root, dirs, files in os.walk(dir_path):
                            for file in files:
                                total_size += os.path.getsize(os.path.join(root, file))
                        
                        unnecessary_files.append({
                            'path': dir_path,
                            'type': file_types[dir_name],
                            'size': total_size
                        })
                    except:
                        pass
        
        if not unnecessary_files:
            speak("No unnecessary files found in project")
            return True
        
        # Delete files
        deleted_count = 0
        total_size = 0
        
        for file_info in unnecessary_files:
            try:
                if os.path.isfile(file_info['path']):
                    os.remove(file_info['path'])
                    deleted_count += 1
                    total_size += file_info['size']
                elif os.path.isdir(file_info['path']):
                    shutil.rmtree(file_info['path'])
                    deleted_count += 1
                    total_size += file_info['size']
            except Exception as e:
                print(f"Could not delete {file_info['path']}: {e}")
        
        size_mb = total_size / 1024 / 1024
        speak(f"Successfully deleted {deleted_count} unnecessary files")
        speak(f"Freed up {size_mb:.2f} MB of space")
        return True
        
    except Exception as e:
        print(f"Cleanup error: {e}")
        speak("Could not cleanup project files")
        return False

if __name__ == "__main__":
    wishMe()
    
    while True:
        query = takeCommand()
        
        if query == "none":
            continue
        
        print(f"Processing: {query}")
        
        # Introduction commands
        if 'who created you' in query or 'who made you' in query:
            who_created_me()
            continue
            
        if 'who are you' in query:
            speak("I am ILLI, your working virtual assistant created by Muhammad Farhan.")
            continue
        
        # App commands
        if 'open whatsapp' in query:
            launch_whatsapp()
            continue
            
        if 'open instagram' in query:
            launch_instagram()
            continue
            
        if 'open chrome' in query:
            launch_chrome()
            continue
            
        if 'open vs code' in query:
            launch_vscode()
            continue
        
        # YouTube commands
        if 'open youtube' in query:
            open_youtube()
            continue
            
        if 'play' in query:
            play_youtube_video(query)
            continue
        
        # WhatsApp commands
        if 'send message to' in query:
            try:
                parts = query.split("send message to")[1].strip()
                if " saying " in parts:
                    contact, message = parts.split(" saying ")
                    contact = contact.strip()
                    message = message.strip().strip('"\'')
                elif " message " in parts:
                    contact, message = parts.split(" message ")
                    contact = contact.strip()
                    message = message.strip().strip('"\'')
                else:
                    speak("Please specify message after contact name")
                    continue
                
                if contact and message:
                    send_whatsapp_message(contact, message)
                else:
                    speak("Please specify both contact and message")
            except:
                speak("Please specify recipient and message")
            continue
        
        # Email commands
        if 'send email to' in query:
            try:
                parts = query.split('send email to')[1].strip()
                if 'subject' in parts and 'message' in parts:
                    recipient = parts.split('subject')[0].strip()
                    subject_msg = parts.split('subject')[1].strip()
                    subject = subject_msg.split('message')[0].strip()
                    message = subject_msg.split('message')[1].strip()
                    send_email(recipient, subject, message)
                else:
                    speak("Please specify both subject and message")
            except:
                speak("Please specify recipient, subject, and message")
            continue
        
        # Cleanup command
        if 'cleanup' in query or 'clean' in query:
            cleanup_project()
            continue
        
        # Information commands
        if 'what is' in query:
            topic = query.replace('what is', '').strip()
            if topic:
                search_wikipedia(topic)
            continue
                
        if 'time' in query:
            get_time()
            continue
            
        if 'help' in query:
            show_help()
            continue
        
        # System commands
        if 'shutdown' in query:
            speak("Are you sure you want to shutdown your computer?")
            response = takeCommand()
            if 'yes' in response or 'sure' in response:
                speak("Shutting down computer in 5 seconds")
                time.sleep(5)
                os.system("shutdown /s /t 1")
            else:
                speak("Shutdown cancelled")
            continue
            
        if 'restart' in query:
            speak("Are you sure you want to restart your computer?")
            response = takeCommand()
            if 'yes' in response or 'sure' in response:
                speak("Restarting computer in 5 seconds")
                time.sleep(5)
                os.system("shutdown /r /t 1")
            else:
                speak("Restart cancelled")
            continue
            
        if 'sleep' in query:
            speak("Putting computer to sleep")
            os.system("rundll32.exe powrprof.dll,SetSuspendState Sleep")
            continue
        
        # Exit commands
        if 'goodbye' in query or 'bye' in query or 'exit' in query:
            speak("Goodbye Muhammad Farhan! Have a great day!")
            break
        
        # Fallback
        speak("I didn't understand that command. Say 'help' to see what I can do.")
        print(f"Unrecognized command: {query}")
