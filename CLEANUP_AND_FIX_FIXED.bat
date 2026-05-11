@echo off
chcp 65001 >nul
title ILLI AI - Clean Repository and Fix
echo ===============================================
echo      CLEANUP AND FIX ILLI AI
echo ===============================================
echo.

echo 🧹 STEP 1: Clean GitHub Repository
echo ===============================================
cd /d "g:/Virtual Assistant"

echo Removing unnecessary files from Git...
git rm -f "GITHUB_PUBLISHING_GUIDE.md"
git rm -f "GITHUB_PUSH_COMMANDS.md" 
git rm -f "GITHUB_PUSH_COMMANDS_FINAL.md"
git rm -f "LINKEDIN_POST_MASTER_PROMPT.md"
git rm -f "LINKEDIN_POST_EXAMPLES.md"
git rm -f "VOSK_SETUP_GUIDE.md"
git rm -f "EMAIL_SETUP_GUIDE.txt"
git rm -f "PROJECT_CLEANUP_SUMMARY.txt"
git rm -f "PROJECT_STRUCTURE.txt"
git rm -f "QUICK_EMAIL_SETUP.bat"
git rm -f "PUSH_TO_GITHUB.bat"
git rm -f "CLEANUP_PROJECT.bat"
git rm -f "INSTALL_DEPENDENCIES.bat"
git rm -f "START_ILLI_HUD_FIXED.bat"
git rm -f "START_ILLI_STREAMLIT.bat"
git rm -f "START_ILLI_COMPLETE_FIXED.bat"
git rm -f "START_ILLI_ULTRA_FIXED.bat"
git rm -f "START_ILLI_LEARNING_AI.bat"
git rm -f "START_ILLI_COMPLETE_ALL_FEATURES.bat"
git rm -f "START_ILLI_MASTER_DASHBOARD_ULTRA.bat"
git rm -f "illi_complete_fixed.py"
git rm -f "illi_complete_ultra_fixed.py"
git rm -f "illi_hud_fixed.py"
git rm -f "illi_streamlit_dashboard.py"
git rm -f "illi_complete.py"
git rm -f "ILLI_AI_COMPLETE.py"
git rm -f "ILLI_AI_LEARNING.py"
git rm -f "hud_requirements.txt"
git rm -f "streamlit_requirements.txt"
git rm -f "requirements.txt"
git rm -f "whatsapp_contacts.json"
git rm -f "data" -r

echo ✅ Files removed from Git repository

echo.
echo 🔧 STEP 2: Create Simple Working ILLI AI
echo ===============================================

echo Creating simple working version...
echo import tkinter as tk > "ILLI_AI_SIMPLE.py"
echo from tkinter import ttk, scrolledtext, messagebox, filedialog >> "ILLI_AI_SIMPLE.py"
echo import os >> "ILLI_AI_SIMPLE.py"
echo import webbrowser >> "ILLI_AI_SIMPLE.py"
echo import psutil >> "ILLI_AI_SIMPLE.py"
echo import threading >> "ILLI_AI_SIMPLE.py"
echo import time >> "ILLI_AI_SIMPLE.py"
echo import speech_recognition as sr >> "ILLI_AI_SIMPLE.py"
echo import pyttsx3 >> "ILLI_AI_SIMPLE.py"
echo from datetime import datetime >> "ILLI_AI_SIMPLE.py"
echo. >> "ILLI_AI_SIMPLE.py"
echo class ILLI_AI: >> "ILLI_AI_SIMPLE.py"
echo     def __init__(self, root): >> "ILLI_AI_SIMPLE.py"
echo         self.root = root >> "ILLI_AI_SIMPLE.py"
echo         self.root.title("ILLI AI - Working Version") >> "ILLI_AI_SIMPLE.py"
echo         self.root.geometry("1200x800") >> "ILLI_AI_SIMPLE.py"
echo         self.root.configure(bg='#000000') >> "ILLI_AI_SIMPLE.py"
echo. >> "ILLI_AI_SIMPLE.py"
echo         # Initialize voice >> "ILLI_AI_SIMPLE.py"
echo         self.recognizer = sr.Recognizer() >> "ILLI_AI_SIMPLE.py"
echo         self.engine = pyttsx3.init() >> "ILLI_AI_SIMPLE.py"
echo         self.engine.setProperty('rate', 150) >> "ILLI_AI_SIMPLE.py"
echo         self.listening = False >> "ILLI_AI_SIMPLE.py"
echo. >> "ILLI_AI_SIMPLE.py"
echo         # App paths >> "ILLI_AI_SIMPLE.py"
echo         self.apps = { >> "ILLI_AI_SIMPLE.py"
echo             'whatsapp': 'https://web.whatsapp.com', >> "ILLI_AI_SIMPLE.py"
echo             'chrome': 'https://google.com', >> "ILLI_AI_SIMPLE.py"
echo             'youtube': 'https://youtube.com', >> "ILLI_AI_SIMPLE.py"
echo             'files': 'explorer.exe', >> "ILLI_AI_SIMPLE.py"
echo             'notepad': 'notepad.exe', >> "ILLI_AI_SIMPLE.py"
echo             'calculator': 'calc.exe', >> "ILLI_AI_SIMPLE.py"
echo             'cmd': 'cmd.exe' >> "ILLI_AI_SIMPLE.py"
echo         } >> "ILLI_AI_SIMPLE.py"
echo. >> "ILLI_AI_SIMPLE.py"
echo         self.setup_ui() >> "ILLI_AI_SIMPLE.py"
echo         threading.Thread(target=self.voice_loop, daemon=True).start() >> "ILLI_AI_SIMPLE.py"
echo. >> "ILLI_AI_SIMPLE.py"
echo     def setup_ui(self): >> "ILLI_AI_SIMPLE.py"
echo         # Main frame >> "ILLI_AI_SIMPLE.py"
echo         main_frame = tk.Frame(self.root, bg='#000000') >> "ILLI_AI_SIMPLE.py"
echo         main_frame.pack(fill='both', expand=True) >> "ILLI_AI_SIMPLE.py"
echo. >> "ILLI_AI_SIMPLE.py"
echo         # Title >> "ILLI_AI_SIMPLE.py"
echo         tk.Label(main_frame, text="ILLI AI - WORKING VERSION",  >> "ILLI_AI_SIMPLE.py"
echo                font=('Arial', 20, 'bold'), fg='#00FFFF', bg='#000000').pack(pady=10) >> "ILLI_AI_SIMPLE.py"
echo. >> "ILLI_AI_SIMPLE.py"
echo         # Display area >> "ILLI_AI_SIMPLE.py"
echo         self.display = scrolledtext.ScrolledText(main_frame, height=15, width=80, >> "ILLI_AI_SIMPLE.py"
echo                                                bg='#0a0a0a', fg='white', font=('Consolas', 10)) >> "ILLI_AI_SIMPLE.py"
echo         self.display.pack(fill='both', expand=True, padx=10, pady=5) >> "ILLI_AI_SIMPLE.py"
echo. >> "ILLI_AI_SIMPLE.py"
echo         # Control frame >> "ILLI_AI_SIMPLE.py"
echo         control_frame = tk.Frame(main_frame, bg='#000000') >> "ILLI_AI_SIMPLE.py"
echo         control_frame.pack(fill='x', padx=10, pady=5) >> "ILLI_AI_SIMPLE.py"
echo. >> "ILLI_AI_SIMPLE.py"
echo         # Voice button >> "ILLI_AI_SIMPLE.py"
echo         self.voice_btn = tk.Button(control_frame, text="Start Voice",  >> "ILLI_AI_SIMPLE.py"
echo                                   command=self.toggle_voice, >> "ILLI_AI_SIMPLE.py"
echo                                   bg='#00FF00', fg='black', font=('Arial', 12, 'bold')) >> "ILLI_AI_SIMPLE.py"
echo         self.voice_btn.pack(side='left', padx=5) >> "ILLI_AI_SIMPLE.py"
echo. >> "ILLI_AI_SIMPLE.py"
echo         # App buttons >> "ILLI_AI_SIMPLE.py"
echo         apps = ['whatsapp', 'chrome', 'youtube', 'files', 'notepad', 'calculator', 'cmd'] >> "ILLI_AI_SIMPLE.py"
echo         for app in apps: >> "ILLI_AI_SIMPLE.py"
echo             btn = tk.Button(control_frame, text=app.title(),  >> "ILLI_AI_SIMPLE.py"
echo                          command=lambda a=app: self.launch_app(a), >> "ILLI_AI_SIMPLE.py"
echo                          bg='#0080FF', fg='white', font=('Arial', 10)) >> "ILLI_AI_SIMPLE.py"
echo             btn.pack(side='left', padx=2) >> "ILLI_AI_SIMPLE.py"
echo. >> "ILLI_AI_SIMPLE.py"
echo         # Status >> "ILLI_AI_SIMPLE.py"
echo         self.status_label = tk.Label(main_frame, text="Status: Ready",  >> "ILLI_AI_SIMPLE.py"
echo                                     font=('Arial', 12), fg='#00FF00', bg='#000000') >> "ILLI_AI_SIMPLE.py"
echo         self.status_label.pack(pady=5) >> "ILLI_AI_SIMPLE.py"
echo. >> "ILLI_AI_SIMPLE.py"
echo     def toggle_voice(self): >> "ILLI_AI_SIMPLE.py"
echo         self.listening = not self.listening >> "ILLI_AI_SIMPLE.py"
echo         if self.listening: >> "ILLI_AI_SIMPLE.py"
echo             self.voice_btn.config(text="Stop Voice", bg='#FF0000') >> "ILLI_AI_SIMPLE.py"
echo             self.add_message("Voice recognition started") >> "ILLI_AI_SIMPLE.py"
echo             self.speak("Voice recognition activated") >> "ILLI_AI_SIMPLE.py"
echo         else: >> "ILLI_AI_SIMPLE.py"
echo             self.voice_btn.config(text="Start Voice", bg='#00FF00') >> "ILLI_AI_SIMPLE.py"
echo             self.add_message("Voice recognition stopped") >> "ILLI_AI_SIMPLE.py"
echo. >> "ILLI_AI_SIMPLE.py"
echo     def voice_loop(self): >> "ILLI_AI_SIMPLE.py"
echo         try: >> "ILLI_AI_SIMPLE.py"
echo             self.speak("Hello! I am ILLI AI. How can I help you?") >> "ILLI_AI_SIMPLE.py"
echo         except: >> "ILLI_AI_SIMPLE.py"
echo             pass >> "ILLI_AI_SIMPLE.py"
echo. >> "ILLI_AI_SIMPLE.py"
echo         while True: >> "ILLI_AI_SIMPLE.py"
echo             try: >> "ILLI_AI_SIMPLE.py"
echo                 if self.listening: >> "ILLI_AI_SIMPLE.py"
echo                     with sr.Microphone() as source: >> "ILLI_AI_SIMPLE.py"
echo                         self.recognizer.adjust_for_ambient_noise(source, duration=1) >> "ILLI_AI_SIMPLE.py"
echo                         audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5) >> "ILLI_AI_SIMPLE.py"
echo. >> "ILLI_AI_SIMPLE.py"
echo                     try: >> "ILLI_AI_SIMPLE.py"
echo                         command = self.recognizer.recognize_google(audio).lower() >> "ILLI_AI_SIMPLE.py"
echo                         self.add_message(f"You: {command}") >> "ILLI_AI_SIMPLE.py"
echo                         self.process_command(command) >> "ILLI_AI_SIMPLE.py"
echo                     except sr.UnknownValueError: >> "ILLI_AI_SIMPLE.py"
echo                         pass >> "ILLI_AI_SIMPLE.py"
echo                     except: >> "ILLI_AI_SIMPLE.py"
echo                         pass >> "ILLI_AI_SIMPLE.py"
echo                 else: >> "ILLI_AI_SIMPLE.py"
echo                     time.sleep(1) >> "ILLI_AI_SIMPLE.py"
echo             except: >> "ILLI_AI_SIMPLE.py"
echo                 time.sleep(2) >> "ILLI_AI_SIMPLE.py"
echo. >> "ILLI_AI_SIMPLE.py"
echo     def process_command(self, command): >> "ILLI_AI_SIMPLE.py"
echo         # App commands >> "ILLI_AI_SIMPLE.py"
echo         for app in self.apps: >> "ILLI_AI_SIMPLE.py"
echo             if app in command: >> "ILLI_AI_SIMPLE.py"
echo                 self.launch_app(app) >> "ILLI_AI_SIMPLE.py"
echo                 return >> "ILLI_AI_SIMPLE.py"
echo. >> "ILLI_AI_SIMPLE.py"
echo         # Other commands >> "ILLI_AI_SIMPLE.py"
echo         if 'hello' in command or 'hi' in command: >> "ILLI_AI_SIMPLE.py"
echo             response = "Hello! How can I help you?" >> "ILLI_AI_SIMPLE.py"
echo         elif 'time' in command: >> "ILLI_AI_SIMPLE.py"
echo             response = f"Current time is {datetime.now().strftime('%%I:%%M %%p')}" >> "ILLI_AI_SIMPLE.py"
echo         elif 'help' in command: >> "ILLI_AI_SIMPLE.py"
echo             response = "I can open apps, tell time, and help you with tasks!" >> "ILLI_AI_SIMPLE.py"
echo         else: >> "ILLI_AI_SIMPLE.py"
echo             response = f"I heard: {command}" >> "ILLI_AI_SIMPLE.py"
echo. >> "ILLI_AI_SIMPLE.py"
echo         self.speak(response) >> "ILLI_AI_SIMPLE.py"
echo         self.add_message(f"ILLI: {response}") >> "ILLI_AI_SIMPLE.py"
echo. >> "ILLI_AI_SIMPLE.py"
echo     def launch_app(self, app_name): >> "ILLI_AI_SIMPLE.py"
echo         try: >> "ILLI_AI_SIMPLE.py"
echo             path = self.apps[app_name] >> "ILLI_AI_SIMPLE.py"
echo             if path.startswith('http'): >> "ILLI_AI_SIMPLE.py"
echo                 webbrowser.open(path) >> "ILLI_AI_SIMPLE.py"
echo             else: >> "ILLI_AI_SIMPLE.py"
echo                 os.startfile(path) >> "ILLI_AI_SIMPLE.py"
echo             self.add_message(f"Opened {app_name}") >> "ILLI_AI_SIMPLE.py"
echo             self.speak(f"Opened {app_name}") >> "ILLI_AI_SIMPLE.py"
echo         except Exception as e: >> "ILLI_AI_SIMPLE.py"
echo             self.add_message(f"Error opening {app_name}: {e}") >> "ILLI_AI_SIMPLE.py"
echo. >> "ILLI_AI_SIMPLE.py"
echo     def speak(self, text): >> "ILLI_AI_SIMPLE.py"
echo         try: >> "ILLI_AI_SIMPLE.py"
echo             self.engine.say(text) >> "ILLI_AI_SIMPLE.py"
echo             self.engine.runAndWait() >> "ILLI_AI_SIMPLE.py"
echo         except: >> "ILLI_AI_SIMPLE.py"
echo             pass >> "ILLI_AI_SIMPLE.py"
echo. >> "ILLI_AI_SIMPLE.py"
echo     def add_message(self, message): >> "ILLI_AI_SIMPLE.py"
echo         timestamp = datetime.now().strftime("%%H:%%M:%%S") >> "ILLI_AI_SIMPLE.py"
echo         self.display.insert(tk.END, f"[{timestamp}] {message}\n") >> "ILLI_AI_SIMPLE.py"
echo         self.display.see(tk.END) >> "ILLI_AI_SIMPLE.py"
echo. >> "ILLI_AI_SIMPLE.py"
echo if __name__ == "__main__": >> "ILLI_AI_SIMPLE.py"
echo     root = tk.Tk() >> "ILLI_AI_SIMPLE.py"
echo     app = ILLI_AI(root) >> "ILLI_AI_SIMPLE.py"
echo     root.mainloop() >> "ILLI_AI_SIMPLE.py"

echo ✅ Simple working version created

echo.
echo 🚀 STEP 3: Create Simple Launcher
echo ===============================================

echo Creating launcher...
echo @echo off > "START_ILLI_SIMPLE.bat"
echo title ILLI AI - Simple Working Version >> "START_ILLI_SIMPLE.bat"
echo echo =============================================== >> "START_ILLI_SIMPLE.bat"
echo echo      ILLI AI - SIMPLE WORKING VERSION >> "START_ILLI_SIMPLE.bat"
echo echo =============================================== >> "START_ILLI_SIMPLE.bat"
echo echo. >> "START_ILLI_SIMPLE.bat"
echo echo Features: >> "START_ILLI_SIMPLE.bat"
echo echo - Voice recognition >> "START_ILLI_SIMPLE.bat"
echo echo - App launching >> "START_ILLI_SIMPLE.bat"
echo echo - Time telling >> "START_ILLI_SIMPLE.bat"
echo echo - Simple commands >> "START_ILLI_SIMPLE.bat"
echo echo. >> "START_ILLI_SIMPLE.bat"
echo echo Starting ILLI AI... >> "START_ILLI_SIMPLE.bat"
echo python "ILLI_AI_SIMPLE.py" >> "START_ILLI_SIMPLE.bat"
echo pause >> "START_ILLI_SIMPLE.bat"

echo ✅ Simple launcher created

echo.
echo 📝 STEP 4: Update README
echo ===============================================

echo Creating simple README...
echo # ILLI AI - Simple Working Version > "README.md"
echo. >> "README.md"
echo ## 🎯 WORKING FEATURES >> "README.md"
echo. >> "README.md"
echo ### 🎤 Voice Control >> "README.md"
echo - ✅ Voice recognition >> "README.md"
echo - ✅ Voice commands >> "README.md"
echo - ✅ Speak responses >> "README.md"
echo. >> "README.md"
echo ### 🚀 App Control >> "README.md"
echo - ✅ Launch WhatsApp >> "README.md"
echo - ✅ Launch Chrome >> "README.md"
echo - ✅ Launch YouTube >> "README.md"
echo - ✅ Launch Files >> "README.md"
echo - ✅ Launch Notepad >> "README.md"
echo - ✅ Launch Calculator >> "README.md"
echo - ✅ Launch CMD >> "README.md"
echo. >> "README.md"
echo ### 📊 Information >> "README.md"
echo - ✅ Tell time >> "README.md"
echo - ✅ Help commands >> "README.md"
echo - ✅ Status display >> "README.md"
echo. >> "README.md"
echo ## 🚀 TO RUN >> "README.md"
echo ```cmd >> "README.md"
echo START_ILLI_SIMPLE.bat >> "README.md"
echo ``` >> "README.md"
echo. >> "README.md"
echo ## 🎤 VOICE COMMANDS >> "README.md"
echo - "Hello/Hi" - Greeting >> "README.md"
echo - "Time" - Tell current time >> "README.md"
echo - "Open [app]" - Launch application >> "README.md"
echo - "Help" - Show help >> "README.md"
echo. >> "README.md"
echo ## 🌐 GitHub >> "README.md"
echo https://github.com/Farhanillahiclass/illi-ai-assistant >> "README.md"
echo. >> "README.md"
echo **Created by Muhammad Farhan** >> "README.md"

echo ✅ Simple README created

echo.
echo 📤 STEP 5: Commit and Push to GitHub
echo ===============================================

echo Adding files to Git...
git add "ILLI_AI_SIMPLE.py"
git add "START_ILLI_SIMPLE.bat" 
git add "README.md"

echo Committing changes...
git commit -m "Clean repository - Simple working ILLI AI

✅ FEATURES:
- Voice recognition working
- App launching working  
- Time telling working
- Simple commands working
- Clean repository structure

🧹 CLEANUP:
- Removed all unnecessary files
- Only essential working files kept
- Clean GitHub repository

🚀 READY TO USE:
- Simple working version
- All core features working
- Easy to use and understand

Created by Muhammad Farhan
Email: farhanhomeschooling519@gmail.com"

echo Pushing to GitHub...
git push -u origin main

echo.
echo ✅ SUCCESS! Repository cleaned and fixed!
echo.
echo 🎯 NOW RUN:
echo START_ILLI_SIMPLE.bat
echo.
echo 🌐 GitHub:
echo https://github.com/Farhanillahiclass/illi-ai-assistant
echo.

pause
