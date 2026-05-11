import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import os
import webbrowser
import psutil
import threading
import time
import speech_recognition as sr
import pyttsx3
from datetime import datetime

class ILLI_AI:
    def __init__(self, root):
        self.root = root
        self.root.title("ILLI AI - Working Version")
        self.root.geometry("1200x800")
        self.root.configure(bg='#000000')
        
        # Initialize voice
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.listening = False
        
        # App paths
        self.apps = {
            'whatsapp': 'https://web.whatsapp.com',
            'chrome': 'https://google.com',
            'youtube': 'https://youtube.com',
            'files': 'explorer.exe',
            'notepad': 'notepad.exe',
            'calculator': 'calc.exe',
            'cmd': 'cmd.exe',
            'powershell': 'powershell.exe',
            'gmail': 'https://gmail.com',
            'chatgpt': 'https://chat.openai.com',
            'spotify': 'https://open.spotify.com',
            'discord': 'https://discord.com',
            'linkedin': 'https://linkedin.com',
            'github': 'https://github.com',
            'facebook': 'https://facebook.com',
            'twitter': 'https://twitter.com'
        }
        
        self.setup_ui()
        threading.Thread(target=self.voice_loop, daemon=True).start()
    
    def setup_ui(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg='#000000')
        main_frame.pack(fill='both', expand=True)
        
        # Title
        tk.Label(main_frame, text="ILLI AI - WORKING VERSION", 
               font=('Arial', 20, 'bold'), fg='#00FFFF', bg='#000000').pack(pady=10)
        
        # Display area
        self.display = scrolledtext.ScrolledText(main_frame, height=15, width=80,
                                               bg='#0a0a0a', fg='white', font=('Consolas', 10))
        self.display.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Control frame
        control_frame = tk.Frame(main_frame, bg='#000000')
        control_frame.pack(fill='x', padx=10, pady=5)
        
        # Voice button
        self.voice_btn = tk.Button(control_frame, text="Start Voice", 
                              command=self.toggle_voice,
                              bg='#00FF00', fg='black', font=('Arial', 12, 'bold'))
        self.voice_btn.pack(side='left', padx=5)
        
        # App buttons
        apps = ['whatsapp', 'chrome', 'youtube', 'files', 'notepad', 'calculator', 'cmd', 'powershell', 'gmail', 'chatgpt', 'spotify', 'discord', 'linkedin', 'github', 'facebook', 'twitter']
        for app in apps:
            btn = tk.Button(control_frame, text=app.title(), 
                         command=lambda a=app: self.launch_app(a),
                         bg='#0080FF', fg='white', font=('Arial', 10))
            btn.pack(side='left', padx=2)
        
        # Status
        self.status_label = tk.Label(main_frame, text="Status: Ready", 
                                 font=('Arial', 12), fg='#00FF00', bg='#000000')
        self.status_label.pack(pady=5)
    
    def toggle_voice(self):
        self.listening = not self.listening
        if self.listening:
            self.voice_btn.config(text="Stop Voice", bg='#FF0000')
            self.add_message("Voice recognition started")
            self.speak("Voice recognition activated")
        else:
            self.voice_btn.config(text="Start Voice", bg='#00FF00')
            self.add_message("Voice recognition stopped")
    
    def voice_loop(self):
        try:
            self.speak("Hello! I am ILLI AI. How can I help you?")
        except:
            pass
        
        while True:
            try:
                if self.listening:
                    with sr.Microphone() as source:
                        self.recognizer.adjust_for_ambient_noise(source, duration=1)
                        audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)
                    
                    try:
                        command = self.recognizer.recognize_google(audio).lower()
                        self.add_message(f"You: {command}")
                        self.process_command(command)
                    except sr.UnknownValueError:
                        pass
                    except:
                        pass
                else:
                    time.sleep(1)
            except:
                time.sleep(2)
    
    def process_command(self, command):
        # App commands
        for app in self.apps:
            if app in command:
                self.launch_app(app)
                return
        
        # Other commands
        if 'hello' in command or 'hi' in command:
            response = "Hello! How can I help you?"
        elif 'time' in command:
            response = f"Current time is {datetime.now().strftime('%I:%M %p')}"
        elif 'date' in command:
            response = f"Today is {datetime.now().strftime('%A, %B %d, %Y')}"
        elif 'help' in command:
            response = "I can open apps, tell time and date, and help you with tasks!"
        elif 'system' in command:
            if 'scan' in command:
                response = self.system_scan()
            else:
                response = "System commands: system scan"
        elif 'close' in command:
            response = "Use the X button to close applications"
        else:
            response = f"I heard: {command}"
        
        self.speak(response)
        self.add_message(f"ILLI: {response}")
    
    def system_scan(self):
        try:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            scan_results = f"""
System Scan Results:
CPU Usage: {cpu_usage:.1f}%
Memory Usage: {memory.percent:.1f}%
Disk Usage: {disk.percent:.1f}%
Available Memory: {memory.available / (1024**3):.1f} GB
Free Disk Space: {disk.free / (1024**3):.1f} GB
Running Processes: {len(list(psutil.process_iter()))}
"""
            return scan_results
        except Exception as e:
            return f"System scan error: {str(e)}"
    
    def launch_app(self, app_name):
        try:
            path = self.apps[app_name]
            if path.startswith('http'):
                webbrowser.open(path)
            else:
                os.startfile(path)
            self.add_message(f"Opened {app_name}")
            self.speak(f"Opened {app_name}")
        except Exception as e:
            self.add_message(f"Error opening {app_name}: {e}")
    
    def speak(self, text):
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except:
            pass
    
    def add_message(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.display.insert(tk.END, f"[{timestamp}] {message}\n")
        self.display.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ILLI_AI(root)
    root.mainloop()
