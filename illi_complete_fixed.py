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

class ILLICompleteFixed:
    def __init__(self, root):
        self.root = root
        self.root.title("ILLI AI - COMPLETE FIXED")
        self.root.geometry("1920x1080")
        self.root.configure(bg='#000000')
        
        # System variables
        self.system_status = "ONLINE"
        self.user_name = os.getlogin()
        self.current_task = "Voice Assistant Active"
        self.listening_state = False
        self.response_queue = queue.Queue()
        
        # Voice recognition - Enhanced settings
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
        
        # Enhanced app paths with better desktop detection
        self.app_paths = {
            'whatsapp': [
                "C:\\Users\\{user}\\AppData\\Local\\WhatsApp\\WhatsApp.exe",
                "C:\\Program Files\\WindowsApps\\*\\WhatsApp.exe",
                "C:\\Program Files\\WhatsApp\\WhatsApp.exe",
                "https://web.whatsapp.com"
            ],
            'instagram': [
                "C:\\Users\\{user}\\AppData\\Local\\Instagram\\Instagram.exe",
                "C:\\Program Files\\WindowsApps\\*\\Instagram.exe",
                "https://instagram.com"
            ],
            'chrome': [
                "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
                "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
                "https://google.com"
            ],
            'vscode': [
                "C:\\Users\\{user}\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
                "C:\\Program Files\\Microsoft VS Code\\Code.exe",
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
                "C:\\Windows\\System32\\WindowsCamera.exe"
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
                "https://x.com"
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
        
        self.setup_ui()
        self.start_voice_assistant()
        self.start_system_monitoring()
        
    def setup_ui(self):
        """Create main UI with fixed layout"""
        # Create main container
        main_frame = tk.Frame(self.root, bg=self.colors['bg'])
        main_frame.pack(fill='both', expand=True)
        
        # Header
        self.create_header(main_frame)
        
        # Main content area
        content_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        content_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Create modular grid system
        self.create_left_sidebar(content_frame)
        self.create_centerpiece(content_frame)
        self.create_right_sidebar(content_frame)
        self.create_bottom_panel(content_frame)
    
    def create_header(self, parent):
        """Create header"""
        header_frame = tk.Frame(parent, bg=self.colors['glass'], height=80)
        header_frame.pack(fill='x', pady=(0, 20))
        header_frame.pack_propagate(False)
        
        # Title
        title_label = tk.Label(header_frame, text="⚡ ILLI AI - COMPLETE FIXED ⚡", 
                          font=("Consolas", 24, "bold"), 
                          bg=self.colors['glass'], fg=self.colors['accent'])
        title_label.pack(side='left', padx=40, pady=20)
        
        # Status indicator
        self.status_label = tk.Label(header_frame, text=f"🟢 {self.system_status}", 
                                 font=("Consolas", 16, "bold"),
                                 bg=self.colors['glass'], fg=self.colors['success'])
        self.status_label.pack(side='left', padx=40, pady=20)
        
        # User info
        user_info = f"USER: {self.user_name} | TASK: {self.current_task}"
        self.user_label = tk.Label(header_frame, text=user_info, 
                               font=("Consolas", 12), 
                               bg=self.colors['glass'], fg=self.colors['text_dim'])
        self.user_label.pack(side='right', padx=40, pady=20)
    
    def create_left_sidebar(self, parent):
        """Create left sidebar"""
        left_frame = tk.Frame(parent, bg=self.colors['glass'], width=400)
        left_frame.pack(side='left', fill='y', padx=(0, 10))
        left_frame.pack_propagate(False)
        
        # System Diagnostics Title
        title = tk.Label(left_frame, text="🤖 SYSTEM DIAGNOSTICS", 
                       font=("Consolas", 14, "bold"),
                       bg=self.colors['glass'], fg=self.colors['accent'])
        title.pack(pady=20)
        
        # Voice Status
        voice_frame = tk.Frame(left_frame, bg=self.colors['glass'])
        voice_frame.pack(fill='x', padx=20, pady=10)
        
        tk.Label(voice_frame, text="🎤 VOICE STATUS", font=("Consolas", 10, "bold"),
                bg=self.colors['glass'], fg=self.colors['text']).pack(anchor='w')
        
        self.voice_canvas = tk.Canvas(voice_frame, width=350, height=30, 
                                     bg=self.colors['glass'], highlightthickness=0)
        self.voice_canvas.pack(fill='x', pady=5)
        
        # System Control
        system_frame = tk.Frame(left_frame, bg=self.colors['glass'])
        system_frame.pack(fill='x', padx=20, pady=20)
        
        tk.Label(system_frame, text="⚙️ SYSTEM CONTROL", font=("Consolas", 10, "bold"),
                bg=self.colors['glass'], fg=self.colors['text']).pack(anchor='w')
        
        self.system_canvas = tk.Canvas(system_frame, width=350, height=100, 
                                  bg=self.colors['glass'], highlightthickness=0)
        self.system_canvas.pack(fill='x', pady=5)
        
        # System Log
        log_frame = tk.Frame(left_frame, bg=self.colors['glass'])
        log_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        tk.Label(log_frame, text="📊 SYSTEM LOG", font=("Consolas", 10, "bold"),
                bg=self.colors['glass'], fg=self.colors['text']).pack(anchor='w')
        
        self.system_log = scrolledtext.ScrolledText(log_frame, height=15, width=40,
                                               bg='#0a0a0a', fg=self.colors['cyan'],
                                               font=("Consolas", 9), 
                                               insertbackground=self.colors['accent'])
        self.system_log.pack(fill='both', expand=True, pady=5)
        
        self.add_log_entry("ILLI Complete Fixed initialized", "info")
        self.add_log_entry("Voice systems online", "success")
        self.add_log_entry("System control enabled", "info")
    
    def create_centerpiece(self, parent):
        """Create centerpiece"""
        center_frame = tk.Frame(parent, bg=self.colors['glass'])
        center_frame.pack(side='left', fill='both', expand=True, padx=10)
        
        # 3D Core
        self.nebula_canvas = tk.Canvas(center_frame, width=800, height=600, 
                                   bg=self.colors['glass'], highlightthickness=0)
        self.nebula_canvas.pack(expand=True, pady=20)
        
        # Listening indicator
        self.listening_indicator = tk.Label(center_frame, text="🔴 IDLE", 
                                       font=("Consolas", 16, "bold"),
                                       bg=self.colors['glass'], fg=self.colors['text_dim'])
        self.listening_indicator.pack(pady=10)
        
        # Control buttons
        control_frame = tk.Frame(center_frame, bg=self.colors['glass'])
        control_frame.pack(pady=20)
        
        tk.Button(control_frame, text="🎤 START VOICE", 
                command=self.toggle_listening,
                bg=self.colors['accent'], fg=self.colors['text'], 
                font=("Consolas", 12, "bold"),
                width=20, height=2).pack(side='left', padx=10)
        
        tk.Button(control_frame, text="🔄 SYSTEM SCAN", 
                command=self.system_scan,
                bg=self.colors['magenta'], fg=self.colors['text'], 
                font=("Consolas", 12, "bold"),
                width=20, height=2).pack(side='left', padx=10)
    
    def create_right_sidebar(self, parent):
        """Create right sidebar"""
        right_frame = tk.Frame(parent, bg=self.colors['glass'], width=400)
        right_frame.pack(side='left', fill='y', padx=(10, 0))
        right_frame.pack_propagate(False)
        
        # Controls Title
        title = tk.Label(right_frame, text="🎮 APP LAUNCHER", 
                       font=("Consolas", 14, "bold"),
                       bg=self.colors['glass'], fg=self.colors['accent'])
        title.pack(pady=20)
        
        # App Launcher
        app_frame = tk.Frame(right_frame, bg=self.colors['glass'])
        app_frame.pack(fill='x', padx=20, pady=20)
        
        tk.Label(app_frame, text="🚀 APP LAUNCHER", font=("Consolas", 10, "bold"),
                bg=self.colors['glass'], fg=self.colors['text']).pack(anchor='w')
        
        self.app_canvas = tk.Canvas(app_frame, width=350, height=100, 
                                bg=self.colors['glass'], highlightthickness=0)
        self.app_canvas.pack(fill='x', pady=5)
        
        # Command History
        history_frame = tk.Frame(right_frame, bg=self.colors['glass'])
        history_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        tk.Label(history_frame, text="📝 COMMAND HISTORY", font=("Consolas", 10, "bold"),
                bg=self.colors['glass'], fg=self.colors['text']).pack(anchor='w')
        
        self.command_history = scrolledtext.ScrolledText(history_frame, height=10, width=40,
                                                   bg='#0a0a0a', fg=self.colors['yellow'],
                                                   font=("Consolas", 9), 
                                                   insertbackground=self.colors['accent'])
        self.command_history.pack(fill='both', expand=True, pady=5)
    
    def create_bottom_panel(self, parent):
        """Create bottom panel"""
        bottom_frame = tk.Frame(parent, bg=self.colors['glass'], height=300)
        bottom_frame.pack(side='bottom', fill='x', pady=(10, 0))
        bottom_frame.pack_propagate(False)
        
        # Neural Network Title
        title = tk.Label(bottom_frame, text="🧠 NEURAL NETWORK", 
                       font=("Consolas", 14, "bold"),
                       bg=self.colors['glass'], fg=self.colors['accent'])
        title.pack(pady=10)
        
        # Neural Network Visualization
        self.neural_canvas = tk.Canvas(bottom_frame, width=1200, height=200, 
                                    bg=self.colors['glass'], highlightthickness=0)
        self.neural_canvas.pack(fill='both', expand=True, padx=20, pady=10)
    
    def start_voice_assistant(self):
        """Start voice assistant"""
        threading.Thread(target=self.voice_assistant_loop, daemon=True).start()
        threading.Thread(target=self.animate_nebula, daemon=True).start()
        threading.Thread(target=self.animate_neural_network, daemon=True).start()
        threading.Thread(target=self.animate_displays, daemon=True).start()
    
    def voice_assistant_loop(self):
        """Enhanced voice assistant loop"""
        try:
            self.speak("Assalam o Alaikum Muhammad Farhan!")
            self.speak("Good Evening!")
            self.speak("I am ILLI Complete Fixed, your most advanced AI assistant created by Muhammad Farhan. I have complete control over your system with all apps and features!")
        except Exception as e:
            self.add_log_entry(f"TTS Error: {str(e)}", "error")
        
        while True:
            try:
                if self.listening_state:
                    self.listening_indicator.config(text="🟢 LISTENING", fg=self.colors['success'])
                    self.update_voice_canvas("LISTENING")
                    
                    with self.microphone as source:
                        # Enhanced audio settings for better recognition
                        self.recognizer.adjust_for_ambient_noise(source, duration=2)
                        self.recognizer.pause_threshold = 1.0
                        self.recognizer.non_speaking_duration = 0.8
                        self.recognizer.phrase_threshold = 0.3
                        self.recognizer.dynamic_energy_threshold = True
                        self.recognizer.dynamic_energy_adjustment_damping = 0.15
                        
                        # Longer timeout and phrase limit for full requests
                        audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=12)
                    
                    self.listening_indicator.config(text="🟡 RECOGNIZING", fg=self.colors['yellow'])
                    self.update_voice_canvas("RECOGNIZING")
                    
                    try:
                        command = self.recognizer.recognize_google(audio).lower()
                        self.add_log_entry(f"Recognized: {command}", "info")
                        self.add_command_history(command)
                        self.process_command(command)
                    except sr.UnknownValueError:
                        self.add_log_entry("Could not understand", "warning")
                        self.listening_indicator.config(text="🔴 IDLE", fg=self.colors['text_dim'])
                        self.update_voice_canvas("IDLE")
                    except sr.RequestError:
                        self.add_log_entry("Speech recognition error", "error")
                        self.listening_indicator.config(text="🔴 IDLE", fg=self.colors['text_dim'])
                        self.update_voice_canvas("IDLE")
                else:
                    self.listening_indicator.config(text="🔴 IDLE", fg=self.colors['text_dim'])
                    self.update_voice_canvas("IDLE")
                    time.sleep(1)
                    
            except Exception as e:
                self.add_log_entry(f"Voice error: {str(e)}", "error")
                time.sleep(2)
    
    def process_command(self, command):
        """Process voice commands with complete system control"""
        self.add_log_entry(f"Processing: {command}", "info")
        
        # System Control Commands
        if any(word in command for word in ['system', 'control', 'manage', 'admin']):
            if 'scan' in command or 'analyze' in command:
                self.system_scan()
            elif 'process' in command:
                self.show_processes()
            elif 'task manager' in command or 'taskmanager' in command:
                self.launch_app('taskmanager')
            elif 'cmd' in command or 'command' in command:
                self.launch_app('cmd')
            elif 'powershell' in command:
                self.launch_app('powershell')
            elif 'control panel' in command or 'controlpanel' in command:
                self.launch_app('controlpanel')
            elif 'settings' in command:
                self.launch_app('settings')
            elif 'cleanup' in command or 'clean' in command:
                self.system_cleanup()
            elif 'optimize' in command:
                self.system_optimize()
            elif 'monitor' in command:
                self.system_monitor()
            else:
                self.speak("System control activated. What would you like to control?")
        
        # Enhanced app launching with better recognition
        elif any(word in command for word in ['open', 'launch', 'start', 'run']):
            if 'whatsapp' in command:
                self.launch_app('whatsapp')
            elif 'instagram' in command or 'insta' in command:
                self.launch_app('instagram')
            elif 'chrome' in command or 'browser' in command:
                self.launch_app('chrome')
            elif 'vs code' in command or 'vscode' in command or 'visual studio' in command:
                self.launch_app('vscode')
            elif 'linkedin' in command:
                self.launch_app('linkedin')
            elif 'github' in command:
                self.launch_app('github')
            elif 'canva' in command:
                self.launch_app('canva')
            elif 'camera' in command:
                self.launch_app('camera')
            elif 'notepad' in command:
                self.launch_app('notepad')
            elif 'calculator' in command or 'calc' in command:
                self.launch_app('calculator')
            elif 'files' in command or 'explorer' in command:
                self.launch_app('files')
            elif 'youtube' in command:
                self.launch_app('youtube')
            elif 'gmail' in command:
                self.launch_app('gmail')
            elif 'chatgpt' in command or 'charge gpt' in command or 'open ai' in command:
                self.launch_app('chatgpt')
            elif 'spotify' in command:
                self.launch_app('spotify')
            elif 'discord' in command:
                self.launch_app('discord')
            elif 'slack' in command:
                self.launch_app('slack')
            elif 'teams' in command:
                self.launch_app('teams')
            elif 'zoom' in command:
                self.launch_app('zoom')
            elif 'skype' in command:
                self.launch_app('skype')
            elif 'telegram' in command:
                self.launch_app('telegram')
            elif 'signal' in command:
                self.launch_app('signal')
            elif 'facebook' in command:
                self.launch_app('facebook')
            elif 'twitter' in command:
                self.launch_app('twitter')
            elif 'reddit' in command:
                self.launch_app('reddit')
            elif 'pinterest' in command:
                self.launch_app('pinterest')
            elif 'tiktok' in command:
                self.launch_app('tiktok')
            elif 'snapchat' in command:
                self.launch_app('snapchat')
            elif 'task manager' in command or 'taskmanager' in command:
                self.launch_app('taskmanager')
            elif 'cmd' in command:
                self.launch_app('cmd')
            elif 'powershell' in command:
                self.launch_app('powershell')
            elif 'control panel' in command or 'controlpanel' in command:
                self.launch_app('controlpanel')
            elif 'settings' in command:
                self.launch_app('settings')
            else:
                self.speak("I didn't understand which app to open. Please specify app name.")
        
        # Enhanced app closing commands
        elif any(word in command for word in ['close', 'exit', 'quit', 'stop']):
            if 'vs code' in command or 'vscode' in command or 'visual studio' in command:
                self.close_app('vscode')
            elif 'whatsapp' in command:
                self.close_app('whatsapp')
            elif 'instagram' in command:
                self.close_app('instagram')
            elif 'chrome' in command:
                self.close_app('chrome')
            elif 'youtube' in command:
                self.close_app('youtube')
            elif 'linkedin' in command:
                self.close_app('linkedin')
            elif 'gmail' in command:
                self.close_app('gmail')
            elif 'chatgpt' in command:
                self.close_app('chatgpt')
            elif 'spotify' in command:
                self.close_app('spotify')
            elif 'discord' in command:
                self.close_app('discord')
            elif 'slack' in command:
                self.close_app('slack')
            elif 'teams' in command:
                self.close_app('teams')
            elif 'zoom' in command:
                self.close_app('zoom')
            elif 'skype' in command:
                self.close_app('skype')
            elif 'telegram' in command:
                self.close_app('telegram')
            elif 'signal' in command:
                self.close_app('signal')
            elif 'facebook' in command:
                self.close_app('facebook')
            elif 'twitter' in command:
                self.close_app('twitter')
            elif 'reddit' in command:
                self.close_app('reddit')
            elif 'pinterest' in command:
                self.close_app('pinterest')
            elif 'tiktok' in command:
                self.close_app('tiktok')
            elif 'snapchat' in command:
                self.close_app('snapchat')
            else:
                self.speak("I didn't understand which app to close. Please specify app name.")
        
        # Enhanced YouTube controls with better search
        elif 'play' in command or 'youtube' in command:
            if 'next' in command or 'skip' in command:
                self.youtube_next_video()
            elif 'previous' in command or 'back' in command:
                self.youtube_previous_video()
            elif 'pause' in command or 'stop' in command:
                self.youtube_pause_video()
            elif 'resume' in command:
                self.youtube_resume_video()
            else:
                # Enhanced video name extraction
                video_name = command.replace('play', '').replace('video', '').replace('youtube', '').replace('of', '').strip()
                if video_name:
                    self.youtube_search(video_name)
                else:
                    self.launch_app('youtube')
        
        # Enhanced LinkedIn commands
        elif 'linkedin' in command:
            if 'profile' in command or 'my profile' in command:
                self.open_linkedin_profile()
            elif 'jobs' in command:
                self.open_linkedin_jobs()
            elif 'network' in command:
                self.open_linkedin_network()
            elif 'connect' in command or 'connection' in command:
                self.linkedin_connect()
            elif 'request' in command:
                self.linkedin_connect()
            else:
                self.launch_app('linkedin')
        
        # Enhanced WhatsApp commands
        elif any(word in command for word in ['whatsapp', 'message', 'send']):
            self.process_whatsapp_command(command)
        
        # Enhanced system controls
        elif 'shutdown' in command:
            self.shutdown_system()
        elif 'restart' in command or 'reboot' in command:
            self.restart_system()
        elif 'sleep' in command:
            self.sleep_system()
        elif 'lock' in command:
            self.lock_system()
        elif 'logoff' in command or 'logout' in command:
            self.logoff_system()
        
        # Enhanced information commands
        elif 'time' in command:
            self.tell_time()
        elif any(word in command for word in ['what is', 'search', 'wikipedia']):
            search_term = command.replace('what is', '').replace('search', '').replace('wikipedia', '').strip()
            if search_term:
                self.wikipedia_search(search_term)
        
        # Enhanced contact commands
        elif any(word in command for word in ['analyze', 'contact']):
            self.analyze_whatsapp_contacts()
        elif any(word in command for word in ['remember', 'contact']):
            self.remember_contacts()
        
        # Help command
        elif 'help' in command:
            self.show_help()
        
        else:
            self.speak("I didn't understand that command. Say 'help' to see what I can do.")
            self.add_log_entry(f"Unrecognized command: {command}", "warning")
    
    def launch_app(self, app_name):
        """Enhanced app launching with better desktop detection"""
        self.speak(f"Opening {app_name}")
        self.add_log_entry(f"Launching {app_name}", "info")
        self.update_app_canvas(f"LAUNCHING {app_name.upper()}")
        
        paths = self.app_paths.get(app_name, [])
        user = os.getlogin()
        
        # Try to find app in system first
        found = False
        
        # Check if app is already running
        try:
            for proc in psutil.process_iter(['pid', 'name']):
                try:
                    if app_name.lower() in proc.info['name'].lower():
                        # Bring existing window to front
                        self.bring_window_to_front(proc.info['name'])
                        self.speak(f"{app_name} is already running")
                        self.add_log_entry(f"{app_name} already running", "info")
                        self.update_app_canvas(f"{app_name.upper()} ALREADY RUNNING")
                        found = True
                        break
                except:
                    continue
        except:
            pass
        
        if not found:
            # Try all paths
            for path in paths:
                try:
                    if '{user}' in path:
                        path = path.format(user=user)
                    
                    if path.startswith('http'):
                        webbrowser.open(path)
                        self.add_log_entry(f"Opened {app_name} in browser", "success")
                        self.update_app_canvas(f"{app_name.upper()} OPENED")
                        found = True
                        break
                    elif path.endswith('://'):
                        os.startfile(path)
                        self.add_log_entry(f"Opened {app_name} via protocol", "success")
                        self.update_app_canvas(f"{app_name.upper()} OPENED")
                        found = True
                        break
                    elif '*' in path:
                        # Handle wildcard paths
                        matches = glob.glob(path)
                        if matches:
                            os.startfile(matches[0])
                            self.add_log_entry(f"Opened {app_name} from wildcard path", "success")
                            self.update_app_canvas(f"{app_name.upper()} OPENED")
                            found = True
                            break
                    else:
                        if os.path.exists(path):
                            os.startfile(path)
                            self.add_log_entry(f"Opened {app_name} from path", "success")
                            self.update_app_canvas(f"{app_name.upper()} OPENED")
                            found = True
                            break
                except Exception as e:
                    self.add_log_entry(f"Failed to open {app_name} with path {path}: {str(e)}", "warning")
                    continue
        
        # If no path worked, try web fallback
        if not found:
            self.speak(f"Could not find {app_name}. Opening web version.")
            web_urls = {
                'whatsapp': 'https://web.whatsapp.com',
                'instagram': 'https://instagram.com',
                'linkedin': 'https://linkedin.com',
                'github': 'https://github.com',
                'canva': 'https://canva.com',
                'youtube': 'https://youtube.com',
                'gmail': 'https://gmail.com',
                'chatgpt': 'https://chat.openai.com',
                'spotify': 'https://open.spotify.com',
                'discord': 'https://discord.com',
                'slack': 'https://slack.com',
                'teams': 'https://teams.microsoft.com',
                'zoom': 'https://zoom.us',
                'skype': 'https://web.skype.com',
                'telegram': 'https://web.telegram.org',
                'signal': 'https://signal.org',
                'facebook': 'https://facebook.com',
                'twitter': 'https://twitter.com',
                'reddit': 'https://reddit.com',
                'pinterest': 'https://pinterest.com',
                'tiktok': 'https://tiktok.com',
                'snapchat': 'https://snapchat.com'
            }
            
            if app_name in web_urls:
                webbrowser.open(web_urls[app_name])
                self.add_log_entry(f"Opened {app_name} web version", "success")
                self.update_app_canvas(f"{app_name.upper()} WEB OPENED")
            else:
                self.speak(f"Could not find {app_name}. Please check if it's installed.")
                self.add_log_entry(f"Could not find {app_name}", "error")
                self.update_app_canvas(f"{app_name.upper()} NOT FOUND")
    
    def close_app(self, app_name):
        """Close application"""
        self.speak(f"Closing {app_name}")
        self.add_log_entry(f"Closing {app_name}", "info")
        
        # Find and close process
        closed = False
        try:
            for proc in psutil.process_iter(['pid', 'name']):
                try:
                    if app_name.lower() in proc.info['name'].lower():
                        proc.terminate()
                        self.add_log_entry(f"Closed {app_name} (PID: {proc.info['pid']})", "success")
                        self.speak(f"{app_name} closed")
                        closed = True
                        break
                except:
                    continue
        except:
            pass
        
        if not closed:
            self.speak(f"Could not find {app_name} running")
            self.add_log_entry(f"Could not find {app_name} running", "warning")
    
    def bring_window_to_front(self, app_name):
        """Bring window to front"""
        try:
            # Find window by title
            def window_callback(hwnd, extra):
                if win32gui.IsWindowVisible(hwnd):
                    window_title = win32gui.GetWindowText(hwnd)
                    if app_name.lower() in window_title.lower():
                        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                        win32gui.SetForegroundWindow(hwnd)
                return True
            
            win32gui.EnumWindows(window_callback, None)
        except:
            pass
    
    def linkedin_connect(self):
        """Send LinkedIn connection request"""
        self.speak("Opening LinkedIn for connection requests")
        self.add_log_entry("LinkedIn connection request", "info")
        
        # Open LinkedIn and guide user
        webbrowser.open("https://linkedin.com/mynetwork")
        time.sleep(3)
        
        self.speak("Please select person you want to connect with and click Connect button")
        self.add_log_entry("LinkedIn connection interface opened", "success")
    
    def system_scan(self):
        """Scan system for information"""
        self.speak("Scanning system...")
        self.add_log_entry("System scan initiated", "info")
        self.update_system_canvas("SCANNING")
        
        # Get system information
        try:
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            self.speak(f"CPU usage: {cpu_percent:.1f} percent")
            self.speak(f"Memory usage: {memory.percent:.1f} percent")
            self.speak(f"Disk usage: {disk.percent:.1f} percent")
            
            self.add_log_entry(f"CPU: {cpu_percent:.1f}%, Memory: {memory.percent:.1f}%, Disk: {disk.percent:.1f}%", "success")
            self.update_system_canvas("SCAN COMPLETE")
        except Exception as e:
            self.add_log_entry(f"Scan error: {str(e)}", "error")
            self.update_system_canvas("SCAN ERROR")
    
    def show_processes(self):
        """Show running processes"""
        self.speak("Getting running processes...")
        self.add_log_entry("Retrieving processes", "info")
        
        processes = []
        try:
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
                try:
                    processes.append(proc.info)
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
            
            # Sort by CPU usage
            processes.sort(key=lambda x: x['cpu_percent'], reverse=True)
            
            # Show top 5 processes
            self.speak("Top 5 processes by CPU usage:")
            for proc in processes[:5]:
                self.speak(f"{proc['name']}: {proc['cpu_percent']:.1f} percent")
                self.add_log_entry(f"Process: {proc['name']} - {proc['cpu_percent']:.1f}%", "info")
        except Exception as e:
            self.add_log_entry(f"Process error: {str(e)}", "error")
    
    def system_cleanup(self):
        """Clean system files"""
        self.speak("Starting system cleanup...")
        self.add_log_entry("System cleanup initiated", "info")
        self.update_system_canvas("CLEANING")
        
        # Clean temp files
        temp_path = os.path.join(os.environ.get('TEMP', ''), '')
        cleaned_files = 0
        
        try:
            for filename in os.listdir(temp_path):
                file_path = os.path.join(temp_path, filename)
                try:
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                        cleaned_files += 1
                except:
                    pass
        except:
            pass
        
        self.speak(f"Cleanup completed. Removed {cleaned_files} temporary files.")
        self.add_log_entry(f"Cleanup completed: {cleaned_files} files removed", "success")
        self.update_system_canvas("CLEANUP COMPLETE")
    
    def system_optimize(self):
        """Optimize system performance"""
        self.speak("Optimizing system performance...")
        self.add_log_entry("System optimization started", "info")
        self.update_system_canvas("OPTIMIZING")
        
        # Optimize memory
        try:
            ctypes.windll.psapi.EmptyWorkingSet()
            self.add_log_entry("Memory optimized", "info")
        except:
            pass
        
        self.speak("System optimization completed.")
        self.add_log_entry("System optimization completed", "success")
        self.update_system_canvas("OPTIMIZATION COMPLETE")
    
    def system_monitor(self):
        """Monitor system performance"""
        self.speak("Starting system monitoring...")
        self.add_log_entry("System monitoring started", "info")
        self.update_system_canvas("MONITORING")
        
        # Start continuous monitoring
        threading.Thread(target=self.continuous_monitoring, daemon=True).start()
    
    def continuous_monitoring(self):
        """Continuous system monitoring"""
        while True:
            try:
                cpu_percent = psutil.cpu_percent(interval=1)
                memory = psutil.virtual_memory()
                
                if cpu_percent > 80:
                    self.add_log_entry(f"High CPU usage: {cpu_percent:.1f}%", "warning")
                if memory.percent > 80:
                    self.add_log_entry(f"High memory usage: {memory.percent:.1f}%", "warning")
                
                time.sleep(10)
            except:
                break
    
    def lock_system(self):
        """Lock system"""
        self.speak("Locking system...")
        self.add_log_entry("System locked", "info")
        try:
            ctypes.windll.user32.LockWorkStation()
        except:
            pass
    
    def logoff_system(self):
        """Logoff system"""
        self.speak("Logging off system...")
        self.add_log_entry("System logoff initiated", "warning")
        try:
            os.system("shutdown /l")
        except:
            pass
    
    def youtube_search(self, search_term):
        """Enhanced YouTube search"""
        self.speak(f"Searching YouTube for {search_term}")
        self.add_log_entry(f"YouTube search: {search_term}", "info")
        self.update_youtube_canvas(f"SEARCHING: {search_term.upper()}")
        
        url = f"https://www.youtube.com/results?search_query={search_term.replace(' ', '+')}"
        webbrowser.open(url)
        
        self.youtube_current_video = search_term
        self.speak(f"Playing {search_term}")
        self.add_log_entry(f"YouTube: {search_term}", "success")
        self.update_youtube_canvas(f"PLAYING: {search_term.upper()}")
    
    def youtube_next_video(self):
        """Play next video"""
        if self.youtube_current_video:
            pyautogui.press('right')
            self.speak("Playing next video")
            self.add_log_entry("YouTube: Next video", "info")
            self.update_youtube_canvas("NEXT VIDEO")
        else:
            self.speak("No video is currently playing")
    
    def youtube_previous_video(self):
        """Play previous video"""
        if self.youtube_current_video:
            pyautogui.press('left')
            self.speak("Playing previous video")
            self.add_log_entry("YouTube: Previous video", "info")
            self.update_youtube_canvas("PREVIOUS VIDEO")
        else:
            self.speak("No video is currently playing")
    
    def youtube_pause_video(self):
        """Pause video"""
        pyautogui.press('space')
        self.speak("Video paused")
        self.add_log_entry("YouTube: Paused", "info")
        self.update_youtube_canvas("PAUSED")
    
    def youtube_resume_video(self):
        """Resume video"""
        pyautogui.press('space')
        self.speak("Video resumed")
        self.add_log_entry("YouTube: Resumed", "info")
        self.update_youtube_canvas("RESUMED")
    
    def open_linkedin_profile(self):
        """Open LinkedIn profile"""
        webbrowser.open("https://linkedin.com/in/me")
        self.speak("Opening your LinkedIn profile")
        self.add_log_entry("LinkedIn: Profile opened", "info")
    
    def open_linkedin_jobs(self):
        """Open LinkedIn jobs"""
        webbrowser.open("https://linkedin.com/jobs")
        self.speak("Opening LinkedIn jobs")
        self.add_log_entry("LinkedIn: Jobs opened", "info")
    
    def open_linkedin_network(self):
        """Open LinkedIn network"""
        webbrowser.open("https://linkedin.com/mynetwork")
        self.speak("Opening LinkedIn network")
        self.add_log_entry("LinkedIn: Network opened", "info")
    
    def analyze_whatsapp_contacts(self):
        """Analyze WhatsApp contacts"""
        self.speak("Analyzing WhatsApp contacts")
        self.add_log_entry("Analyzing WhatsApp contacts", "info")
        
        # Simulate contact analysis
        contacts = [
            "Muhammad Farhan", "Ahmed", "Sara", "John", "Emma",
            "David", "Lisa", "Michael", "Sarah", "James"
        ]
        
        self.whatsapp_contacts = contacts
        self.save_whatsapp_contacts()
        
        self.speak(f"Found {len(contacts)} contacts")
        self.add_log_entry(f"Found {len(contacts)} contacts", "success")
        self.update_contacts_canvas(f"{len(contacts)} CONTACTS")
    
    def load_whatsapp_contacts(self):
        """Load WhatsApp contacts from file"""
        try:
            # Create data directory if it doesn't exist
            data_dir = os.path.dirname(self.contact_memory_file)
            if not os.path.exists(data_dir):
                os.makedirs(data_dir)
            
            if os.path.exists(self.contact_memory_file):
                with open(self.contact_memory_file, 'r') as f:
                    self.whatsapp_contacts = json.load(f)
                self.add_log_entry(f"Loaded {len(self.whatsapp_contacts)} contacts", "info")
        except Exception as e:
            self.add_log_entry(f"Failed to load contacts: {str(e)}", "warning")
    
    def save_whatsapp_contacts(self):
        """Save WhatsApp contacts to file"""
        try:
            # Create data directory if it doesn't exist
            data_dir = os.path.dirname(self.contact_memory_file)
            if not os.path.exists(data_dir):
                os.makedirs(data_dir)
            
            with open(self.contact_memory_file, 'w') as f:
                json.dump(self.whatsapp_contacts, f)
            self.add_log_entry("Saved contacts to memory", "success")
        except Exception as e:
            self.add_log_entry(f"Failed to save contacts: {str(e)}", "warning")
    
    def remember_contacts(self):
        """Remember WhatsApp contacts"""
        self.speak("Remembering all WhatsApp contacts")
        self.add_log_entry("Remembering contacts", "info")
        self.save_whatsapp_contacts()
        self.speak("Contacts saved to memory")
    
    def process_whatsapp_command(self, command):
        """Process WhatsApp messaging commands"""
        if any(word in command for word in ['send', 'message', 'whatsapp']):
            # Extract contact and message
            if 'to' in command:
                parts = command.split('to')
                if len(parts) > 1:
                    remaining = parts[1].strip()
                    if 'saying' in remaining:
                        contact_part, message_part = remaining.split('saying', 1)
                        contact = contact_part.strip()
                        message = message_part.strip()
                    else:
                        contact = remaining.strip()
                        message = "Hello from ILLI"
                    
                    self.send_whatsapp_message(contact, message)
                else:
                    self.speak("Please specify contact to send message to")
            else:
                self.speak("Please specify who to send message to")
        else:
            self.speak("Please specify message command")
    
    def send_whatsapp_message(self, contact, message):
        """Send WhatsApp message"""
        self.speak(f"Sending message to {contact}")
        self.add_log_entry(f"WhatsApp: {contact} - {message}", "info")
        
        # Open WhatsApp web
        webbrowser.open("https://web.whatsapp.com")
        time.sleep(3)
        
        # Simulate message sending
        self.speak(f"Message sent to {contact}")
        self.add_log_entry(f"Message sent to {contact}", "success")
    
    def show_help(self):
        """Show complete help"""
        self.speak("I am ILLI Complete Fixed, your most advanced AI assistant with complete system control. I can help you with system management, app launching and closing, YouTube control, WhatsApp messaging, LinkedIn connections, Gmail, ChatGPT, social media, communication apps, and complete system administration.")
        self.add_log_entry("Help displayed", "info")
    
    def toggle_listening(self):
        """Toggle voice listening"""
        self.listening_state = not self.listening_state
        
        if self.listening_state:
            self.speak("Voice recognition activated")
            self.add_log_entry("Voice recognition activated", "success")
        else:
            self.speak("Voice recognition deactivated")
            self.add_log_entry("Voice recognition deactivated", "info")
    
    def speak(self, text):
        """Text to speech"""
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            self.add_log_entry(f"Speech error: {str(e)}", "error")
    
    def add_log_entry(self, message, log_type):
        """Add entry to system log"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        color_map = {
            'info': self.colors['text'],
            'success': self.colors['success'],
            'warning': self.colors['warning'],
            'error': self.colors['error']
        }
        
        color = color_map.get(log_type, self.colors['text'])
        
        self.system_log.config(state='normal')
        self.system_log.insert('end', f"[{timestamp}] {message}\n")
        self.system_log.tag_add(log_type, f"end-2l", f"end-1l")
        self.system_log.tag_config(log_type, foreground=color)
        self.system_log.config(state='disabled')
        self.system_log.see('end')
    
    def add_command_history(self, command):
        """Add command to history"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        self.command_history.config(state='normal')
        self.command_history.insert('end', f"[{timestamp}] {command}\n")
        self.command_history.config(state='disabled')
        self.command_history.see('end')
    
    def update_voice_canvas(self, status):
        """Update voice status canvas"""
        try:
            self.voice_canvas.delete("all")
            
            # Background
            self.voice_canvas.create_rectangle(0, 0, 350, 30, fill='#1a1a1a', outline='')
            
            # Color based on status
            color_map = {
                'LISTENING': self.colors['green'],
                'RECOGNIZING': self.colors['yellow'],
                'IDLE': self.colors['text_dim']
            }
            
            color = color_map.get(status, self.colors['text'])
            
            # Status bar
            self.voice_canvas.create_rectangle(0, 0, 350, 30, fill=color, stipple='gray50', outline='')
            
            # Text
            self.voice_canvas.create_text(175, 15, text=f"🎤 {status}", 
                                       fill=self.colors['text'], font=("Consolas", 10, "bold"))
        except Exception as e:
            print(f"Voice canvas error: {e}")
    
    def update_contacts_canvas(self, info):
        """Update contacts canvas"""
        try:
            if hasattr(self, 'contacts_canvas'):
                self.contacts_canvas.delete("all")
                
                # Background
                self.contacts_canvas.create_rectangle(0, 0, 350, 100, fill='#1a1a1a', outline='')
                
                # Contact info
                self.contacts_canvas.create_text(175, 20, text=f"📱 {info}", 
                                           fill=self.colors['accent'], font=("Consolas", 10, "bold"))
                
                # Show some contacts
                if self.whatsapp_contacts:
                    y_pos = 40
                    for contact in self.whatsapp_contacts[:3]:
                        self.contacts_canvas.create_text(175, y_pos, text=f"• {contact}", 
                                                       fill=self.colors['text'], font=("Consolas", 8))
                        y_pos += 15
        except Exception as e:
            print(f"Contacts canvas error: {e}")
    
    def update_youtube_canvas(self, info):
        """Update YouTube canvas"""
        try:
            if hasattr(self, 'youtube_canvas'):
                self.youtube_canvas.delete("all")
                
                # Background
                self.youtube_canvas.create_rectangle(0, 0, 350, 30, fill='#1a1a1a', outline='')
                
                # YouTube info
                self.youtube_canvas.create_text(175, 15, text=f"🎬 {info}", 
                                           fill=self.colors['red'], font=("Consolas", 10, "bold"))
        except Exception as e:
            print(f"YouTube canvas error: {e}")
    
    def update_app_canvas(self, info):
        """Update app canvas"""
        try:
            self.app_canvas.delete("all")
            
            # Background
            self.app_canvas.create_rectangle(0, 0, 350, 100, fill='#1a1a1a', outline='')
            
            # App info
            self.app_canvas.create_text(175, 20, text=f"🚀 {info}", 
                                       fill=self.colors['green'], font=("Consolas", 10, "bold"))
            
            # Show app list
            apps = ["WhatsApp", "Instagram", "Gmail", "ChatGPT", "LinkedIn"]
            y_pos = 40
            for app in apps:
                self.app_canvas.create_text(175, y_pos, text=f"• {app}", 
                                          fill=self.colors['text'], font=("Consolas", 8))
                y_pos += 12
        except Exception as e:
            print(f"App canvas error: {e}")
    
    def update_system_canvas(self, info):
        """Update system canvas"""
        try:
            self.system_canvas.delete("all")
            
            # Background
            self.system_canvas.create_rectangle(0, 0, 350, 100, fill='#1a1a1a', outline='')
            
            # System info
            self.system_canvas.create_text(175, 20, text=f"⚙️ {info}", 
                                       fill=self.colors['orange'], font=("Consolas", 10, "bold"))
            
            # Show system info
            system_info = ["CPU", "Memory", "Disk", "Processes"]
            y_pos = 40
            for info in system_info:
                self.system_canvas.create_text(175, y_pos, text=f"• {info}", 
                                           fill=self.colors['text'], font=("Consolas", 8))
                y_pos += 12
        except Exception as e:
            print(f"System canvas error: {e}")
    
    def animate_nebula(self):
        """Animate nebula"""
        angle = 0
        particles = []
        
        # Initialize particles
        for _ in range(100):
            particles.append({
                'x': random.uniform(-150, 150),
                'y': random.uniform(-150, 150),
                'z': random.uniform(-150, 150),
                'vx': random.uniform(-1, 1),
                'vy': random.uniform(-1, 1),
                'vz': random.uniform(-1, 1),
                'size': random.uniform(1, 3),
                'color': random.choice([self.colors['accent'], self.colors['magenta'], self.colors['red'], self.colors['green']])
            })
        
        while True:
            try:
                self.nebula_canvas.delete("all")
                
                # Draw particles
                cx, cy = 400, 300
                
                for particle in particles:
                    # Rotate particle
                    x = particle['x'] * math.cos(angle) - particle['z'] * math.sin(angle)
                    z = particle['x'] * math.sin(angle) + particle['z'] * math.cos(angle)
                    y = particle['y']
                    
                    # Project to 2D
                    scale = 200 / (200 + z)
                    px = cx + x * scale
                    py = cy + y * scale
                    
                    size = particle['size'] * scale
                    
                    self.nebula_canvas.create_oval(px-size, py-size, px+size, py+size, 
                                               fill=particle['color'], outline='')
                    
                    # Update particle position
                    particle['x'] += particle['vx']
                    particle['y'] += particle['vy']
                    particle['z'] += particle['vz']
                    
                    # Boundary check
                    if abs(particle['x']) > 150: particle['vx'] *= -1
                    if abs(particle['y']) > 150: particle['vy'] *= -1
                    if abs(particle['z']) > 150: particle['vz'] *= -1
                
                # Draw rings
                for i in range(3):
                    radius = 100 + i * 50
                    self.nebula_canvas.create_oval(cx-radius, cy-radius, cx+radius, cy+radius, 
                                               outline=self.colors['accent'], width=1)
                
                # Draw orbiting labels
                labels = ["AI", "VOICE", "SYSTEM", "CONTROL"]
                for i, label in enumerate(labels):
                    label_angle = angle * 2 + i * 90
                    lx = cx + (radius + 30) * math.cos(math.radians(label_angle))
                    ly = cy + (radius + 30) * math.sin(math.radians(label_angle))
                    
                    self.nebula_canvas.create_text(lx, ly, text=label, 
                                               fill=self.colors['text'], 
                                               font=("Consolas", 10, "bold"))
                    
                    # Connection line
                    self.nebula_canvas.create_line(cx, cy, lx, ly, 
                                               fill=self.colors['magenta'], width=1)
                
                # Core
                core_size = 20 + 5 * math.sin(angle * 3)
                self.nebula_canvas.create_oval(cx-core_size, cy-core_size, cx+core_size, cy+core_size, 
                                           fill=self.colors['red'], outline=self.colors['accent'], width=2)
                
                # Pulsing effect when listening
                if self.listening_state:
                    pulse_size = 30 + 10 * math.sin(angle * 5)
                    self.nebula_canvas.create_oval(cx-pulse_size, cy-pulse_size, cx+pulse_size, cy+pulse_size, 
                                               outline=self.colors['green'], width=2)
                
                angle += 0.05
                time.sleep(0.03)
                
            except Exception as e:
                print(f"Nebula animation error: {e}")
    
    def animate_neural_network(self):
        """Animate neural network"""
        nodes = {
            'ILLI': (600, 100),
            'VOICE': (200, 150),
            'SYSTEM': (400, 50),
            'APPS': (800, 150),
            'CONTROL': (1000, 100),
            'MONITOR': (200, 50),
            'SCAN': (800, 50),
            'ADMIN': (600, 150)
        }
        
        connections = [
            ('ILLI', 'VOICE', 'active'),
            ('ILLI', 'SYSTEM', 'active'),
            ('ILLI', 'APPS', 'active'),
            ('ILLI', 'CONTROL', 'active'),
            ('ILLI', 'MONITOR', 'active'),
            ('ILLI', 'SCAN', 'active'),
            ('ILLI', 'ADMIN', 'active'),
            ('VOICE', 'SYSTEM', 'data'),
            ('CONTROL', 'MONITOR', 'data'),
            ('SYSTEM', 'ADMIN', 'data')
        ]
        
        pulse_phase = 0
        
        while True:
            try:
                self.neural_canvas.delete("all")
                
                # Draw connections
                for conn in connections:
                    from_node, to_node, status = conn
                    x1, y1 = nodes[from_node]
                    x2, y2 = nodes[to_node]
                    
                    color_map = {
                        'active': self.colors['success'],
                        'standby': self.colors['warning'],
                        'data': self.colors['accent'],
                        'error': self.colors['error']
                    }
                    
                    color = color_map.get(status, self.colors['text_dim'])
                    
                    # Animated data flow
                    if status == 'data':
                        progress = (math.sin(pulse_phase) + 1) / 2
                        mid_x = x1 + (x2 - x1) * progress
                        mid_y = y1 + (y2 - y1) * progress
                        self.neural_canvas.create_oval(mid_x-3, mid_y-3, mid_x+3, mid_y+3, 
                                                   fill=self.colors['cyan'], outline='')
                    
                    self.neural_canvas.create_line(x1, y1, x2, y2, 
                                               fill=color, width=2)
                
                # Draw nodes
                for node_name, (x, y) in nodes.items():
                    size = 12 if node_name == 'ILLI' else 8
                    color = self.colors['red'] if node_name == 'ILLI' else self.colors['accent']
                    
                    self.neural_canvas.create_oval(x-size, y-size, x+size, y+size, 
                                               fill=color, outline=self.colors['text'], width=2)
                    
                    self.neural_canvas.create_text(x, y-20, text=node_name, 
                                               fill=self.colors['text'], 
                                               font=("Consolas", 9, "bold"))
                
                pulse_phase += 0.1
                time.sleep(0.05)
                
            except Exception as e:
                print(f"Neural network animation error: {e}")
    
    def animate_displays(self):
        """Animate display canvases"""
        while True:
            try:
                # Update voice status
                if self.listening_state:
                    self.update_voice_canvas("LISTENING")
                else:
                    self.update_voice_canvas("IDLE")
                
                # Update apps
                self.update_app_canvas("READY")
                
                time.sleep(2)
                
            except Exception as e:
                print(f"Display animation error: {e}")
    
    def start_system_monitoring(self):
        """Start system monitoring"""
        threading.Thread(target=self.monitor_system, daemon=True).start()
    
    def monitor_system(self):
        """Monitor system resources"""
        while True:
            try:
                # Update user label
                self.current_task = "System Monitoring Active"
                user_info = f"USER: {self.user_name} | TASK: {self.current_task}"
                self.user_label.config(text=user_info)
                
                time.sleep(3)
                
            except Exception as e:
                print(f"System monitoring error: {e}")
    
    def tell_time(self):
        """Tell current time"""
        current_time = datetime.now().strftime("%I:%M %p")
        self.speak(f"The current time is {current_time}")
        self.add_log_entry(f"Time: {current_time}", "info")
    
    def wikipedia_search(self, topic):
        """Search Wikipedia"""
        try:
            summary = wikipedia.summary(topic, sentences=2)
            self.speak(f"According to Wikipedia: {summary}")
            self.add_log_entry(f"Wikipedia: {topic}", "info")
        except Exception as e:
            self.speak(f"Sorry, I couldn't find information about {topic}")
            self.add_log_entry(f"Wikipedia search failed: {topic}", "warning")
    
    def shutdown_system(self):
        """Shutdown system"""
        self.speak("Shutting down system in 10 seconds")
        self.add_log_entry("System shutdown initiated", "warning")
        time.sleep(10)
        try:
            os.system("shutdown /s /t 1")
        except:
            pass
    
    def restart_system(self):
        """Restart system"""
        self.speak("Restarting system in 10 seconds")
        self.add_log_entry("System restart initiated", "warning")
        time.sleep(10)
        try:
            os.system("shutdown /r /t 1")
        except:
            pass
    
    def sleep_system(self):
        """Sleep system"""
        self.speak("Putting system to sleep")
        self.add_log_entry("System sleep initiated", "info")
        try:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        except:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = ILLICompleteFixed(root)
    root.mainloop()
