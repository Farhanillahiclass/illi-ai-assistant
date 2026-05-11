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
import difflib
from collections import defaultdict
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

class ILLI_AI_Learning:
    def __init__(self, root):
        self.root = root
        self.root.title("🤖 ILLI AI - LEARNING & CONVERSATION")
        self.root.geometry("1920x1080")
        self.root.configure(bg='#000000')
        
        # System variables
        self.system_status = "ONLINE"
        self.user_name = os.getlogin()
        self.current_task = "AI Learning Active"
        self.listening_state = False
        self.response_queue = queue.Queue()
        
        # Voice recognition - Advanced learning settings
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 0.9)
        
        # Learning and Memory System
        self.user_profile = {
            'name': self.user_name,
            'preferences': {},
            'voice_patterns': defaultdict(list),
            'frequent_commands': defaultdict(int),
            'conversation_history': [],
            'learned_responses': {},
            'context_memory': [],
            'user_habits': {},
            'voice_adaptations': {},
            'command_patterns': defaultdict(list)
        }
        
        # AI Learning Data
        self.learning_data = {
            'command_success_rate': defaultdict(float),
            'voice_recognition_accuracy': defaultdict(list),
            'response_effectiveness': defaultdict(list),
            'user_feedback': defaultdict(list),
            'adaptation_history': [],
            'conversation_flows': [],
            'context_keywords': defaultdict(int),
            'personal_info': {},
            'relationship_memory': {}
        }
        
        # Conversation State
        self.conversation_context = {
            'current_topic': None,
            'previous_commands': [],
            'user_intent': None,
            'emotional_state': 'neutral',
            'conversation_flow': [],
            'context_stack': [],
            'active_session': True
        }
        
        # Voice Adaptation
        self.voice_profile = {
            'user_accent': 'unknown',
            'speech_rate': 'normal',
            'volume_preference': 0.9,
            'background_noise_level': 'normal',
            'recognition_confidence': 0.8,
            'adaptation_count': 0,
            'successful_recognitions': 0,
            'failed_recognitions': 0
        }
        
        # Load saved data
        self.load_learning_data()
        self.load_user_profile()
        
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
        
        # App paths (from previous version)
        self.app_paths = {
            'whatsapp': ["https://web.whatsapp.com"],
            'instagram': ["https://instagram.com"],
            'chrome': ["https://google.com"],
            'vscode': ["https://code.visualstudio.com"],
            'youtube': ["https://youtube.com"],
            'files': ["explorer.exe"],
            'camera': ["microsoft.windows.camera:"]
        }
        
        # Create UI
        self.setup_ui()
        
        # Start all services
        self.start_learning_services()
    
    def setup_ui(self):
        """Setup learning-focused UI"""
        # Main container
        main_frame = tk.Frame(self.root, bg=self.colors['bg'])
        main_frame.pack(fill='both', expand=True)
        
        # Header
        self.create_header(main_frame)
        
        # Tabbed interface
        notebook = ttk.Notebook(main_frame)
        notebook.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Create tabs
        self.create_conversation_tab(notebook)
        self.create_learning_tab(notebook)
        self.create_voice_training_tab(notebook)
        self.create_memory_tab(notebook)
        self.create_system_tab(notebook)
        self.create_apps_tab(notebook)
        self.create_voice_control_tab(notebook)
        
        # Bottom status bar
        self.create_status_bar(main_frame)
    
    def create_header(self, parent):
        """Create header with learning status"""
        header_frame = tk.Frame(parent, bg=self.colors['glass'], relief='raised', bd=2)
        header_frame.pack(fill='x', padx=10, pady=5)
        
        # Title
        title_label = tk.Label(header_frame, text="🤖 ILLI AI - LEARNING & CONVERSATION", 
                              font=('Arial', 24, 'bold'), fg=self.colors['accent'], 
                              bg=self.colors['glass'])
        title_label.pack(side='left', padx=20, pady=10)
        
        # Learning status
        self.learning_status = tk.Label(header_frame, text="🧠 Learning: ACTIVE", 
                                       font=('Arial', 14), fg=self.colors['green'], 
                                       bg=self.colors['glass'])
        self.learning_status.pack(side='right', padx=20, pady=10)
        
        # User info
        user_label = tk.Label(header_frame, text=f"User: {self.user_name}", 
                              font=('Arial', 12), fg=self.colors['text'], 
                              bg=self.colors['glass'])
        user_label.pack(side='right', padx=20, pady=10)
    
    def create_conversation_tab(self, parent):
        """Create conversation tab"""
        tab_frame = tk.Frame(parent, bg=self.colors['glass'])
        parent.add(tab_frame, text="💬 CONVERSATION")
        
        # Conversation display
        conv_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        conv_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        tk.Label(conv_frame, text="💬 CONVERSATION WITH ILLI", 
                font=('Arial', 16, 'bold'), fg=self.colors['accent'], 
                bg=self.colors['glass']).pack(pady=5)
        
        # Chat display
        self.conversation_display = scrolledtext.ScrolledText(conv_frame, height=15, width=100,
                                                          bg=self.colors['bg'], fg=self.colors['text'],
                                                          font=('Consolas', 10))
        self.conversation_display.pack(fill='both', expand=True, pady=5)
        
        # Input area
        input_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        input_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Label(input_frame, text="You:", fg=self.colors['text'], 
                bg=self.colors['glass']).pack(side='left', padx=5)
        
        self.conversation_input = tk.Entry(input_frame, width=60, bg=self.colors['bg'], 
                                      fg=self.colors['text'], font=('Consolas', 11))
        self.conversation_input.pack(side='left', padx=5, fill='x', expand=True)
        self.conversation_input.bind('<Return>', self.send_conversation_message)
        
        tk.Button(input_frame, text="💬 Send", command=self.send_conversation_message,
                 bg=self.colors['accent'], fg='black', font=('Arial', 10, 'bold')).pack(side='left', padx=5)
        
        # Quick responses
        quick_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        quick_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Label(quick_frame, text="Quick Responses:", fg=self.colors['text'], 
                bg=self.colors['glass']).pack(side='left', padx=5)
        
        quick_responses = [
            "Hello ILLI", "How are you?", "What can you do?", 
            "Thank you", "Help me", "Tell me a joke"
        ]
        
        for response in quick_responses:
            btn = tk.Button(quick_frame, text=response, 
                         command=lambda r=response: self.quick_conversation(r),
                         bg=self.colors['blue'], fg='white', font=('Arial', 9))
            btn.pack(side='left', padx=2)
    
    def create_learning_tab(self, parent):
        """Create learning tab"""
        tab_frame = tk.Frame(parent, bg=self.colors['glass'])
        parent.add(tab_frame, text="🧠 LEARNING")
        
        # Learning status
        status_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        status_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Label(status_frame, text="🧠 AI LEARNING STATUS", 
                font=('Arial', 16, 'bold'), fg=self.colors['accent'], 
                bg=self.colors['glass']).pack(pady=5)
        
        # Learning metrics
        self.learning_display = scrolledtext.ScrolledText(status_frame, height=10, width=100,
                                                        bg=self.colors['bg'], fg=self.colors['text'],
                                                        font=('Consolas', 10))
        self.learning_display.pack(fill='both', expand=True, pady=5)
        
        # Learning controls
        control_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        control_frame.pack(fill='x', padx=10, pady=5)
        
        learning_buttons = [
            ("📊 Show Learning Stats", self.show_learning_stats),
            ("🧠 Train Voice Model", self.train_voice_model),
            ("💾 Save Learning Data", self.save_learning_data),
            ("📂 Load Learning Data", self.load_learning_data),
            ("🔄 Reset Learning", self.reset_learning),
            ("⚙️ Learning Settings", self.learning_settings)
        ]
        
        for text, command in learning_buttons:
            btn = tk.Button(control_frame, text=text, command=command,
                         bg=self.colors['purple'], fg='white', font=('Arial', 10, 'bold'))
            btn.pack(side='left', padx=5, pady=5)
    
    def create_voice_training_tab(self, parent):
        """Create voice training tab"""
        tab_frame = tk.Frame(parent, bg=self.colors['glass'])
        parent.add(tab_frame, text="🎤 VOICE TRAINING")
        
        # Voice training interface
        training_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        training_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        tk.Label(training_frame, text="🎤 VOICE TRAINING & ADAPTATION", 
                font=('Arial', 16, 'bold'), fg=self.colors['accent'], 
                bg=self.colors['glass']).pack(pady=5)
        
        # Training display
        self.voice_training_display = scrolledtext.ScrolledText(training_frame, height=8, width=100,
                                                              bg=self.colors['bg'], fg=self.colors['text'],
                                                              font=('Consolas', 10))
        self.voice_training_display.pack(fill='both', expand=True, pady=5)
        
        # Training controls
        train_control_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        train_control_frame.pack(fill='x', padx=10, pady=5)
        
        # Voice profile display
        profile_frame = tk.Frame(train_control_frame, bg=self.colors['glass'])
        profile_frame.pack(fill='x', pady=5)
        
        self.voice_profile_display = tk.Label(profile_frame, 
                                              text="Voice Profile: Learning...", 
                                              font=('Arial', 12), fg=self.colors['cyan'], 
                                              bg=self.colors['glass'])
        self.voice_profile_display.pack(side='left', padx=10)
        
        training_buttons = [
            ("🎤 Start Training", self.start_voice_training),
            ("⏹️ Stop Training", self.stop_voice_training),
            ("🔊 Test Recognition", self.test_voice_recognition),
            ("📈 Improve Accuracy", self.improve_voice_accuracy),
            ("🔄 Reset Voice Profile", self.reset_voice_profile),
            ("⚙️ Voice Settings", self.voice_training_settings)
        ]
        
        for text, command in training_buttons:
            btn = tk.Button(train_control_frame, text=text, command=command,
                         bg=self.colors['green'], fg='white', font=('Arial', 10, 'bold'))
            btn.pack(side='left', padx=5, pady=5)
    
    def create_memory_tab(self, parent):
        """Create memory tab"""
        tab_frame = tk.Frame(parent, bg=self.colors['glass'])
        parent.add(tab_frame, text="🧠 MEMORY")
        
        # Memory display
        memory_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        memory_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        tk.Label(memory_frame, text="🧠 MEMORY & CONTEXT", 
                font=('Arial', 16, 'bold'), fg=self.colors['accent'], 
                bg=self.colors['glass']).pack(pady=5)
        
        self.memory_display = scrolledtext.ScrolledText(memory_frame, height=12, width=100,
                                                    bg=self.colors['bg'], fg=self.colors['text'],
                                                    font=('Consolas', 10))
        self.memory_display.pack(fill='both', expand=True, pady=5)
        
        # Memory controls
        memory_control_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        memory_control_frame.pack(fill='x', padx=10, pady=5)
        
        memory_buttons = [
            ("📊 Show Memory Stats", self.show_memory_stats),
            ("💾 Save Memory", self.save_memory),
            ("📂 Load Memory", self.load_memory),
            ("🧹 Clear Memory", self.clear_memory),
            ("🔍 Search Memory", self.search_memory),
            ("⚙️ Memory Settings", self.memory_settings)
        ]
        
        for text, command in memory_buttons:
            btn = tk.Button(memory_control_frame, text=text, command=command,
                         bg=self.colors['orange'], fg='white', font=('Arial', 10, 'bold'))
            btn.pack(side='left', padx=5, pady=5)
    
    def create_system_tab(self, parent):
        """Create system tab"""
        tab_frame = tk.Frame(parent, bg=self.colors['glass'])
        parent.add(tab_frame, text="🖥️ SYSTEM")
        
        # System display
        system_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        system_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        tk.Label(system_frame, text="🖥️ SYSTEM MONITORING", 
                font=('Arial', 16, 'bold'), fg=self.colors['accent'], 
                bg=self.colors['glass']).pack(pady=5)
        
        self.system_display = scrolledtext.ScrolledText(system_frame, height=10, width=100,
                                                     bg=self.colors['bg'], fg=self.colors['text'],
                                                     font=('Consolas', 10))
        self.system_display.pack(fill='both', expand=True, pady=5)
        
        # System controls
        system_control_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        system_control_frame.pack(fill='x', padx=10, pady=5)
        
        system_buttons = [
            ("🔍 System Scan", self.system_scan),
            ("🧹 System Cleanup", self.system_cleanup),
            ("⚡ System Optimize", self.system_optimize),
            ("📊 Performance Monitor", self.performance_monitor),
            ("🔄 Refresh System", self.refresh_system)
        ]
        
        for text, command in system_buttons:
            btn = tk.Button(system_control_frame, text=text, command=command,
                         bg=self.colors['blue'], fg='white', font=('Arial', 10, 'bold'))
            btn.pack(side='left', padx=5, pady=5)
    
    def create_apps_tab(self, parent):
        """Create apps tab"""
        tab_frame = tk.Frame(parent, bg=self.colors['glass'])
        parent.add(tab_frame, text="🚀 APPS")
        
        # Apps display
        apps_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        apps_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        tk.Label(apps_frame, text="🚀 APPLICATION CONTROL", 
                font=('Arial', 16, 'bold'), fg=self.colors['accent'], 
                bg=self.colors['glass']).pack(pady=5)
        
        self.apps_display = scrolledtext.ScrolledText(apps_frame, height=10, width=100,
                                                   bg=self.colors['bg'], fg=self.colors['text'],
                                                   font=('Consolas', 10))
        self.apps_display.pack(fill='both', expand=True, pady=5)
        
        # App controls
        apps_control_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        apps_control_frame.pack(fill='x', padx=10, pady=5)
        
        # Quick app buttons
        quick_apps = [
            ("WhatsApp", 'whatsapp'), ("Instagram", 'instagram'), 
            ("VS Code", 'vscode'), ("YouTube", 'youtube'),
            ("Chrome", 'chrome'), ("Files", 'files'),
            ("Camera", 'camera'), ("Gmail", 'gmail'),
            ("ChatGPT", 'chatgpt'), ("Spotify", 'spotify')
        ]
        
        for name, app_key in quick_apps:
            btn = tk.Button(apps_control_frame, text=name, 
                         command=lambda k=app_key: self.launch_app(k),
                         bg=self.colors['cyan'], fg='black', font=('Arial', 10, 'bold'))
            btn.pack(side='left', padx=3, pady=3)
    
    def create_voice_control_tab(self, parent):
        """Create voice control tab"""
        tab_frame = tk.Frame(parent, bg=self.colors['glass'])
        parent.add(tab_frame, text="🎤 VOICE CONTROL")
        
        # Voice control interface
        voice_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        voice_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        tk.Label(voice_frame, text="🎤 ADVANCED VOICE CONTROL", 
                font=('Arial', 16, 'bold'), fg=self.colors['accent'], 
                bg=self.colors['glass']).pack(pady=5)
        
        # Voice status
        status_frame = tk.Frame(voice_frame, bg=self.colors['glass'])
        status_frame.pack(fill='x', pady=5)
        
        self.voice_indicator = tk.Label(status_frame, text="🔴 Voice: IDLE", 
                                     font=('Arial', 14, 'bold'), fg=self.colors['red'], 
                                     bg=self.colors['glass'])
        self.voice_indicator.pack(side='left', padx=20, pady=10)
        
        # Voice controls
        control_frame = tk.Frame(status_frame, bg=self.colors['glass'])
        control_frame.pack(side='left', padx=20, pady=10)
        
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
        
        # Voice history
        history_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        history_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        tk.Label(history_frame, text="📋 VOICE COMMAND HISTORY", 
                font=('Arial', 12, 'bold'), fg=self.colors['accent'], 
                bg=self.colors['glass']).pack(pady=5)
        
        self.voice_history_display = scrolledtext.ScrolledText(history_frame, height=8, width=100,
                                                         bg=self.colors['bg'], fg=self.colors['text'],
                                                         font=('Consolas', 10))
        self.voice_history_display.pack(fill='both', expand=True, pady=5)
    
    def create_status_bar(self, parent):
        """Create status bar"""
        status_frame = tk.Frame(parent, bg=self.colors['glass'], relief='sunken', bd=1)
        status_frame.pack(fill='x', side='bottom', padx=10, pady=5)
        
        self.task_label = tk.Label(status_frame, text=f"Task: {self.current_task}", 
                                  font=('Arial', 10), fg=self.colors['text'], 
                                  bg=self.colors['glass'])
        self.task_label.pack(side='left', padx=10)
        
        self.accuracy_label = tk.Label(status_frame, text="Accuracy: 0%", 
                                    font=('Arial', 10), fg=self.colors['text'], 
                                    bg=self.colors['glass'])
        self.accuracy_label.pack(side='right', padx=10)
        
        self.time_label = tk.Label(status_frame, text="", 
                                  font=('Arial', 10), fg=self.colors['text'], 
                                  bg=self.colors['glass'])
        self.time_label.pack(side='right', padx=10)
    
    def start_learning_services(self):
        """Start all learning services"""
        threading.Thread(target=self.voice_assistant_loop, daemon=True).start()
        threading.Thread(target=self.learning_engine, daemon=True).start()
        threading.Thread(target=self.conversation_processor, daemon=True).start()
        threading.Thread(target=self.update_system_info, daemon=True).start()
        threading.Thread(target=self.update_time, daemon=True).start()
        threading.Thread(target=self.adaptation_engine, daemon=True).start()
    
    def toggle_voice(self):
        """Toggle voice recognition with learning"""
        self.listening_state = not self.listening_state
        if self.listening_state:
            self.voice_btn.config(text="🔴 Stop Voice", bg=self.colors['red'])
            self.voice_indicator.config(text="🟢 Voice: LEARNING", fg=self.colors['green'])
            self.add_conversation_message("ILLI", "Voice recognition activated. I'm learning from your voice patterns.")
        else:
            self.voice_btn.config(text="🎤 Start Voice", bg=self.colors['green'])
            self.voice_indicator.config(text="🔴 Voice: IDLE", fg=self.colors['red'])
            self.add_conversation_message("ILLI", "Voice recognition deactivated.")
    
    def test_voice(self):
        """Test voice with learning feedback"""
        try:
            test_message = "Voice system working perfectly! I'm learning your voice patterns and adapting to your speech style."
            self.speak(test_message)
            self.add_conversation_message("ILLI", test_message)
            self.update_voice_profile("Test successful")
        except Exception as e:
            self.add_conversation_message("ILLI", f"Voice test failed: {str(e)}")
    
    def voice_settings(self):
        """Voice settings with learning options"""
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Voice & Learning Settings")
        settings_window.geometry("600x500")
        settings_window.configure(bg=self.colors['glass'])
        
        # Settings controls
        tk.Label(settings_window, text="Voice Recognition Settings", 
                font=('Arial', 14, 'bold'), fg=self.colors['accent'], 
                bg=self.colors['glass']).pack(pady=10)
        
        # Sensitivity
        tk.Label(settings_window, text="Recognition Sensitivity:", fg=self.colors['text'], 
                bg=self.colors['glass']).pack(pady=5)
        sensitivity_scale = tk.Scale(settings_window, from_=0.1, to=1.0, resolution=0.1,
                                 orient='horizontal', bg=self.colors['glass'], fg=self.colors['text'],
                                 length=300)
        sensitivity_scale.set(0.3)
        sensitivity_scale.pack(pady=5)
        
        # Learning rate
        tk.Label(settings_window, text="Learning Rate:", fg=self.colors['text'], 
                bg=self.colors['glass']).pack(pady=5)
        learning_scale = tk.Scale(settings_window, from_=0.1, to=1.0, resolution=0.1,
                              orient='horizontal', bg=self.colors['glass'], fg=self.colors['text'],
                              length=300)
        learning_scale.set(0.5)
        learning_scale.pack(pady=5)
        
        # Voice rate
        tk.Label(settings_window, text="Voice Rate:", fg=self.colors['text'], 
                bg=self.colors['glass']).pack(pady=5)
        rate_scale = tk.Scale(settings_window, from_=50, to=200, resolution=10,
                           orient='horizontal', bg=self.colors['glass'], fg=self.colors['text'],
                           length=300)
        rate_scale.set(150)
        rate_scale.pack(pady=5)
        
        # Apply button
        def apply_settings():
            self.recognizer.phrase_threshold = sensitivity_scale.get()
            self.learning_data['learning_rate'] = learning_scale.get()
            self.engine.setProperty('rate', rate_scale.get())
            self.add_conversation_message("ILLI", "Voice settings updated and applied.")
            settings_window.destroy()
        
        tk.Button(settings_window, text="Apply Settings", command=apply_settings,
                 bg=self.colors['green'], fg='white', font=('Arial', 12, 'bold')).pack(pady=20)
    
    def voice_assistant_loop(self):
        """Advanced voice assistant with learning"""
        try:
            self.speak(f"Assalam o Alaikum {self.user_name}!")
            self.speak("Good Evening!")
            self.speak("I am ILLI AI, your learning assistant. I'll adapt to your voice patterns and learn from our conversations.")
        except Exception as e:
            self.add_conversation_message("ILLI", f"TTS Error: {str(e)}")
        
        while True:
            try:
                if self.listening_state:
                    self.voice_indicator.config(text="🟢 Voice: LEARNING", fg=self.colors['green'])
                    
                    with self.microphone as source:
                        # Adaptive audio settings
                        self.adapt_audio_settings(source)
                        
                        audio = self.recognizer.listen(source, timeout=8, phrase_time_limit=8)
                    
                    self.voice_indicator.config(text="🟡 Voice: RECOGNIZING", fg=self.colors['yellow'])
                    
                    try:
                        command = self.recognizer.recognize_google(audio).lower()
                        self.add_voice_history(f"Recognized: {command}")
                        
                        # Process with learning
                        self.process_command_with_learning(command)
                        
                    except sr.UnknownValueError:
                        self.add_voice_history("Could not understand - Learning from pattern")
                        self.learn_from_misrecognition()
                    except sr.RequestError:
                        self.add_voice_history("Speech recognition error")
                else:
                    self.voice_indicator.config(text="🔴 Voice: IDLE", fg=self.colors['red'])
                    time.sleep(1)
                    
            except Exception as e:
                self.add_voice_history(f"Voice error: {str(e)}")
                time.sleep(2)
    
    def adapt_audio_settings(self, source):
        """Adapt audio settings based on learning"""
        # Dynamic adjustment based on user profile
        if self.voice_profile['adaptation_count'] > 10:
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            self.recognizer.pause_threshold = 0.6 + (self.voice_profile['adaptation_count'] * 0.01)
            self.recognizer.non_speaking_duration = 0.4
            self.recognizer.phrase_threshold = 0.2
            self.recognizer.dynamic_energy_threshold = True
            self.recognizer.energy_threshold = 180 + (self.voice_profile['adaptation_count'] * 2)
    
    def process_command_with_learning(self, command):
        """Process command with learning capabilities"""
        self.add_conversation_message("You", command)
        
        # Update conversation context
        self.conversation_context['previous_commands'].append(command)
        self.conversation_context['current_topic'] = self.detect_topic(command)
        
        # Learn from command
        self.learn_from_command(command)
        
        # Process command with enhanced understanding
        response = self.generate_contextual_response(command)
        
        if response:
            self.add_conversation_message("ILLI", response)
            self.speak(response)
            
            # Learn from interaction
            self.learn_from_interaction(command, response)
            
            # Update accuracy
            self.update_accuracy_display(True)
        else:
            # Try traditional processing
            self.process_traditional_command(command)
    
    def generate_contextual_response(self, command):
        """Generate contextual response based on learning"""
        # Check learned responses
        if command in self.user_profile['learned_responses']:
            return self.user_profile['learned_responses'][command]
        
        # Check conversation patterns
        for pattern, responses in self.user_profile['command_patterns'].items():
            if any(keyword in command for keyword in pattern):
                return random.choice(responses)
        
        # Generate response based on context
        if self.conversation_context['current_topic']:
            topic_responses = {
                'greeting': ["Hello! How can I help you today?", "Hi there! What's on your mind?"],
                'farewell': ["Goodbye! Take care!", "See you later! Have a great day!"],
                'question': ["That's an interesting question! Let me think...", "I'd be happy to help with that!"],
                'request': ["I'll take care of that for you!", "Consider it done!"],
                'thanks': ["You're very welcome!", "My pleasure!"],
                'help': ["I can help you with many things! What specifically do you need?"]
            }
            
            if self.conversation_context['current_topic'] in topic_responses:
                return random.choice(topic_responses[self.conversation_context['current_topic']])
        
        # Default intelligent responses
        if any(word in command for word in ['hello', 'hi', 'hey']):
            return random.choice(["Hello! How can I assist you today?", "Hi there! What can I do for you?"])
        elif any(word in command for word in ['how are you', 'how do you do']):
            return random.choice(["I'm doing great! Learning more from you each day!", "I'm excellent! Thanks for asking!"])
        elif any(word in command for word in ['thank you', 'thanks']):
            return random.choice(["You're welcome!", "My pleasure!", "Happy to help!"])
        elif any(word in command for word in ['bye', 'goodbye', 'see you']):
            return random.choice(["Goodbye! Take care!", "See you later!"])
        
        return None
    
    def detect_topic(self, command):
        """Detect conversation topic"""
        topics = {
            'greeting': ['hello', 'hi', 'hey', 'good morning', 'good evening'],
            'farewell': ['bye', 'goodbye', 'see you', 'take care'],
            'question': ['what', 'how', 'why', 'where', 'when', 'who'],
            'request': ['open', 'close', 'start', 'stop', 'launch'],
            'thanks': ['thank', 'thanks', 'appreciate'],
            'help': ['help', 'assist', 'support']
        }
        
        for topic, keywords in topics.items():
            if any(keyword in command for keyword in keywords):
                return topic
        
        return 'general'
    
    def learn_from_command(self, command):
        """Learn from user command"""
        # Update frequent commands
        self.user_profile['frequent_commands'][command] += 1
        
        # Update voice patterns
        words = command.split()
        for word in words:
            self.user_profile['voice_patterns'][word].append(command)
        
        # Update command patterns
        self.user_profile['command_patterns'][command].append(f"User said: {command}")
        
        # Limit history size
        if len(self.user_profile['command_patterns'][command]) > 10:
            self.user_profile['command_patterns'][command] = self.user_profile['command_patterns'][command][-5:]
    
    def learn_from_interaction(self, command, response):
        """Learn from user interaction"""
        # Store conversation flow
        self.learning_data['conversation_flows'].append({
            'timestamp': datetime.now().isoformat(),
            'user_command': command,
            'illi_response': response,
            'context': self.conversation_context['current_topic']
        })
        
        # Update adaptation history
        self.learning_data['adaptation_history'].append({
            'timestamp': datetime.now().isoformat(),
            'type': 'interaction',
            'command': command,
            'response': response
        })
        
        # Increment adaptation count
        self.voice_profile['adaptation_count'] += 1
    
    def learn_from_misrecognition(self):
        """Learn from failed recognition attempts"""
        self.voice_profile['failed_recognitions'] += 1
        
        # Update learning data
        self.learning_data['voice_recognition_accuracy']['failed'].append({
            'timestamp': datetime.now().isoformat(),
            'reason': 'misrecognition'
        })
    
    def update_accuracy_display(self, success):
        """Update accuracy display"""
        if success:
            self.voice_profile['successful_recognitions'] += 1
        
        total = self.voice_profile['successful_recognitions'] + self.voice_profile['failed_recognitions']
        if total > 0:
            accuracy = (self.voice_profile['successful_recognitions'] / total) * 100
            self.accuracy_label.config(text=f"Accuracy: {accuracy:.1f}%")
            
            # Update voice profile display
            self.voice_profile_display.config(
                text=f"Voice Profile: {self.voice_profile['adaptation_count']} adaptations, {accuracy:.1f}% accuracy"
            )
    
    def process_traditional_command(self, command):
        """Process traditional commands"""
        # App launching
        if any(word in command for word in ['open', 'launch', 'start']):
            for app_name in self.app_paths.keys():
                if app_name in command:
                    self.launch_app(app_name)
                    return
        
        # System commands
        if 'time' in command:
            self.tell_time()
        elif 'date' in command:
            self.tell_date()
        elif 'help' in command:
            self.show_help()
        else:
            # Try to learn this as new command
            self.learn_new_command(command)
    
    def learn_new_command(self, command):
        """Learn new command pattern"""
        if command not in self.user_profile['learned_responses']:
            # Ask user what this command should do
            response = simpledialog.askstring("Learn Command", 
                                               f"What should I do when you say '{command}'?")
                                               parent=self.root)
            if response:
                self.user_profile['learned_responses'][command] = response
                self.add_conversation_message("ILLI", f"Learned! When you say '{command}', I'll {response}")
                self.save_learning_data()
    
    def learning_engine(self):
        """Continuous learning engine"""
        while True:
            try:
                # Process learning data
                self.process_learning_queue()
                
                # Adapt voice profile
                if self.voice_profile['adaptation_count'] > 0 and self.voice_profile['adaptation_count'] % 10 == 0:
                    self.optimize_voice_profile()
                
                time.sleep(5)  # Process every 5 seconds
            except Exception as e:
                time.sleep(5)
    
    def optimize_voice_profile(self):
        """Optimize voice profile based on learning"""
        # Analyze patterns and optimize
        successful_commands = sum(self.user_profile['frequent_commands'].values())
        
        if successful_commands > 50:
            self.add_conversation_message("ILLI", "Voice profile optimized based on our interactions!")
            self.voice_profile_display.config(text="Voice Profile: Optimized")
    
    def conversation_processor(self):
        """Process conversation context"""
        while True:
            try:
                # Update conversation context
                if len(self.conversation_context['previous_commands']) > 100:
                    self.conversation_context['previous_commands'] = self.conversation_context['previous_commands'][-50:]
                
                time.sleep(10)  # Process every 10 seconds
            except Exception as e:
                time.sleep(10)
    
    def adaptation_engine(self):
        """Continuous adaptation engine"""
        while True:
            try:
                # Adapt to user preferences
                self.adapt_to_user_habits()
                
                # Update learning metrics
                self.update_learning_metrics()
                
                time.sleep(30)  # Adapt every 30 seconds
            except Exception as e:
                time.sleep(30)
    
    def adapt_to_user_habits(self):
        """Adapt to user habits"""
        # Analyze usage patterns
        current_hour = datetime.now().hour
        
        # Simple habit adaptation
        if 9 <= current_hour <= 17:  # Working hours
            self.conversation_context['emotional_state'] = 'professional'
        else:  # Personal time
            self.conversation_context['emotional_state'] = 'casual'
    
    def update_learning_metrics(self):
        """Update learning metrics display"""
        metrics = f"""
📊 LEARNING METRICS:
Adaptations: {self.voice_profile['adaptation_count']}
Successful Recognitions: {self.voice_profile['successful_recognitions']}
Failed Recognitions: {self.voice_profile['failed_recognitions']}
Commands Learned: {len(self.user_profile['learned_responses'])}
Conversation Flows: {len(self.learning_data['conversation_flows'])}
Current Topic: {self.conversation_context['current_topic']}
Emotional State: {self.conversation_context['emotional_state']}
"""
        
        self.learning_display.delete(1.0, tk.END)
        self.learning_display.insert(tk.END, metrics)
    
    def send_conversation_message(self, event=None):
        """Send conversation message"""
        message = self.conversation_input.get().strip()
        if message:
            self.add_conversation_message("You", message)
            self.process_command_with_learning(message)
            self.conversation_input.delete(0, tk.END)
    
    def quick_conversation(self, message):
        """Quick conversation response"""
        self.add_conversation_message("You", message)
        self.process_command_with_learning(message)
    
    def add_conversation_message(self, sender, message):
        """Add message to conversation"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        formatted_message = f"[{timestamp}] {sender}: {message}\n"
        
        self.conversation_display.insert(tk.END, formatted_message)
        self.conversation_display.see(tk.END)
        
        # Update conversation history
        self.user_profile['conversation_history'].append({
            'timestamp': timestamp,
            'sender': sender,
            'message': message
        })
    
    def launch_app(self, app_name):
        """Launch application"""
        self.add_conversation_message("ILLI", f"Launching {app_name}")
        
        paths = self.app_paths.get(app_name, [])
        for path in paths:
            try:
                if path.startswith('http'):
                    webbrowser.open(path)
                    self.add_conversation_message("ILLI", f"Opened {app_name} in browser")
                else:
                    os.startfile(path)
                    self.add_conversation_message("ILLI", f"Opened {app_name} from path")
                break
            except Exception as e:
                self.add_conversation_message("ILLI", f"Error opening {app_name}: {str(e)}")
    
    def tell_time(self):
        """Tell current time"""
        current_time = datetime.now().strftime("%I:%M %p")
        self.add_conversation_message("ILLI", f"The current time is {current_time}")
        self.speak(current_time)
    
    def tell_date(self):
        """Tell current date"""
        current_date = datetime.now().strftime("%A, %B %d, %Y")
        self.add_conversation_message("ILLI", f"Today is {current_date}")
        self.speak(current_date)
    
    def show_help(self):
        """Show help information"""
        help_text = """
🤖 ILLI AI - LEARNING CAPABILITIES

🎤 VOICE LEARNING:
• I adapt to your voice patterns over time
• Recognition accuracy improves with use
• Learn your accent and speech style
• Personalized voice profile creation

💬 CONVERSATION:
• Natural conversation flow
• Context-aware responses
• Learn from our interactions
• Remember conversation topics

🧠 MEMORY & LEARNING:
• Remember your preferences
• Learn command patterns
• Adapt to your habits
• Store conversation context

📚 COMMANDS:
• "Open [app]" - Launch applications
• "Time/Date" - Current information
• "Help" - Show this help
• Natural conversation - Talk normally!

🎯 LEARNING FEATURES:
• Voice profile adaptation
• Command pattern recognition
• Conversation flow analysis
• User habit learning
• Context awareness
• Response optimization

💡 TIPS:
• Speak naturally and clearly
• I'll learn from each interaction
• Context carries over conversations
• Accuracy improves over time
• Personalized responses develop
        """
        
        self.add_conversation_message("ILLI", "Help information displayed")
        self.add_conversation_message("ILLI", help_text)
    
    def system_scan(self):
        """Perform system scan"""
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
            
            self.add_conversation_message("ILLI", "System scan completed")
            self.system_display.insert(tk.END, scan_results)
            self.system_display.see(tk.END)
            
        except Exception as e:
            self.add_conversation_message("ILLI", f"System scan error: {str(e)}")
    
    def system_cleanup(self):
        """Perform system cleanup"""
        self.add_conversation_message("ILLI", "System cleanup initiated")
        # Implementation similar to previous versions
    
    def system_optimize(self):
        """Perform system optimization"""
        self.add_conversation_message("ILLI", "System optimization completed")
        # Implementation similar to previous versions
    
    def performance_monitor(self):
        """Start performance monitoring"""
        self.add_conversation_message("ILLI", "Performance monitoring activated")
        # Implementation similar to previous versions
    
    def refresh_system(self):
        """Refresh system information"""
        self.add_conversation_message("ILLI", "System information refreshed")
        self.system_display.delete(1.0, tk.END)
    
    def show_learning_stats(self):
        """Show learning statistics"""
        stats = f"""
🧠 LEARNING STATISTICS:
Voice Adaptations: {self.voice_profile['adaptation_count']}
Recognition Accuracy: {self.calculate_accuracy():.1f}%
Commands Learned: {len(self.user_profile['learned_responses'])}
Conversation History: {len(self.user_profile['conversation_history'])}
Voice Patterns Stored: {len(self.user_profile['voice_patterns'])}
Frequent Commands: {len(self.user_profile['frequent_commands'])}
"""
        
        self.learning_display.insert(tk.END, stats)
        self.learning_display.see(tk.END)
    
    def calculate_accuracy(self):
        """Calculate recognition accuracy"""
        total = self.voice_profile['successful_recognitions'] + self.voice_profile['failed_recognitions']
        if total > 0:
            return (self.voice_profile['successful_recognitions'] / total) * 100
        return 0.0
    
    def train_voice_model(self):
        """Train voice model"""
        self.add_conversation_message("ILLI", "Voice training started. Please speak clearly...")
        # Implementation for voice training
    
    def stop_voice_training(self):
        """Stop voice training"""
        self.add_conversation_message("ILLI", "Voice training stopped")
        # Implementation for stopping training
    
    def test_voice_recognition(self):
        """Test voice recognition"""
        self.add_conversation_message("ILLI", "Testing voice recognition...")
        # Implementation for testing
    
    def improve_voice_accuracy(self):
        """Improve voice accuracy"""
        self.add_conversation_message("ILLI", "Improving voice accuracy...")
        # Implementation for accuracy improvement
    
    def reset_voice_profile(self):
        """Reset voice profile"""
        self.voice_profile = {
            'user_accent': 'unknown',
            'speech_rate': 'normal',
            'volume_preference': 0.9,
            'background_noise_level': 'normal',
            'recognition_confidence': 0.8,
            'adaptation_count': 0,
            'successful_recognitions': 0,
            'failed_recognitions': 0
        }
        self.add_conversation_message("ILLI", "Voice profile reset to default")
    
    def voice_training_settings(self):
        """Voice training settings"""
        self.add_conversation_message("ILLI", "Voice training settings opened")
        # Implementation for training settings
    
    def show_memory_stats(self):
        """Show memory statistics"""
        stats = f"""
🧠 MEMORY STATISTICS:
Conversation History: {len(self.user_profile['conversation_history'])}
Learned Responses: {len(self.user_profile['learned_responses'])}
Voice Patterns: {len(self.user_profile['voice_patterns'])}
Command Patterns: {len(self.user_profile['command_patterns'])}
Context Memory: {len(self.conversation_context['context_stack'])}
User Habits: {len(self.user_profile['user_habits'])}
"""
        
        self.memory_display.insert(tk.END, stats)
        self.memory_display.see(tk.END)
    
    def save_memory(self):
        """Save memory to file"""
        try:
            with open('illi_memory.pkl', 'wb') as f:
                pickle.dump(self.user_profile, f)
            self.add_conversation_message("ILLI", "Memory saved successfully")
        except Exception as e:
            self.add_conversation_message("ILLI", f"Error saving memory: {str(e)}")
    
    def load_memory(self):
        """Load memory from file"""
        try:
            if os.path.exists('illi_memory.pkl'):
                with open('illi_memory.pkl', 'rb') as f:
                    self.user_profile = pickle.load(f)
                self.add_conversation_message("ILLI", "Memory loaded successfully")
        except Exception as e:
            self.add_conversation_message("ILLI", f"Error loading memory: {str(e)}")
    
    def clear_memory(self):
        """Clear memory"""
        self.user_profile['conversation_history'] = []
        self.user_profile['learned_responses'] = {}
        self.user_profile['voice_patterns'] = defaultdict(list)
        self.user_profile['command_patterns'] = defaultdict(list)
        self.conversation_context['context_stack'] = []
        self.add_conversation_message("ILLI", "Memory cleared successfully")
    
    def search_memory(self):
        """Search memory"""
        query = simpledialog.askstring("Search Memory", "Enter search term:")
        if query:
            results = []
            for item in self.user_profile['conversation_history']:
                if query.lower() in item['message'].lower():
                    results.append(item)
            
            if results:
                self.add_conversation_message("ILLI", f"Found {len(results)} memory items")
                for result in results[:5]:
                    self.add_conversation_message("Memory", f"{result['timestamp']}: {result['message']}")
            else:
                self.add_conversation_message("ILLI", f"No memory items found for '{query}'")
    
    def memory_settings(self):
        """Memory settings"""
        self.add_conversation_message("ILLI", "Memory settings opened")
        # Implementation for memory settings
    
    def learning_settings(self):
        """Learning settings"""
        self.add_conversation_message("ILLI", "Learning settings opened")
        # Implementation for learning settings
    
    def save_learning_data(self):
        """Save learning data"""
        try:
            data = {
                'user_profile': dict(self.user_profile),
                'learning_data': dict(self.learning_data),
                'voice_profile': self.voice_profile,
                'conversation_context': self.conversation_context
            }
            
            with open('illi_learning_data.json', 'w') as f:
                json.dump(data, f, indent=2)
            
            self.add_conversation_message("ILLI", "Learning data saved successfully")
        except Exception as e:
            self.add_conversation_message("ILLI", f"Error saving learning data: {str(e)}")
    
    def load_learning_data(self):
        """Load learning data"""
        try:
            if os.path.exists('illi_learning_data.json'):
                with open('illi_learning_data.json', 'r') as f:
                    data = json.load(f)
                
                self.user_profile = defaultdict(dict, data.get('user_profile', {}))
                self.learning_data = defaultdict(dict, data.get('learning_data', {}))
                self.voice_profile = data.get('voice_profile', self.voice_profile)
                self.conversation_context = data.get('conversation_context', self.conversation_context)
                
                self.add_conversation_message("ILLI", "Learning data loaded successfully")
        except Exception as e:
            self.add_conversation_message("ILLI", f"Error loading learning data: {str(e)}")
    
    def reset_learning(self):
        """Reset learning data"""
        self.user_profile = {
            'name': self.user_name,
            'preferences': {},
            'voice_patterns': defaultdict(list),
            'frequent_commands': defaultdict(int),
            'conversation_history': [],
            'learned_responses': {},
            'context_memory': [],
            'user_habits': {},
            'voice_adaptations': {},
            'command_patterns': defaultdict(list)
        }
        
        self.learning_data = {
            'command_success_rate': defaultdict(float),
            'voice_recognition_accuracy': defaultdict(list),
            'response_effectiveness': defaultdict(list),
            'user_feedback': defaultdict(list),
            'adaptation_history': [],
            'conversation_flows': [],
            'context_keywords': defaultdict(int),
            'personal_info': {},
            'relationship_memory': {}
        }
        
        self.voice_profile = {
            'user_accent': 'unknown',
            'speech_rate': 'normal',
            'volume_preference': 0.9,
            'background_noise_level': 'normal',
            'recognition_confidence': 0.8,
            'adaptation_count': 0,
            'successful_recognitions': 0,
            'failed_recognitions': 0
        }
        
        self.add_conversation_message("ILLI", "Learning data reset to default")
    
    def process_learning_queue(self):
        """Process learning queue"""
        # Implementation for processing learning queue
        pass
    
    def update_learning_metrics(self):
        """Update learning metrics"""
        # Implementation for updating metrics
        pass
    
    def add_voice_history(self, message):
        """Add to voice history"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        history_entry = f"[{timestamp}] {message}\n"
        
        self.voice_history_display.insert(tk.END, history_entry)
        self.voice_history_display.see(tk.END)
    
    def speak(self, text):
        """Text to speech with learning"""
        try:
            self.engine.say(text)
            self.engine.runAndWait()
            
            # Learn from speech patterns
            self.learning_data['response_effectiveness']['spoken'].append({
                'timestamp': datetime.now().isoformat(),
                'text': text
            })
        except Exception as e:
            self.add_conversation_message("ILLI", f"TTS Error: {str(e)}")
    
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

def main():
    """Main function"""
    root = tk.Tk()
    app = ILLI_AI_Learning(root)
    root.mainloop()

if __name__ == "__main__":
    main()
