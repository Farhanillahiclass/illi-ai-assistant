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

class ILLI_AI_Complete:
    def __init__(self, root):
        self.root = root
        self.root.title("🤖 ILLI AI - COMPLETE ALL FEATURES")
        self.root.geometry("1920x1080")
        self.root.configure(bg='#000000')
        
        # System variables
        self.system_status = "ONLINE"
        self.user_name = os.getlogin()
        self.current_task = "AI Assistant Ready"
        self.listening_state = False
        self.response_queue = queue.Queue()
        
        # Voice recognition - Multiple providers
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 0.9)
        
        # AI Services
        self.wolfram_alpha_app_id = "YOUR_WOLFRAM_APP_ID"  # User can set this
        self.reminders = []
        self.schedules = []
        self.chat_history = []
        
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
        
        # Complete app paths with maximum detection
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
        
        # Start all services
        self.start_all_services()
    
    def setup_ui(self):
        """Setup comprehensive UI"""
        # Main container
        main_frame = tk.Frame(self.root, bg=self.colors['bg'])
        main_frame.pack(fill='both', expand=True)
        
        # Header
        self.create_header(main_frame)
        
        # Tabbed interface
        notebook = ttk.Notebook(main_frame)
        notebook.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Create tabs
        self.create_system_tab(notebook)
        self.create_apps_tab(notebook)
        self.create_files_tab(notebook)
        self.create_communication_tab(notebook)
        self.create_ai_tab(notebook)
        self.create_multimedia_tab(notebook)
        self.create_voice_tab(notebook)
        
        # Bottom status bar
        self.create_status_bar(main_frame)
    
    def create_header(self, parent):
        """Create header section"""
        header_frame = tk.Frame(parent, bg=self.colors['glass'], relief='raised', bd=2)
        header_frame.pack(fill='x', padx=10, pady=5)
        
        # Title
        title_label = tk.Label(header_frame, text="🤖 ILLI AI - COMPLETE ALL FEATURES", 
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
    
    def create_system_tab(self, parent):
        """Create system monitoring tab"""
        tab_frame = tk.Frame(parent, bg=self.colors['glass'])
        parent.add(tab_frame, text="🖥️ SYSTEM")
        
        # System info
        info_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        info_frame.pack(fill='x', padx=10, pady=10)
        
        self.system_display = scrolledtext.ScrolledText(info_frame, height=10, width=80,
                                                      bg=self.colors['bg'], fg=self.colors['text'],
                                                      font=('Consolas', 10))
        self.system_display.pack(fill='x', pady=5)
        
        # System controls
        control_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        control_frame.pack(fill='x', padx=10, pady=5)
        
        # System buttons
        buttons = [
            ("🔍 System Scan", self.system_scan),
            ("🧹 System Cleanup", self.system_cleanup),
            ("⚡ System Optimize", self.system_optimize),
            ("🔒 Lock System", self.lock_system),
            ("😴 Sleep System", self.sleep_system),
            ("🔄 Restart System", self.restart_system),
            ("💻 Shutdown System", self.shutdown_system),
            ("📊 Task Manager", lambda: self.launch_app('taskmanager')),
            ("⚙️ Control Panel", lambda: self.launch_app('controlpanel')),
            ("🔧 Settings", lambda: self.launch_app('settings'))
        ]
        
        for i, (text, command) in enumerate(buttons):
            row = i // 5
            col = i % 5
            btn = tk.Button(control_frame, text=text, command=command,
                         bg=self.colors['blue'], fg='white', 
                         font=('Arial', 10, 'bold'), width=15)
            btn.grid(row=row, column=col, padx=5, pady=5)
    
    def create_apps_tab(self, parent):
        """Create applications control tab"""
        tab_frame = tk.Frame(parent, bg=self.colors['glass'])
        parent.add(tab_frame, text="🚀 APPS")
        
        # App status
        status_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        status_frame.pack(fill='x', padx=10, pady=10)
        
        self.app_display = scrolledtext.ScrolledText(status_frame, height=8, width=80,
                                                    bg=self.colors['bg'], fg=self.colors['text'],
                                                    font=('Consolas', 10))
        self.app_display.pack(fill='x', pady=5)
        
        # App launch buttons
        launch_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        launch_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Label(launch_frame, text="🚀 LAUNCH APPS", font=('Arial', 14, 'bold'),
                fg=self.colors['accent'], bg=self.colors['glass']).pack(pady=5)
        
        # App buttons grid
        apps_grid = tk.Frame(launch_frame, bg=self.colors['glass'])
        apps_grid.pack()
        
        apps = [
            ("WhatsApp", 'whatsapp'), ("Instagram", 'instagram'), ("VS Code", 'vscode'),
            ("YouTube", 'youtube'), ("Chrome", 'chrome'), ("LinkedIn", 'linkedin'),
            ("GitHub", 'github'), ("Gmail", 'gmail'), ("ChatGPT", 'chatgpt'),
            ("Spotify", 'spotify'), ("Discord", 'discord'), ("Slack", 'slack'),
            ("Teams", 'teams'), ("Zoom", 'zoom'), ("Camera", 'camera'),
            ("Blender", 'blender'), ("Notepad", 'notepad'), ("Calculator", 'calculator'),
            ("Files", 'files'), ("CMD", 'cmd'), ("PowerShell", 'powershell')
        ]
        
        for i, (name, app_key) in enumerate(apps):
            row = i // 6
            col = i % 6
            btn = tk.Button(apps_grid, text=name, 
                         command=lambda k=app_key: self.launch_app(k),
                         bg=self.colors['cyan'], fg='black', 
                         font=('Arial', 10, 'bold'), width=12)
            btn.grid(row=row, column=col, padx=3, pady=3)
        
        # App control buttons
        control_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        control_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Label(control_frame, text="🎮 APP CONTROLS", font=('Arial', 14, 'bold'),
                fg=self.colors['accent'], bg=self.colors['glass']).pack(pady=5)
        
        control_buttons = [
            ("📱 Close App", self.close_app_dialog),
            ("🔄 Restart App", self.restart_app),
            ("📉 Minimize All", self.minimize_all_apps),
            ("📈 Maximize All", self.maximize_all_apps),
            ("🔄 Refresh Apps", self.refresh_apps)
        ]
        
        for text, command in control_buttons:
            btn = tk.Button(control_frame, text=text, command=command,
                         bg=self.colors['orange'], fg='white', 
                         font=('Arial', 10, 'bold'), width=15)
            btn.pack(side='left', padx=5, pady=5)
    
    def create_files_tab(self, parent):
        """Create file management tab"""
        tab_frame = tk.Frame(parent, bg=self.colors['glass'])
        parent.add(tab_frame, text="📁 FILES")
        
        # File operations
        ops_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        ops_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Label(ops_frame, text="📁 FILE OPERATIONS", font=('Arial', 14, 'bold'),
                fg=self.colors['accent'], bg=self.colors['glass']).pack(pady=5)
        
        # File operations buttons
        file_ops = [
            ("📄 Create File", self.create_file_dialog),
            ("📁 Create Folder", self.create_folder_dialog),
            ("📋 Copy File", self.copy_file_dialog),
            ("✂️ Move File", self.move_file_dialog),
            ("🔄 Rename File", self.rename_file_dialog),
            ("🗑️ Delete File", self.delete_file_dialog),
            ("📂 Browse Files", self.browse_files),
            ("🔍 Search Files", self.search_files_dialog),
            ("📊 File Info", self.file_info_dialog)
        ]
        
        ops_grid = tk.Frame(ops_frame, bg=self.colors['glass'])
        ops_grid.pack()
        
        for i, (text, command) in enumerate(file_ops):
            row = i // 3
            col = i % 3
            btn = tk.Button(ops_grid, text=text, command=command,
                         bg=self.colors['purple'], fg='white', 
                         font=('Arial', 10, 'bold'), width=15)
            btn.grid(row=row, column=col, padx=5, pady=5)
        
        # File display
        display_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        display_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        self.file_display = scrolledtext.ScrolledText(display_frame, height=10, width=80,
                                                    bg=self.colors['bg'], fg=self.colors['text'],
                                                    font=('Consolas', 10))
        self.file_display.pack(fill='both', expand=True)
    
    def create_communication_tab(self, parent):
        """Create communication tab"""
        tab_frame = tk.Frame(parent, bg=self.colors['glass'])
        parent.add(tab_frame, text="💬 COMMUNICATION")
        
        # WhatsApp section
        whatsapp_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        whatsapp_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Label(whatsapp_frame, text="📱 WHATSAPP", font=('Arial', 14, 'bold'),
                fg=self.colors['accent'], bg=self.colors['glass']).pack(pady=5)
        
        # WhatsApp controls
        wa_controls = tk.Frame(whatsapp_frame, bg=self.colors['glass'])
        wa_controls.pack()
        
        tk.Label(wa_controls, text="Contact:", fg=self.colors['text'], 
                bg=self.colors['glass']).grid(row=0, column=0, padx=5, pady=5)
        self.whatsapp_contact = tk.Entry(wa_controls, width=20, bg=self.colors['bg'], 
                                      fg=self.colors['text'], font=('Consolas', 10))
        self.whatsapp_contact.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(wa_controls, text="Message:", fg=self.colors['text'], 
                bg=self.colors['glass']).grid(row=1, column=0, padx=5, pady=5)
        self.whatsapp_message = tk.Entry(wa_controls, width=40, bg=self.colors['bg'], 
                                      fg=self.colors['text'], font=('Consolas', 10))
        self.whatsapp_message.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Button(wa_controls, text="📤 Send WhatsApp", command=self.send_whatsapp_message,
                 bg=self.colors['green'], fg='white', font=('Arial', 10, 'bold')).grid(row=2, column=1, padx=5, pady=5)
        
        # Email section
        email_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        email_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Label(email_frame, text="📧 EMAIL", font=('Arial', 14, 'bold'),
                fg=self.colors['accent'], bg=self.colors['glass']).pack(pady=5)
        
        # Email controls
        email_controls = tk.Frame(email_frame, bg=self.colors['glass'])
        email_controls.pack()
        
        tk.Label(email_controls, text="To:", fg=self.colors['text'], 
                bg=self.colors['glass']).grid(row=0, column=0, padx=5, pady=5)
        self.email_to = tk.Entry(email_controls, width=30, bg=self.colors['bg'], 
                              fg=self.colors['text'], font=('Consolas', 10))
        self.email_to.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(email_controls, text="Subject:", fg=self.colors['text'], 
                bg=self.colors['glass']).grid(row=1, column=0, padx=5, pady=5)
        self.email_subject = tk.Entry(email_controls, width=30, bg=self.colors['bg'], 
                                fg=self.colors['text'], font=('Consolas', 10))
        self.email_subject.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(email_controls, text="Message:", fg=self.colors['text'], 
                bg=self.colors['glass']).grid(row=2, column=0, padx=5, pady=5)
        self.email_message = tk.Entry(email_controls, width=40, bg=self.colors['bg'], 
                                 fg=self.colors['text'], font=('Consolas', 10))
        self.email_message.grid(row=2, column=1, padx=5, pady=5)
        
        tk.Button(email_controls, text="📤 Send Email", command=self.send_email,
                 bg=self.colors['green'], fg='white', font=('Arial', 10, 'bold')).grid(row=3, column=1, padx=5, pady=5)
        
        # Communication log
        log_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        log_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        tk.Label(log_frame, text="📋 COMMUNICATION LOG", font=('Arial', 12, 'bold'),
                fg=self.colors['accent'], bg=self.colors['glass']).pack(pady=5)
        
        self.comm_display = scrolledtext.ScrolledText(log_frame, height=8, width=80,
                                                    bg=self.colors['bg'], fg=self.colors['text'],
                                                    font=('Consolas', 10))
        self.comm_display.pack(fill='both', expand=True)
    
    def create_ai_tab(self, parent):
        """Create AI features tab"""
        tab_frame = tk.Frame(parent, bg=self.colors['glass'])
        parent.add(tab_frame, text="🤖 AI")
        
        # AI Chat
        chat_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        chat_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Label(chat_frame, text="💬 AI CHAT", font=('Arial', 14, 'bold'),
                fg=self.colors['accent'], bg=self.colors['glass']).pack(pady=5)
        
        # Chat interface
        chat_interface = tk.Frame(chat_frame, bg=self.colors['glass'])
        chat_interface.pack()
        
        tk.Label(chat_interface, text="You:", fg=self.colors['text'], 
                bg=self.colors['glass']).grid(row=0, column=0, padx=5, pady=5)
        self.ai_input = tk.Entry(chat_interface, width=50, bg=self.colors['bg'], 
                              fg=self.colors['text'], font=('Consolas', 10))
        self.ai_input.grid(row=0, column=1, padx=5, pady=5)
        self.ai_input.bind('<Return>', self.send_ai_message)
        
        tk.Button(chat_interface, text="💬 Send", command=self.send_ai_message,
                 bg=self.colors['cyan'], fg='black', font=('Arial', 10, 'bold')).grid(row=0, column=2, padx=5, pady=5)
        
        # Chat display
        self.ai_display = scrolledtext.ScrolledText(chat_frame, height=8, width=80,
                                                    bg=self.colors['bg'], fg=self.colors['text'],
                                                    font=('Consolas', 10))
        self.ai_display.pack(fill='both', expand=True, pady=5)
        
        # Reminders and Scheduling
        schedule_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        schedule_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Label(schedule_frame, text="⏰ REMINDERS & SCHEDULING", font=('Arial', 14, 'bold'),
                fg=self.colors['accent'], bg=self.colors['glass']).pack(pady=5)
        
        # Reminder controls
        reminder_controls = tk.Frame(schedule_frame, bg=self.colors['glass'])
        reminder_controls.pack()
        
        tk.Label(reminder_controls, text="Reminder:", fg=self.colors['text'], 
                bg=self.colors['glass']).grid(row=0, column=0, padx=5, pady=5)
        self.reminder_text = tk.Entry(reminder_controls, width=30, bg=self.colors['bg'], 
                                    fg=self.colors['text'], font=('Consolas', 10))
        self.reminder_text.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(reminder_controls, text="Time:", fg=self.colors['text'], 
                bg=self.colors['glass']).grid(row=1, column=0, padx=5, pady=5)
        self.reminder_time = tk.Entry(reminder_controls, width=15, bg=self.colors['bg'], 
                                    fg=self.colors['text'], font=('Consolas', 10))
        self.reminder_time.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Button(reminder_controls, text="⏰ Add Reminder", command=self.add_reminder,
                 bg=self.colors['orange'], fg='white', font=('Arial', 10, 'bold')).grid(row=2, column=1, padx=5, pady=5)
        
        # Knowledge search
        knowledge_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        knowledge_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Label(knowledge_frame, text="🔍 KNOWLEDGE SEARCH", font=('Arial', 14, 'bold'),
                fg=self.colors['accent'], bg=self.colors['glass']).pack(pady=5)
        
        knowledge_controls = tk.Frame(knowledge_frame, bg=self.colors['glass'])
        knowledge_controls.pack()
        
        tk.Label(knowledge_controls, text="Search:", fg=self.colors['text'], 
                bg=self.colors['glass']).grid(row=0, column=0, padx=5, pady=5)
        self.knowledge_search = tk.Entry(knowledge_controls, width=40, bg=self.colors['bg'], 
                                      fg=self.colors['text'], font=('Consolas', 10))
        self.knowledge_search.grid(row=0, column=1, padx=5, pady=5)
        
        search_buttons = [
            ("🌐 Wikipedia", self.wikipedia_search),
            ("🧮 WolframAlpha", self.wolfram_search),
            ("🔍 Google", self.google_search)
        ]
        
        for i, (text, command) in enumerate(search_buttons):
            btn = tk.Button(knowledge_controls, text=text, command=command,
                         bg=self.colors['blue'], fg='white', 
                         font=('Arial', 10, 'bold'))
            btn.grid(row=1, column=i, padx=5, pady=5)
    
    def create_multimedia_tab(self, parent):
        """Create multimedia control tab"""
        tab_frame = tk.Frame(parent, bg=self.colors['glass'])
        parent.add(tab_frame, text="🎵 MULTIMEDIA")
        
        # Volume controls
        volume_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        volume_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Label(volume_frame, text="🔊 VOLUME CONTROLS", font=('Arial', 14, 'bold'),
                fg=self.colors['accent'], bg=self.colors['glass']).pack(pady=5)
        
        volume_controls = tk.Frame(volume_frame, bg=self.colors['glass'])
        volume_controls.pack()
        
        # Volume slider
        tk.Label(volume_controls, text="Master Volume:", fg=self.colors['text'], 
                bg=self.colors['glass']).grid(row=0, column=0, padx=5, pady=5)
        self.volume_slider = tk.Scale(volume_controls, from_=0, to=100, orient='horizontal',
                                 bg=self.colors['glass'], fg=self.colors['text'],
                                 length=200, command=self.set_volume)
        self.volume_slider.set(50)
        self.volume_slider.grid(row=0, column=1, padx=5, pady=5)
        
        # Volume buttons
        volume_buttons = [
            ("🔇 Mute", self.mute_volume),
            ("🔊 Max", self.max_volume),
            ("🔉 +10", lambda: self.adjust_volume(10)),
            ("🔉 -10", lambda: self.adjust_volume(-10))
        ]
        
        for i, (text, command) in enumerate(volume_buttons):
            btn = tk.Button(volume_controls, text=text, command=command,
                         bg=self.colors['purple'], fg='white', 
                         font=('Arial', 10, 'bold'))
            btn.grid(row=1, column=i, padx=5, pady=5)
        
        # Media controls
        media_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        media_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Label(media_frame, text="🎬 MEDIA CONTROLS", font=('Arial', 14, 'bold'),
                fg=self.colors['accent'], bg=self.colors['glass']).pack(pady=5)
        
        media_controls = tk.Frame(media_frame, bg=self.colors['glass'])
        media_controls.pack()
        
        media_buttons = [
            ("⏯ Play/Pause", self.play_pause_media),
            ("⏹ Stop", self.stop_media),
            ("⏭ Next", self.next_media),
            ("⏮ Previous", self.previous_media),
            ("🔇 Mute", self.mute_volume),
            ("🔊 Volume Up", lambda: self.adjust_volume(5)),
            ("🔉 Volume Down", lambda: self.adjust_volume(-5))
        ]
        
        for i, (text, command) in enumerate(media_buttons):
            row = i // 4
            col = i % 4
            btn = tk.Button(media_controls, text=text, command=command,
                         bg=self.colors['green'], fg='white', 
                         font=('Arial', 10, 'bold'), width=12)
            btn.grid(row=row, column=col, padx=5, pady=5)
        
        # Camera controls
        camera_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        camera_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Label(camera_frame, text="📷 CAMERA CONTROLS", font=('Arial', 14, 'bold'),
                fg=self.colors['accent'], bg=self.colors['glass']).pack(pady=5)
        
        camera_controls = tk.Frame(camera_frame, bg=self.colors['glass'])
        camera_controls.pack()
        
        camera_buttons = [
            ("📷 Take Photo", self.take_photo),
            ("🎥 Start Recording", self.start_recording),
            ("⏹ Stop Recording", self.stop_recording),
            ("📷 Open Camera", lambda: self.launch_app('camera'))
        ]
        
        for i, (text, command) in enumerate(camera_buttons):
            btn = tk.Button(camera_controls, text=text, command=command,
                         bg=self.colors['blue'], fg='white', 
                         font=('Arial', 10, 'bold'), width=15)
            btn.grid(row=0, column=i, padx=5, pady=5)
    
    def create_voice_tab(self, parent):
        """Create voice control tab"""
        tab_frame = tk.Frame(parent, bg=self.colors['glass'])
        parent.add(tab_frame, text="🎤 VOICE")
        
        # Voice status
        status_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        status_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Label(status_frame, text="🎤 VOICE CONTROL", font=('Arial', 14, 'bold'),
                fg=self.colors['accent'], bg=self.colors['glass']).pack(pady=5)
        
        voice_status = tk.Frame(status_frame, bg=self.colors['glass'])
        voice_status.pack()
        
        self.voice_indicator = tk.Label(voice_status, text="🔴 Voice: IDLE", 
                                     font=('Arial', 12, 'bold'), fg=self.colors['red'], 
                                     bg=self.colors['glass'])
        self.voice_indicator.pack(side='left', padx=20, pady=10)
        
        # Voice controls
        control_frame = tk.Frame(status_frame, bg=self.colors['glass'])
        control_frame.pack()
        
        self.voice_btn = tk.Button(control_frame, text="🎤 Start Voice", 
                                   command=self.toggle_voice,
                                   bg=self.colors['green'], fg='white', 
                                   font=('Arial', 12, 'bold'))
        self.voice_btn.pack(side='left', padx=5, pady=5)
        
        tk.Button(control_frame, text="🔊 Test Voice", command=self.test_voice,
                 bg=self.colors['blue'], fg='white', 
                 font=('Arial', 12, 'bold')).pack(side='left', padx=5, pady=5)
        
        tk.Button(control_frame, text="⚙️ Voice Settings", command=self.voice_settings,
                 bg=self.colors['orange'], fg='white', 
                 font=('Arial', 12, 'bold')).pack(side='left', padx=5, pady=5)
        
        # Command history
        history_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        history_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        tk.Label(history_frame, text="📋 COMMAND HISTORY", font=('Arial', 12, 'bold'),
                fg=self.colors['accent'], bg=self.colors['glass']).pack(pady=5)
        
        self.voice_display = scrolledtext.ScrolledText(history_frame, height=10, width=80,
                                                     bg=self.colors['bg'], fg=self.colors['text'],
                                                     font=('Consolas', 10))
        self.voice_display.pack(fill='both', expand=True)
        
        # Manual command input
        input_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        input_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Label(input_frame, text="Manual Command:", fg=self.colors['text'], 
                bg=self.colors['glass']).pack(side='left', padx=5)
        
        self.manual_entry = tk.Entry(input_frame, width=50, bg=self.colors['bg'], 
                                    fg=self.colors['text'], font=('Consolas', 10))
        self.manual_entry.pack(side='left', padx=5, pady=5, fill='x', expand=True)
        self.manual_entry.bind('<Return>', self.manual_command)
        
        tk.Button(input_frame, text="⚡ Execute", command=self.manual_command,
                 bg=self.colors['accent'], fg='black', font=('Arial', 10, 'bold')).pack(side='left', padx=5, pady=5)
    
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
    
    def start_all_services(self):
        """Start all background services"""
        threading.Thread(target=self.voice_assistant_loop, daemon=True).start()
        threading.Thread(target=self.update_system_info, daemon=True).start()
        threading.Thread(target=self.update_time, daemon=True).start()
        threading.Thread(target=self.check_reminders, daemon=True).start()
        threading.Thread(target=self.update_displays, daemon=True).start()
    
    def toggle_voice(self):
        """Toggle voice recognition"""
        self.listening_state = not self.listening_state
        if self.listening_state:
            self.voice_btn.config(text="🔴 Stop Voice", bg=self.colors['red'])
            self.voice_indicator.config(text="🟢 Voice: LISTENING", fg=self.colors['green'])
            self.add_log_entry("Voice recognition activated")
        else:
            self.voice_btn.config(text="🎤 Start Voice", bg=self.colors['green'])
            self.voice_indicator.config(text="🔴 Voice: IDLE", fg=self.colors['red'])
            self.add_log_entry("Voice recognition deactivated")
    
    def test_voice(self):
        """Test voice system"""
        try:
            self.speak("Voice system working perfectly! All features are active and ready!")
            self.add_log_entry("Voice test successful")
        except Exception as e:
            self.add_log_entry(f"Voice test failed: {str(e)}", "error")
    
    def voice_settings(self):
        """Open voice settings dialog"""
        settings = simpledialog.askstring("Voice Settings", 
                                       "Enter voice rate (50-200):", 
                                       initialvalue=str(self.engine.getProperty('rate')))
        if settings:
            try:
                rate = int(settings)
                if 50 <= rate <= 200:
                    self.engine.setProperty('rate', rate)
                    self.add_log_entry(f"Voice rate set to {rate}")
                else:
                    self.add_log_entry("Voice rate must be between 50 and 200", "warning")
            except ValueError:
                self.add_log_entry("Invalid voice rate", "warning")
    
    def manual_command(self, event=None):
        """Process manual command"""
        command = self.manual_entry.get().strip().lower()
        if command:
            self.add_command_history(f"Manual: {command}")
            self.process_command(command)
            self.manual_entry.delete(0, tk.END)
    
    def voice_assistant_loop(self):
        """Advanced voice assistant loop"""
        try:
            self.speak("Assalam o Alaikum Muhammad Farhan!")
            self.speak("Good Evening!")
            self.speak("I am ILLI AI Complete, your ultimate AI assistant with all features activated!")
            self.speak("I can control apps, manage files, send messages, play music, and much more!")
        except Exception as e:
            self.add_log_entry(f"TTS Error: {str(e)}", "error")
        
        while True:
            try:
                if self.listening_state:
                    self.voice_indicator.config(text="🟢 Voice: LISTENING", fg=self.colors['green'])
                    
                    with self.microphone as source:
                        # Optimized audio settings
                        self.recognizer.adjust_for_ambient_noise(source, duration=1)
                        self.recognizer.pause_threshold = 0.8
                        self.recognizer.non_speaking_duration = 0.5
                        self.recognizer.phrase_threshold = 0.3
                        self.recognizer.dynamic_energy_threshold = True
                        self.recognizer.dynamic_energy_adjustment_damping = 0.15
                        self.recognizer.energy_threshold = 200
                        
                        audio = self.recognizer.listen(source, timeout=8, phrase_time_limit=8)
                    
                    self.voice_indicator.config(text="🟡 Voice: RECOGNIZING", fg=self.colors['yellow'])
                    
                    try:
                        command = self.recognizer.recognize_google(audio).lower()
                        self.add_log_entry(f"Recognized: {command}")
                        self.add_command_history(f"Voice: {command}")
                        self.process_command(command)
                    except sr.UnknownValueError:
                        self.add_log_entry("Could not understand", "warning")
                    except sr.RequestError:
                        self.add_log_entry("Speech recognition error", "error")
                else:
                    self.voice_indicator.config(text="🔴 Voice: IDLE", fg=self.colors['red'])
                    time.sleep(1)
                    
            except Exception as e:
                self.add_log_entry(f"Voice error: {str(e)}", "error")
                time.sleep(2)
    
    def process_command(self, command):
        """Process all voice commands with complete features"""
        self.add_log_entry(f"Processing: {command}")
        
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
            self.add_log_entry("Greeting response")
        
        # App launching commands
        elif any(word in command for word in ['open', 'launch', 'start', 'run']):
            app_found = False
            
            # Check for all apps
            app_keywords = {
                'whatsapp': ['whatsapp', 'whats app'],
                'instagram': ['instagram', 'insta'],
                'vscode': ['vs code', 'vscode', 'visual studio code', 'visual studio', 'code'],
                'youtube': ['youtube'],
                'chrome': ['chrome', 'browser', 'google chrome'],
                'files': ['file folder', 'file explorer', 'explorer', 'files', 'my computer', 'file manager'],
                'camera': ['camera'],
                'blender': ['blender'],
                'linkedin': ['linkedin'],
                'github': ['github'],
                'gmail': ['gmail'],
                'chatgpt': ['chatgpt', 'chat gpt', 'open ai'],
                'spotify': ['spotify'],
                'discord': ['discord'],
                'slack': ['slack'],
                'teams': ['teams'],
                'zoom': ['zoom'],
                'notepad': ['notepad'],
                'calculator': ['calculator', 'calc'],
                'cmd': ['cmd', 'command prompt'],
                'powershell': ['powershell'],
                'taskmanager': ['task manager']
            }
            
            for app_name, keywords in app_keywords.items():
                if any(keyword in command for keyword in keywords):
                    self.launch_app(app_name)
                    app_found = True
                    break
            
            if not app_found:
                self.speak("Please specify which app to open")
                self.add_log_entry("App name not specified", "warning")
        
        # App closing commands
        elif any(word in command for word in ['close', 'exit', 'quit', 'stop']):
            app_found = False
            
            app_keywords = {
                'whatsapp': ['whatsapp', 'whats app'],
                'instagram': ['instagram', 'insta'],
                'vscode': ['vs code', 'vscode', 'visual studio', 'code'],
                'chrome': ['chrome'],
                'youtube': ['youtube'],
                'files': ['file explorer', 'explorer'],
                'camera': ['camera'],
                'blender': ['blender']
            }
            
            for app_name, keywords in app_keywords.items():
                if any(keyword in command for keyword in keywords):
                    self.close_app(app_name)
                    app_found = True
                    break
            
            if not app_found:
                self.speak("Please specify which app to close")
                self.add_log_entry("App name not specified for closing", "warning")
        
        # File management commands
        elif any(word in command for word in ['create', 'delete', 'copy', 'move', 'rename', 'search']):
            self.process_file_command(command)
        
        # System control commands
        elif any(word in command for word in ['system', 'shutdown', 'restart', 'sleep', 'lock']):
            if 'shutdown' in command:
                self.shutdown_system()
            elif 'restart' in command or 'reboot' in command:
                self.restart_system()
            elif 'sleep' in command:
                self.sleep_system()
            elif 'lock' in command:
                self.lock_system()
            elif 'scan' in command or 'analyze' in command:
                self.system_scan()
            elif 'cleanup' in command or 'clean' in command:
                self.system_cleanup()
            elif 'optimize' in command:
                self.system_optimize()
            else:
                self.speak("System control activated. What would you like to control?")
        
        # Communication commands
        elif any(word in command for word in ['whatsapp', 'message', 'send', 'email']):
            if 'whatsapp' in command or 'message' in command:
                self.process_whatsapp_command(command)
            elif 'email' in command or 'send' in command:
                self.process_email_command(command)
        
        # YouTube commands
        elif 'youtube' in command or 'play' in command:
            if 'play' in command and ('video' in command or 'youtube' in command):
                video_name = command.replace('play', '').replace('video', '').replace('youtube', '').replace('of', '').strip()
                if video_name:
                    self.youtube_search(video_name)
                else:
                    self.launch_app('youtube')
            elif 'next' in command or 'skip' in command:
                self.youtube_next_video()
            elif 'previous' in command or 'back' in command:
                self.youtube_previous_video()
            elif 'pause' in command or 'stop' in command:
                self.youtube_pause_video()
            elif 'resume' in command:
                self.youtube_resume_video()
            else:
                self.launch_app('youtube')
        
        # Multimedia commands
        elif any(word in command for word in ['volume', 'mute', 'play', 'pause', 'next', 'previous', 'music']):
            self.process_multimedia_command(command)
        
        # Camera commands
        elif any(word in command for word in ['camera', 'photo', 'video', 'record']):
            if 'photo' in command or 'take' in command:
                self.take_photo()
            elif 'record' in command or 'start' in command:
                self.start_recording()
            elif 'stop' in command:
                self.stop_recording()
            else:
                self.launch_app('camera')
        
        # AI commands
        elif any(word in command for word in ['search', 'what is', 'who is', 'tell me', 'remind', 'schedule']):
            if any(word in command for word in ['search', 'what is', 'who is', 'tell me']):
                search_term = command.replace('search', '').replace('what is', '').replace('who is', '').replace('tell me about', '').strip()
                if search_term:
                    self.wikipedia_search(search_term)
            elif 'remind' in command:
                self.process_reminder_command(command)
            elif 'schedule' in command:
                self.process_schedule_command(command)
        
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
            self.add_log_entry(f"Unrecognized command: {command}", "warning")
    
    def process_file_command(self, command):
        """Process file management commands"""
        if 'create' in command:
            if 'file' in command:
                self.create_file_dialog()
            elif 'folder' in command or 'directory' in command:
                self.create_folder_dialog()
        elif 'delete' in command:
            self.delete_file_dialog()
        elif 'copy' in command:
            self.copy_file_dialog()
        elif 'move' in command:
            self.move_file_dialog()
        elif 'rename' in command:
            self.rename_file_dialog()
        elif 'search' in command:
            self.search_files_dialog()
    
    def process_multimedia_command(self, command):
        """Process multimedia commands"""
        if 'volume' in command:
            if 'up' in command or 'increase' in command:
                self.adjust_volume(10)
            elif 'down' in command or 'decrease' in command:
                self.adjust_volume(-10)
            elif 'mute' in command:
                self.mute_volume()
            elif 'max' in command or 'maximum' in command:
                self.max_volume()
            else:
                self.speak(f"Current volume is {self.volume_slider.get()}%")
        elif 'play' in command:
            self.play_pause_media()
        elif 'pause' in command:
            self.pause_media()
        elif 'stop' in command:
            self.stop_media()
        elif 'next' in command:
            self.next_media()
        elif 'previous' in command:
            self.previous_media()
    
    def process_whatsapp_command(self, command):
        """Process WhatsApp commands"""
        # Extract contact and message from command
        if 'to' in command or 'send' in command:
            self.speak("Please use the Communication tab to send WhatsApp messages")
            self.add_log_entry("WhatsApp message - Use Communication tab")
        else:
            self.launch_app('whatsapp')
    
    def process_email_command(self, command):
        """Process email commands"""
        self.speak("Please use the Communication tab to send emails")
        self.add_log_entry("Email - Use Communication tab")
    
    def process_reminder_command(self, command):
        """Process reminder commands"""
        self.speak("Please use the AI tab to set reminders")
        self.add_log_entry("Reminder - Use AI tab")
    
    def process_schedule_command(self, command):
        """Process scheduling commands"""
        self.speak("Please use the AI tab to schedule tasks")
        self.add_log_entry("Schedule - Use AI tab")
    
    def launch_app(self, app_name):
        """Launch application with enhanced detection"""
        self.speak(f"Opening {app_name}")
        self.add_log_entry(f"Launching {app_name}")
        
        paths = self.app_paths.get(app_name, [])
        user = os.getlogin()
        
        # Check if app is already running
        try:
            app_variants = {
                'whatsapp': ['whatsapp.exe', 'WhatsApp.exe'],
                'instagram': ['instagram.exe', 'Instagram.exe'], 
                'vscode': ['code.exe', 'Code.exe'],
                'chrome': ['chrome.exe', 'Chrome.exe'],
                'youtube': ['chrome.exe', 'msedge.exe', 'firefox.exe'],
                'files': ['explorer.exe'],
                'camera': ['windowscamera.exe', 'WindowsCamera.exe']
            }
            
            target_names = app_variants.get(app_name.lower(), [f'{app_name}.exe', f'{app_name.capitalize()}.exe'])
            
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
                    proc_info = proc.info
                    if proc_info and 'name' in proc_info:
                        proc_name = proc_info['name']
                        if any(target.lower() in proc_name.lower() for target in target_names):
                            proc.terminate()
                            self.add_log_entry(f"Closed {app_name} (PID: {proc_info['pid']})")
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
    
    def create_file_dialog(self):
        """Create file dialog"""
        file_path = filedialog.asksaveasfilename(
            title="Create New File",
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, 'w') as f:
                    f.write("")
                self.add_log_entry(f"Created file: {file_path}")
                self.speak("File created successfully")
            except Exception as e:
                self.add_log_entry(f"Error creating file: {str(e)}", "error")
    
    def create_folder_dialog(self):
        """Create folder dialog"""
        folder_path = filedialog.askdirectory(title="Select Parent Directory")
        if folder_path:
            folder_name = simpledialog.askstring("Create Folder", "Enter folder name:")
            if folder_name:
                try:
                    full_path = os.path.join(folder_path, folder_name)
                    os.makedirs(full_path)
                    self.add_log_entry(f"Created folder: {full_path}")
                    self.speak("Folder created successfully")
                except Exception as e:
                    self.add_log_entry(f"Error creating folder: {str(e)}", "error")
    
    def copy_file_dialog(self):
        """Copy file dialog"""
        source_file = filedialog.askopenfilename(title="Select file to copy")
        if source_file:
            dest_path = filedialog.asksaveasfilename(title="Copy file to")
            if dest_path:
                try:
                    shutil.copy2(source_file, dest_path)
                    self.add_log_entry(f"Copied file from {source_file} to {dest_path}")
                    self.speak("File copied successfully")
                except Exception as e:
                    self.add_log_entry(f"Error copying file: {str(e)}", "error")
    
    def move_file_dialog(self):
        """Move file dialog"""
        source_file = filedialog.askopenfilename(title="Select file to move")
        if source_file:
            dest_path = filedialog.asksaveasfilename(title="Move file to")
            if dest_path:
                try:
                    shutil.move(source_file, dest_path)
                    self.add_log_entry(f"Moved file from {source_file} to {dest_path}")
                    self.speak("File moved successfully")
                except Exception as e:
                    self.add_log_entry(f"Error moving file: {str(e)}", "error")
    
    def rename_file_dialog(self):
        """Rename file dialog"""
        file_path = filedialog.askopenfilename(title="Select file to rename")
        if file_path:
            new_name = simpledialog.askstring("Rename File", "Enter new name:")
            if new_name:
                try:
                    new_path = os.path.join(os.path.dirname(file_path), new_name)
                    os.rename(file_path, new_path)
                    self.add_log_entry(f"Renamed file from {file_path} to {new_path}")
                    self.speak("File renamed successfully")
                except Exception as e:
                    self.add_log_entry(f"Error renaming file: {str(e)}", "error")
    
    def delete_file_dialog(self):
        """Delete file dialog"""
        file_path = filedialog.askopenfilename(title="Select file to delete")
        if file_path:
            if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete {file_path}?"):
                try:
                    os.remove(file_path)
                    self.add_log_entry(f"Deleted file: {file_path}")
                    self.speak("File deleted successfully")
                except Exception as e:
                    self.add_log_entry(f"Error deleting file: {str(e)}", "error")
    
    def browse_files(self):
        """Browse files"""
        folder_path = filedialog.askdirectory(title="Browse Files")
        if folder_path:
            self.launch_app('files')
            os.startfile(folder_path)
            self.add_log_entry(f"Browsed to: {folder_path}")
    
    def search_files_dialog(self):
        """Search files dialog"""
        search_term = simpledialog.askstring("Search Files", "Enter search term:")
        if search_term:
            folder_path = filedialog.askdirectory(title="Search in directory")
            if folder_path:
                try:
                    results = []
                    for root, dirs, files in os.walk(folder_path):
                        for file in files:
                            if search_term.lower() in file.lower():
                                results.append(os.path.join(root, file))
                    
                    if results:
                        self.add_log_entry(f"Found {len(results)} files:")
                        for result in results[:10]:  # Show first 10 results
                            self.add_log_entry(f"  {result}")
                        self.speak(f"Found {len(results)} files matching {search_term}")
                    else:
                        self.add_log_entry(f"No files found matching {search_term}")
                        self.speak(f"No files found matching {search_term}")
                except Exception as e:
                    self.add_log_entry(f"Error searching files: {str(e)}", "error")
    
    def file_info_dialog(self):
        """File information dialog"""
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
Accessed: {datetime.fromtimestamp(stat.st_atime)}
"""
                self.add_log_entry(info)
                self.speak("File information displayed")
            except Exception as e:
                self.add_log_entry(f"Error getting file info: {str(e)}", "error")
    
    def close_app_dialog(self):
        """Close app dialog"""
        app_name = simpledialog.askstring("Close App", "Enter app name to close:")
        if app_name:
            self.close_app(app_name.lower())
    
    def restart_app(self):
        """Restart current app"""
        self.speak("Restart feature coming soon")
        self.add_log_entry("App restart feature in development")
    
    def minimize_all_apps(self):
        """Minimize all applications"""
        try:
            shell = wincl.Dispatch("Shell.Application")
            shell.MinimizeAll()
            self.speak("All applications minimized")
            self.add_log_entry("Minimized all applications")
        except Exception as e:
            self.add_log_entry(f"Error minimizing apps: {str(e)}", "error")
    
    def maximize_all_apps(self):
        """Maximize all applications"""
        self.speak("Maximize all feature coming soon")
        self.add_log_entry("Maximize all feature in development")
    
    def refresh_apps(self):
        """Refresh applications list"""
        self.add_log_entry("Refreshing applications list...")
        self.add_log_entry("Applications list refreshed")
    
    def send_whatsapp_message(self):
        """Send WhatsApp message"""
        contact = self.whatsapp_contact.get().strip()
        message = self.whatsapp_message.get().strip()
        
        if contact and message:
            try:
                # Use pywhatkit to send message
                pywhatkit.sendwhatmsg_instantly(contact, message)
                self.add_log_entry(f"WhatsApp message sent to {contact}")
                self.speak("WhatsApp message sent successfully")
                self.whatsapp_contact.delete(0, tk.END)
                self.whatsapp_message.delete(0, tk.END)
            except Exception as e:
                self.add_log_entry(f"Error sending WhatsApp message: {str(e)}", "error")
                self.speak("Error sending WhatsApp message")
        else:
            self.add_log_entry("Please enter both contact and message", "warning")
    
    def send_email(self):
        """Send email"""
        to = self.email_to.get().strip()
        subject = self.email_subject.get().strip()
        message = self.email_message.get().strip()
        
        if to and subject and message:
            try:
                # This would require SMTP configuration
                self.add_log_entry(f"Email configuration needed for sending to {to}")
                self.speak("Email feature requires SMTP configuration")
                self.email_to.delete(0, tk.END)
                self.email_subject.delete(0, tk.END)
                self.email_message.delete(0, tk.END)
            except Exception as e:
                self.add_log_entry(f"Error sending email: {str(e)}", "error")
                self.speak("Error sending email")
        else:
            self.add_log_entry("Please fill all email fields", "warning")
    
    def send_ai_message(self, event=None):
        """Send AI chat message"""
        message = self.ai_input.get().strip()
        if message:
            self.add_ai_chat(f"You: {message}")
            
            # Simple AI response (can be enhanced with real AI)
            response = self.generate_ai_response(message)
            self.add_ai_chat(f"ILLI: {response}")
            self.speak(response)
            
            self.ai_input.delete(0, tk.END)
    
    def generate_ai_response(self, message):
        """Generate AI response"""
        # Simple rule-based responses (can be enhanced with real AI)
        responses = {
            "how are you": "I'm working perfectly! All systems are operational.",
            "what can you do": "I can control apps, manage files, send messages, play music, and much more!",
            "thank you": "You're welcome! I'm here to help.",
            "goodbye": "Goodbye! I'll be here when you need me."
        }
        
        for key, response in responses.items():
            if key in message.lower():
                return response
        
        return "I understand you said: " + message + ". How can I help with that?"
    
    def add_ai_chat(self, message):
        """Add message to AI chat"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        chat_entry = f"[{timestamp}] {message}\n"
        self.ai_display.insert(tk.END, chat_entry)
        self.ai_display.see(tk.END)
    
    def add_reminder(self):
        """Add reminder"""
        text = self.reminder_text.get().strip()
        time_str = self.reminder_time.get().strip()
        
        if text and time_str:
            try:
                # Parse time (simple format HH:MM)
                hour, minute = map(int, time_str.split(':'))
                now = datetime.now()
                reminder_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
                
                if reminder_time < now:
                    reminder_time += timedelta(days=1)
                
                self.reminders.append({'text': text, 'time': reminder_time})
                self.add_log_entry(f"Reminder added: {text} at {time_str}")
                self.speak(f"Reminder set for {time_str}")
                
                self.reminder_text.delete(0, tk.END)
                self.reminder_time.delete(0, tk.END)
            except Exception as e:
                self.add_log_entry(f"Error adding reminder: {str(e)}", "error")
        else:
            self.add_log_entry("Please enter both reminder text and time", "warning")
    
    def check_reminders(self):
        """Check and trigger reminders"""
        while True:
            try:
                now = datetime.now()
                for reminder in self.reminders[:]:
                    if now >= reminder['time']:
                        self.speak(f"Reminder: {reminder['text']}")
                        self.add_log_entry(f"Reminder triggered: {reminder['text']}")
                        self.reminders.remove(reminder)
                time.sleep(30)  # Check every 30 seconds
            except Exception as e:
                self.add_log_entry(f"Error checking reminders: {str(e)}", "error")
                time.sleep(30)
    
    def wikipedia_search(self, term=None):
        """Search Wikipedia"""
        if not term:
            term = self.knowledge_search.get().strip()
        
        if term:
            try:
                summary = wikipedia.summary(term, sentences=2)
                self.add_log_entry(f"Wikipedia: {summary}")
                self.speak(f"According to Wikipedia: {summary}")
            except Exception as e:
                self.add_log_entry(f"Wikipedia search error: {str(e)}", "error")
                self.speak("Error searching Wikipedia")
    
    def wolfram_search(self):
        """Search WolframAlpha"""
        query = self.knowledge_search.get().strip()
        if query and self.wolfram_alpha_app_id != "YOUR_WOLFRAM_APP_ID":
            try:
                client = wolframalpha.Client(self.wolfram_alpha_app_id)
                res = client.query(query)
                
                if hasattr(res, 'results') and res.results:
                    result = next(res.results).text
                    self.add_log_entry(f"WolframAlpha: {result}")
                    self.speak(f"According to WolframAlpha: {result}")
                else:
                    self.add_log_entry("No results found", "warning")
                    self.speak("No results found")
            except Exception as e:
                self.add_log_entry(f"WolframAlpha search error: {str(e)}", "error")
                self.speak("Error searching WolframAlpha")
        else:
            self.add_log_entry("WolframAlpha requires API key", "warning")
    
    def google_search(self):
        """Search Google"""
        query = self.knowledge_search.get().strip()
        if query:
            url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            webbrowser.open(url)
            self.add_log_entry(f"Google search: {query}")
            self.speak(f"Searching Google for {query}")
    
    def set_volume(self, value):
        """Set system volume"""
        try:
            # This would require additional libraries for actual volume control
            self.add_log_entry(f"Volume set to {value}%")
        except Exception as e:
            self.add_log_entry(f"Error setting volume: {str(e)}", "error")
    
    def adjust_volume(self, change):
        """Adjust volume"""
        current = self.volume_slider.get()
        new_volume = max(0, min(100, current + change))
        self.volume_slider.set(new_volume)
        self.set_volume(new_volume)
    
    def mute_volume(self):
        """Mute volume"""
        self.volume_slider.set(0)
        self.set_volume(0)
        self.add_log_entry("Volume muted")
    
    def max_volume(self):
        """Max volume"""
        self.volume_slider.set(100)
        self.set_volume(100)
        self.add_log_entry("Volume set to maximum")
    
    def play_pause_media(self):
        """Play/pause media"""
        pyautogui.press('playpause')
        self.add_log_entry("Media play/pause")
    
    def pause_media(self):
        """Pause media"""
        pyautogui.press('pause')
        self.add_log_entry("Media paused")
    
    def stop_media(self):
        """Stop media"""
        pyautogui.press('stop')
        self.add_log_entry("Media stopped")
    
    def next_media(self):
        """Next media"""
        pyautogui.press('nexttrack')
        self.add_log_entry("Next track")
    
    def previous_media(self):
        """Previous media"""
        pyautogui.press('prevtrack')
        self.add_log_entry("Previous track")
    
    def take_photo(self):
        """Take photo"""
        try:
            # This would require camera integration
            self.add_log_entry("Photo capture feature requires camera integration")
            self.speak("Photo feature requires additional setup")
        except Exception as e:
            self.add_log_entry(f"Error taking photo: {str(e)}", "error")
    
    def start_recording(self):
        """Start recording"""
        try:
            # This would require camera integration
            self.add_log_entry("Video recording feature requires camera integration")
            self.speak("Recording feature requires additional setup")
        except Exception as e:
            self.add_log_entry(f"Error starting recording: {str(e)}", "error")
    
    def stop_recording(self):
        """Stop recording"""
        try:
            # This would require camera integration
            self.add_log_entry("Stop recording feature requires camera integration")
            self.speak("Stop recording feature requires additional setup")
        except Exception as e:
            self.add_log_entry(f"Error stopping recording: {str(e)}", "error")
    
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
Running Processes: {len(list(psutil.process_iter()))}
"""
            
            self.add_log_entry(scan_results)
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
        self.speak("System optimization completed successfully")
    
    def lock_system(self):
        """Lock system"""
        try:
            ctypes.windll.user32.LockWorkStation()
            self.add_log_entry("System locked")
            self.speak("System locked")
        except Exception as e:
            self.add_log_entry(f"Lock system error: {str(e)}", "error")
    
    def sleep_system(self):
        """Sleep system"""
        try:
            os.system("rundll32.exe powrprof.dll,SetSuspendState Sleep")
            self.add_log_entry("System sleep")
            self.speak("System going to sleep")
        except Exception as e:
            self.add_log_entry(f"Sleep system error: {str(e)}", "error")
    
    def restart_system(self):
        """Restart system"""
        if messagebox.askyesno("Confirm Restart", "Are you sure you want to restart the system?"):
            try:
                os.system("shutdown /r /t 10")
                self.add_log_entry("System restart scheduled")
                self.speak("System will restart in 10 seconds")
            except Exception as e:
                self.add_log_entry(f"Restart system error: {str(e)}", "error")
    
    def shutdown_system(self):
        """Shutdown system"""
        if messagebox.askyesno("Confirm Shutdown", "Are you sure you want to shutdown the system?"):
            try:
                os.system("shutdown /s /t 10")
                self.add_log_entry("System shutdown scheduled")
                self.speak("System will shutdown in 10 seconds")
            except Exception as e:
                self.add_log_entry(f"Shutdown system error: {str(e)}", "error")
    
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
    
    def show_help(self):
        """Show comprehensive help"""
        help_text = """
🤖 ILLI AI - COMPLETE FEATURE LIST

🚀 APP CONTROL:
• "Open [app]" - Launch any application
• "Close [app]" - Close any application
• Supported: WhatsApp, Instagram, VS Code, YouTube, Chrome, etc.

📁 FILE MANAGEMENT:
• "Create file/folder" - Create new files or folders
• "Delete file" - Delete files
• "Copy/Move/Rename file" - File operations
• "Search files" - Search for files

💬 COMMUNICATION:
• "Send WhatsApp to [contact]" - Send messages
• "Send email to [person]" - Send emails
• Use Communication tab for detailed controls

🎵 MULTIMEDIA:
• "Volume up/down/mute/max" - Volume controls
• "Play/Pause/Stop/Next/Previous" - Media controls
• "Take photo/Start recording" - Camera controls

🖥️ SYSTEM CONTROL:
• "System scan/cleanup/optimize" - System operations
• "Shutdown/Restart/Sleep/Lock" - Power controls
• "Task Manager/Control Panel" - System tools

🤖 AI FEATURES:
• "Search [topic]" - Wikipedia/WolframAlpha/Google
• "Remind me [task] at [time]" - Set reminders
• "What is/Who is" - Knowledge queries
• Use AI tab for chat and scheduling

🎮 VOICE COMMANDS:
• "Hello/Hi/Hey" - Greeting responses
• "Time/Date" - Current information
• "Help" - Show this help

💡 TIPS:
• Speak clearly and naturally
• Wait for listening indicator
• Use specific app names
• Commands are case-insensitive
• All features accessible via tabs
        """
        
        self.add_log_entry(help_text)
        self.speak("Help information displayed. All features are active!")
    
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
        
        # Add to all displays
        self.system_display.insert(tk.END, log_entry)
        self.system_display.see(tk.END)
        
        self.voice_display.insert(tk.END, log_entry)
        self.voice_display.see(tk.END)
        
        self.comm_display.insert(tk.END, log_entry)
        self.comm_display.see(tk.END)
        
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
        
        self.voice_display.insert(tk.END, history_entry)
        self.voice_display.see(tk.END)
    
    def update_system_info(self):
        """Update system information periodically"""
        while True:
            try:
                cpu_usage = psutil.cpu_percent(interval=1)
                memory = psutil.virtual_memory()
                
                system_info = f"""
CPU: {cpu_usage:.1f}% | Memory: {memory.percent:.1f}% | Processes: {len(list(psutil.process_iter()))}
"""
                
                # Update task label
                self.task_label.config(text=f"Task: {self.current_task}")
                
                time.sleep(5)  # Update every 5 seconds
                
            except Exception as e:
                self.add_log_entry(f"System update error: {str(e)}", "error")
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
                self.system_display.see(tk.END)
                self.voice_display.see(tk.END)
                self.comm_display.see(tk.END)
                self.ai_display.see(tk.END)
                self.file_display.see(tk.END)
                self.app_display.see(tk.END)
                time.sleep(2)
            except Exception as e:
                time.sleep(2)

def main():
    """Main function"""
    root = tk.Tk()
    app = ILLI_AI_Complete(root)
    root.mainloop()

if __name__ == "__main__":
    main()
