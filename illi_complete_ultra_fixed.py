import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import os
import subprocess
import time
import webbrowser
import psutil
import threading
import queue
import math
import random
import json
import hashlib
import base64
from datetime import datetime
import pyautogui
import glob
import win32gui
import win32con
import win32process
import speech_recognition as sr
import pyttsx3
import wikipedia
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
import shutil
import ctypes
import platform

class ILLICompleteUltraFixed:
    def __init__(self, root):
        self.root = root
        self.root.title("ILLI AI - COMPLETE ULTRA FIXED")
        self.root.geometry("1920x1080")
        self.root.configure(bg='#000000')
        
        # System variables
        self.system_status = "ONLINE"
        self.user_name = os.getlogin()
        self.current_task = "Voice Assistant Active"
        self.listening_state = False
        self.response_queue = queue.Queue()
        
        # Voice recognition - Ultra optimized settings
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 140)
        self.engine.setProperty('volume', 0.9)
        
        # WhatsApp contacts memory
        self.whatsapp_contacts = []
        self.contact_memory_file = "g:/Virtual Assistant/data/whatsapp_contacts.json"
        self.load_whatsapp_contacts()
        
        # YouTube control
        self.youtube_current_video = None
        self.youtube_playlist = []
        
        # System control
        self.system_processes = []
        self.system_files = []
        
        # Color scheme - Professional
        self.colors = {
            'bg': '#000000',
            'glass': '#0a0a0a',
            'glass_border': '#1a1a1a',
            'accent': '#00FFFF',
            'magenta': '#FF00FF',
            'red': '#FF0000',
            'green': '#00FF00',
            'yellow': '#FFFF00',
            'blue': '#0080FF',
            'purple': '#8000FF',
            'orange': '#FF8000',
            'text': '#FFFFFF',
            'text_dim': '#666666',
            'success': '#00FF00',
            'warning': '#FFAA00',
            'error': '#FF0000',
            'cyan': '#00FFFF'
        }
        
        # Ultra enhanced app paths with maximum detection
        self.app_paths = {
            'whatsapp': [
                "C:\\Users\\{user}\\AppData\\Local\\WhatsApp\\WhatsApp.exe",
                "C:\\Program Files\\WindowsApps\\*\\WhatsApp.exe",
                "C:\\Program Files\\WhatsApp\\WhatsApp.exe",
                "C:\\Users\\{user}\\AppData\\Local\\Programs\\WhatsApp\\WhatsApp.exe",
                "https://web.whatsapp.com"
            ],
            'instagram': [
                "C:\\Users\\{user}\\AppData\\Local\\Instagram\\Instagram.exe",
                "C:\\Program Files\\WindowsApps\\*\\Instagram.exe",
                "C:\\Users\\{user}\\AppData\\Local\\Programs\\Instagram\\Instagram.exe",
                "https://instagram.com"
            ],
            'chrome': [
                "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
                "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
                "C:\\Users\\{user}\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe",
                "https://google.com"
            ],
            'vscode': [
                "C:\\Users\\{user}\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
                "C:\\Program Files\\Microsoft VS Code\\Code.exe",
                "C:\\Program Files (x86)\\Microsoft VS Code\\Code.exe",
                "C:\\Users\\{user}\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
                "Code.exe",
                "https://code.visualstudio.com"
            ],
            'linkedin': [
                "https://linkedin.com",
                "https://www.linkedin.com"
            ],
            'github': [
                "https://github.com",
                "https://www.github.com"
            ],
            'canva': [
                "https://canva.com",
                "https://www.canva.com"
            ],
            'camera': [
                "microsoft.windows.camera:",
                "C:\\Windows\\System32\\WindowsCamera.exe",
                "start microsoft.windows.camera:",
                "explorer.exe shell:appsfolder\\Microsoft.WindowsCamera_8wekyb3d8bbwe!App"
            ],
            'blender': [
                "C:\\Program Files\\Blender Foundation\\Blender 3.*\\blender.exe",
                "C:\\Program Files (x86)\\Blender Foundation\\Blender 3.*\\blender.exe",
                "C:\\Users\\{user}\\AppData\\Local\\Programs\\Blender\\blender.exe",
                "blender.exe",
                "https://blender.org"
            ],
            'notepad': [
                "notepad.exe",
                "C:\\Windows\\System32\\notepad.exe"
            ],
            'calculator': [
                "calc.exe",
                "C:\\Windows\\System32\\calc.exe"
            ],
            'files': [
                "explorer.exe"
            ],
            'youtube': [
                "https://youtube.com",
                "https://www.youtube.com"
            ],
            'taskmanager': [
                "taskmgr.exe"
            ],
            'cmd': [
                "cmd.exe"
            ],
            'powershell': [
                "powershell.exe"
            ],
            'controlpanel': [
                "control.exe"
            ],
            'settings': [
                "ms-settings:"
            ],
            'gmail': [
                "https://gmail.com",
                "https://mail.google.com"
            ],
            'chatgpt': [
                "https://chat.openai.com",
                "https://chatgpt.com"
            ],
            'spotify': [
                "C:\\Users\\{user}\\AppData\\Roaming\\Spotify\\Spotify.exe",
                "https://open.spotify.com"
            ],
            'discord': [
                "C:\\Users\\{user}\\AppData\\Local\\Discord\\app-*\\Discord.exe",
                "https://discord.com"
            ],
            'slack': [
                "C:\\Users\\{user}\\AppData\\Local\\slack\\slack.exe",
                "https://slack.com"
            ],
            'teams': [
                "C:\\Users\\{user}\\AppData\\Local\\Microsoft\\Teams\\Teams.exe",
                "https://teams.microsoft.com"
            ],
            'zoom': [
                "C:\\Users\\{user}\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe",
                "https://zoom.us"
            ],
            'skype': [
                "C:\\Program Files\\Microsoft Office\\root\\Office16\\lync.exe",
                "https://web.skype.com"
            ],
            'telegram': [
                "C:\\Users\\{user}\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe",
                "https://web.telegram.org"
            ],
            'signal': [
                "C:\\Users\\{user}\\AppData\\Local\\Programs\\signal-desktop\\Signal.exe",
                "https://signal.org"
            ],
            'facebook': [
                "https://facebook.com",
                "https://www.facebook.com"
            ],
            'twitter': [
                "https://twitter.com",
                "https://www.twitter.com"
            ],
            'reddit': [
                "https://reddit.com",
                "https://www.reddit.com"
            ],
            'pinterest': [
                "https://pinterest.com",
                "https://www.pinterest.com"
            ],
            'tiktok': [
                "https://tiktok.com",
                "https://www.tiktok.com"
            ],
            'snapchat': [
                "https://snapchat.com",
                "https://www.snapchat.com"
            ]
        }
        
        # Create UI
        self.setup_ui()
        
        # Start voice assistant
        self.start_voice_assistant()
    
    def setup_ui(self):
        """Setup the main UI"""
        # Main container
        main_frame = tk.Frame(self.root, bg=self.colors['bg'])
        main_frame.pack(fill='both', expand=True)
        
        # Header
        self.create_header(main_frame)
        
        # Content area
        content_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        content_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Left panel - System monitoring
        self.create_system_panel(content_frame)
        
        # Center panel - Command history
        self.create_command_panel(content_frame)
        
        # Right panel - App controls
        self.create_app_panel(content_frame)
        
        # Bottom panel - Voice controls
        self.create_voice_panel(main_frame)
    
    def create_header(self, parent):
        """Create header section"""
        header_frame = tk.Frame(parent, bg=self.colors['glass'], relief='raised', bd=2)
        header_frame.pack(fill='x', padx=10, pady=5)
        
        # Title
        title_label = tk.Label(header_frame, text="🤖 ILLI AI - COMPLETE ULTRA FIXED", 
                              font=('Arial', 24, 'bold'), fg=self.colors['accent'], 
                              bg=self.colors['glass'])
        title_label.pack(side='left', padx=20, pady=10)
        
        # Status
        self.status_label = tk.Label(header_frame, text=f"Status: {self.system_status}", 
                                    font=('Arial', 14), fg=self.colors['success'], 
                                    bg=self.colors['glass'])
        self.status_label.pack(side='right', padx=20, pady=10)
        
        # User info
        user_label = tk.Label(header_frame, text=f"User: {self.user_name}", 
                              font=('Arial', 12), fg=self.colors['text'], 
                              bg=self.colors['glass'])
        user_label.pack(side='right', padx=20, pady=10)
    
    def create_system_panel(self, parent):
        """Create system monitoring panel"""
        panel_frame = tk.Frame(parent, bg=self.colors['glass'], relief='raised', bd=2)
        panel_frame.pack(side='left', fill='both', expand=True, padx=5, pady=5)
        
        # Title
        title_label = tk.Label(panel_frame, text="📊 SYSTEM MONITORING", 
                              font=('Arial', 16, 'bold'), fg=self.colors['accent'], 
                              bg=self.colors['glass'])
        title_label.pack(pady=10)
        
        # System info display
        self.system_display = scrolledtext.ScrolledText(panel_frame, height=15, width=40,
                                                      bg=self.colors['bg'], fg=self.colors['text'],
                                                      font=('Consolas', 10))
        self.system_display.pack(padx=10, pady=5, fill='both', expand=True)
        
        # Control buttons
        btn_frame = tk.Frame(panel_frame, bg=self.colors['glass'])
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="🔍 System Scan", command=self.system_scan,
                 bg=self.colors['blue'], fg='white', font=('Arial', 10, 'bold')).pack(side='left', padx=5)
        tk.Button(btn_frame, text="🧹 System Cleanup", command=self.system_cleanup,
                 bg=self.colors['orange'], fg='white', font=('Arial', 10, 'bold')).pack(side='left', padx=5)
        tk.Button(btn_frame, text="⚡ System Optimize", command=self.system_optimize,
                 bg=self.colors['green'], fg='white', font=('Arial', 10, 'bold')).pack(side='left', padx=5)
    
    def create_command_panel(self, parent):
        """Create command history panel"""
        panel_frame = tk.Frame(parent, bg=self.colors['glass'], relief='raised', bd=2)
        panel_frame.pack(side='left', fill='both', expand=True, padx=5, pady=5)
        
        # Title
        title_label = tk.Label(panel_frame, text="📝 COMMAND HISTORY", 
                              font=('Arial', 16, 'bold'), fg=self.colors['accent'], 
                              bg=self.colors['glass'])
        title_label.pack(pady=10)
        
        # Command history display
        self.command_display = scrolledtext.ScrolledText(panel_frame, height=15, width=50,
                                                        bg=self.colors['bg'], fg=self.colors['text'],
                                                        font=('Consolas', 10))
        self.command_display.pack(padx=10, pady=5, fill='both', expand=True)
        
        # Manual command input
        input_frame = tk.Frame(panel_frame, bg=self.colors['glass'])
        input_frame.pack(pady=10)
        
        tk.Label(input_frame, text="Manual Command:", fg=self.colors['text'], 
                bg=self.colors['glass']).pack(side='left', padx=5)
        
        self.manual_entry = tk.Entry(input_frame, width=30, bg=self.colors['bg'], 
                                    fg=self.colors['text'], font=('Consolas', 10))
        self.manual_entry.pack(side='left', padx=5)
        self.manual_entry.bind('<Return>', self.manual_command)
        
        tk.Button(input_frame, text="Execute", command=self.manual_command,
                 bg=self.colors['accent'], fg='black', font=('Arial', 10, 'bold')).pack(side='left', padx=5)
    
    def create_app_panel(self, parent):
        """Create app control panel"""
        panel_frame = tk.Frame(parent, bg=self.colors['glass'], relief='raised', bd=2)
        panel_frame.pack(side='left', fill='both', expand=True, padx=5, pady=5)
        
        # Title
        title_label = tk.Label(panel_frame, text="🚀 APP CONTROL", 
                              font=('Arial', 16, 'bold'), fg=self.colors['accent'], 
                              bg=self.colors['glass'])
        title_label.pack(pady=10)
        
        # App status display
        self.app_display = scrolledtext.ScrolledText(panel_frame, height=15, width=40,
                                                    bg=self.colors['bg'], fg=self.colors['text'],
                                                    font=('Consolas', 10))
        self.app_display.pack(padx=10, pady=5, fill='both', expand=True)
        
        # Quick app buttons
        btn_frame = tk.Frame(panel_frame, bg=self.colors['glass'])
        btn_frame.pack(pady=10)
        
        apps = [('WhatsApp', 'whatsapp'), ('Instagram', 'instagram'), 
                ('VS Code', 'vscode'), ('YouTube', 'youtube'),
                ('Chrome', 'chrome'), ('Files', 'files')]
        
        for i, (name, app_key) in enumerate(apps):
            row = i // 3
            col = i % 3
            btn_frame_row = btn_frame.winfo_children()[row] if row < len(btn_frame.winfo_children()) else tk.Frame(btn_frame, bg=self.colors['glass'])
            if row >= len(btn_frame.winfo_children()):
                btn_frame_row.pack(pady=2)
            
            tk.Button(btn_frame_row, text=name, 
                     command=lambda k=app_key: self.launch_app(k),
                     bg=self.colors['cyan'], fg='black', 
                     font=('Arial', 9, 'bold')).pack(side='left', padx=2)
    
    def create_voice_panel(self, parent):
        """Create voice control panel"""
        panel_frame = tk.Frame(parent, bg=self.colors['glass'], relief='raised', bd=2)
        panel_frame.pack(fill='x', padx=10, pady=5)
        
        # Voice status
        self.voice_status = tk.Label(panel_frame, text="🔴 Voice: IDLE", 
                                    font=('Arial', 14, 'bold'), fg=self.colors['red'], 
                                    bg=self.colors['glass'])
        self.voice_status.pack(side='left', padx=20, pady=10)
        
        # Voice controls
        voice_frame = tk.Frame(panel_frame, bg=self.colors['glass'])
        voice_frame.pack(side='left', padx=20, pady=10)
        
        self.voice_btn = tk.Button(voice_frame, text="🎤 Start Voice", 
                                   command=self.toggle_voice,
                                   bg=self.colors['green'], fg='white', 
                                   font=('Arial', 12, 'bold'))
        self.voice_btn.pack(side='left', padx=5)
        
        tk.Button(voice_frame, text="🔊 Test Voice", command=self.test_voice,
                 bg=self.colors['blue'], fg='white', 
                 font=('Arial', 12, 'bold')).pack(side='left', padx=5)
        
        # Current task
        self.task_label = tk.Label(panel_frame, text=f"Task: {self.current_task}", 
                                  font=('Arial', 12), fg=self.colors['text'], 
                                  bg=self.colors['glass'])
        self.task_label.pack(side='right', padx=20, pady=10)
    
    def toggle_voice(self):
        """Toggle voice recognition"""
        self.listening_state = not self.listening_state
        if self.listening_state:
            self.voice_btn.config(text="🔴 Stop Voice", bg=self.colors['red'])
            self.voice_status.config(text="🟢 Voice: LISTENING", fg=self.colors['green'])
            self.add_log_entry("Voice recognition activated")
        else:
            self.voice_btn.config(text="🎤 Start Voice", bg=self.colors['green'])
            self.voice_status.config(text="🔴 Voice: IDLE", fg=self.colors['red'])
            self.add_log_entry("Voice recognition deactivated")
    
    def test_voice(self):
        """Test voice system"""
        try:
            self.speak("Voice system working perfectly!")
            self.add_log_entry("Voice test successful")
        except Exception as e:
            self.add_log_entry(f"Voice test failed: {str(e)}", "error")
    
    def manual_command(self, event=None):
        """Process manual command"""
        command = self.manual_entry.get().strip().lower()
        if command:
            self.add_command_history(f"Manual: {command}")
            self.process_command(command)
            self.manual_entry.delete(0, tk.END)
    
    def start_voice_assistant(self):
        """Start voice assistant"""
        threading.Thread(target=self.voice_assistant_loop, daemon=True).start()
        threading.Thread(target=self.update_system_info, daemon=True).start()
    
    def voice_assistant_loop(self):
        """Ultra optimized voice assistant loop"""
        try:
            self.speak("Assalam o Alaikum Muhammad Farhan!")
            self.speak("Good Evening!")
            self.speak("I am ILLI Complete Ultra Fixed, your most advanced AI assistant!")
        except Exception as e:
            self.add_log_entry(f"TTS Error: {str(e)}", "error")
        
        while True:
            try:
                if self.listening_state:
                    self.voice_status.config(text="🟢 Voice: LISTENING", fg=self.colors['green'])
                    
                    with self.microphone as source:
                        # Ultra optimized audio settings - FIXED
                        self.recognizer.adjust_for_ambient_noise(source, duration=1)
                        self.recognizer.pause_threshold = 0.8
                        self.recognizer.non_speaking_duration = 0.5
                        self.recognizer.phrase_threshold = 0.3
                        self.recognizer.dynamic_energy_threshold = True
                        self.recognizer.dynamic_energy_adjustment_damping = 0.15
                        self.recognizer.energy_threshold = 200
                        
                        # Optimized timeout for better recognition
                        audio = self.recognizer.listen(source, timeout=8, phrase_time_limit=8)
                    
                    self.voice_status.config(text="🟡 Voice: RECOGNIZING", fg=self.colors['yellow'])
                    
                    try:
                        command = self.recognizer.recognize_google(audio).lower()
                        self.add_log_entry(f"Recognized: {command}")
                        self.add_command_history(f"Voice: {command}")
                        self.process_command(command)
                    except sr.UnknownValueError:
                        self.add_log_entry("Could not understand", "warning")
                        # Don't speak on every error to avoid interruption
                    except sr.RequestError:
                        self.add_log_entry("Speech recognition error", "error")
                else:
                    self.voice_status.config(text="🔴 Voice: IDLE", fg=self.colors['red'])
                    time.sleep(1)
                    
            except Exception as e:
                self.add_log_entry(f"Voice error: {str(e)}", "error")
                time.sleep(2)
    
    def process_command(self, command):
        """Process voice commands with ultra enhanced recognition"""
        self.add_log_entry(f"Processing: {command}")
        
        # Enhanced greeting commands - FIXED ORDER
        if any(word in command for word in ['hello', 'hi', 'hey', 'good morning', 'good evening', 'assalam']):
            responses = [
                "Hello! How can I help you today?",
                "Hi there! What can I do for you?",
                "Hey! Ready to assist you!",
                "Good to hear from you! How may I help?"
            ]
            response = random.choice(responses)
            self.speak(response)
            self.add_log_entry("Greeting response")
        
        # Enhanced app launching with comprehensive recognition
        elif any(word in command for word in ['open', 'launch', 'start', 'run']):
            app_found = False
            
            # Check for WhatsApp
            if any(word in command for word in ['whatsapp', 'whats app']):
                self.launch_app('whatsapp')
                app_found = True
            
            # Check for Instagram
            elif any(word in command for word in ['instagram', 'insta']):
                self.launch_app('instagram')
                app_found = True
            
            # Check for VS Code
            elif any(word in command for word in ['vs code', 'vscode', 'visual studio code', 'visual studio', 'code']):
                self.launch_app('vscode')
                app_found = True
            
            # Check for YouTube
            elif 'youtube' in command:
                self.launch_app('youtube')
                app_found = True
            
            # Check for Chrome
            elif any(word in command for word in ['chrome', 'browser', 'google chrome']):
                self.launch_app('chrome')
                app_found = True
            
            # Check for File Explorer - ENHANCED
            elif any(word in command for word in ['file folder', 'file explorer', 'explorer', 'files', 'my computer', 'file manager']):
                self.launch_app('files')
                app_found = True
            
            # Check for Camera
            elif 'camera' in command:
                self.launch_app('camera')
                app_found = True
            
            # Check for Blender
            elif 'blender' in command:
                self.launch_app('blender')
                app_found = True
            
            # Check for other apps
            elif 'linkedin' in command:
                self.launch_app('linkedin')
                app_found = True
            elif 'github' in command:
                self.launch_app('github')
                app_found = True
            elif 'gmail' in command:
                self.launch_app('gmail')
                app_found = True
            elif any(word in command for word in ['chatgpt', 'chat gpt', 'open ai']):
                self.launch_app('chatgpt')
                app_found = True
            elif 'spotify' in command:
                self.launch_app('spotify')
                app_found = True
            elif 'discord' in command:
                self.launch_app('discord')
                app_found = True
            elif 'slack' in command:
                self.launch_app('slack')
                app_found = True
            elif 'teams' in command:
                self.launch_app('teams')
                app_found = True
            elif 'zoom' in command:
                self.launch_app('zoom')
                app_found = True
            elif 'notepad' in command:
                self.launch_app('notepad')
                app_found = True
            elif any(word in command for word in ['calculator', 'calc']):
                self.launch_app('calculator')
                app_found = True
            elif any(word in command for word in ['cmd', 'command prompt']):
                self.launch_app('cmd')
                app_found = True
            elif 'powershell' in command:
                self.launch_app('powershell')
                app_found = True
            elif 'task manager' in command:
                self.launch_app('taskmanager')
                app_found = True
            
            if not app_found:
                self.speak("Please specify which app to open")
                self.add_log_entry("App name not specified", "warning")
        
        # Enhanced app closing
        elif any(word in command for word in ['close', 'exit', 'quit', 'stop']):
            app_found = False
            
            if any(word in command for word in ['whatsapp', 'whats app']):
                self.close_app('whatsapp')
                app_found = True
            elif 'instagram' in command:
                self.close_app('instagram')
                app_found = True
            elif any(word in command for word in ['vs code', 'vscode', 'visual studio']):
                self.close_app('vscode')
                app_found = True
            elif 'chrome' in command:
                self.close_app('chrome')
                app_found = True
            elif 'youtube' in command:
                self.close_app('youtube')
                app_found = True
            
            if not app_found:
                self.speak("Please specify which app to close")
                self.add_log_entry("App name not specified for closing", "warning")
        
        # Enhanced YouTube controls - FIXED ORDER
        elif 'play' in command and ('video' in command or 'youtube' in command):
            # Extract video name for search
            video_name = command.replace('play', '').replace('video', '').replace('youtube', '').replace('of', '').strip()
            if video_name:
                self.youtube_search(video_name)
            else:
                self.launch_app('youtube')
        elif 'youtube' in command:
            if 'next' in command or 'skip' in command:
                self.youtube_next_video()
            elif 'previous' in command or 'back' in command:
                self.youtube_previous_video()
            elif 'pause' in command or 'stop' in command:
                self.youtube_pause_video()
            elif 'resume' in command:
                self.youtube_resume_video()
            else:
                self.launch_app('youtube')
        
        # Enhanced WhatsApp commands
        elif any(word in command for word in ['whatsapp', 'message', 'send']):
            if 'message' in command and ('in' in command or 'to' in command):
                self.process_whatsapp_command(command)
            elif 'whatsapp' in command:
                self.launch_app('whatsapp')
            else:
                self.process_whatsapp_command(command)
        
        # System control commands
        elif 'system' in command:
            if 'scan' in command or 'analyze' in command:
                self.system_scan()
            elif 'cleanup' in command or 'clean' in command:
                self.system_cleanup()
            elif 'optimize' in command:
                self.system_optimize()
            elif 'monitor' in command:
                self.system_monitor()
            else:
                self.speak("System control activated. What would you like to control?")
        
        # Information commands
        elif 'time' in command:
            self.tell_time()
        elif 'date' in command:
            self.tell_date()
        elif 'help' in command:
            self.show_help()
        
        else:
            # Enhanced response for unrecognized commands
            response = f"I didn't understand '{command}'. Say 'help' for available commands."
            self.speak(response)
            self.add_log_entry(f"Unrecognized command: {command}", "warning")
    
    def launch_app(self, app_name):
        """Ultra enhanced app launching"""
        self.speak(f"Opening {app_name}")
        self.add_log_entry(f"Launching {app_name}")
        
        paths = self.app_paths.get(app_name, [])
        user = os.getlogin()
        
        # Ultra enhanced app detection
        try:
            app_variants = {
                'whatsapp': ['whatsapp.exe', 'WhatsApp.exe'],
                'instagram': ['instagram.exe', 'Instagram.exe'], 
                'vscode': ['code.exe', 'Code.exe'],
                'chrome': ['chrome.exe', 'Chrome.exe'],
                'discord': ['discord.exe', 'Discord.exe'],
                'spotify': ['spotify.exe', 'Spotify.exe'],
                'youtube': ['chrome.exe', 'msedge.exe', 'firefox.exe'],
                'gmail': ['chrome.exe', 'msedge.exe', 'firefox.exe'],
                'chatgpt': ['chrome.exe', 'msedge.exe', 'firefox.exe'],
                'linkedin': ['chrome.exe', 'msedge.exe', 'firefox.exe'],
                'github': ['chrome.exe', 'msedge.exe', 'firefox.exe'],
                'facebook': ['chrome.exe', 'msedge.exe', 'firefox.exe'],
                'twitter': ['chrome.exe', 'msedge.exe', 'firefox.exe'],
                'reddit': ['chrome.exe', 'msedge.exe', 'firefox.exe'],
                'teams': ['teams.exe', 'Teams.exe'],
                'zoom': ['zoom.exe', 'Zoom.exe'],
                'skype': ['skype.exe', 'Skype.exe'],
                'telegram': ['telegram.exe', 'Telegram.exe'],
                'signal': ['signal.exe', 'Signal.exe'],
                'slack': ['slack.exe', 'Slack.exe'],
                'blender': ['blender.exe', 'Blender.exe'],
                'notepad': ['notepad.exe', 'Notepad.exe'],
                'calculator': ['calc.exe', 'Calculator.exe'],
                'camera': ['windowscamera.exe', 'WindowsCamera.exe']
            }
            
            target_names = app_variants.get(app_name.lower(), [f'{app_name}.exe', f'{app_name.capitalize()}.exe'])
            
            # Check if app is already running - FIXED
            for proc in psutil.process_iter(['pid', 'name']):
                try:
                    proc_info = proc.info
                    if proc_info and 'name' in proc_info:
                        proc_name = proc_info['name']
                        if any(target.lower() in proc_name.lower() for target in target_names):
                            self.bring_window_to_front(proc_name)
                            self.speak(f"{app_name} is already running")
                            self.add_log_entry(f"{app_name} already running (PID: {proc_info['pid']})")
                            return
                except:
                    continue
        except Exception as e:
            self.add_log_entry(f"Error checking running apps: {str(e)}", "warning")
        
        # Try all paths
        found = False
        for path in paths:
            try:
                if '{user}' in path:
                    path = path.format(user=user)
                
                if path.startswith('http'):
                    webbrowser.open(path)
                    self.add_log_entry(f"Opened {app_name} in browser")
                    found = True
                    break
                elif path.endswith('://'):
                    os.startfile(path)
                    self.add_log_entry(f"Opened {app_name} via protocol")
                    found = True
                    break
                elif '*' in path:
                    matches = glob.glob(path)
                    if matches:
                        os.startfile(matches[0])
                        self.add_log_entry(f"Opened {app_name} from wildcard path")
                        found = True
                        break
                else:
                    if os.path.exists(path):
                        os.startfile(path)
                        self.add_log_entry(f"Opened {app_name} from path")
                        found = True
                        break
            except Exception as e:
                self.add_log_entry(f"Failed to open {app_name}: {str(e)}", "warning")
                continue
        
        if not found:
            self.speak(f"Could not find {app_name}")
            self.add_log_entry(f"Could not find {app_name}", "error")
    
    def close_app(self, app_name):
        """Close application"""
        self.speak(f"Closing {app_name}")
        self.add_log_entry(f"Closing {app_name}")
        
        try:
            app_variants = {
                'whatsapp': ['whatsapp.exe', 'WhatsApp.exe'],
                'instagram': ['instagram.exe', 'Instagram.exe'],
                'vscode': ['code.exe', 'Code.exe'],
                'chrome': ['chrome.exe', 'Chrome.exe'],
                'youtube': ['chrome.exe', 'msedge.exe', 'firefox.exe']
            }
            
            target_names = app_variants.get(app_name.lower(), [f'{app_name}.exe', f'{app_name.capitalize()}.exe'])
            
            closed = False
            for proc in psutil.process_iter(['pid', 'name']):
                try:
                    proc_name = proc.info['name']
                    if any(target.lower() in proc_name.lower() for target in target_names):
                        proc.terminate()
                        self.add_log_entry(f"Closed {app_name} (PID: {proc.info['pid']})")
                        closed = True
                        break
                except:
                    continue
            
            if closed:
                self.speak(f"{app_name} closed successfully")
            else:
                self.speak(f"{app_name} was not running")
                self.add_log_entry(f"{app_name} was not running", "warning")
        except Exception as e:
            self.add_log_entry(f"Error closing {app_name}: {str(e)}", "error")
    
    def bring_window_to_front(self, window_title):
        """Bring window to front"""
        try:
            def callback(hwnd, hwnd_list):
                if win32gui.IsWindowVisible(hwnd):
                    title = win32gui.GetWindowText(hwnd)
                    if window_title.lower() in title.lower():
                        hwnd_list.append(hwnd)
                return True
            
            hwnd_list = []
            win32gui.EnumWindows(callback, hwnd_list)
            
            if hwnd_list:
                hwnd = hwnd_list[0]
                win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                win32gui.SetForegroundWindow(hwnd)
        except:
            pass
    
    def system_scan(self):
        """Perform system scan"""
        self.add_log_entry("System scan initiated")
        
        try:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            scan_results = f"""
SYSTEM SCAN RESULTS:
CPU Usage: {cpu_usage:.1f}%
Memory Usage: {memory.percent:.1f}%
Disk Usage: {disk.percent:.1f}%
Available Memory: {memory.available / (1024**3):.1f} GB
Free Disk Space: {disk.free / (1024**3):.1f} GB
"""
            
            self.add_system_info(scan_results)
            self.speak("System scan completed")
            
        except Exception as e:
            self.add_log_entry(f"System scan error: {str(e)}", "error")
    
    def system_cleanup(self):
        """Perform system cleanup"""
        self.add_log_entry("System cleanup initiated")
        
        try:
            # Clean temp files
            temp_path = os.environ.get('TEMP', '')
            cleaned_files = 0
            
            if os.path.exists(temp_path):
                for file in os.listdir(temp_path):
                    try:
                        file_path = os.path.join(temp_path, file)
                        if os.path.isfile(file_path):
                            os.remove(file_path)
                            cleaned_files += 1
                    except:
                        pass
            
            self.add_log_entry(f"Cleanup completed: {cleaned_files} files removed")
            self.speak(f"System cleanup completed. Removed {cleaned_files} temporary files")
            
        except Exception as e:
            self.add_log_entry(f"System cleanup error: {str(e)}", "error")
    
    def system_optimize(self):
        """Perform system optimization"""
        self.add_log_entry("System optimization initiated")
        
        try:
            # Clear recycle bin
            import winshell
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
            
            self.add_log_entry("System optimization completed")
            self.speak("System optimization completed successfully")
            
        except Exception as e:
            self.add_log_entry(f"System optimization error: {str(e)}", "error")
    
    def system_monitor(self):
        """Start system monitoring"""
        self.add_log_entry("System monitoring started")
        self.speak("System monitoring activated")
    
    def tell_time(self):
        """Tell current time"""
        current_time = datetime.now().strftime("%I:%M %p")
        self.speak(f"The current time is {current_time}")
        self.add_log_entry(f"Time: {current_time}")
    
    def tell_date(self):
        """Tell current date"""
        current_date = datetime.now().strftime("%A, %B %d, %Y")
        self.speak(f"Today is {current_date}")
        self.add_log_entry(f"Date: {current_date}")
    
    def show_help(self):
        """Show help information"""
        help_text = """
ILLI AI ASSISTANT - AVAILABLE COMMANDS:

🚀 APP LAUNCHING:
• "Open [app name]" - Launch any application
• Examples: "Open WhatsApp", "Open VS Code", "Open YouTube"

📱 SUPPORTED APPS:
• WhatsApp, Instagram, VS Code, YouTube, Chrome
• LinkedIn, GitHub, Gmail, ChatGPT, Spotify
• Discord, Slack, Teams, Zoom, Camera, Blender
• Notepad, Calculator, File Explorer, CMD, PowerShell

🔧 APP CONTROL:
• "Close [app name]" - Close any application
• Examples: "Close Chrome", "Close WhatsApp"

🎬 YOUTUBE CONTROL:
• "Play [video name]" - Search and play video
• "Next video", "Previous video"
• "Pause video", "Resume video"

📊 SYSTEM CONTROL:
• "System scan" - Analyze system performance
• "System cleanup" - Clean temporary files
• "System optimize" - Optimize system performance
• "System monitor" - Start monitoring

📱 WHATSAPP:
• "Send message to [contact] saying [message]"
• "Message in [group name] [message]"

📊 INFORMATION:
• "Time" - Current time
• "Date" - Current date
• "Help" - Show this help

🗣️ VOICE COMMANDS:
• "Hello", "Hi", "Hey" - Greeting responses
• Any command works with voice recognition

💡 TIPS:
• Speak clearly and naturally
• Wait for the listening indicator
• Use specific app names
• Commands are case-insensitive
        """
        
        self.add_system_info(help_text)
        self.speak("Help information displayed")
    
    def process_whatsapp_command(self, command):
        """Process WhatsApp commands"""
        self.add_log_entry("WhatsApp command processing")
        self.speak("WhatsApp feature requires web interface. Opening WhatsApp...")
        self.launch_app('whatsapp')
    
    def youtube_search(self, video_name):
        """Search YouTube"""
        search_url = f"https://www.youtube.com/results?search_query={video_name.replace(' ', '+')}"
        webbrowser.open(search_url)
        self.add_log_entry(f"YouTube search: {video_name}")
        self.speak(f"Searching YouTube for {video_name}")
    
    def youtube_next_video(self):
        """Play next YouTube video"""
        pyautogui.press('shift', 'n')
        self.add_log_entry("YouTube: Next video")
        self.speak("Next video")
    
    def youtube_previous_video(self):
        """Play previous YouTube video"""
        pyautogui.press('shift', 'p')
        self.add_log_entry("YouTube: Previous video")
        self.speak("Previous video")
    
    def youtube_pause_video(self):
        """Pause YouTube video"""
        pyautogui.press('space')
        self.add_log_entry("YouTube: Video paused")
        self.speak("Video paused")
    
    def youtube_resume_video(self):
        """Resume YouTube video"""
        pyautogui.press('space')
        self.add_log_entry("YouTube: Video resumed")
        self.speak("Video resumed")
    
    def load_whatsapp_contacts(self):
        """Load WhatsApp contacts"""
        try:
            if os.path.exists(self.contact_memory_file):
                with open(self.contact_memory_file, 'r') as f:
                    self.whatsapp_contacts = json.load(f)
        except:
            self.whatsapp_contacts = []
    
    def save_whatsapp_contacts(self):
        """Save WhatsApp contacts"""
        try:
            os.makedirs(os.path.dirname(self.contact_memory_file), exist_ok=True)
            with open(self.contact_memory_file, 'w') as f:
                json.dump(self.whatsapp_contacts, f)
        except Exception as e:
            self.add_log_entry(f"Error saving contacts: {str(e)}", "error")
    
    def analyze_whatsapp_contacts(self):
        """Analyze WhatsApp contacts"""
        self.add_log_entry("WhatsApp contact analysis")
        self.speak("Contact analysis feature available in web interface")
    
    def remember_contacts(self):
        """Remember contacts"""
        self.add_log_entry("Contact memory activated")
        self.speak("Contact memory feature available in web interface")
    
    def speak(self, text):
        """Text to speech"""
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            self.add_log_entry(f"TTS Error: {str(e)}", "error")
    
    def add_log_entry(self, message, level="info"):
        """Add log entry"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        
        # Add to system display
        self.system_display.insert(tk.END, log_entry)
        self.system_display.see(tk.END)
        
        # Update status
        if level == "error":
            self.status_label.config(text=f"Status: ERROR", fg=self.colors['error'])
        elif level == "warning":
            self.status_label.config(text=f"Status: WARNING", fg=self.colors['warning'])
        else:
            self.status_label.config(text=f"Status: ONLINE", fg=self.colors['success'])
    
    def add_command_history(self, command):
        """Add command to history"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        history_entry = f"[{timestamp}] {command}\n"
        
        self.command_display.insert(tk.END, history_entry)
        self.command_display.see(tk.END)
    
    def add_system_info(self, info):
        """Add system information"""
        self.system_display.insert(tk.END, info + "\n")
        self.system_display.see(tk.END)
    
    def add_app_info(self, info):
        """Add app information"""
        self.app_display.insert(tk.END, info + "\n")
        self.app_display.see(tk.END)
    
    def update_system_info(self):
        """Update system information periodically"""
        while True:
            try:
                cpu_usage = psutil.cpu_percent(interval=1)
                memory = psutil.virtual_memory()
                
                system_info = f"""
CPU: {cpu_usage:.1f}%
Memory: {memory.percent:.1f}%
Processes: {len(list(psutil.process_iter()))}
"""
                
                # Update task label
                self.task_label.config(text=f"Task: {self.current_task}")
                
                time.sleep(5)  # Update every 5 seconds
                
            except Exception as e:
                self.add_log_entry(f"System update error: {str(e)}", "error")
                time.sleep(5)

def main():
    """Main function"""
    root = tk.Tk()
    app = ILLICompleteUltraFixed(root)
    root.mainloop()

if __name__ == "__main__":
    main()
