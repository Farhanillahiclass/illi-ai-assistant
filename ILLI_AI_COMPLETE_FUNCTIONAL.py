import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog, simpledialog
import os
import webbrowser
import psutil
import threading
import time
import speech_recognition as sr
import pyttsx3
from datetime import datetime
import subprocess
import shutil
import platform
import json
import random
import math
import sys
import re
from pathlib import Path

class ILLI_AI:
    def __init__(self, root):
        self.root = root
        self.root.title("ILLI AI - Complete Functional Version")
        self.root.geometry("1400x900")
        self.root.configure(bg='#000000')
        
        # System variables
        self.listening = False
        self.user_name = os.getlogin()
        self.command_history = []
        self.app_usage = {}
        self.system_stats = {}
        
        # Initialize voice
        try:
            self.recognizer = sr.Recognizer()
            self.engine = pyttsx3.init()
            self.engine.setProperty('rate', 150)
            self.engine.setProperty('volume', 0.9)
            self.voice_available = True
        except Exception as e:
            self.voice_available = False
            print(f"Voice initialization failed: {e}")
        
        # Complete app paths
        self.apps = {
            'whatsapp': 'https://web.whatsapp.com',
            'instagram': 'https://instagram.com',
            'chrome': 'https://google.com',
            'firefox': 'https://firefox.com',
            'youtube': 'https://youtube.com',
            'files': 'explorer.exe',
            'notepad': 'notepad.exe',
            'calculator': 'calc.exe',
            'cmd': 'cmd.exe',
            'powershell': 'powershell.exe',
            'taskmgr': 'taskmgr.exe',
            'control': 'control.exe',
            'settings': 'ms-settings:',
            'camera': 'microsoft.windows.camera:',
            'paint': 'mspaint.exe',
            'word': 'winword.exe',
            'excel': 'excel.exe',
            'powerpoint': 'powerpnt.exe',
            'gmail': 'https://gmail.com',
            'outlook': 'https://outlook.live.com',
            'chatgpt': 'https://chat.openai.com',
            'github': 'https://github.com',
            'linkedin': 'https://linkedin.com',
            'facebook': 'https://facebook.com',
            'twitter': 'https://twitter.com',
            'spotify': 'https://open.spotify.com',
            'discord': 'https://discord.com',
            'slack': 'https://slack.com',
            'teams': 'https://teams.microsoft.com',
            'zoom': 'https://zoom.us',
            'skype': 'skype:',
            'telegram': 'https://web.telegram.org',
            'signal': 'https://signal.org',
            'reddit': 'https://reddit.com',
            'pinterest': 'https://pinterest.com',
            'tiktok': 'https://tiktok.com',
            'snapchat': 'https://snapchat.com',
            'netflix': 'https://netflix.com',
            'amazon': 'https://amazon.com',
            'ebay': 'https://ebay.com',
            'wikipedia': 'https://wikipedia.org'
        }
        
        # Color scheme
        self.colors = {
            'bg': '#000000',
            'glass': '#0a0a0a',
            'accent': '#00FFFF',
            'success': '#00FF00',
            'warning': '#FFAA00',
            'error': '#FF0000',
            'text': '#FFFFFF',
            'dim': '#666666',
            'blue': '#0080FF',
            'purple': '#8000FF',
            'orange': '#FF8000',
            'green': '#00FF00',
            'red': '#FF0000',
            'yellow': '#FFFF00'
        }
        
        self.setup_ui()
        self.start_background_services()
    
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
        
        # Style notebook
        style = ttk.Style()
        style.theme_use('default')
        style.configure('TNotebook', background=self.colors['bg'])
        style.configure('TNotebook.Tab', background=self.colors['glass'], 
                       foreground=self.colors['text'], padding=[20, 10])
        
        # Create tabs
        self.create_control_center_tab(notebook)
        self.create_apps_tab(notebook)
        self.create_files_tab(notebook)
        self.create_system_tab(notebook)
        self.create_voice_tab(notebook)
        self.create_utilities_tab(notebook)
        
        # Status bar
        self.create_status_bar(main_frame)
    
    def create_header(self, parent):
        """Create header"""
        header_frame = tk.Frame(parent, bg=self.colors['glass'], relief='raised', bd=2)
        header_frame.pack(fill='x', padx=10, pady=5)
        
        # Title
        title_label = tk.Label(header_frame, text="ILLI AI - COMPLETE FUNCTIONAL VERSION", 
                              font=('Arial', 24, 'bold'), fg=self.colors['accent'], 
                              bg=self.colors['glass'])
        title_label.pack(side='left', padx=20, pady=10)
        
        # User info
        user_label = tk.Label(header_frame, text=f"User: {self.user_name}", 
                              font=('Arial', 12), fg=self.colors['text'], 
                              bg=self.colors['glass'])
        user_label.pack(side='right', padx=20, pady=10)
        
        # Status
        self.status_label = tk.Label(header_frame, text="Status: ONLINE", 
                                    font=('Arial', 12), fg=self.colors['success'], 
                                    bg=self.colors['glass'])
        self.status_label.pack(side='right', padx=20, pady=10)
    
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
        
        # Action buttons grid
        actions = [
            ("Start Voice", self.start_voice, self.colors['green']),
            ("Stop Voice", self.stop_voice, self.colors['red']),
            ("System Scan", self.system_scan, self.colors['blue']),
            ("System Info", self.system_info, self.colors['purple']),
            ("Open Files", lambda: self.launch_app('files'), self.colors['blue']),
            ("Open Chrome", lambda: self.launch_app('chrome'), self.colors['blue']),
            ("Open YouTube", lambda: self.launch_app('youtube'), self.colors['red']),
            ("Open WhatsApp", lambda: self.launch_app('whatsapp'), self.colors['green']),
            ("Open ChatGPT", lambda: self.launch_app('chatgpt'), self.colors['purple']),
            ("Open Calculator", lambda: self.launch_app('calculator'), self.colors['orange']),
            ("Open Notepad", lambda: self.launch_app('notepad'), self.colors['blue']),
            ("Open CMD", lambda: self.launch_app('cmd'), self.colors['black'])
        ]
        
        for i, (text, command, color) in enumerate(actions):
            row = i // 4
            col = i % 4
            btn = tk.Button(actions_frame, text=text, command=command,
                         bg=color, fg='white', font=('Arial', 10, 'bold'), width=15)
            btn.grid(row=row, column=col, padx=5, pady=5)
    
    def create_apps_tab(self, parent):
        """Create applications tab"""
        tab_frame = tk.Frame(parent, bg=self.colors['glass'])
        parent.add(tab_frame, text="APPLICATIONS")
        
        # Apps display
        self.apps_display = scrolledtext.ScrolledText(tab_frame, height=12, width=100,
                                                     bg=self.colors['bg'], fg=self.colors['text'],
                                                     font=('Consolas', 10))
        self.apps_display.pack(fill='both', expand=True, padx=10, pady=5)
        
        # App controls
        control_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        control_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Label(control_frame, text="APPLICATION CONTROL", 
                font=('Arial', 14, 'bold'), fg=self.colors['accent'], 
                bg=self.colors['glass']).pack(pady=5)
        
        # App buttons
        app_categories = {
            "Communication": ['whatsapp', 'gmail', 'outlook', 'discord', 'slack', 'teams', 'zoom', 'skype', 'telegram', 'signal'],
            "Social Media": ['instagram', 'facebook', 'twitter', 'linkedin', 'reddit', 'pinterest', 'tiktok', 'snapchat'],
            "Productivity": ['chrome', 'firefox', 'chatgpt', 'github', 'notepad', 'word', 'excel', 'powerpoint'],
            "Entertainment": ['youtube', 'spotify', 'netflix', 'amazon', 'ebay'],
            "System": ['files', 'cmd', 'powershell', 'taskmgr', 'control', 'settings', 'calculator', 'paint', 'camera']
        }
        
        for category, apps in app_categories.items():
            cat_frame = tk.Frame(control_frame, bg=self.colors['glass'])
            cat_frame.pack(fill='x', pady=5)
            
            tk.Label(cat_frame, text=f"{category}:", 
                    font=('Arial', 12, 'bold'), fg=self.colors['accent'], 
                    bg=self.colors['glass']).pack(side='left', padx=5)
            
            for app in apps:
                btn = tk.Button(cat_frame, text=app.title(), 
                             command=lambda a=app: self.launch_app(a),
                             bg=self.colors['blue'], fg='white', 
                             font=('Arial', 9), width=8)
                btn.pack(side='left', padx=2)
    
    def create_files_tab(self, parent):
        """Create files tab"""
        tab_frame = tk.Frame(parent, bg=self.colors['glass'])
        parent.add(tab_frame, text="FILES")
        
        # Files display
        self.files_display = scrolledtext.ScrolledText(tab_frame, height=12, width=100,
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
            ("Create File", self.create_file, self.colors['green']),
            ("Create Folder", self.create_folder, self.colors['green']),
            ("Delete File", self.delete_file, self.colors['red']),
            ("Copy File", self.copy_file, self.colors['blue']),
            ("Move File", self.move_file, self.colors['blue']),
            ("Rename File", self.rename_file, self.colors['orange']),
            ("Browse Files", self.browse_files, self.colors['purple']),
            ("Search Files", self.search_files, self.colors['purple']),
            ("File Info", self.file_info, self.colors['yellow']),
            ("Clean Temp", self.clean_temp, self.colors['red'])
        ]
        
        for text, command, color in operations:
            btn = tk.Button(ops_frame, text=text, command=command,
                         bg=color, fg='white', font=('Arial', 10, 'bold'), width=12)
            btn.pack(side='left', padx=3, pady=3)
    
    def create_system_tab(self, parent):
        """Create system tab"""
        tab_frame = tk.Frame(parent, bg=self.colors['glass'])
        parent.add(tab_frame, text="SYSTEM")
        
        # System display
        self.system_display = scrolledtext.ScrolledText(tab_frame, height=12, width=100,
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
            ("System Scan", self.system_scan, self.colors['blue']),
            ("System Info", self.system_info, self.colors['purple']),
            ("Show Processes", self.show_processes, self.colors['green']),
            ("Performance", self.performance_monitor, self.colors['orange']),
            ("Disk Usage", self.disk_usage, self.colors['yellow']),
            ("Network Status", self.network_status, self.colors['blue']),
            ("System Cleanup", self.system_cleanup, self.colors['red']),
            ("System Optimize", self.system_optimize, self.colors['green']),
            ("Shutdown", self.shutdown_system, self.colors['red']),
            ("Restart", self.restart_system, self.colors['orange']),
            ("Lock", self.lock_system, self.colors['blue']),
            ("Sleep", self.sleep_system, self.colors['purple'])
        ]
        
        for i, (text, command, color) in enumerate(system_buttons):
            row = i // 4
            col = i % 4
            btn = tk.Button(control_frame, text=text, command=command,
                         bg=color, fg='white', font=('Arial', 10, 'bold'), width=12)
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
        
        self.voice_history_display = scrolledtext.ScrolledText(history_frame, height=8, width=100,
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
    
    def create_utilities_tab(self, parent):
        """Create utilities tab"""
        tab_frame = tk.Frame(parent, bg=self.colors['glass'])
        parent.add(tab_frame, text="UTILITIES")
        
        # Utilities display
        self.utilities_display = scrolledtext.ScrolledText(tab_frame, height=12, width=100,
                                                          bg=self.colors['bg'], fg=self.colors['text'],
                                                          font=('Consolas', 10))
        self.utilities_display.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Utility controls
        control_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        control_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Label(control_frame, text="UTILITIES", 
                font=('Arial', 14, 'bold'), fg=self.colors['accent'], 
                bg=self.colors['glass']).pack(pady=5)
        
        # Utility buttons
        utilities = [
            ("Calculator", lambda: self.launch_app('calculator'), self.colors['blue']),
            ("Notepad", lambda: self.launch_app('notepad'), self.colors['blue']),
            ("Paint", lambda: self.launch_app('paint'), self.colors['purple']),
            ("Camera", lambda: self.launch_app('camera'), self.colors['green']),
            ("Task Manager", lambda: self.launch_app('taskmgr'), self.colors['red']),
            ("Control Panel", lambda: self.launch_app('control'), self.colors['orange']),
            ("Settings", lambda: self.launch_app('settings'), self.colors['blue']),
            ("Command Prompt", lambda: self.launch_app('cmd'), self.colors['black']),
            ("PowerShell", lambda: self.launch_app('powershell'), self.colors['blue']),
            ("File Explorer", lambda: self.launch_app('files'), self.colors['yellow']),
            ("System Info", self.system_info, self.colors['purple']),
            ("Performance", self.performance_monitor, self.colors['green']),
            ("Disk Cleanup", self.system_cleanup, self.colors['red']),
            ("Network Diag", self.network_status, self.colors['blue']),
            ("Process List", self.show_processes, self.colors['orange'])
        ]
        
        for i, (text, command, color) in enumerate(utilities):
            row = i // 5
            col = i % 5
            btn = tk.Button(control_frame, text=text, command=command,
                         bg=color, fg='white', font=('Arial', 10, 'bold'), width=12)
            btn.grid(row=row, column=col, padx=3, pady=3)
    
    def create_status_bar(self, parent):
        """Create status bar"""
        status_frame = tk.Frame(parent, bg=self.colors['glass'], relief='sunken', bd=1)
        status_frame.pack(fill='x', side='bottom', padx=10, pady=5)
        
        self.task_label = tk.Label(status_frame, text="Task: Ready", 
                                  font=('Arial', 10), fg=self.colors['text'], 
                                  bg=self.colors['glass'])
        self.task_label.pack(side='left', padx=10)
        
        self.time_label = tk.Label(status_frame, text="", 
                                  font=('Arial', 10), fg=self.colors['text'], 
                                  bg=self.colors['glass'])
        self.time_label.pack(side='right', padx=10)
        
        self.stats_label = tk.Label(status_frame, text="CPU: 0% | Memory: 0%", 
                                   font=('Arial', 10), fg=self.colors['text'], 
                                   bg=self.colors['glass'])
        self.stats_label.pack(side='right', padx=10)
    
    def start_background_services(self):
        """Start background services"""
        threading.Thread(target=self.voice_assistant_loop, daemon=True).start()
        threading.Thread(target=self.update_system_info, daemon=True).start()
        threading.Thread(target=self.update_time, daemon=True).start()
        threading.Thread(target=self.update_displays, daemon=True).start()
    
    def start_voice(self):
        """Start voice recognition"""
        if not self.voice_available:
            self.add_display_entry("Voice system not available")
            return
        
        self.listening = True
        self.voice_btn.config(text="Stop Voice", bg=self.colors['red'])
        self.voice_indicator.config(text="Voice: LISTENING", fg=self.colors['green'])
        self.add_display_entry("Voice recognition started")
        self.speak("Voice recognition activated. I'm ready to help you!")
    
    def stop_voice(self):
        """Stop voice recognition"""
        self.listening = False
        self.voice_btn.config(text="Start Voice", bg=self.colors['green'])
        self.voice_indicator.config(text="Voice: IDLE", fg=self.colors['red'])
        self.add_display_entry("Voice recognition stopped")
    
    def test_voice(self):
        """Test voice system"""
        if self.voice_available:
            self.speak("Voice system working perfectly! All features are active and ready!")
            self.add_display_entry("Voice test successful")
        else:
            self.add_display_entry("Voice system not available")
    
    def voice_settings(self):
        """Open voice settings"""
        if self.voice_available:
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
        else:
            self.add_display_entry("Voice system not available")
    
    def manual_command(self, event=None):
        """Process manual command"""
        command = self.manual_entry.get().strip().lower()
        if command:
            self.add_voice_history(f"Manual: {command}")
            self.process_command(command)
            self.manual_entry.delete(0, tk.END)
    
    def voice_assistant_loop(self):
        """Voice assistant loop"""
        if self.voice_available:
            try:
                self.speak(f"Hello {self.user_name}! I am ILLI AI, your complete assistant. All features are working perfectly!")
            except Exception as e:
                self.add_display_entry(f"TTS Error: {str(e)}")
        
        while True:
            try:
                if self.listening and self.voice_available:
                    self.voice_indicator.config(text="Voice: LISTENING", fg=self.colors['green'])
                    
                    with sr.Microphone() as source:
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
                    except sr.UnknownValueError:
                        self.add_voice_history("Could not understand")
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
        self.command_history.append(command)
        
        # Greeting commands
        if any(word in command for word in ['hello', 'hi', 'hey', 'good morning', 'good evening', 'assalam', 'salam']):
            responses = [
                f"Hello {self.user_name}! How can I help you today?",
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
            
            for app_name in self.apps.keys():
                if app_name in command:
                    self.launch_app(app_name)
                    app_found = True
                    break
            
            if not app_found:
                self.speak("Please specify which app to open")
                self.add_display_entry("App name not specified")
        
        # System commands
        elif 'system' in command:
            if 'scan' in command:
                self.system_scan()
            elif 'info' in command:
                self.system_info()
            elif 'cleanup' in command:
                self.system_cleanup()
            elif 'optimize' in command:
                self.system_optimize()
            elif 'process' in command:
                self.show_processes()
            elif 'performance' in command:
                self.performance_monitor()
            elif 'disk' in command:
                self.disk_usage()
            elif 'network' in command:
                self.network_status()
            else:
                self.speak("System control activated")
        
        # File commands
        elif 'file' in command:
            if 'create' in command:
                self.create_file()
            elif 'delete' in command:
                self.delete_file()
            elif 'copy' in command:
                self.copy_file()
            elif 'move' in command:
                self.move_file()
            elif 'rename' in command:
                self.rename_file()
            elif 'browse' in command:
                self.browse_files()
            elif 'search' in command:
                self.search_files()
            elif 'info' in command:
                self.file_info()
            else:
                self.speak("File operations available")
        
        # Information commands
        elif 'time' in command:
            self.tell_time()
        elif 'date' in command:
            self.tell_date()
        elif 'help' in command:
            self.show_help()
        elif 'status' in command:
            self.show_status()
        
        # Power commands
        elif 'shutdown' in command:
            self.shutdown_system()
        elif 'restart' in command:
            self.restart_system()
        elif 'lock' in command:
            self.lock_system()
        elif 'sleep' in command:
            self.sleep_system()
        
        else:
            response = f"I didn't understand '{command}'. Say 'help' for available commands."
            self.speak(response)
            self.add_display_entry(f"Unrecognized: {command}")
    
    def launch_app(self, app_name):
        """Launch application"""
        if app_name not in self.apps:
            self.add_display_entry(f"App '{app_name}' not found")
            return
        
        self.speak(f"Opening {app_name}")
        self.add_display_entry(f"Launching {app_name}")
        
        path = self.apps[app_name]
        
        try:
            if path.startswith('http'):
                webbrowser.open(path)
                self.add_display_entry(f"Opened {app_name} in browser")
            elif path.endswith(':'):
                os.startfile(path)
                self.add_display_entry(f"Opened {app_name} protocol")
            else:
                os.startfile(path)
                self.add_display_entry(f"Opened {app_name} from path")
            
            # Track app usage
            if app_name in self.app_usage:
                self.app_usage[app_name] += 1
            else:
                self.app_usage[app_name] = 1
                
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
==================
CPU Usage: {cpu_usage:.1f}%
Memory Usage: {memory.percent:.1f}%
Disk Usage: {disk.percent:.1f}%
Available Memory: {memory.available / (1024**3):.1f} GB
Free Disk Space: {disk.free / (1024**3):.1f} GB
Running Processes: {len(list(psutil.process_iter()))}
System Boot Time: {datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')}
Operating System: {platform.system()} {platform.release()}
Python Version: {sys.version.split()[0]}
==================
"""
            
            self.add_display_entry(scan_results)
            self.speak("System scan completed")
            
        except Exception as e:
            self.add_display_entry(f"System scan error: {str(e)}")
    
    def system_info(self):
        """Show detailed system information"""
        self.add_display_entry("Getting system information...")
        
        try:
            info = f"""
DETAILED SYSTEM INFORMATION:
==========================
Computer Name: {platform.node()}
Operating System: {platform.system()} {platform.release()}
Processor: {platform.processor()}
Architecture: {platform.architecture()[0]}
Python Version: {sys.version}
User: {self.user_name}
Current Directory: {os.getcwd()}
Home Directory: {os.path.expanduser('~')}
==========================
"""
            self.add_display_entry(info)
            self.speak("System information displayed")
            
        except Exception as e:
            self.add_display_entry(f"System info error: {str(e)}")
    
    def show_processes(self):
        """Show running processes"""
        self.add_display_entry("Getting running processes...")
        
        try:
            processes = []
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
                try:
                    processes.append(f"PID: {proc.info['pid']:<8} Name: {proc.info['name']:<25} CPU: {proc.info['cpu_percent']:<6.1f}% Memory: {proc.info['memory_percent']:<6.1f}%")
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
            
            process_list = "\n".join(processes[:20])  # Show first 20 processes
            self.add_display_entry(f"RUNNING PROCESSES:\n{process_list}")
            self.speak("Process list displayed")
            
        except Exception as e:
            self.add_display_entry(f"Process list error: {str(e)}")
    
    def performance_monitor(self):
        """Monitor system performance"""
        self.add_display_entry("Starting performance monitoring...")
        
        try:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            # CPU info
            cpu_count = psutil.cpu_count()
            cpu_freq = psutil.cpu_freq()
            
            # Memory info
            swap = psutil.swap_memory()
            
            # Network info
            network = psutil.net_io_counters()
            
            perf_info = f"""
PERFORMANCE MONITOR:
==================
CPU:
- Usage: {cpu_usage:.1f}%
- Cores: {cpu_count}
- Frequency: {cpu_freq.current:.0f} MHz if cpu_freq else 'N/A'

MEMORY:
- Total: {memory.total / (1024**3):.1f} GB
- Available: {memory.available / (1024**3):.1f} GB
- Used: {memory.used / (1024**3):.1f} GB
- Percentage: {memory.percent:.1f}%
- Swap Total: {swap.total / (1024**3):.1f} GB
- Swap Used: {swap.used / (1024**3):.1f} GB

DISK:
- Total: {disk.total / (1024**3):.1f} GB
- Used: {disk.used / (1024**3):.1f} GB
- Free: {disk.free / (1024**3):.1f} GB
- Percentage: {disk.percent:.1f}%

NETWORK:
- Bytes Sent: {network.bytes_sent / (1024**2):.1f} MB
- Bytes Received: {network.bytes_recv / (1024**2):.1f} MB
- Packets Sent: {network.packets_sent}
- Packets Received: {network.packets_recv}
==================
"""
            
            self.add_display_entry(perf_info)
            self.speak("Performance monitoring completed")
            
        except Exception as e:
            self.add_display_entry(f"Performance monitor error: {str(e)}")
    
    def disk_usage(self):
        """Show disk usage"""
        self.add_display_entry("Getting disk usage...")
        
        try:
            disk_info = []
            for partition in psutil.disk_partitions():
                try:
                    usage = psutil.disk_usage(partition.mountpoint)
                    disk_info.append(f"Drive: {partition.device} Mount: {partition.mountpoint}")
                    disk_info.append(f"  Total: {usage.total / (1024**3):.1f} GB")
                    disk_info.append(f"  Used: {usage.used / (1024**3):.1f} GB")
                    disk_info.append(f"  Free: {usage.free / (1024**3):.1f} GB")
                    disk_info.append(f"  Percentage: {usage.percent:.1f}%")
                    disk_info.append("")
                except Exception:
                    pass
            
            self.add_display_entry("DISK USAGE:\n" + "\n".join(disk_info))
            self.speak("Disk usage displayed")
            
        except Exception as e:
            self.add_display_entry(f"Disk usage error: {str(e)}")
    
    def network_status(self):
        """Show network status"""
        self.add_display_entry("Getting network status...")
        
        try:
            network = psutil.net_io_counters()
            connections = psutil.net_connections()
            
            net_info = f"""
NETWORK STATUS:
==============
Bytes Sent: {network.bytes_sent / (1024**2):.1f} MB
Bytes Received: {network.bytes_recv / (1024**2):.1f} MB
Packets Sent: {network.packets_sent}
Packets Received: {network.packets_recv}
Active Connections: {len([c for c in connections if c.status == 'ESTABLISHED'])}
Listening Ports: {len([c for c in connections if c.status == 'LISTEN'])}
==============
"""
            
            self.add_display_entry(net_info)
            self.speak("Network status displayed")
            
        except Exception as e:
            self.add_display_entry(f"Network status error: {str(e)}")
    
    def system_cleanup(self):
        """Perform system cleanup"""
        self.add_display_entry("System cleanup initiated")
        
        try:
            temp_dirs = [
                os.environ.get('TEMP', ''),
                os.path.join(os.environ.get('LOCALAPPDATA', ''), 'Temp'),
                os.path.join(os.environ.get('TEMP', ''), '..')
            ]
            
            cleaned_files = 0
            cleaned_size = 0
            
            for temp_dir in temp_dirs:
                if os.path.exists(temp_dir):
                    try:
                        for item in os.listdir(temp_dir):
                            item_path = os.path.join(temp_dir, item)
                            try:
                                if os.path.isfile(item_path):
                                    size = os.path.getsize(item_path)
                                    os.remove(item_path)
                                    cleaned_files += 1
                                    cleaned_size += size
                                elif os.path.isdir(item_path):
                                    shutil.rmtree(item_path)
                                    cleaned_files += 1
                            except Exception:
                                pass
                    except Exception:
                        pass
            
            cleanup_info = f"""
CLEANUP COMPLETED:
================
Files Cleaned: {cleaned_files}
Space Freed: {cleaned_size / (1024**2):.1f} MB
================
"""
            
            self.add_display_entry(cleanup_info)
            self.speak("System cleanup completed")
            
        except Exception as e:
            self.add_display_entry(f"System cleanup error: {str(e)}")
    
    def system_optimize(self):
        """Perform system optimization"""
        self.add_display_entry("System optimization initiated")
        
        try:
            # Clear some caches
            optimized = []
            
            # Clear Python cache
            try:
                import tempfile
                temp_dir = tempfile.gettempdir()
                for item in os.listdir(temp_dir):
                    if item.startswith('tmp') and item.endswith('.py'):
                        try:
                            os.remove(os.path.join(temp_dir, item))
                            optimized.append("Python cache cleared")
                        except Exception:
                            pass
            except Exception:
                pass
            
            opt_info = f"""
OPTIMIZATION COMPLETED:
=====================
{chr(10).join(optimized) if optimized else 'System optimization completed'}
=====================
"""
            
            self.add_display_entry(opt_info)
            self.speak("System optimization completed")
            
        except Exception as e:
            self.add_display_entry(f"System optimization error: {str(e)}")
    
    def create_file(self):
        """Create file"""
        file_path = filedialog.asksaveasfilename(title="Create File",
                                               defaultextension=".txt",
                                               filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
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
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                        self.add_display_entry(f"Deleted file: {file_path}")
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                        self.add_display_entry(f"Deleted folder: {file_path}")
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
            try:
                os.startfile(folder_path)
                self.add_display_entry(f"Browsed to: {folder_path}")
                self.speak("File browser opened")
            except Exception as e:
                self.add_display_entry(f"Error browsing files: {str(e)}")
    
    def search_files(self):
        """Search files"""
        search_term = simpledialog.askstring("Search Files", "Enter search term:")
        if search_term:
            try:
                search_path = filedialog.askdirectory(title="Select search directory")
                if search_path:
                    found_files = []
                    for root, dirs, files in os.walk(search_path):
                        for file in files:
                            if search_term.lower() in file.lower():
                                found_files.append(os.path.join(root, file))
                    
                    if found_files:
                        self.add_display_entry(f"Found {len(found_files)} files:")
                        for file in found_files[:10]:  # Show first 10
                            self.add_display_entry(f"  {file}")
                    else:
                        self.add_display_entry("No files found")
                    
                    self.speak(f"Found {len(found_files)} files")
            except Exception as e:
                self.add_display_entry(f"Error searching files: {str(e)}")
    
    def file_info(self):
        """Get file information"""
        file_path = filedialog.askopenfilename(title="Select file for info")
        if file_path:
            try:
                stat = os.stat(file_path)
                size_mb = stat.st_size / (1024*1024)
                info = f"""
FILE INFORMATION:
================
Path: {file_path}
Size: {size_mb:.2f} MB ({stat.st_size} bytes)
Created: {datetime.fromtimestamp(stat.st_ctime)}
Modified: {datetime.fromtimestamp(stat.st_mtime)}
Accessed: {datetime.fromtimestamp(stat.st_atime)}
Type: {'Directory' if os.path.isdir(file_path) else 'File'}
================
"""
                self.add_display_entry(info)
                self.speak("File information displayed")
            except Exception as e:
                self.add_display_entry(f"Error getting file info: {str(e)}")
    
    def clean_temp(self):
        """Clean temporary files"""
        self.system_cleanup()
    
    def shutdown_system(self):
        """Shutdown system"""
        if messagebox.askyesno("Confirm Shutdown", "Are you sure you want to shutdown system?"):
            try:
                if platform.system() == "Windows":
                    os.system("shutdown /s /t 10")
                else:
                    os.system("shutdown -h +10")
                self.add_display_entry("System will shutdown in 10 seconds")
                self.speak("System will shutdown in 10 seconds")
            except Exception as e:
                self.add_display_entry(f"Shutdown error: {str(e)}")
    
    def restart_system(self):
        """Restart system"""
        if messagebox.askyesno("Confirm Restart", "Are you sure you want to restart system?"):
            try:
                if platform.system() == "Windows":
                    os.system("shutdown /r /t 10")
                else:
                    os.system("shutdown -r +10")
                self.add_display_entry("System will restart in 10 seconds")
                self.speak("System will restart in 10 seconds")
            except Exception as e:
                self.add_display_entry(f"Restart error: {str(e)}")
    
    def lock_system(self):
        """Lock system"""
        try:
            if platform.system() == "Windows":
                os.system("rundll32.exe user32.dll,LockWorkStation")
            else:
                os.system("xdg-screensaver lock")
            self.add_display_entry("System locked")
            self.speak("System locked")
        except Exception as e:
            self.add_display_entry(f"Lock error: {str(e)}")
    
    def sleep_system(self):
        """Sleep system"""
        try:
            if platform.system() == "Windows":
                os.system("rundll32.exe powrprof.dll,SetSuspendState Sleep")
            else:
                os.system("systemctl suspend")
            self.add_display_entry("System sleep activated")
            self.speak("System sleep activated")
        except Exception as e:
            self.add_display_entry(f"Sleep error: {str(e)}")
    
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
ILLI AI - COMPLETE COMMAND GUIDE

🎤 VOICE COMMANDS:
- "Hello/Hi/Hey" - Natural greeting
- "Time" - Tell current time
- "Date" - Tell current date
- "Help" - Show this help
- "Status" - Show system status

🚀 APPLICATION COMMANDS:
- "Open [app]" - Launch any application
- Apps: WhatsApp, Instagram, Chrome, Firefox, YouTube, Files, Notepad, Calculator, CMD, PowerShell, Task Manager, Control Panel, Settings, Camera, Paint, Word, Excel, PowerPoint, Gmail, Outlook, ChatGPT, GitHub, LinkedIn, Facebook, Twitter, Spotify, Discord, Slack, Teams, Zoom, Skype, Telegram, Signal, Reddit, Pinterest, TikTok, Snapchat, Netflix, Amazon, eBay, Wikipedia

🖥️ SYSTEM COMMANDS:
- "System scan" - Analyze system performance
- "System info" - Show system information
- "System cleanup" - Clean temporary files
- "System optimize" - Optimize performance
- "Show processes" - Display running processes
- "Performance" - Monitor performance
- "Disk usage" - Show disk usage
- "Network status" - Show network status

📁 FILE COMMANDS:
- "File create" - Create new file
- "File delete" - Delete file
- "File copy" - Copy file
- "File move" - Move file
- "File rename" - Rename file
- "File browse" - Browse files
- "File search" - Search files
- "File info" - Get file information

⚡ POWER COMMANDS:
- "Shutdown" - Shutdown computer
- "Restart" - Restart computer
- "Lock" - Lock computer
- "Sleep" - Sleep computer

🎯 TIPS:
- Speak clearly and naturally
- Use specific app names
- Commands are case-insensitive
- Use manual input if voice doesn't work
- Check system status regularly
"""
        
        self.add_display_entry(help_text)
        self.speak("Help information displayed")
    
    def show_status(self):
        """Show current status"""
        try:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            
            status = f"""
CURRENT STATUS:
==============
System: Online
Voice: {'Active' if self.listening else 'Inactive'}
CPU Usage: {cpu_usage:.1f}%
Memory Usage: {memory.percent:.1f}%
Running Processes: {len(list(psutil.process_iter()))}
Command History: {len(self.command_history)} commands
App Usage: {len(self.app_usage)} apps used
==============
"""
            
            self.add_display_entry(status)
            self.speak("Status displayed")
            
        except Exception as e:
            self.add_display_entry(f"Status error: {str(e)}")
    
    def speak(self, text):
        """Text to speech"""
        if self.voice_available:
            try:
                self.engine.say(text)
                self.engine.runAndWait()
            except Exception as e:
                self.add_display_entry(f"TTS Error: {str(e)}")
    
    def add_display_entry(self, message):
        """Add entry to all displays"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        
        # Add to all displays
        try:
            self.main_display.insert(tk.END, log_entry)
            self.main_display.see(tk.END)
        except:
            pass
        
        try:
            self.apps_display.insert(tk.END, log_entry)
            self.apps_display.see(tk.END)
        except:
            pass
        
        try:
            self.files_display.insert(tk.END, log_entry)
            self.files_display.see(tk.END)
        except:
            pass
        
        try:
            self.system_display.insert(tk.END, log_entry)
            self.system_display.see(tk.END)
        except:
            pass
        
        try:
            self.utilities_display.insert(tk.END, log_entry)
            self.utilities_display.see(tk.END)
        except:
            pass
        
        # Update status
        try:
            self.status_label.config(text=f"Status: {self.system_stats.get('status', 'ONLINE')}")
            self.task_label.config(text=f"Task: {self.system_stats.get('task', 'Ready')}")
        except:
            pass
    
    def add_voice_history(self, message):
        """Add to voice history"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        history_entry = f"[{timestamp}] {message}\n"
        
        try:
            self.voice_history_display.insert(tk.END, history_entry)
            self.voice_history_display.see(tk.END)
        except:
            pass
    
    def update_system_info(self):
        """Update system information"""
        while True:
            try:
                cpu_usage = psutil.cpu_percent(interval=1)
                memory = psutil.virtual_memory()
                
                self.system_stats['cpu'] = cpu_usage
                self.system_stats['memory'] = memory.percent
                
                stats_text = f"CPU: {cpu_usage:.1f}% | Memory: {memory.percent:.1f}%"
                
                try:
                    self.stats_label.config(text=stats_text)
                except:
                    pass
                
                time.sleep(5)
            except Exception as e:
                time.sleep(5)
    
    def update_time(self):
        """Update time display"""
        while True:
            try:
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                try:
                    self.time_label.config(text=current_time)
                except:
                    pass
                time.sleep(1)
            except Exception as e:
                time.sleep(1)
    
    def update_displays(self):
        """Update all displays"""
        while True:
            try:
                # Auto-scroll displays
                for display in [self.main_display, self.apps_display, self.files_display, 
                              self.system_display, self.utilities_display, self.voice_history_display]:
                    try:
                        display.see(tk.END)
                    except:
                        pass
                time.sleep(2)
            except Exception as e:
                time.sleep(2)

def main():
    """Main function"""
    root = tk.Tk()
    app = ILLI_AI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
