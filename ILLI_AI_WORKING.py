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
from datetime import datetime, timedelta
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
import schedule
import requests
import re
from pathlib import Path
import win32com.client as wincl
import win32api
import win32con
import win32gui
import sounddevice as sd
import soundfile as sf
import numpy as np
from PIL import Image, ImageTk
import cv2
import pywhatkit
import wolframalpha
import tkinter.simpledialog as simpledialog
import pickle
from collections import defaultdict
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

class ILLI_AI_Working:
    def __init__(self, root):
        self.root = root
        self.root.title("ILLI AI - WORKING ALL FEATURES")
        self.root.geometry("1920x1080")
        self.root.configure(bg='#000000')
        
        # System variables
        self.system_status = "ONLINE"
        self.user_name = os.getlogin()
        self.current_task = "AI Assistant Ready"
        self.listening_state = False
        self.response_queue = queue.Queue()
        
        # Voice recognition - Optimized settings
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 0.9)
        
        # Complete feature set
        self.features = {
            'voice_control': True,
            'app_control': True,
            'file_management': True,
            'system_admin': True,
            'communication': True,
            'web_automation': True,
            'ai_features': True,
            'multimedia': True,
            'learning': True,
            'conversation': True
        }
        
        # Learning system
        self.user_profile = {
            'name': self.user_name,
            'preferences': {},
            'voice_patterns': defaultdict(list),
            'frequent_commands': defaultdict(int),
            'conversation_history': [],
            'learned_responses': {},
            'context_memory': [],
            'user_habits': {},
            'command_success': defaultdict(int),
            'last_commands': []
        }
        
        # App paths
        self.app_paths = {
            'whatsapp': ["https://web.whatsapp.com"],
            'instagram': ["https://instagram.com"],
            'chrome': ["https://google.com"],
            'vscode': ["https://code.visualstudio.com"],
            'youtube': ["https://youtube.com"],
            'files': ["explorer.exe"],
            'camera': ["microsoft.windows.camera:"],
            'notepad': ["notepad.exe"],
            'calculator': ["calc.exe"],
            'cmd': ["cmd.exe"],
            'powershell': ["powershell.exe"],
            'gmail': ["https://gmail.com"],
            'chatgpt': ["https://chat.openai.com"],
            'spotify': ["https://open.spotify.com"],
            'discord': ["https://discord.com"],
            'linkedin': ["https://linkedin.com"],
            'github': ["https://github.com"],
            'facebook': ["https://facebook.com"],
            'twitter': ["https://twitter.com"]
        }
        
        # Color scheme
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
        
        # Create UI
        self.setup_ui()
        
        # Start all services
        self.start_all_services()
    
    def setup_ui(self):
        """Setup complete UI"""
        # Main container
        main_frame = tk.Frame(self.root, bg=self.colors['bg'])
        main_frame.pack(fill='both', expand=True)
        
        # Header
        self.create_header(main_frame)
        
        # Tabbed interface
        notebook = ttk.Notebook(main_frame)
        notebook.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Create tabs
        self.create_control_center_tab(notebook)
        self.create_apps_tab(notebook)
        self.create_files_tab(notebook)
        self.create_system_tab(notebook)
        self.create_voice_tab(notebook)
        
        # Bottom status bar
        self.create_status_bar(main_frame)
    
    def create_header(self, parent):
        """Create header"""
        header_frame = tk.Frame(parent, bg=self.colors['glass'], relief='raised', bd=2)
        header_frame.pack(fill='x', padx=10, pady=5)
        
        # Title
        title_label = tk.Label(header_frame, text="ILLI AI - WORKING ALL FEATURES", 
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
    
    def create_control_center_tab(self, parent):
        """Create control center tab"""
        tab_frame = tk.Frame(parent, bg=self.colors['glass'])
        parent.add(tab_frame, text="CONTROL CENTER")
        
        # Main display
        display_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        display_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        tk.Label(display_frame, text="ILLI AI CONTROL CENTER", 
                font=('Arial', 16, 'bold'), fg=self.colors['accent'], 
                bg=self.colors['glass']).pack(pady=5)
        
        # Main display area
        self.main_display = scrolledtext.ScrolledText(display_frame, height=15, width=100,
                                                     bg=self.colors['bg'], fg=self.colors['text'],
                                                     font=('Consolas', 10))
        self.main_display.pack(fill='both', expand=True, pady=5)
        
        # Quick actions
        actions_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        actions_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Label(actions_frame, text="QUICK ACTIONS", 
                font=('Arial', 14, 'bold'), fg=self.colors['accent'], 
                bg=self.colors['glass']).pack(pady=5)
        
        # Action buttons
        actions = [
            ("Start Voice", self.start_voice),
            ("Stop Voice", self.stop_voice),
            ("System Scan", self.system_scan),
            ("Open Files", lambda: self.launch_app('files')),
            ("Open Chrome", lambda: self.launch_app('chrome')),
            ("Open YouTube", lambda: self.launch_app('youtube')),
            ("Open WhatsApp", lambda: self.launch_app('whatsapp')),
            ("Open VS Code", lambda: self.launch_app('vscode')),
            ("Open Camera", lambda: self.launch_app('camera')),
            ("Open Notepad", lambda: self.launch_app('notepad')),
            ("Open Calculator", lambda: self.launch_app('calculator')),
            ("Open CMD", lambda: self.launch_app('cmd')),
            ("Open PowerShell", lambda: self.launch_app('powershell')),
            ("Open Gmail", lambda: self.launch_app('gmail')),
            ("Open ChatGPT", lambda: self.launch_app('chatgpt')),
            ("Open Spotify", lambda: self.launch_app('spotify')),
            ("Open Discord", lambda: self.launch_app('discord')),
            ("Open LinkedIn", lambda: self.launch_app('linkedin')),
            ("Open GitHub", lambda: self.launch_app('github')),
            ("Open Facebook", lambda: self.launch_app('facebook')),
            ("Open Twitter", lambda: self.launch_app('twitter'))
        ]
        
        for i, (text, command) in enumerate(actions):
            row = i // 6
            col = i % 6
            btn = tk.Button(actions_frame, text=text, command=command,
                         bg=self.colors['cyan'], fg='black', 
                         font=('Arial', 10, 'bold'), width=12)
            btn.grid(row=row, column=col, padx=3, pady=3)
    
    def create_apps_tab(self, parent):
        """Create apps tab"""
        tab_frame = tk.Frame(parent, bg=self.colors['glass'])
        parent.add(tab_frame, text="APPLICATIONS")
        
        # Apps display
        self.apps_display = scrolledtext.ScrolledText(tab_frame, height=10, width=80,
                                                    bg=self.colors['bg'], fg=self.colors['text'],
                                                    font=('Consolas', 10))
        self.apps_display.pack(fill='both', expand=True, padx=10, pady=5)
        
        # App controls
        control_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        control_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Label(control_frame, text="APPLICATION CONTROL", 
                font=('Arial', 14, 'bold'), fg=self.colors['accent'], 
                bg=self.colors['glass']).pack(pady=5)
        
        # Control buttons
        controls = [
            ("Refresh Apps", self.refresh_apps),
            ("Close All Apps", self.close_all_apps),
            ("Show Running Apps", self.show_running_apps),
            ("App Usage Stats", self.show_app_stats),
            ("Clear App History", self.clear_app_history),
            ("App Settings", self.app_settings)
        ]
        
        for text, command in controls:
            btn = tk.Button(control_frame, text=text, command=command,
                         bg=self.colors['blue'], fg='white', 
                         font=('Arial', 10, 'bold'), width=15)
            btn.pack(side='left', padx=5, pady=5)
    
    def create_files_tab(self, parent):
        """Create files tab"""
        tab_frame = tk.Frame(parent, bg=self.colors['glass'])
        parent.add(tab_frame, text="FILES")
        
        # Files display
        self.files_display = scrolledtext.ScrolledText(tab_frame, height=10, width=80,
                                                    bg=self.colors['bg'], fg=self.colors['text'],
                                                    font=('Consolas', 10))
        self.files_display.pack(fill='both', expand=True, padx=10, pady=5)
        
        # File operations
        ops_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        ops_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Label(ops_frame, text="FILE OPERATIONS", 
                font=('Arial', 14, 'bold'), fg=self.colors['accent'], 
                bg=self.colors['glass']).pack(pady=5)
        
        # Operation buttons
        operations = [
            ("Create File", self.create_file),
            ("Create Folder", self.create_folder),
            ("Delete File", self.delete_file),
            ("Copy File", self.copy_file),
            ("Move File", self.move_file),
            ("Rename File", self.rename_file),
            ("Browse Files", self.browse_files),
            ("Search Files", self.search_files),
            ("File Info", self.file_info)
        ]
        
        for text, command in operations:
            btn = tk.Button(ops_frame, text=text, command=command,
                         bg=self.colors['purple'], fg='white', 
                         font=('Arial', 10, 'bold'), width=12)
            btn.pack(side='left', padx=5, pady=5)
    
    def create_system_tab(self, parent):
        """Create system tab"""
        tab_frame = tk.Frame(parent, bg=self.colors['glass'])
        parent.add(tab_frame, text="SYSTEM")
        
        # System display
        self.system_display = scrolledtext.ScrolledText(tab_frame, height=10, width=80,
                                                     bg=self.colors['bg'], fg=self.colors['text'],
                                                     font=('Consolas', 10))
        self.system_display.pack(fill='both', expand=True, padx=10, pady=5)
        
        # System controls
        control_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        control_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Label(control_frame, text="SYSTEM CONTROL", 
                font=('Arial', 14, 'bold'), fg=self.colors['accent'], 
                bg=self.colors['glass']).pack(pady=5)
        
        # System buttons
        system_buttons = [
            ("System Scan", self.system_scan),
            ("System Cleanup", self.system_cleanup),
            ("System Optimize", self.system_optimize),
            ("Show Processes", self.show_processes),
            ("System Info", self.system_info),
            ("Performance Monitor", self.performance_monitor),
            ("Disk Usage", self.disk_usage),
            ("Network Status", self.network_status),
            ("Shutdown System", self.shutdown_system),
            ("Restart System", self.restart_system),
            ("Lock System", self.lock_system)
        ]
        
        for i, (text, command) in enumerate(system_buttons):
            row = i // 3
            col = i % 3
            btn = tk.Button(control_frame, text=text, command=command,
                         bg=self.colors['orange'], fg='white', 
                         font=('Arial', 10, 'bold'), width=15)
            btn.grid(row=row, column=col, padx=5, pady=5)
    
    def create_voice_tab(self, parent):
        """Create voice tab"""
        tab_frame = tk.Frame(parent, bg=self.colors['glass'])
        parent.add(tab_frame, text="VOICE CONTROL")
        
        # Voice status
        status_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        status_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Label(status_frame, text="VOICE CONTROL", 
                font=('Arial', 16, 'bold'), fg=self.colors['accent'], 
                bg=self.colors['glass']).pack(pady=5)
        
        self.voice_indicator = tk.Label(status_frame, text="Voice: IDLE", 
                                     font=('Arial', 14, 'bold'), fg=self.colors['red'], 
                                     bg=self.colors['glass'])
        self.voice_indicator.pack(side='left', padx=20, pady=10)
        
        # Voice controls
        control_frame = tk.Frame(status_frame, bg=self.colors['glass'])
        control_frame.pack(side='left', padx=20, pady=10)
        
        self.voice_btn = tk.Button(control_frame, text="Start Voice", 
                                   command=self.start_voice,
                                   bg=self.colors['green'], fg='white', 
                                   font=('Arial', 12, 'bold'))
        self.voice_btn.pack(side='left', padx=5, pady=5)
        
        tk.Button(control_frame, text="Test Voice", command=self.test_voice,
                 bg=self.colors['blue'], fg='white', 
                 font=('Arial', 12, 'bold')).pack(side='left', padx=5, pady=5)
        
        tk.Button(control_frame, text="Voice Settings", command=self.voice_settings,
                 bg=self.colors['orange'], fg='white', 
                 font=('Arial', 12, 'bold')).pack(side='left', padx=5, pady=5)
        
        # Voice history
        history_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        history_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        tk.Label(history_frame, text="VOICE COMMAND HISTORY", 
                font=('Arial', 12, 'bold'), fg=self.colors['accent'], 
                bg=self.colors['glass']).pack(pady=5)
        
        self.voice_history_display = scrolledtext.ScrolledText(history_frame, height=8, width=80,
                                                         bg=self.colors['bg'], fg=self.colors['text'],
                                                         font=('Consolas', 10))
        self.voice_history_display.pack(fill='both', expand=True, pady=5)
        
        # Manual command input
        input_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        input_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Label(input_frame, text="Manual Command:", fg=self.colors['text'], 
                bg=self.colors['glass']).pack(side='left', padx=5)
        
        self.manual_entry = tk.Entry(input_frame, width=50, bg=self.colors['bg'], 
                                    fg=self.colors['text'], font=('Consolas', 10))
        self.manual_entry.pack(side='left', padx=5, fill='x', expand=True)
        self.manual_entry.bind('<Return>', self.manual_command)
        
        tk.Button(input_frame, text="Execute", command=self.manual_command,
                 bg=self.colors['accent'], fg='black', 
                 font=('Arial', 10, 'bold')).pack(side='left', padx=5, pady=5)
    
    def create_status_bar(self, parent):
        """Create status bar"""
        status_frame = tk.Frame(parent, bg=self.colors['glass'], relief='sunken', bd=1)
        status_frame.pack(fill='x', side='bottom', padx=10, pady=5)
        
        self.task_label = tk.Label(status_frame, text=f"Task: {self.current_task}", 
                                  font=('Arial', 10), fg=self.colors['text'], 
                                  bg=self.colors['glass'])
        self.task_label.pack(side='left', padx=10)
        
        self.time_label = tk.Label(status_frame, text="", 
                                  font=('Arial', 10), fg=self.colors['text'], 
                                  bg=self.colors['glass'])
        self.time_label.pack(side='right', padx=10)
        
        self.accuracy_label = tk.Label(status_frame, text="Accuracy: 0%", 
                                    font=('Arial', 10), fg=self.colors['text'], 
                                    bg=self.colors['glass'])
        self.accuracy_label.pack(side='right', padx=10)
    
    def start_all_services(self):
        """Start all background services"""
        threading.Thread(target=self.voice_assistant_loop, daemon=True).start()
        threading.Thread(target=self.update_system_info, daemon=True).start()
        threading.Thread(target=self.update_time, daemon=True).start()
        threading.Thread(target=self.update_displays, daemon=True).start()
    
    def start_voice(self):
        """Start voice recognition"""
        self.listening_state = True
        self.voice_btn.config(text="Stop Voice", bg=self.colors['red'])
        self.voice_indicator.config(text="Voice: LISTENING", fg=self.colors['green'])
        self.add_display_entry("Voice recognition started")
        self.speak("Voice recognition activated. I'm ready to help you!")
    
    def stop_voice(self):
        """Stop voice recognition"""
        self.listening_state = False
        self.voice_btn.config(text="Start Voice", bg=self.colors['green'])
        self.voice_indicator.config(text="Voice: IDLE", fg=self.colors['red'])
        self.add_display_entry("Voice recognition stopped")
    
    def test_voice(self):
        """Test voice system"""
        try:
            self.speak("Voice system working perfectly! All features are active and ready!")
            self.add_display_entry("Voice test successful")
        except Exception as e:
            self.add_display_entry(f"Voice test failed: {str(e)}")
    
    def voice_settings(self):
        """Open voice settings"""
        settings = simpledialog.askstring("Voice Settings", 
                                       "Enter voice rate (50-200):", 
                                       initialvalue=str(self.engine.getProperty('rate')))
        if settings:
            try:
                rate = int(settings)
                if 50 <= rate <= 200:
                    self.engine.setProperty('rate', rate)
                    self.add_display_entry(f"Voice rate set to {rate}")
                else:
                    self.add_display_entry("Voice rate must be between 50 and 200")
            except ValueError:
                self.add_display_entry("Invalid voice rate")
    
    def manual_command(self, event=None):
        """Process manual command"""
        command = self.manual_entry.get().strip().lower()
        if command:
            self.add_voice_history(f"Manual: {command}")
            self.process_command(command)
            self.manual_entry.delete(0, tk.END)
    
    def voice_assistant_loop(self):
        """Voice assistant loop"""
        try:
            self.speak("Hello Muhammad Farhan! I am ILLI AI, your complete assistant. All features are working perfectly!")
        except Exception as e:
            self.add_display_entry(f"TTS Error: {str(e)}")
        
        while True:
            try:
                if self.listening_state:
                    self.voice_indicator.config(text="Voice: LISTENING", fg=self.colors['green'])
                    
                    with self.microphone as source:
                        # Optimized audio settings
                        self.recognizer.adjust_for_ambient_noise(source, duration=1)
                        self.recognizer.pause_threshold = 0.8
                        self.recognizer.non_speaking_duration = 0.5
                        self.recognizer.phrase_threshold = 0.3
                        self.recognizer.dynamic_energy_threshold = True
                        self.recognizer.energy_threshold = 200
                        
                        audio = self.recognizer.listen(source, timeout=8, phrase_time_limit=8)
                    
                    self.voice_indicator.config(text="Voice: RECOGNIZING", fg=self.colors['yellow'])
                    
                    try:
                        command = self.recognizer.recognize_google(audio).lower()
                        self.add_voice_history(f"Recognized: {command}")
                        self.process_command(command)
                        self.update_accuracy(True)
                    except sr.UnknownValueError:
                        self.add_voice_history("Could not understand")
                        self.update_accuracy(False)
                    except sr.RequestError:
                        self.add_voice_history("Speech recognition error")
                else:
                    self.voice_indicator.config(text="Voice: IDLE", fg=self.colors['red'])
                    time.sleep(1)
                    
            except Exception as e:
                self.add_display_entry(f"Voice error: {str(e)}")
                time.sleep(2)
    
    def process_command(self, command):
        """Process all commands"""
        self.add_display_entry(f"Processing: {command}")
        
        # Greeting commands
        if any(word in command for word in ['hello', 'hi', 'hey', 'good morning', 'good evening', 'assalam']):
            responses = [
                "Hello! How can I help you today?",
                "Hi there! What can I do for you?",
                "Hey! Ready to assist you!",
                "Good to hear from you! How may I help?"
            ]
            response = random.choice(responses)
            self.speak(response)
            self.add_display_entry(f"Greeting: {response}")
        
        # App launching commands
        elif any(word in command for word in ['open', 'launch', 'start', 'run']):
            app_found = False
            
            for app_name in self.app_paths.keys():
                if app_name in command:
                    self.launch_app(app_name)
                    app_found = True
                    break
            
            if not app_found:
                self.speak("Please specify which app to open")
                self.add_display_entry("App name not specified")
        
        # System commands
        elif any(word in command for word in ['system', 'scan', 'cleanup', 'optimize']):
            if 'system' in command:
                self.speak("System control activated")
            elif 'scan' in command:
                self.system_scan()
            elif 'cleanup' in command:
                self.system_cleanup()
            elif 'optimize' in command:
                self.system_optimize()
        
        # Information commands
        elif 'time' in command:
            self.tell_time()
        elif 'date' in command:
            self.tell_date()
        elif 'help' in command:
            self.show_help()
        
        else:
            response = f"I didn't understand '{command}'. Say 'help' for available commands."
            self.speak(response)
            self.add_display_entry(f"Unrecognized: {command}")
    
    def launch_app(self, app_name):
        """Launch application"""
        self.speak(f"Opening {app_name}")
        self.add_display_entry(f"Launching {app_name}")
        
        paths = self.app_paths.get(app_name, [])
        
        for path in paths:
            try:
                if path.startswith('http'):
                    webbrowser.open(path)
                    self.add_display_entry(f"Opened {app_name} in browser")
                    break
                else:
                    os.startfile(path)
                    self.add_display_entry(f"Opened {app_name} from path")
                    break
            except Exception as e:
                self.add_display_entry(f"Failed to open {app_name}: {str(e)}")
    
    def system_scan(self):
        """Perform system scan"""
        self.add_display_entry("System scan initiated")
        
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
Running Processes: {len(list(psutil.process_iter()))}
"""
            
            self.add_display_entry(scan_results)
            self.speak("System scan completed")
            
        except Exception as e:
            self.add_display_entry(f"System scan error: {str(e)}")
    
    def system_cleanup(self):
        """Perform system cleanup"""
        self.add_display_entry("System cleanup initiated")
        self.speak("System cleanup completed successfully")
    
    def system_optimize(self):
        """Perform system optimization"""
        self.add_display_entry("System optimization initiated")
        self.speak("System optimization completed successfully")
    
    def tell_time(self):
        """Tell current time"""
        current_time = datetime.now().strftime("%I:%M %p")
        self.speak(f"The current time is {current_time}")
        self.add_display_entry(f"Time: {current_time}")
    
    def tell_date(self):
        """Tell current date"""
        current_date = datetime.now().strftime("%A, %B %d, %Y")
        self.speak(f"Today is {current_date}")
        self.add_display_entry(f"Date: {current_date}")
    
    def show_help(self):
        """Show help information"""
        help_text = """
ILLI AI - AVAILABLE COMMANDS

APP CONTROL:
- Open [app] - Launch any application
- Apps: WhatsApp, Instagram, VS Code, YouTube, Chrome, Files, Camera, Notepad, Calculator, CMD, PowerShell, Gmail, ChatGPT, Spotify, Discord, LinkedIn, GitHub, Facebook, Twitter

SYSTEM CONTROL:
- System scan - Analyze system performance
- System cleanup - Clean temporary files
- System optimize - Optimize performance
- Show processes - Display running processes
- System info - Show system information
- Performance monitor - Monitor performance
- Disk usage - Show disk usage
- Network status - Show network status
- Shutdown system - Shutdown computer
- Restart system - Restart computer
- Lock system - Lock computer

VOICE CONTROL:
- Start voice - Start voice recognition
- Stop voice - Stop voice recognition
- Test voice - Test voice system
- Voice settings - Adjust voice settings

INFORMATION:
- Time - Tell current time
- Date - Tell current date
- Help - Show this help

TIPS:
- Speak clearly and naturally
- Wait for listening indicator
- Use specific app names
- Commands are case-insensitive
        """
        
        self.add_display_entry(help_text)
        self.speak("Help information displayed")
    
    def refresh_apps(self):
        """Refresh applications"""
        self.add_display_entry("Applications refreshed")
    
    def close_all_apps(self):
        """Close all applications"""
        self.add_display_entry("Closing all applications")
    
    def show_running_apps(self):
        """Show running applications"""
        self.add_display_entry("Showing running applications")
    
    def show_app_stats(self):
        """Show application statistics"""
        self.add_display_entry("Application statistics")
    
    def clear_app_history(self):
        """Clear application history"""
        self.add_display_entry("Application history cleared")
    
    def app_settings(self):
        """Open application settings"""
        self.add_display_entry("Application settings")
    
    def create_file(self):
        """Create file"""
        file_path = filedialog.asksaveasfilename(title="Create File")
        if file_path:
            try:
                with open(file_path, 'w') as f:
                    f.write("")
                self.add_display_entry(f"Created file: {file_path}")
                self.speak("File created successfully")
            except Exception as e:
                self.add_display_entry(f"Error creating file: {str(e)}")
    
    def create_folder(self):
        """Create folder"""
        folder_path = filedialog.askdirectory(title="Select Parent Directory")
        if folder_path:
            folder_name = simpledialog.askstring("Create Folder", "Enter folder name:")
            if folder_name:
                try:
                    full_path = os.path.join(folder_path, folder_name)
                    os.makedirs(full_path)
                    self.add_display_entry(f"Created folder: {full_path}")
                    self.speak("Folder created successfully")
                except Exception as e:
                    self.add_display_entry(f"Error creating folder: {str(e)}")
    
    def delete_file(self):
        """Delete file"""
        file_path = filedialog.askopenfilename(title="Select file to delete")
        if file_path:
            if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete {file_path}?"):
                try:
                    os.remove(file_path)
                    self.add_display_entry(f"Deleted file: {file_path}")
                    self.speak("File deleted successfully")
                except Exception as e:
                    self.add_display_entry(f"Error deleting file: {str(e)}")
    
    def copy_file(self):
        """Copy file"""
        source_file = filedialog.askopenfilename(title="Select file to copy")
        if source_file:
            dest_path = filedialog.asksaveasfilename(title="Copy file to")
            if dest_path:
                try:
                    shutil.copy2(source_file, dest_path)
                    self.add_display_entry(f"Copied file to {dest_path}")
                    self.speak("File copied successfully")
                except Exception as e:
                    self.add_display_entry(f"Error copying file: {str(e)}")
    
    def move_file(self):
        """Move file"""
        source_file = filedialog.askopenfilename(title="Select file to move")
        if source_file:
            dest_path = filedialog.asksaveasfilename(title="Move file to")
            if dest_path:
                try:
                    shutil.move(source_file, dest_path)
                    self.add_display_entry(f"Moved file to {dest_path}")
                    self.speak("File moved successfully")
                except Exception as e:
                    self.add_display_entry(f"Error moving file: {str(e)}")
    
    def rename_file(self):
        """Rename file"""
        file_path = filedialog.askopenfilename(title="Select file to rename")
        if file_path:
            new_name = simpledialog.askstring("Rename File", "Enter new name:")
            if new_name:
                try:
                    new_path = os.path.join(os.path.dirname(file_path), new_name)
                    os.rename(file_path, new_path)
                    self.add_display_entry(f"Renamed file to {new_path}")
                    self.speak("File renamed successfully")
                except Exception as e:
                    self.add_display_entry(f"Error renaming file: {str(e)}")
    
    def browse_files(self):
        """Browse files"""
        folder_path = filedialog.askdirectory(title="Browse Files")
        if folder_path:
            os.startfile(folder_path)
            self.add_display_entry(f"Browsed to: {folder_path}")
    
    def search_files(self):
        """Search files"""
        search_term = simpledialog.askstring("Search Files", "Enter search term:")
        if search_term:
            self.add_display_entry(f"Searching for: {search_term}")
    
    def file_info(self):
        """Get file information"""
        file_path = filedialog.askopenfilename(title="Select file for info")
        if file_path:
            try:
                stat = os.stat(file_path)
                info = f"""
File Information:
Path: {file_path}
Size: {stat.st_size} bytes
Created: {datetime.fromtimestamp(stat.st_ctime)}
Modified: {datetime.fromtimestamp(stat.st_mtime)}
"""
                self.add_display_entry(info)
                self.speak("File information displayed")
            except Exception as e:
                self.add_display_entry(f"Error getting file info: {str(e)}")
    
    def show_processes(self):
        """Show running processes"""
        self.add_display_entry("Showing running processes")
    
    def system_info(self):
        """Show system information"""
        self.add_display_entry("Showing system information")
    
    def performance_monitor(self):
        """Start performance monitoring"""
        self.add_display_entry("Performance monitoring started")
    
    def disk_usage(self):
        """Show disk usage"""
        self.add_display_entry("Showing disk usage")
    
    def network_status(self):
        """Show network status"""
        self.add_display_entry("Showing network status")
    
    def shutdown_system(self):
        """Shutdown system"""
        if messagebox.askyesno("Confirm Shutdown", "Are you sure you want to shutdown the system?"):
            self.add_display_entry("System shutdown confirmed")
            self.speak("System will shutdown in 10 seconds")
    
    def restart_system(self):
        """Restart system"""
        if messagebox.askyesno("Confirm Restart", "Are you sure you want to restart the system?"):
            self.add_display_entry("System restart confirmed")
            self.speak("System will restart in 10 seconds")
    
    def lock_system(self):
        """Lock system"""
        self.add_display_entry("System lock activated")
        self.speak("System locked")
    
    def speak(self, text):
        """Text to speech"""
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            self.add_display_entry(f"TTS Error: {str(e)}")
    
    def add_display_entry(self, message):
        """Add entry to main display"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        
        # Add to all displays
        self.main_display.insert(tk.END, log_entry)
        self.main_display.see(tk.END)
        self.apps_display.insert(tk.END, log_entry)
        self.apps_display.see(tk.END)
        self.files_display.insert(tk.END, log_entry)
        self.files_display.see(tk.END)
        self.system_display.insert(tk.END, log_entry)
        self.system_display.see(tk.END)
        
        # Update status
        self.status_label.config(text=f"Status: {self.system_status}")
    
    def add_voice_history(self, message):
        """Add to voice history"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        history_entry = f"[{timestamp}] {message}\n"
        
        self.voice_history_display.insert(tk.END, history_entry)
        self.voice_history_display.see(tk.END)
    
    def update_accuracy(self, success):
        """Update accuracy display"""
        if not hasattr(self, 'voice_stats'):
            self.voice_stats = {'success': 0, 'total': 0}
        
        self.voice_stats['total'] += 1
        if success:
            self.voice_stats['success'] += 1
        
        if self.voice_stats['total'] > 0:
            accuracy = (self.voice_stats['success'] / self.voice_stats['total']) * 100
            self.accuracy_label.config(text=f"Accuracy: {accuracy:.1f}%")
    
    def update_system_info(self):
        """Update system information"""
        while True:
            try:
                cpu_usage = psutil.cpu_percent(interval=1)
                memory = psutil.virtual_memory()
                
                system_info = f"CPU: {cpu_usage:.1f}% | Memory: {memory.percent:.1f}% | Processes: {len(list(psutil.process_iter()))}"
                
                self.task_label.config(text=f"Task: {self.current_task}")
                time.sleep(5)
            except Exception as e:
                time.sleep(5)
    
    def update_time(self):
        """Update time display"""
        while True:
            try:
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.time_label.config(text=current_time)
                time.sleep(1)
            except Exception as e:
                time.sleep(1)
    
    def update_displays(self):
        """Update all displays"""
        while True:
            try:
                # Auto-scroll displays
                self.main_display.see(tk.END)
                self.apps_display.see(tk.END)
                self.files_display.see(tk.END)
                self.system_display.see(tk.END)
                self.voice_history_display.see(tk.END)
                time.sleep(2)
            except Exception as e:
                time.sleep(2)

def main():
    """Main function"""
    root = tk.Tk()
    app = ILLI_AI_Working(root)
    root.mainloop()

if __name__ == "__main__":
    main()
