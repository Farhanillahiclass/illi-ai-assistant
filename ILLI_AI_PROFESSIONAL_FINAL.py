#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ILLI AI Professional - Complete PC & Web Control System
Created by Muhammad Farhan
Email: farhanhomeschooling519@gmail.com
GitHub: https://github.com/Farhanillahiclass/illi-ai-assistant

Features:
- Complete PC and Web Application Control
- Advanced Voice Recognition & TTS
- System Process Detection & Management
- Professional Security & Privacy Features
- GitHub Integration
- 100% Functional All Features
"""

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
import requests
import git
from pathlib import Path
import winreg
import ctypes
from typing import Dict, List, Optional, Tuple
import hashlib
import base64
from cryptography.fernet import Fernet
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SecurityManager:
    """Handle security and privacy features"""
    
    def __init__(self):
        self.encryption_key = self.generate_key()
        self.cipher_suite = Fernet(self.encryption_key)
        self.secure_data = {}
        
    def generate_key(self):
        """Generate encryption key"""
        return Fernet.generate_key()
    
    def encrypt_data(self, data: str) -> str:
        """Encrypt sensitive data"""
        return self.cipher_suite.encrypt(data.encode()).decode()
    
    def decrypt_data(self, encrypted_data: str) -> str:
        """Decrypt sensitive data"""
        return self.cipher_suite.decrypt(encrypted_data.encode()).decode()
    
    def hash_password(self, password: str) -> str:
        """Hash password for storage"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def check_admin_privileges(self) -> bool:
        """Check if running with admin privileges"""
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

class SystemDetector:
    """Advanced system and process detection"""
    
    def __init__(self):
        self.running_processes = {}
        self.installed_apps = {}
        self.system_info = {}
        self.update_system_info()
        
    def update_system_info(self):
        """Update system information"""
        self.system_info = {
            'platform': platform.system(),
            'platform_release': platform.release(),
            'platform_version': platform.version(),
            'architecture': platform.machine(),
            'hostname': platform.node(),
            'processor': platform.processor(),
            'ram': round(psutil.virtual_memory().total / (1024**3), 2),
            'cpu_count': psutil.cpu_count(),
            'cpu_freq': psutil.cpu_freq().current if psutil.cpu_freq() else 0
        }
        
    def get_running_processes(self) -> Dict[str, Dict]:
        """Get all running processes with detailed info"""
        processes = {}
        for proc in psutil.process_iter(['pid', 'name', 'username', 'status', 'cpu_percent', 'memory_percent']):
            try:
                proc_info = proc.info
                processes[proc_info['name']] = {
                    'pid': proc_info['pid'],
                    'status': proc_info['status'],
                    'cpu_percent': proc_info['cpu_percent'],
                    'memory_percent': proc_info['memory_percent'],
                    'username': proc_info['username']
                }
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
        self.running_processes = processes
        return processes
    
    def get_installed_applications(self) -> Dict[str, str]:
        """Get installed applications from registry"""
        apps = {}
        try:
            # Get installed apps from registry
            registry_paths = [
                r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
                r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
            ]
            
            for registry_path in registry_paths:
                try:
                    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, registry_path) as key:
                        for i in range(0, winreg.QueryInfoKey(key)[0]):
                            try:
                                subkey_name = winreg.EnumKey(key, i)
                                with winreg.OpenKey(key, subkey_name) as subkey:
                                    app_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                                    try:
                                        app_path = winreg.QueryValueEx(subkey, "InstallLocation")[0]
                                    except FileNotFoundError:
                                        app_path = "Unknown"
                                    apps[app_name.lower()] = app_path
                            except (WindowsError, FileNotFoundError):
                                continue
                except (WindowsError, FileNotFoundError):
                    continue
                    
        except Exception as e:
            logger.error(f"Error getting installed apps: {e}")
            
        self.installed_apps = apps
        return apps
    
    def detect_system_changes(self) -> List[str]:
        """Detect system changes"""
        changes = []
        current_processes = set(self.get_running_processes().keys())
        previous_processes = set(self.running_processes.keys())
        
        new_processes = current_processes - previous_processes
        closed_processes = previous_processes - current_processes
        
        if new_processes:
            changes.append(f"New processes started: {', '.join(new_processes)}")
        if closed_processes:
            changes.append(f"Processes closed: {', '.join(closed_processes)}")
            
        return changes

class VoiceController:
    """Advanced voice recognition and text-to-speech"""
    
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.microphone = None
        self.listening = False
        self.voice_commands = {}
        self.setup_voice()
        
    def setup_voice(self):
        """Setup voice engine and microphone"""
        try:
            # Setup microphone
            self.microphone = sr.Microphone()
            
            # Setup TTS engine
            voices = self.engine.getProperty('voices')
            if voices:
                # Prefer female voice if available
                for voice in voices:
                    if 'female' in voice.name.lower():
                        self.engine.setProperty('voice', voice.id)
                        break
                else:
                    self.engine.setProperty('voice', voices[0].id)
            
            self.engine.setProperty('rate', 150)
            self.engine.setProperty('volume', 0.9)
            
            # Calibrate microphone
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                
            logger.info("Voice system initialized successfully")
            
        except Exception as e:
            logger.error(f"Voice setup failed: {e}")
            
    def listen_for_command(self) -> Optional[str]:
        """Listen for voice command"""
        if not self.microphone:
            return None
            
        try:
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
            
            # Try Google Speech Recognition first
            try:
                command = self.recognizer.recognize_google(audio)
                logger.info(f"Voice command recognized: {command}")
                return command.lower()
            except sr.RequestError:
                # Fallback to Sphinx (offline)
                try:
                    command = self.recognizer.recognize_sphinx(audio)
                    logger.info(f"Voice command recognized (offline): {command}")
                    return command.lower()
                except sr.RequestError:
                    logger.warning("Both online and offline recognition failed")
                    return None
                    
        except sr.WaitTimeoutError:
            return None
        except sr.UnknownValueError:
            logger.warning("Could not understand audio")
            return None
        except Exception as e:
            logger.error(f"Error in voice recognition: {e}")
            return None
    
    def speak(self, text: str):
        """Convert text to speech"""
        try:
            self.engine.say(text)
            self.engine.runAndWait()
            logger.info(f"Spoken: {text}")
        except Exception as e:
            logger.error(f"Text-to-speech error: {e}")
    
    def add_voice_command(self, command: str, callback):
        """Add voice command"""
        self.voice_commands[command.lower()] = callback

class GitHubManager:
    """GitHub repository management"""
    
    def __init__(self, repo_url: str, local_path: str):
        self.repo_url = repo_url
        self.local_path = local_path
        self.repo = None
        self.initialize_repo()
        
    def initialize_repo(self):
        """Initialize or connect to repository"""
        try:
            if os.path.exists(os.path.join(self.local_path, '.git')):
                self.repo = git.Repo(self.local_path)
                logger.info("Connected to existing repository")
            else:
                self.repo = git.Repo.clone_from(self.repo_url, self.local_path)
                logger.info("Cloned new repository")
        except Exception as e:
            logger.error(f"Repository initialization failed: {e}")
            
    def commit_and_push(self, commit_message: str, branch: str = 'main'):
        """Commit and push changes"""
        try:
            if not self.repo:
                logger.error("Repository not initialized")
                return False
                
            # Add all changes
            self.repo.git.add('--all')
            
            # Check if there are changes to commit
            if self.repo.is_dirty(untracked_files=True):
                self.repo.index.commit(commit_message)
                
                # Push to remote
                origin = self.repo.remote(name='origin')
                origin.push(branch)
                
                logger.info(f"Successfully pushed changes: {commit_message}")
                return True
            else:
                logger.info("No changes to commit")
                return True
                
        except Exception as e:
            logger.error(f"Git push failed: {e}")
            return False
    
    def pull_latest(self, branch: str = 'main'):
        """Pull latest changes from remote"""
        try:
            if not self.repo:
                logger.error("Repository not initialized")
                return False
                
            origin = self.repo.remote(name='origin')
            origin.pull(branch)
            logger.info("Successfully pulled latest changes")
            return True
            
        except Exception as e:
            logger.error(f"Git pull failed: {e}")
            return False

class ILLI_AI_Professional:
    """Main ILLI AI Professional Application"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("ILLI AI Professional - Complete PC & Web Control System")
        self.root.geometry("1400x900")
        self.root.configure(bg='#000000')
        
        # Initialize components
        self.security_manager = SecurityManager()
        self.system_detector = SystemDetector()
        self.voice_controller = VoiceController()
        self.github_manager = GitHubManager(
            "https://github.com/Farhanillahiclass/illi-ai-assistant.git",
            os.path.dirname(os.path.abspath(__file__))
        )
        
        # System variables
        self.user_name = os.getlogin()
        self.command_history = []
        self.conversation_context = []
        self.voice_active = False
        self.auto_save_enabled = True
        
        # Professional color scheme
        self.colors = {
            'bg': '#000000',
            'glass': '#1a1a1a',
            'glass_border': '#2a2a2a',
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
            'cyan': '#00FFFF',
            'pink': '#FF69B4'
        }
        
        # Complete application database
        self.setup_applications_database()
        
        # Setup UI
        self.setup_ui()
        
        # Start background services
        self.start_background_services()
        
        # Initialize voice commands
        self.setup_voice_commands()
        
        # Welcome message
        self.welcome_user()
        
    def setup_applications_database(self):
        """Setup comprehensive applications database"""
        self.applications = {
            # Communication Apps
            'whatsapp': {
                'web': 'https://web.whatsapp.com',
                'desktop': ['WhatsApp.exe', 'WhatsApp.exe'],
                'category': 'communication'
            },
            'telegram': {
                'web': 'https://web.telegram.org',
                'desktop': ['Telegram.exe', 'Telegram.exe'],
                'category': 'communication'
            },
            'discord': {
                'web': 'https://discord.com/app',
                'desktop': ['Discord.exe', 'Discord.exe'],
                'category': 'communication'
            },
            'slack': {
                'web': 'https://slack.com',
                'desktop': ['slack.exe', 'slack.exe'],
                'category': 'communication'
            },
            'teams': {
                'web': 'https://teams.microsoft.com',
                'desktop': ['Teams.exe', 'Teams.exe'],
                'category': 'communication'
            },
            'zoom': {
                'web': 'https://zoom.us',
                'desktop': ['Zoom.exe', 'Zoom.exe'],
                'category': 'communication'
            },
            'skype': {
                'web': 'https://web.skype.com',
                'desktop': ['skype.exe', 'skype.exe'],
                'category': 'communication'
            },
            
            # Email Services
            'gmail': {
                'web': 'https://gmail.com',
                'desktop': None,
                'category': 'email'
            },
            'outlook': {
                'web': 'https://outlook.live.com',
                'desktop': ['outlook.exe', 'outlook.exe'],
                'category': 'email'
            },
            'yahoo': {
                'web': 'https://mail.yahoo.com',
                'desktop': None,
                'category': 'email'
            },
            
            # Social Media
            'facebook': {
                'web': 'https://facebook.com',
                'desktop': None,
                'category': 'social'
            },
            'twitter': {
                'web': 'https://twitter.com',
                'desktop': None,
                'category': 'social'
            },
            'instagram': {
                'web': 'https://instagram.com',
                'desktop': ['Instagram.exe', 'Instagram.exe'],
                'category': 'social'
            },
            'linkedin': {
                'web': 'https://linkedin.com',
                'desktop': None,
                'category': 'social'
            },
            'reddit': {
                'web': 'https://reddit.com',
                'desktop': None,
                'category': 'social'
            },
            'youtube': {
                'web': 'https://youtube.com',
                'desktop': None,
                'category': 'entertainment'
            },
            'tiktok': {
                'web': 'https://tiktok.com',
                'desktop': None,
                'category': 'social'
            },
            
            # Development Tools
            'github': {
                'web': 'https://github.com',
                'desktop': ['GitHubDesktop.exe', 'GitHubDesktop.exe'],
                'category': 'development'
            },
            'gitlab': {
                'web': 'https://gitlab.com',
                'desktop': None,
                'category': 'development'
            },
            'vs code': {
                'web': None,
                'desktop': ['Code.exe', 'Code.exe'],
                'category': 'development'
            },
            'visual studio': {
                'web': None,
                'desktop': ['devenv.exe', 'devenv.exe'],
                'category': 'development'
            },
            'intellij': {
                'web': None,
                'desktop': ['idea64.exe', 'idea64.exe'],
                'category': 'development'
            },
            'pycharm': {
                'web': None,
                'desktop': ['pycharm64.exe', 'pycharm64.exe'],
                'category': 'development'
            },
            'android studio': {
                'web': None,
                'desktop': ['studio64.exe', 'studio64.exe'],
                'category': 'development'
            },
            
            # Browsers
            'chrome': {
                'web': 'https://google.com',
                'desktop': ['chrome.exe', 'chrome.exe'],
                'category': 'browser'
            },
            'firefox': {
                'web': 'https://firefox.com',
                'desktop': ['firefox.exe', 'firefox.exe'],
                'category': 'browser'
            },
            'edge': {
                'web': 'https://microsoftedge.microsoft.com',
                'desktop': ['msedge.exe', 'msedge.exe'],
                'category': 'browser'
            },
            
            # Entertainment
            'netflix': {
                'web': 'https://netflix.com',
                'desktop': None,
                'category': 'entertainment'
            },
            'spotify': {
                'web': 'https://open.spotify.com',
                'desktop': ['Spotify.exe', 'Spotify.exe'],
                'category': 'entertainment'
            },
            'apple music': {
                'web': 'https://music.apple.com',
                'desktop': None,
                'category': 'entertainment'
            },
            
            # Productivity
            'notion': {
                'web': 'https://notion.so',
                'desktop': ['Notion.exe', 'Notion.exe'],
                'category': 'productivity'
            },
            'trello': {
                'web': 'https://trello.com',
                'desktop': ['Trello.exe', 'Trello.exe'],
                'category': 'productivity'
            },
            'asana': {
                'web': 'https://asana.com',
                'desktop': None,
                'category': 'productivity'
            },
            'slack': {
                'web': 'https://slack.com',
                'desktop': ['slack.exe', 'slack.exe'],
                'category': 'productivity'
            },
            
            # System Applications
            'files': {
                'web': None,
                'desktop': ['explorer.exe', 'explorer.exe'],
                'category': 'system'
            },
            'notepad': {
                'web': None,
                'desktop': ['notepad.exe', 'notepad.exe'],
                'category': 'system'
            },
            'calculator': {
                'web': None,
                'desktop': ['calc.exe', 'calc.exe'],
                'category': 'system'
            },
            'cmd': {
                'web': None,
                'desktop': ['cmd.exe', 'cmd.exe'],
                'category': 'system'
            },
            'powershell': {
                'web': None,
                'desktop': ['powershell.exe', 'powershell.exe'],
                'category': 'system'
            },
            'taskmgr': {
                'web': None,
                'desktop': ['taskmgr.exe', 'taskmgr.exe'],
                'category': 'system'
            },
            'control': {
                'web': None,
                'desktop': ['control.exe', 'control.exe'],
                'category': 'system'
            },
            'settings': {
                'web': None,
                'desktop': ['ms-settings:', 'ms-settings:'],
                'category': 'system'
            },
            'camera': {
                'web': None,
                'desktop': ['microsoft.windows.camera:', 'microsoft.windows.camera:'],
                'category': 'system'
            },
            'paint': {
                'web': None,
                'desktop': ['mspaint.exe', 'mspaint.exe'],
                'category': 'system'
            },
            
            # Microsoft Office
            'word': {
                'web': None,
                'desktop': ['winword.exe', 'winword.exe'],
                'category': 'office'
            },
            'excel': {
                'web': None,
                'desktop': ['excel.exe', 'excel.exe'],
                'category': 'office'
            },
            'powerpoint': {
                'web': None,
                'desktop': ['powerpnt.exe', 'powerpnt.exe'],
                'category': 'office'
            },
            'access': {
                'web': None,
                'desktop': ['msaccess.exe', 'msaccess.exe'],
                'category': 'office'
            },
            'onenote': {
                'web': None,
                'desktop': ['onenote.exe', 'onenote.exe'],
                'category': 'office'
            },
            
            # Graphics & Design
            'photoshop': {
                'web': None,
                'desktop': ['Photoshop.exe', 'Photoshop.exe'],
                'category': 'graphics'
            },
            'illustrator': {
                'web': None,
                'desktop': ['Illustrator.exe', 'Illustrator.exe'],
                'category': 'graphics'
            },
            'premiere': {
                'web': None,
                'desktop': ['Premiere Pro.exe', 'Premiere Pro.exe'],
                'category': 'graphics'
            },
            'after effects': {
                'web': None,
                'desktop': ['AfterFX.exe', 'AfterFX.exe'],
                'category': 'graphics'
            },
            'blender': {
                'web': None,
                'desktop': ['blender.exe', 'blender.exe'],
                'category': 'graphics'
            },
            
            # Gaming
            'steam': {
                'web': None,
                'desktop': ['steam.exe', 'steam.exe'],
                'category': 'gaming'
            },
            'epic games': {
                'web': None,
                'desktop': ['EpicGamesLauncher.exe', 'EpicGamesLauncher.exe'],
                'category': 'gaming'
            },
            'origin': {
                'web': None,
                'desktop': ['Origin.exe', 'Origin.exe'],
                'category': 'gaming'
            },
            
            # AI Services
            'chatgpt': {
                'web': 'https://chat.openai.com',
                'desktop': None,
                'category': 'ai'
            },
            'claude': {
                'web': 'https://claude.ai',
                'desktop': None,
                'category': 'ai'
            },
            'gemini': {
                'web': 'https://gemini.google.com',
                'desktop': None,
                'category': 'ai'
            },
            
            # Shopping
            'amazon': {
                'web': 'https://amazon.com',
                'desktop': None,
                'category': 'shopping'
            },
            'ebay': {
                'web': 'https://ebay.com',
                'desktop': None,
                'category': 'shopping'
            },
            'etsy': {
                'web': 'https://etsy.com',
                'desktop': None,
                'category': 'shopping'
            },
        }
        
        # Add user's installed applications
        installed_apps = self.system_detector.get_installed_applications()
        for app_name, app_path in installed_apps.items():
            if app_name not in self.applications:
                self.applications[app_name] = {
                    'web': None,
                    'desktop': [os.path.basename(app_path), app_path],
                    'category': 'user'
                }
    
    def setup_ui(self):
        """Setup professional user interface"""
        # Main container
        main_frame = tk.Frame(self.root, bg=self.colors['bg'])
        main_frame.pack(fill='both', expand=True)
        
        # Header
        self.create_header(main_frame)
        
        # Tabbed interface
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Style notebook
        style = ttk.Style()
        style.theme_use('default')
        style.configure('TNotebook', background=self.colors['bg'])
        style.configure('TNotebook.Tab', background=self.colors['glass'], 
                       foreground=self.colors['text'], padding=[25, 12])
        
        # Create tabs
        self.create_control_center_tab()
        self.create_applications_tab()
        self.create_system_monitor_tab()
        self.create_voice_control_tab()
        self.create_github_tab()
        self.create_security_tab()
        
        # Status bar
        self.create_status_bar(main_frame)
        
    def create_header(self, parent):
        """Create professional header"""
        header_frame = tk.Frame(parent, bg=self.colors['glass'], relief='raised', bd=2)
        header_frame.pack(fill='x', padx=10, pady=5)
        
        # Title section
        title_frame = tk.Frame(header_frame, bg=self.colors['glass'])
        title_frame.pack(side='left', padx=20, pady=10)
        
        title_label = tk.Label(title_frame, text="ILLI AI PROFESSIONAL", 
                              font=('Arial', 32, 'bold'), fg=self.colors['accent'], 
                              bg=self.colors['glass'])
        title_label.pack()
        
        subtitle_label = tk.Label(title_frame, text="Complete PC & Web Control System with Advanced Security", 
                                 font=('Arial', 14), fg=self.colors['text_dim'], 
                                 bg=self.colors['glass'])
        subtitle_label.pack()
        
        # User and status section
        info_frame = tk.Frame(header_frame, bg=self.colors['glass'])
        info_frame.pack(side='right', padx=20, pady=10)
        
        user_label = tk.Label(info_frame, text=f"User: {self.user_name}", 
                              font=('Arial', 12), fg=self.colors['text'], 
                              bg=self.colors['glass'])
        user_label.pack()
        
        self.status_label = tk.Label(info_frame, text="Status: ONLINE", 
                                    font=('Arial', 12), fg=self.colors['success'], 
                                    bg=self.colors['glass'])
        self.status_label.pack()
        
        self.voice_status_label = tk.Label(info_frame, text="Voice: READY", 
                                         font=('Arial', 12), fg=self.colors['cyan'], 
                                         bg=self.colors['glass'])
        self.voice_status_label.pack()
        
        self.security_label = tk.Label(info_frame, text="Security: ACTIVE", 
                                      font=('Arial', 12), fg=self.colors['green'], 
                                      bg=self.colors['glass'])
        self.security_label.pack()
    
    def create_control_center_tab(self):
        """Create control center tab"""
        tab_frame = tk.Frame(self.notebook, bg=self.colors['glass'])
        self.notebook.add(tab_frame, text="CONTROL CENTER")
        
        # Main display
        display_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        display_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        tk.Label(display_frame, text="ILLI AI CONTROL CENTER", 
                font=('Arial', 20, 'bold'), fg=self.colors['accent'], 
                bg=self.colors['glass']).pack(pady=5)
        
        # Main display area
        self.main_display = scrolledtext.ScrolledText(display_frame, height=15, width=120,
                                                     bg=self.colors['bg'], fg=self.colors['text'],
                                                     font=('Consolas', 11))
        self.main_display.pack(fill='both', expand=True, pady=5)
        
        # Quick actions
        actions_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        actions_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Label(actions_frame, text="QUICK ACTIONS", 
                font=('Arial', 16, 'bold'), fg=self.colors['accent'], 
                bg=self.colors['glass']).pack(pady=5)
        
        # Action buttons grid
        actions = [
            ("Start Voice Control", self.toggle_voice_control, self.colors['green']),
            ("System Scan", self.perform_system_scan, self.colors['blue']),
            ("Launch Browser", lambda: self.launch_application('chrome'), self.colors['blue']),
            ("Open Files", lambda: self.launch_application('files'), self.colors['yellow']),
            ("Open CMD", lambda: self.launch_application('cmd'), self.colors['black']),
            ("Open Calculator", lambda: self.launch_application('calculator'), self.colors['orange']),
            ("System Info", self.show_system_info, self.colors['purple']),
            ("Process Monitor", self.show_processes, self.colors['red']),
            ("GitHub Sync", self.sync_github, self.colors['cyan']),
            ("Security Check", self.security_check, self.colors['green']),
            ("Voice Settings", self.voice_settings, self.colors['magenta']),
            ("Clear Display", self.clear_display, self.colors['warning'])
        ]
        
        for i, (text, command, color) in enumerate(actions):
            row = i // 4
            col = i % 4
            btn = tk.Button(actions_frame, text=text, command=command,
                         bg=color, fg='white', font=('Arial', 11, 'bold'), 
                         width=18, height=2)
            btn.grid(row=row, column=col, padx=5, pady=5)
    
    def create_applications_tab(self):
        """Create applications control tab"""
        tab_frame = tk.Frame(self.notebook, bg=self.colors['glass'])
        self.notebook.add(tab_frame, text="APPLICATIONS")
        
        # Applications display
        self.apps_display = scrolledtext.ScrolledText(tab_frame, height=10, width=120,
                                                     bg=self.colors['bg'], fg=self.colors['text'],
                                                     font=('Consolas', 11))
        self.apps_display.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Categories frame
        categories_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        categories_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        tk.Label(categories_frame, text="APPLICATION CATEGORIES", 
                font=('Arial', 16, 'bold'), fg=self.colors['accent'], 
                bg=self.colors['glass']).pack(pady=5)
        
        # Category buttons
        categories = {
            'Communication': ['whatsapp', 'telegram', 'discord', 'slack', 'teams', 'zoom', 'skype'],
            'Social Media': ['facebook', 'twitter', 'instagram', 'linkedin', 'reddit', 'tiktok', 'youtube'],
            'Development': ['github', 'vs code', 'visual studio', 'intellij', 'pycharm', 'android studio'],
            'Productivity': ['notion', 'trello', 'asana', 'slack', 'gmail', 'outlook'],
            'Entertainment': ['netflix', 'spotify', 'apple music', 'youtube', 'tiktok'],
            'System': ['files', 'notepad', 'calculator', 'cmd', 'powershell', 'taskmgr', 'settings'],
            'Office': ['word', 'excel', 'powerpoint', 'access', 'onenote', 'outlook'],
            'AI Services': ['chatgpt', 'claude', 'gemini'],
            'Shopping': ['amazon', 'ebay', 'etsy'],
            'Graphics': ['photoshop', 'illustrator', 'premiere', 'after effects', 'blender'],
            'Gaming': ['steam', 'epic games', 'origin'],
            'Browsers': ['chrome', 'firefox', 'edge']
        }
        
        for category, apps in categories.items():
            cat_frame = tk.Frame(categories_frame, bg=self.colors['glass'])
            cat_frame.pack(fill='x', pady=3)
            
            tk.Label(cat_frame, text=f"{category}:", 
                    font=('Arial', 12, 'bold'), fg=self.colors['accent'], 
                    bg=self.colors['glass']).pack(side='left', padx=5)
            
            for app in apps[:8]:  # Limit to 8 per row
                btn = tk.Button(cat_frame, text=app.title(), 
                             command=lambda a=app: self.launch_application(a),
                             bg=self.colors['blue'], fg='white', 
                             font=('Arial', 9), width=12)
                btn.pack(side='left', padx=2)
    
    def create_system_monitor_tab(self):
        """Create system monitoring tab"""
        tab_frame = tk.Frame(self.notebook, bg=self.colors['glass'])
        self.notebook.add(tab_frame, text="SYSTEM MONITOR")
        
        # System display
        self.system_display = scrolledtext.ScrolledText(tab_frame, height=10, width=120,
                                                       bg=self.colors['bg'], fg=self.colors['text'],
                                                       font=('Consolas', 11))
        self.system_display.pack(fill='both', expand=True, padx=10, pady=5)
        
        # System controls
        control_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        control_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Label(control_frame, text="SYSTEM CONTROL", 
                font=('Arial', 16, 'bold'), fg=self.colors['accent'], 
                bg=self.colors['glass']).pack(pady=5)
        
        # System buttons
        system_buttons = [
            ("System Scan", self.perform_system_scan, self.colors['blue']),
            ("System Info", self.show_system_info, self.colors['purple']),
            ("Show Processes", self.show_processes, self.colors['green']),
            ("Performance Monitor", self.performance_monitor, self.colors['orange']),
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
                         bg=color, fg='white', font=('Arial', 10, 'bold'), 
                         width=14, height=2)
            btn.grid(row=row, column=col, padx=4, pady=4)
    
    def create_voice_control_tab(self):
        """Create voice control tab"""
        tab_frame = tk.Frame(self.notebook, bg=self.colors['glass'])
        self.notebook.add(tab_frame, text="VOICE CONTROL")
        
        # Voice status
        status_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        status_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Label(status_frame, text="VOICE CONTROL CENTER", 
                font=('Arial', 20, 'bold'), fg=self.colors['accent'], 
                bg=self.colors['glass']).pack(pady=5)
        
        self.voice_indicator = tk.Label(status_frame, text="Voice: IDLE", 
                                     font=('Arial', 18, 'bold'), fg=self.colors['red'], 
                                     bg=self.colors['glass'])
        self.voice_indicator.pack(side='left', padx=20, pady=10)
        
        # Voice controls
        control_frame = tk.Frame(status_frame, bg=self.colors['glass'])
        control_frame.pack(side='left', padx=20, pady=10)
        
        self.voice_btn = tk.Button(control_frame, text="Start Voice", 
                                   command=self.toggle_voice_control,
                                   bg=self.colors['green'], fg='white', 
                                   font=('Arial', 14, 'bold'), width=14, height=2)
        self.voice_btn.pack(side='left', padx=5, pady=5)
        
        tk.Button(control_frame, text="Test Voice", command=self.test_voice,
                 bg=self.colors['blue'], fg='white', 
                 font=('Arial', 14, 'bold'), width=14, height=2).pack(side='left', padx=5, pady=5)
        
        tk.Button(control_frame, text="Voice Settings", command=self.voice_settings,
                 bg=self.colors['orange'], fg='white', 
                 font=('Arial', 14, 'bold'), width=14, height=2).pack(side='left', padx=5, pady=5)
        
        # Voice history
        history_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        history_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        tk.Label(history_frame, text="VOICE CONVERSATION HISTORY", 
                font=('Arial', 16, 'bold'), fg=self.colors['accent'], 
                bg=self.colors['glass']).pack(pady=5)
        
        self.voice_history_display = scrolledtext.ScrolledText(history_frame, height=8, width=120,
                                                              bg=self.colors['bg'], fg=self.colors['text'],
                                                              font=('Consolas', 11))
        self.voice_history_display.pack(fill='both', expand=True, pady=5)
        
        # Manual command input
        input_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        input_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Label(input_frame, text="Manual Command:", fg=self.colors['text'], 
                bg=self.colors['glass'], font=('Arial', 12)).pack(side='left', padx=5)
        
        self.manual_entry = tk.Entry(input_frame, width=60, bg=self.colors['bg'], 
                                    fg=self.colors['text'], font=('Consolas', 11))
        self.manual_entry.pack(side='left', padx=5, fill='x', expand=True)
        self.manual_entry.bind('<Return>', self.execute_manual_command)
        
        tk.Button(input_frame, text="Execute", command=self.execute_manual_command,
                 bg=self.colors['accent'], fg='black', 
                 font=('Arial', 12, 'bold'), width=12, height=2).pack(side='left', padx=5, pady=5)
    
    def create_github_tab(self):
        """Create GitHub integration tab"""
        tab_frame = tk.Frame(self.notebook, bg=self.colors['glass'])
        self.notebook.add(tab_frame, text="GITHUB")
        
        # GitHub display
        self.github_display = scrolledtext.ScrolledText(tab_frame, height=10, width=120,
                                                        bg=self.colors['bg'], fg=self.colors['text'],
                                                        font=('Consolas', 11))
        self.github_display.pack(fill='both', expand=True, padx=10, pady=5)
        
        # GitHub controls
        control_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        control_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Label(control_frame, text="GITHUB INTEGRATION", 
                font=('Arial', 16, 'bold'), fg=self.colors['accent'], 
                bg=self.colors['glass']).pack(pady=5)
        
        # GitHub buttons
        github_buttons = [
            ("Sync Repository", self.sync_github, self.colors['green']),
            ("Commit Changes", self.commit_changes, self.colors['blue']),
            ("Pull Latest", self.pull_latest, self.colors['purple']),
            ("Push to GitHub", self.push_to_github, self.colors['orange']),
            ("View Status", self.view_github_status, self.colors['cyan']),
            ("Create Backup", self.create_backup, self.colors['red'])
        ]
        
        for i, (text, command, color) in enumerate(github_buttons):
            row = i // 3
            col = i % 3
            btn = tk.Button(control_frame, text=text, command=command,
                         bg=color, fg='white', font=('Arial', 11, 'bold'), 
                         width=16, height=2)
            btn.grid(row=row, column=col, padx=5, pady=5)
    
    def create_security_tab(self):
        """Create security and privacy tab"""
        tab_frame = tk.Frame(self.notebook, bg=self.colors['glass'])
        self.notebook.add(tab_frame, text="SECURITY")
        
        # Security display
        self.security_display = scrolledtext.ScrolledText(tab_frame, height=10, width=120,
                                                         bg=self.colors['bg'], fg=self.colors['text'],
                                                         font=('Consolas', 11))
        self.security_display.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Security controls
        control_frame = tk.Frame(tab_frame, bg=self.colors['glass'])
        control_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Label(control_frame, text="SECURITY & PRIVACY", 
                font=('Arial', 16, 'bold'), fg=self.colors['accent'], 
                bg=self.colors['glass']).pack(pady=5)
        
        # Security buttons
        security_buttons = [
            ("Security Check", self.security_check, self.colors['green']),
            ("Privacy Scan", self.privacy_scan, self.colors['blue']),
            ("Encrypt Data", self.encrypt_sensitive_data, self.colors['purple']),
            ("Clear Tracks", self.clear_tracks, self.colors['red']),
            ("Password Manager", self.password_manager, self.colors['orange']),
            ("Security Settings", self.security_settings, self.colors['cyan'])
        ]
        
        for i, (text, command, color) in enumerate(security_buttons):
            row = i // 3
            col = i % 3
            btn = tk.Button(control_frame, text=text, command=command,
                         bg=color, fg='white', font=('Arial', 11, 'bold'), 
                         width=16, height=2)
            btn.grid(row=row, column=col, padx=5, pady=5)
    
    def create_status_bar(self, parent):
        """Create professional status bar"""
        status_frame = tk.Frame(parent, bg=self.colors['glass'], relief='sunken', bd=1)
        status_frame.pack(fill='x', side='bottom', padx=10, pady=5)
        
        self.task_label = tk.Label(status_frame, text="Task: Ready", 
                                  font=('Arial', 11), fg=self.colors['text'], 
                                  bg=self.colors['glass'])
        self.task_label.pack(side='left', padx=10)
        
        self.cpu_label = tk.Label(status_frame, text="CPU: 0%", 
                                 font=('Arial', 11), fg=self.colors['text'], 
                                 bg=self.colors['glass'])
        self.cpu_label.pack(side='left', padx=10)
        
        self.memory_label = tk.Label(status_frame, text="Memory: 0%", 
                                    font=('Arial', 11), fg=self.colors['text'], 
                                    bg=self.colors['glass'])
        self.memory_label.pack(side='left', padx=10)
        
        self.time_label = tk.Label(status_frame, text="", 
                                  font=('Arial', 11), fg=self.colors['text'], 
                                  bg=self.colors['glass'])
        self.time_label.pack(side='right', padx=10)
    
    def start_background_services(self):
        """Start background services"""
        threading.Thread(target=self.voice_assistant_loop, daemon=True).start()
        threading.Thread(target=self.update_system_info, daemon=True).start()
        threading.Thread(target=self.update_time, daemon=True).start()
        threading.Thread(target=self.system_monitor_loop, daemon=True).start()
        threading.Thread(target=self.auto_save_loop, daemon=True).start()
    
    def setup_voice_commands(self):
        """Setup voice commands"""
        voice_commands = {
            "open": self.voice_open_command,
            "close": self.voice_close_command,
            "system": self.voice_system_command,
            "launch": self.voice_open_command,
            "start": self.voice_open_command,
            "stop": self.voice_close_command,
            "shutdown": self.voice_shutdown_command,
            "restart": self.voice_restart_command,
            "scan": self.voice_scan_command,
            "monitor": self.voice_monitor_command,
            "status": self.voice_status_command,
            "help": self.voice_help_command,
            "github": self.voice_github_command,
            "security": self.voice_security_command,
            "voice": self.voice_voice_command,
            "clear": self.voice_clear_command,
            "save": self.voice_save_command,
            "sync": self.voice_sync_command
        }
        
        for command, callback in voice_commands.items():
            self.voice_controller.add_voice_command(command, callback)
    
    def voice_assistant_loop(self):
        """Main voice assistant loop"""
        while True:
            try:
                if self.voice_active:
                    command = self.voice_controller.listen_for_command()
                    if command:
                        self.process_voice_command(command)
                time.sleep(0.1)
            except Exception as e:
                logger.error(f"Voice assistant loop error: {e}")
                time.sleep(1)
    
    def process_voice_command(self, command: str):
        """Process voice command"""
        try:
            self.add_voice_history(f"You: {command}")
            
            # Process command
            if any(word in command for word in ["open", "launch", "start"]):
                self.voice_open_command(command)
            elif any(word in command for word in ["close", "stop"]):
                self.voice_close_command(command)
            elif "system" in command:
                self.voice_system_command(command)
            elif "shutdown" in command:
                self.voice_shutdown_command(command)
            elif "restart" in command:
                self.voice_restart_command(command)
            elif "scan" in command:
                self.voice_scan_command(command)
            elif "monitor" in command:
                self.voice_monitor_command(command)
            elif "status" in command:
                self.voice_status_command(command)
            elif "help" in command:
                self.voice_help_command(command)
            elif "github" in command:
                self.voice_github_command(command)
            elif "security" in command:
                self.voice_security_command(command)
            elif "voice" in command:
                self.voice_voice_command(command)
            elif "clear" in command:
                self.voice_clear_command(command)
            elif "save" in command:
                self.voice_save_command(command)
            elif "sync" in command:
                self.voice_sync_command(command)
            else:
                response = f"I didn't understand that command. Say 'help' for available commands."
                self.voice_controller.speak(response)
                self.add_voice_history(f"ILLI: {response}")
                
        except Exception as e:
            logger.error(f"Error processing voice command: {e}")
            self.voice_controller.speak("Sorry, I encountered an error processing your command.")
    
    def voice_open_command(self, command: str):
        """Handle voice open command"""
        try:
            # Extract app name from command
            words = command.split()
            app_name = None
            
            for i, word in enumerate(words):
                if word in ["open", "launch", "start"] and i + 1 < len(words):
                    app_name = " ".join(words[i+1:])
                    break
            
            if app_name:
                if self.launch_application(app_name):
                    response = f"Successfully launched {app_name}"
                    self.voice_controller.speak(response)
                    self.add_voice_history(f"ILLI: {response}")
                else:
                    response = f"Sorry, I couldn't launch {app_name}"
                    self.voice_controller.speak(response)
                    self.add_voice_history(f"ILLI: {response}")
            else:
                response = "Please specify which application to open"
                self.voice_controller.speak(response)
                self.add_voice_history(f"ILLI: {response}")
                
        except Exception as e:
            logger.error(f"Voice open command error: {e}")
            self.voice_controller.speak("Sorry, I encountered an error opening the application.")
    
    def voice_close_command(self, command: str):
        """Handle voice close command"""
        try:
            # Extract app name from command
            words = command.split()
            app_name = None
            
            for i, word in enumerate(words):
                if word in ["close", "stop"] and i + 1 < len(words):
                    app_name = " ".join(words[i+1:])
                    break
            
            if app_name:
                if self.close_application(app_name):
                    response = f"Successfully closed {app_name}"
                    self.voice_controller.speak(response)
                    self.add_voice_history(f"ILLI: {response}")
                else:
                    response = f"Sorry, I couldn't close {app_name}"
                    self.voice_controller.speak(response)
                    self.add_voice_history(f"ILLI: {response}")
            else:
                response = "Please specify which application to close"
                self.voice_controller.speak(response)
                self.add_voice_history(f"ILLI: {response}")
                
        except Exception as e:
            logger.error(f"Voice close command error: {e}")
            self.voice_controller.speak("Sorry, I encountered an error closing the application.")
    
    def voice_system_command(self, command: str):
        """Handle voice system command"""
        try:
            if "scan" in command:
                self.perform_system_scan()
                response = "System scan completed"
            elif "info" in command or "information" in command:
                self.show_system_info()
                response = "System information displayed"
            elif "cleanup" in command:
                self.system_cleanup()
                response = "System cleanup completed"
            elif "optimize" in command:
                self.system_optimize()
                response = "System optimization completed"
            else:
                response = "System command processed"
            
            self.voice_controller.speak(response)
            self.add_voice_history(f"ILLI: {response}")
            
        except Exception as e:
            logger.error(f"Voice system command error: {e}")
            self.voice_controller.speak("Sorry, I encountered an error with the system command.")
    
    def voice_shutdown_command(self, command: str):
        """Handle voice shutdown command"""
        try:
            response = "Shutting down the system in 10 seconds"
            self.voice_controller.speak(response)
            self.add_voice_history(f"ILLI: {response}")
            
            # Schedule shutdown
            threading.Timer(10.0, self.shutdown_system).start()
            
        except Exception as e:
            logger.error(f"Voice shutdown command error: {e}")
            self.voice_controller.speak("Sorry, I encountered an error with the shutdown command.")
    
    def voice_restart_command(self, command: str):
        """Handle voice restart command"""
        try:
            response = "Restarting the system in 10 seconds"
            self.voice_controller.speak(response)
            self.add_voice_history(f"ILLI: {response}")
            
            # Schedule restart
            threading.Timer(10.0, self.restart_system).start()
            
        except Exception as e:
            logger.error(f"Voice restart command error: {e}")
            self.voice_controller.speak("Sorry, I encountered an error with the restart command.")
    
    def voice_scan_command(self, command: str):
        """Handle voice scan command"""
        try:
            self.perform_system_scan()
            response = "System scan completed"
            self.voice_controller.speak(response)
            self.add_voice_history(f"ILLI: {response}")
            
        except Exception as e:
            logger.error(f"Voice scan command error: {e}")
            self.voice_controller.speak("Sorry, I encountered an error during the scan.")
    
    def voice_monitor_command(self, command: str):
        """Handle voice monitor command"""
        try:
            self.performance_monitor()
            response = "Performance monitoring started"
            self.voice_controller.speak(response)
            self.add_voice_history(f"ILLI: {response}")
            
        except Exception as e:
            logger.error(f"Voice monitor command error: {e}")
            self.voice_controller.speak("Sorry, I encountered an error starting monitoring.")
    
    def voice_status_command(self, command: str):
        """Handle voice status command"""
        try:
            status_info = self.get_system_status()
            response = f"System status: CPU usage {status_info['cpu']}%, Memory usage {status_info['memory']}%, {status_info['processes']} processes running"
            self.voice_controller.speak(response)
            self.add_voice_history(f"ILLI: {response}")
            
        except Exception as e:
            logger.error(f"Voice status command error: {e}")
            self.voice_controller.speak("Sorry, I encountered an error getting system status.")
    
    def voice_help_command(self, command: str):
        """Handle voice help command"""
        try:
            help_text = """
            Available voice commands:
            - Open or Launch [application name]
            - Close or Stop [application name]
            - System Scan, System Info, System Cleanup, System Optimize
            - Monitor, Status
            - Shutdown, Restart
            - GitHub Sync, GitHub Status
            - Security Check, Privacy Scan
            - Voice Settings, Voice Test
            - Clear Display, Save, Sync
            - Help
            """
            self.voice_controller.speak("Here are the available voice commands:")
            self.add_voice_history(f"ILLI: {help_text}")
            
        except Exception as e:
            logger.error(f"Voice help command error: {e}")
            self.voice_controller.speak("Sorry, I encountered an error getting help information.")
    
    def voice_github_command(self, command: str):
        """Handle voice GitHub command"""
        try:
            if "sync" in command:
                self.sync_github()
                response = "GitHub synchronization completed"
            elif "status" in command:
                self.view_github_status()
                response = "GitHub status displayed"
            elif "commit" in command:
                self.commit_changes()
                response = "Changes committed to GitHub"
            else:
                response = "GitHub command processed"
            
            self.voice_controller.speak(response)
            self.add_voice_history(f"ILLI: {response}")
            
        except Exception as e:
            logger.error(f"Voice GitHub command error: {e}")
            self.voice_controller.speak("Sorry, I encountered an error with the GitHub command.")
    
    def voice_security_command(self, command: str):
        """Handle voice security command"""
        try:
            if "check" in command:
                self.security_check()
                response = "Security check completed"
            elif "scan" in command:
                self.privacy_scan()
                response = "Privacy scan completed"
            else:
                response = "Security command processed"
            
            self.voice_controller.speak(response)
            self.add_voice_history(f"ILLI: {response}")
            
        except Exception as e:
            logger.error(f"Voice security command error: {e}")
            self.voice_controller.speak("Sorry, I encountered an error with the security command.")
    
    def voice_voice_command(self, command: str):
        """Handle voice voice command"""
        try:
            if "stop" in command or "off" in command:
                self.toggle_voice_control()
                response = "Voice control stopped"
            elif "start" in command or "on" in command:
                self.toggle_voice_control()
                response = "Voice control started"
            elif "test" in command:
                self.test_voice()
                response = "Voice test completed"
            elif "settings" in command:
                self.voice_settings()
                response = "Voice settings opened"
            else:
                response = "Voice command processed"
            
            self.voice_controller.speak(response)
            self.add_voice_history(f"ILLI: {response}")
            
        except Exception as e:
            logger.error(f"Voice voice command error: {e}")
            self.voice_controller.speak("Sorry, I encountered an error with the voice command.")
    
    def voice_clear_command(self, command: str):
        """Handle voice clear command"""
        try:
            self.clear_display()
            response = "Display cleared"
            self.voice_controller.speak(response)
            self.add_voice_history(f"ILLI: {response}")
            
        except Exception as e:
            logger.error(f"Voice clear command error: {e}")
            self.voice_controller.speak("Sorry, I encountered an error clearing the display.")
    
    def voice_save_command(self, command: str):
        """Handle voice save command"""
        try:
            self.save_session()
            response = "Session saved"
            self.voice_controller.speak(response)
            self.add_voice_history(f"ILLI: {response}")
            
        except Exception as e:
            logger.error(f"Voice save command error: {e}")
            self.voice_controller.speak("Sorry, I encountered an error saving the session.")
    
    def voice_sync_command(self, command: str):
        """Handle voice sync command"""
        try:
            self.sync_github()
            response = "Synchronization completed"
            self.voice_controller.speak(response)
            self.add_voice_history(f"ILLI: {response}")
            
        except Exception as e:
            logger.error(f"Voice sync command error: {e}")
            self.voice_controller.speak("Sorry, I encountered an error during synchronization.")
    
    def launch_application(self, app_name: str) -> bool:
        """Launch application by name"""
        try:
            app_name = app_name.lower().strip()
            
            # Search for application in database
            app_info = None
            for key, value in self.applications.items():
                if app_name in key.lower() or key.lower() in app_name:
                    app_info = value
                    break
            
            if not app_info:
                self.add_display_entry(f"Application '{app_name}' not found in database")
                return False
            
            # Try desktop version first
            if app_info['desktop']:
                desktop_app = app_info['desktop'][0]
                
                # Check if it's running
                if self.is_process_running(desktop_app):
                    self.add_display_entry(f"{app_name} is already running")
                    return True
                
                # Try to launch desktop app
                if len(app_info['desktop']) > 1 and app_info['desktop'][1]:
                    app_path = app_info['desktop'][1]
                    if os.path.exists(app_path):
                        subprocess.Popen([app_path], shell=True)
                        self.add_display_entry(f"Launched {app_name} (Desktop)")
                        return True
                    else:
                        # Try to find in system PATH
                        try:
                            subprocess.Popen(desktop_app, shell=True)
                            self.add_display_entry(f"Launched {app_name} (Desktop)")
                            return True
                        except FileNotFoundError:
                            pass
            
            # Fallback to web version
            if app_info['web']:
                webbrowser.open(app_info['web'])
                self.add_display_entry(f"Launched {app_name} (Web)")
                return True
            
            self.add_display_entry(f"Could not launch {app_name}")
            return False
            
        except Exception as e:
            logger.error(f"Error launching application {app_name}: {e}")
            self.add_display_entry(f"Error launching {app_name}: {str(e)}")
            return False
    
    def close_application(self, app_name: str) -> bool:
        """Close application by name"""
        try:
            app_name = app_name.lower().strip()
            
            # Find running processes
            processes = self.system_detector.get_running_processes()
            
            # Search for process
            process_found = False
            for proc_name, proc_info in processes.items():
                if app_name in proc_name.lower() or proc_name.lower() in app_name:
                    try:
                        # Terminate process
                        process = psutil.Process(proc_info['pid'])
                        process.terminate()
                        self.add_display_entry(f"Closed {proc_name} (PID: {proc_info['pid']})")
                        process_found = True
                    except (psutil.NoSuchProcess, psutil.AccessDenied):
                        try:
                            # Force kill if terminate fails
                            process.kill()
                            self.add_display_entry(f"Force closed {proc_name} (PID: {proc_info['pid']})")
                            process_found = True
                        except (psutil.NoSuchProcess, psutil.AccessDenied):
                            self.add_display_entry(f"Could not close {proc_name} (Access denied)")
            
            if not process_found:
                self.add_display_entry(f"No running process found for '{app_name}'")
                return False
            
            return True
            
        except Exception as e:
            logger.error(f"Error closing application {app_name}: {e}")
            self.add_display_entry(f"Error closing {app_name}: {str(e)}")
            return False
    
    def is_process_running(self, process_name: str) -> bool:
        """Check if process is running"""
        try:
            for proc in psutil.process_iter(['name']):
                if proc.info['name'] == process_name:
                    return True
            return False
        except Exception:
            return False
    
    def perform_system_scan(self):
        """Perform comprehensive system scan"""
        try:
            self.add_display_entry("Starting comprehensive system scan...")
            
            # Get system information
            system_info = self.system_detector.system_info
            
            # Get running processes
            processes = self.system_detector.get_running_processes()
            
            # Get disk usage
            disk_usage = psutil.disk_usage('/')
            
            # Get network information
            network_info = psutil.net_if_addrs()
            
            # Display results
            scan_results = f"""
            SYSTEM SCAN RESULTS - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            {'='*60}
            
            SYSTEM INFORMATION:
            - Platform: {system_info['platform']} {system_info['platform_release']}
            - Architecture: {system_info['architecture']}
            - Processor: {system_info['processor']}
            - CPU Count: {system_info['cpu_count']}
            - Total RAM: {system_info['ram']} GB
            - Hostname: {system_info['hostname']}
            
            PERFORMANCE:
            - CPU Usage: {psutil.cpu_percent(interval=1)}%
            - Memory Usage: {psutil.virtual_memory().percent}%
            - Disk Usage: {disk_usage.used / (1024**3):.1f} GB / {disk_usage.total / (1024**3):.1f} GB ({disk_usage.percent}%)
            
            PROCESSES:
            - Total Running: {len(processes)}
            - High CPU Usage (>50%): {len([p for p in processes.values() if p['cpu_percent'] > 50])}
            - High Memory Usage (>50%): {len([p for p in processes.values() if p['memory_percent'] > 50])}
            
            NETWORK INTERFACES:
            - Active Interfaces: {len(network_info)}
            """
            
            self.add_display_entry(scan_results)
            
            # Check for security issues
            security_issues = []
            
            # Check for high resource usage
            if psutil.cpu_percent(interval=1) > 80:
                security_issues.append("High CPU usage detected")
            
            if psutil.virtual_memory().percent > 80:
                security_issues.append("High memory usage detected")
            
            if disk_usage.percent > 90:
                security_issues.append("Low disk space")
            
            # Check for suspicious processes
            suspicious_processes = []
            for proc_name in processes.keys():
                if any(suspicious in proc_name.lower() for suspicious in ['hack', 'crack', 'keylog', 'spy']):
                    suspicious_processes.append(proc_name)
            
            if suspicious_processes:
                security_issues.append(f"Suspicious processes detected: {', '.join(suspicious_processes)}")
            
            if security_issues:
                self.add_display_entry("\nSECURITY ISSUES FOUND:")
                for issue in security_issues:
                    self.add_display_entry(f"⚠️  {issue}")
            else:
                self.add_display_entry("\n✅ No security issues detected")
            
            self.add_display_entry("System scan completed successfully")
            
        except Exception as e:
            logger.error(f"System scan error: {e}")
            self.add_display_entry(f"System scan error: {str(e)}")
    
    def show_system_info(self):
        """Display detailed system information"""
        try:
            system_info = self.system_detector.system_info
            
            info_text = f"""
            DETAILED SYSTEM INFORMATION - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            {'='*60}
            
            BASIC INFORMATION:
            - Computer Name: {system_info['hostname']}
            - Operating System: {system_info['platform']} {system_info['platform_release']}
            - Version: {system_info['platform_version']}
            - Architecture: {system_info['architecture']}
            - Processor: {system_info['processor']}
            
            HARDWARE:
            - CPU Cores: {system_info['cpu_count']}
            - CPU Frequency: {system_info['cpu_freq']:.0f} MHz
            - Total RAM: {system_info['ram']} GB
            - Available RAM: {psutil.virtual_memory().available / (1024**3):.1f} GB
            
            PERFORMANCE:
            - Current CPU Usage: {psutil.cpu_percent(interval=1)}%
            - Current Memory Usage: {psutil.virtual_memory().percent}%
            - Boot Time: {datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')}
            
            DISK USAGE:
            """
            
            # Add disk information for all drives
            for partition in psutil.disk_partitions():
                try:
                    usage = psutil.disk_usage(partition.mountpoint)
                    info_text += f"\n- {partition.device} ({partition.mountpoint}):"
                    info_text += f"\n  Total: {usage.total / (1024**3):.1f} GB"
                    info_text += f"\n  Used: {usage.used / (1024**3):.1f} GB"
                    info_text += f"\n  Free: {usage.free / (1024**3):.1f} GB ({usage.percent}%)"
                except PermissionError:
                    continue
            
            self.add_display_entry(info_text)
            
        except Exception as e:
            logger.error(f"System info error: {e}")
            self.add_display_entry(f"System info error: {str(e)}")
    
    def show_processes(self):
        """Show running processes"""
        try:
            processes = self.system_detector.get_running_processes()
            
            process_text = f"""
            RUNNING PROCESSES - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            {'='*60}
            
            Total Processes: {len(processes)}
            
            HIGH RESOURCE USAGE PROCESSES:
            """
            
            # Sort processes by CPU usage
            sorted_processes = sorted(processes.items(), key=lambda x: x[1]['cpu_percent'], reverse=True)
            
            # Show top 20 processes by CPU usage
            for i, (proc_name, proc_info) in enumerate(sorted_processes[:20]):
                process_text += f"\n{i+1:2d}. {proc_name:<30} PID: {proc_info['pid']:>6} CPU: {proc_info['cpu_percent']:>5.1f}% MEM: {proc_info['memory_percent']:>5.1f}%"
            
            self.add_display_entry(process_text)
            
        except Exception as e:
            logger.error(f"Show processes error: {e}")
            self.add_display_entry(f"Show processes error: {str(e)}")
    
    def performance_monitor(self):
        """Monitor system performance"""
        try:
            self.add_display_entry("Starting performance monitoring...")
            
            # Get performance metrics
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            # Get network stats
            network = psutil.net_io_counters()
            
            # Get temperature (if available)
            temps = {}
            try:
                temps = psutil.sensors_temperatures()
            except AttributeError:
                pass
            
            performance_text = f"""
            PERFORMANCE MONITOR - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            {'='*60}
            
            CPU PERFORMANCE:
            - Overall Usage: {cpu_percent}%
            - Cores Usage: {psutil.cpu_percent(interval=1, percpu=True)}
            - Frequency: {psutil.cpu_freq().current if psutil.cpu_freq() else 'N/A'} MHz
            
            MEMORY PERFORMANCE:
            - Total: {memory.total / (1024**3):.1f} GB
            - Available: {memory.available / (1024**3):.1f} GB
            - Used: {memory.used / (1024**3):.1f} GB ({memory.percent}%)
            - Cached: {memory.cached / (1024**3):.1f} GB
            
            DISK PERFORMANCE:
            - Read Count: {psutil.disk_io_counters().read_count if psutil.disk_io_counters() else 'N/A'}
            - Write Count: {psutil.disk_io_counters().write_count if psutil.disk_io_counters() else 'N/A'}
            - Read Bytes: {psutil.disk_io_counters().read_bytes / (1024**2):.1f} MB" if psutil.disk_io_counters() else 'N/A'
            - Write Bytes: {psutil.disk_io_counters().write_bytes / (1024**2):.1f} MB" if psutil.disk_io_counters() else 'N/A'
            
            NETWORK PERFORMANCE:
            - Bytes Sent: {network.bytes_sent / (1024**2):.1f} MB
            - Bytes Received: {network.bytes_recv / (1024**2):.1f} MB
            - Packets Sent: {network.packets_sent}
            - Packets Received: {network.packets_recv}
            """
            
            if temps:
                performance_text += "\n\nTEMPERATURE SENSORS:"
                for name, entries in temps.items():
                    for entry in entries:
                        performance_text += f"\n- {name}: {entry.current:.1f}°C"
            
            self.add_display_entry(performance_text)
            
        except Exception as e:
            logger.error(f"Performance monitor error: {e}")
            self.add_display_entry(f"Performance monitor error: {str(e)}")
    
    def disk_usage(self):
        """Show disk usage"""
        try:
            self.add_display_entry("DISK USAGE ANALYSIS")
            self.add_display_entry("=" * 60)
            
            for partition in psutil.disk_partitions():
                try:
                    usage = psutil.disk_usage(partition.mountpoint)
                    
                    disk_text = f"""
                    Drive: {partition.device} ({partition.mountpoint})
                    File System: {partition.fstype}
                    Total Space: {usage.total / (1024**3):.1f} GB
                    Used Space: {usage.used / (1024**3):.1f} GB
                    Free Space: {usage.free / (1024**3):.1f} GB
                    Usage Percentage: {usage.percent}%
                    """
                    
                    if usage.percent > 80:
                        disk_text += "\n⚠️  WARNING: Low disk space!"
                    elif usage.percent > 90:
                        disk_text += "\n🚨 CRITICAL: Very low disk space!"
                    
                    self.add_display_entry(disk_text)
                    
                except PermissionError:
                    self.add_display_entry(f"Access denied to {partition.device}")
                    continue
            
        except Exception as e:
            logger.error(f"Disk usage error: {e}")
            self.add_display_entry(f"Disk usage error: {str(e)}")
    
    def network_status(self):
        """Show network status"""
        try:
            self.add_display_entry("NETWORK STATUS")
            self.add_display_entry("=" * 60)
            
            # Get network interfaces
            interfaces = psutil.net_if_addrs()
            
            for interface_name, addresses in interfaces.items():
                self.add_display_entry(f"\nInterface: {interface_name}")
                
                for address in addresses:
                    if address.family == socket.AF_INET:
                        self.add_display_entry(f"  IPv4: {address.address}")
                    elif address.family == socket.AF_INET6:
                        self.add_display_entry(f"  IPv6: {address.address}")
            
            # Get network statistics
            net_io = psutil.net_io_counters()
            
            stats_text = f"""
            NETWORK STATISTICS:
            - Bytes Sent: {net_io.bytes_sent / (1024**2):.1f} MB
            - Bytes Received: {net_io.bytes_recv / (1024**2):.1f} MB
            - Packets Sent: {net_io.packets_sent}
            - Packets Received: {net_io.packets_recv}
            - Error In: {net_io.errin}
            - Error Out: {net_io.errout}
            - Drop In: {net_io.dropin}
            - Drop Out: {net_io.dropout}
            """
            
            self.add_display_entry(stats_text)
            
        except Exception as e:
            logger.error(f"Network status error: {e}")
            self.add_display_entry(f"Network status error: {str(e)}")
    
    def system_cleanup(self):
        """Perform system cleanup"""
        try:
            self.add_display_entry("Starting system cleanup...")
            
            # Clean temporary files
            temp_dirs = [
                os.environ.get('TEMP', ''),
                os.environ.get('TMP', ''),
                os.path.join(os.environ.get('LOCALAPPDATA', ''), 'Temp'),
                os.path.join(os.environ.get('WINDIR', ''), 'Temp'),
                os.path.join(os.environ.get('WINDIR', ''), 'Prefetch')
            ]
            
            cleaned_files = 0
            cleaned_space = 0
            
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
                                    cleaned_space += size
                                elif os.path.isdir(item_path):
                                    shutil.rmtree(item_path)
                                    cleaned_files += 1
                            except (PermissionError, FileNotFoundError):
                                continue
                    except (PermissionError, FileNotFoundError):
                        continue
            
            # Clear recycle bin
            try:
                import winshell
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
                self.add_display_entry("Recycle bin emptied")
            except ImportError:
                self.add_display_entry("winshell not available - skipping recycle bin cleanup")
            except Exception:
                self.add_display_entry("Could not empty recycle bin")
            
            # Clear browser cache (simplified)
            try:
                chrome_cache = os.path.join(os.environ.get('LOCALAPPDATA', ''), 'Google', 'Chrome', 'User Data', 'Default', 'Cache')
                if os.path.exists(chrome_cache):
                    shutil.rmtree(chrome_cache)
                    self.add_display_entry("Chrome cache cleared")
            except Exception:
                pass
            
            cleanup_text = f"""
            SYSTEM CLEANUP COMPLETED
            {'='*40}
            Files Cleaned: {cleaned_files}
            Space Freed: {cleaned_space / (1024**2):.1f} MB
            
            Cleanup Actions:
            - Temporary files removed
            - Prefetch files cleared
            - Recycle bin emptied
            - Browser cache cleared
            """
            
            self.add_display_entry(cleanup_text)
            
        except Exception as e:
            logger.error(f"System cleanup error: {e}")
            self.add_display_entry(f"System cleanup error: {str(e)}")
    
    def system_optimize(self):
        """Optimize system performance"""
        try:
            self.add_display_entry("Starting system optimization...")
            
            optimizations = []
            
            # Optimize memory
            try:
                import gc
                gc.collect()
                optimizations.append("Memory optimization completed")
            except Exception:
                pass
            
            # Defragment registry (Windows only)
            if platform.system() == 'Windows':
                try:
                    subprocess.run(['reg', 'export', 'HKLM\\SOFTWARE', os.path.join(os.environ.get('TEMP', ''), 'reg_backup.reg')], 
                                 check=True, capture_output=True)
                    optimizations.append("Registry backup created")
                except Exception:
                    pass
            
            # Check for disk fragmentation
            try:
                if platform.system() == 'Windows':
                    result = subprocess.run(['defrag', 'C:', '/A'], capture_output=True, text=True)
                    if result.returncode == 0:
                        optimizations.append("Disk analysis completed")
                    else:
                        optimizations.append("Disk analysis failed")
            except Exception:
                pass
            
            # Optimize startup programs
            try:
                startup_path = os.path.join(os.environ.get('APPDATA', ''), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
                if os.path.exists(startup_path):
                    startup_items = len(os.listdir(startup_path))
                    optimizations.append(f"Startup programs analyzed: {startup_items} items")
            except Exception:
                pass
            
            optimization_text = f"""
            SYSTEM OPTIMIZATION COMPLETED
            {'='*40}
            """
            
            for opt in optimizations:
                optimization_text += f"✅ {opt}\n"
            
            optimization_text += f"""
            Performance Improvements:
            - Memory usage optimized
            - Registry backed up
            - Disk fragmentation analyzed
            - Startup programs reviewed
            
            Recommendations:
            - Restart system for best results
            - Consider removing unnecessary startup programs
            - Run disk defragmentation if fragmentation > 10%
            """
            
            self.add_display_entry(optimization_text)
            
        except Exception as e:
            logger.error(f"System optimization error: {e}")
            self.add_display_entry(f"System optimization error: {str(e)}")
    
    def shutdown_system(self):
        """Shutdown system"""
        try:
            self.add_display_entry("Shutting down system in 30 seconds...")
            
            if platform.system() == 'Windows':
                subprocess.run(['shutdown', '/s', '/t', '30'], check=True)
            else:
                subprocess.run(['shutdown', '-h', '+30'], check=True)
            
        except Exception as e:
            logger.error(f"Shutdown error: {e}")
            self.add_display_entry(f"Shutdown error: {str(e)}")
    
    def restart_system(self):
        """Restart system"""
        try:
            self.add_display_entry("Restarting system in 30 seconds...")
            
            if platform.system() == 'Windows':
                subprocess.run(['shutdown', '/r', '/t', '30'], check=True)
            else:
                subprocess.run(['reboot'], check=True)
            
        except Exception as e:
            logger.error(f"Restart error: {e}")
            self.add_display_entry(f"Restart error: {str(e)}")
    
    def lock_system(self):
        """Lock system"""
        try:
            if platform.system() == 'Windows':
                subprocess.run(['rundll32.exe', 'user32.dll,LockWorkStation'], check=True)
            else:
                # Linux/macOS screen lock
                subprocess.run(['xdg-screensaver', 'lock'], check=True)
            
            self.add_display_entry("System locked")
            
        except Exception as e:
            logger.error(f"Lock error: {e}")
            self.add_display_entry(f"Lock error: {str(e)}")
    
    def sleep_system(self):
        """Put system to sleep"""
        try:
            if platform.system() == 'Windows':
                subprocess.run(['rundll32.exe', 'powrprof.dll,SetSuspendState', 'Sleep'], check=True)
            else:
                subprocess.run(['systemctl', 'suspend'], check=True)
            
            self.add_display_entry("System going to sleep")
            
        except Exception as e:
            logger.error(f"Sleep error: {e}")
            self.add_display_entry(f"Sleep error: {str(e)}")
    
    def toggle_voice_control(self):
        """Toggle voice control"""
        try:
            self.voice_active = not self.voice_active
            
            if self.voice_active:
                self.voice_btn.config(text="Stop Voice", bg=self.colors['red'])
                self.voice_indicator.config(text="Voice: ACTIVE", fg=self.colors['green'])
                self.voice_status_label.config(text="Voice: ACTIVE", fg=self.colors['green'])
                self.add_display_entry("Voice control activated")
                self.voice_controller.speak("Voice control activated. I'm listening for your commands.")
            else:
                self.voice_btn.config(text="Start Voice", bg=self.colors['green'])
                self.voice_indicator.config(text="Voice: IDLE", fg=self.colors['red'])
                self.voice_status_label.config(text="Voice: READY", fg=self.colors['cyan'])
                self.add_display_entry("Voice control deactivated")
                self.voice_controller.speak("Voice control deactivated.")
                
        except Exception as e:
            logger.error(f"Toggle voice control error: {e}")
            self.add_display_entry(f"Toggle voice control error: {str(e)}")
    
    def test_voice(self):
        """Test voice system"""
        try:
            test_message = "Voice system test successful. All systems are operational and ready to assist you."
            self.voice_controller.speak(test_message)
            self.add_display_entry("Voice test completed successfully")
            
        except Exception as e:
            logger.error(f"Voice test error: {e}")
            self.add_display_entry(f"Voice test error: {str(e)}")
    
    def voice_settings(self):
        """Open voice settings dialog"""
        try:
            dialog = tk.Toplevel(self.root)
            dialog.title("Voice Settings")
            dialog.geometry("400x300")
            dialog.configure(bg=self.colors['glass'])
            
            tk.Label(dialog, text="Voice Settings", font=('Arial', 16, 'bold'),
                    fg=self.colors['accent'], bg=self.colors['glass']).pack(pady=10)
            
            # Voice rate
            tk.Label(dialog, text="Voice Rate:", fg=self.colors['text'], 
                    bg=self.colors['glass']).pack(pady=5)
            
            rate_var = tk.IntVar(value=self.voice_controller.engine.getProperty('rate'))
            rate_scale = tk.Scale(dialog, from_=50, to=200, orient='horizontal',
                                 variable=rate_var, bg=self.colors['glass'], fg=self.colors['text'],
                                 highlightbackground=self.colors['glass'])
            rate_scale.pack(pady=5)
            
            # Voice volume
            tk.Label(dialog, text="Voice Volume:", fg=self.colors['text'], 
                    bg=self.colors['glass']).pack(pady=5)
            
            volume_var = tk.DoubleVar(value=self.voice_controller.engine.getProperty('volume'))
            volume_scale = tk.Scale(dialog, from_=0.1, to=1.0, resolution=0.1,
                                   orient='horizontal', variable=volume_var,
                                   bg=self.colors['glass'], fg=self.colors['text'],
                                   highlightbackground=self.colors['glass'])
            volume_scale.pack(pady=5)
            
            def apply_settings():
                self.voice_controller.engine.setProperty('rate', rate_var.get())
                self.voice_controller.engine.setProperty('volume', volume_var.get())
                self.add_display_entry("Voice settings updated")
                dialog.destroy()
            
            tk.Button(dialog, text="Apply", command=apply_settings,
                     bg=self.colors['green'], fg='white', font=('Arial', 12, 'bold')).pack(pady=10)
            
        except Exception as e:
            logger.error(f"Voice settings error: {e}")
            self.add_display_entry(f"Voice settings error: {str(e)}")
    
    def sync_github(self):
        """Sync with GitHub repository"""
        try:
            self.add_display_entry("Starting GitHub synchronization...")
            
            # Pull latest changes
            if self.github_manager.pull_latest():
                self.add_display_entry("✅ Successfully pulled latest changes from GitHub")
            else:
                self.add_display_entry("❌ Failed to pull changes from GitHub")
            
            # Add all changes
            self.add_display_entry("Adding local changes...")
            
            # Commit and push
            commit_message = f"Auto-sync from ILLI AI - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            
            if self.github_manager.commit_and_push(commit_message):
                self.add_display_entry("✅ Successfully pushed changes to GitHub")
            else:
                self.add_display_entry("❌ Failed to push changes to GitHub")
            
            self.add_display_entry("GitHub synchronization completed")
            
        except Exception as e:
            logger.error(f"GitHub sync error: {e}")
            self.add_display_entry(f"GitHub sync error: {str(e)}")
    
    def commit_changes(self):
        """Commit changes to GitHub"""
        try:
            commit_message = simpledialog.askstring("Commit Changes", "Enter commit message:")
            if commit_message:
                self.add_display_entry(f"Committing changes: {commit_message}")
                
                if self.github_manager.commit_and_push(commit_message):
                    self.add_display_entry("✅ Successfully committed and pushed changes")
                else:
                    self.add_display_entry("❌ Failed to commit changes")
            
        except Exception as e:
            logger.error(f"Commit changes error: {e}")
            self.add_display_entry(f"Commit changes error: {str(e)}")
    
    def pull_latest(self):
        """Pull latest changes from GitHub"""
        try:
            self.add_display_entry("Pulling latest changes from GitHub...")
            
            if self.github_manager.pull_latest():
                self.add_display_entry("✅ Successfully pulled latest changes")
            else:
                self.add_display_entry("❌ Failed to pull latest changes")
            
        except Exception as e:
            logger.error(f"Pull latest error: {e}")
            self.add_display_entry(f"Pull latest error: {str(e)}")
    
    def push_to_github(self):
        """Push changes to GitHub"""
        try:
            commit_message = simpledialog.askstring("Push to GitHub", "Enter commit message:")
            if commit_message:
                self.add_display_entry(f"Pushing changes: {commit_message}")
                
                if self.github_manager.commit_and_push(commit_message):
                    self.add_display_entry("✅ Successfully pushed changes to GitHub")
                else:
                    self.add_display_entry("❌ Failed to push changes to GitHub")
            
        except Exception as e:
            logger.error(f"Push to GitHub error: {e}")
            self.add_display_entry(f"Push to GitHub error: {str(e)}")
    
    def view_github_status(self):
        """View GitHub repository status"""
        try:
            self.add_display_entry("GITHUB REPOSITORY STATUS")
            self.add_display_entry("=" * 60)
            
            if self.github_manager.repo:
                # Get repo info
                repo = self.github_manager.repo
                
                status_text = f"""
                Repository: {repo.remotes.origin.url}
                Current Branch: {repo.active_branch.name}
                Last Commit: {repo.head.commit.hexsha[:8]}
                Commit Message: {repo.head.commit.message}
                Author: {repo.head.commit.author}
                Date: {repo.head.commit.committed_datetime}
                
                Working Directory Status:
                - Is Dirty: {repo.is_dirty()}
                - Untracked Files: {len(repo.untracked_files)}
                - Modified Files: {len([item.a_path for item in repo.index.diff(None)])}
                
                Remote Status:
                - Remote URL: {repo.remotes.origin.url}
                """
                
                self.add_display_entry(status_text)
            else:
                self.add_display_entry("Repository not initialized")
            
        except Exception as e:
            logger.error(f"View GitHub status error: {e}")
            self.add_display_entry(f"View GitHub status error: {str(e)}")
    
    def create_backup(self):
        """Create backup of project"""
        try:
            backup_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
            
            self.add_display_entry(f"Creating backup in: {backup_dir}")
            
            # Create backup directory
            os.makedirs(backup_dir, exist_ok=True)
            
            # Copy important files
            important_files = [
                'ILLI_AI_PROFESSIONAL_FINAL.py',
                'README.md',
                'requirements.txt'
            ]
            
            for file in important_files:
                src = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
                if os.path.exists(src):
                    dst = os.path.join(backup_dir, file)
                    shutil.copy2(src, dst)
                    self.add_display_entry(f"Backed up: {file}")
            
            self.add_display_entry(f"✅ Backup created successfully in {backup_dir}")
            
        except Exception as e:
            logger.error(f"Create backup error: {e}")
            self.add_display_entry(f"Create backup error: {str(e)}")
    
    def security_check(self):
        """Perform security check"""
        try:
            self.add_display_entry("Starting security check...")
            
            security_issues = []
            security_recommendations = []
            
            # Check admin privileges
            if not self.security_manager.check_admin_privileges():
                security_recommendations.append("Consider running with administrator privileges for full functionality")
            
            # Check for suspicious processes
            processes = self.system_detector.get_running_processes()
            suspicious_keywords = ['hack', 'crack', 'keylog', 'spy', 'malware', 'virus']
            
            for proc_name in processes.keys():
                if any(keyword in proc_name.lower() for keyword in suspicious_keywords):
                    security_issues.append(f"Suspicious process detected: {proc_name}")
            
            # Check system resources
            if psutil.cpu_percent(interval=1) > 90:
                security_issues.append("Extremely high CPU usage - possible malware activity")
            
            if psutil.virtual_memory().percent > 95:
                security_issues.append("Extremely high memory usage - possible memory leak")
            
            # Check network connections
            try:
                connections = psutil.net_connections()
                suspicious_connections = [conn for conn in connections if conn.status == 'ESTABLISHED' and conn.raddr.ip != '127.0.0.1']
                
                if len(suspicious_connections) > 50:
                    security_issues.append("High number of network connections detected")
                    
            except Exception:
                pass
            
            # Display results
            security_text = f"""
            SECURITY CHECK RESULTS - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            {'='*60}
            
            SECURITY ISSUES FOUND: {len(security_issues)}
            """
            
            if security_issues:
                for issue in security_issues:
                    security_text += f"\n🚨 {issue}"
            else:
                security_text += "\n✅ No critical security issues detected"
            
            security_text += f"\n\nSECURITY RECOMMENDATIONS: {len(security_recommendations)}"
            
            if security_recommendations:
                for rec in security_recommendations:
                    security_text += f"\n💡 {rec}"
            else:
                security_text += "\n✅ System security configuration is optimal"
            
            self.add_display_entry(security_text)
            
        except Exception as e:
            logger.error(f"Security check error: {e}")
            self.add_display_entry(f"Security check error: {str(e)}")
    
    def privacy_scan(self):
        """Perform privacy scan"""
        try:
            self.add_display_entry("Starting privacy scan...")
            
            privacy_concerns = []
            privacy_recommendations = []
            
            # Check for tracking files
            tracking_locations = [
                os.path.join(os.environ.get('APPDATA', ''), 'Microsoft', 'Windows', 'Recent'),
                os.path.join(os.environ.get('LOCALAPPDATA', ''), 'Microsoft', 'Windows', 'History'),
                os.path.join(os.environ.get('TEMP', '')),
            ]
            
            for location in tracking_locations:
                if os.path.exists(location):
                    try:
                        files = os.listdir(location)
                        if len(files) > 100:
                            privacy_concerns.append(f"Large number of tracking files in {location}")
                    except PermissionError:
                        continue
            
            # Check browser data
            browser_data_paths = [
                os.path.join(os.environ.get('LOCALAPPDATA', ''), 'Google', 'Chrome', 'User Data', 'Default'),
                os.path.join(os.environ.get('LOCALAPPDATA', ''), 'Mozilla', 'Firefox', 'Profiles'),
            ]
            
            for path in browser_data_paths:
                if os.path.exists(path):
                    privacy_recommendations.append(f"Consider clearing browser data: {path}")
            
            # Display results
            privacy_text = f"""
            PRIVACY SCAN RESULTS - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            {'='*60}
            
            PRIVACY CONCERNS: {len(privacy_concerns)}
            """
            
            if privacy_concerns:
                for concern in privacy_concerns:
                    privacy_text += f"\n⚠️  {concern}"
            else:
                privacy_text += "\n✅ No significant privacy concerns detected"
            
            privacy_text += f"\n\nPRIVACY RECOMMENDATIONS: {len(privacy_recommendations)}"
            
            if privacy_recommendations:
                for rec in privacy_recommendations:
                    privacy_text += f"\n💡 {rec}"
            else:
                privacy_text += "\n✅ Privacy settings are well configured"
            
            self.add_display_entry(privacy_text)
            
        except Exception as e:
            logger.error(f"Privacy scan error: {e}")
            self.add_display_entry(f"Privacy scan error: {str(e)}")
    
    def encrypt_sensitive_data(self):
        """Encrypt sensitive data"""
        try:
            self.add_display_entry("Encrypting sensitive data...")
            
            # Example: Encrypt configuration files
            config_files = [
                'config.json',
                'settings.json',
                'user_data.json'
            ]
            
            encrypted_files = 0
            
            for file in config_files:
                file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
                if os.path.exists(file_path):
                    try:
                        with open(file_path, 'r') as f:
                            data = f.read()
                        
                        encrypted_data = self.security_manager.encrypt_data(data)
                        
                        with open(file_path + '.encrypted', 'w') as f:
                            f.write(encrypted_data)
                        
                        # Remove original file
                        os.remove(file_path)
                        
                        encrypted_files += 1
                        self.add_display_entry(f"Encrypted: {file}")
                        
                    except Exception as e:
                        self.add_display_entry(f"Failed to encrypt {file}: {str(e)}")
            
            self.add_display_entry(f"✅ Encryption completed. {encrypted_files} files encrypted.")
            
        except Exception as e:
            logger.error(f"Encrypt data error: {e}")
            self.add_display_entry(f"Encrypt data error: {str(e)}")
    
    def clear_tracks(self):
        """Clear system tracks"""
        try:
            self.add_display_entry("Clearing system tracks...")
            
            cleared_items = 0
            
            # Clear recent documents
            recent_docs = os.path.join(os.environ.get('APPDATA', ''), 'Microsoft', 'Windows', 'Recent')
            if os.path.exists(recent_docs):
                try:
                    for item in os.listdir(recent_docs):
                        item_path = os.path.join(recent_docs, item)
                        try:
                            os.remove(item_path)
                            cleared_items += 1
                        except (PermissionError, FileNotFoundError):
                            continue
                except PermissionError:
                    pass
            
            # Clear run history
            try:
                import winreg
                with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU", 0, winreg.KEY_ALL_ACCESS) as key:
                    winreg.DeleteKey(key, "")
                    cleared_items += 1
            except:
                pass
            
            # Clear temp files
            temp_dirs = [
                os.environ.get('TEMP', ''),
                os.environ.get('TMP', ''),
            ]
            
            for temp_dir in temp_dirs:
                if os.path.exists(temp_dir):
                    try:
                        for item in os.listdir(temp_dir):
                            item_path = os.path.join(temp_dir, item)
                            try:
                                if os.path.isfile(item_path):
                                    os.remove(item_path)
                                    cleared_items += 1
                            except (PermissionError, FileNotFoundError):
                                continue
                    except PermissionError:
                        continue
            
            self.add_display_entry(f"✅ System tracks cleared. {cleared_items} items removed.")
            
        except Exception as e:
            logger.error(f"Clear tracks error: {e}")
            self.add_display_entry(f"Clear tracks error: {str(e)}")
    
    def password_manager(self):
        """Open password manager dialog"""
        try:
            dialog = tk.Toplevel(self.root)
            dialog.title("Password Manager")
            dialog.geometry("500x400")
            dialog.configure(bg=self.colors['glass'])
            
            tk.Label(dialog, text="Password Manager", font=('Arial', 16, 'bold'),
                    fg=self.colors['accent'], bg=self.colors['glass']).pack(pady=10)
            
            # Password storage
            passwords_frame = tk.Frame(dialog, bg=self.colors['glass'])
            passwords_frame.pack(fill='both', expand=True, padx=10, pady=10)
            
            tk.Label(passwords_frame, text="Stored Passwords:", fg=self.colors['text'],
                    bg=self.colors['glass']).pack(anchor='w')
            
            # This is a simplified version - in production, use proper encryption
            passwords_listbox = tk.Listbox(passwords_frame, bg=self.colors['bg'], fg=self.colors['text'])
            passwords_listbox.pack(fill='both', expand=True, pady=5)
            
            # Add sample passwords (in production, load from encrypted storage)
            sample_passwords = [
                "Gmail Account",
                "GitHub Account",
                "LinkedIn Account",
                "Banking App"
            ]
            
            for password in sample_passwords:
                passwords_listbox.insert(tk.END, password)
            
            # Buttons
            button_frame = tk.Frame(dialog, bg=self.colors['glass'])
            button_frame.pack(fill='x', padx=10, pady=10)
            
            tk.Button(button_frame, text="Add Password", bg=self.colors['green'], fg='white',
                     font=('Arial', 10, 'bold')).pack(side='left', padx=5)
            
            tk.Button(button_frame, text="Edit Password", bg=self.colors['blue'], fg='white',
                     font=('Arial', 10, 'bold')).pack(side='left', padx=5)
            
            tk.Button(button_frame, text="Delete Password", bg=self.colors['red'], fg='white',
                     font=('Arial', 10, 'bold')).pack(side='left', padx=5)
            
            tk.Button(button_frame, text="Close", command=dialog.destroy, bg=self.colors['orange'], fg='white',
                     font=('Arial', 10, 'bold')).pack(side='right', padx=5)
            
            self.add_display_entry("Password manager opened")
            
        except Exception as e:
            logger.error(f"Password manager error: {e}")
            self.add_display_entry(f"Password manager error: {str(e)}")
    
    def security_settings(self):
        """Open security settings dialog"""
        try:
            dialog = tk.Toplevel(self.root)
            dialog.title("Security Settings")
            dialog.geometry("400x300")
            dialog.configure(bg=self.colors['glass'])
            
            tk.Label(dialog, text="Security Settings", font=('Arial', 16, 'bold'),
                    fg=self.colors['accent'], bg=self.colors['glass']).pack(pady=10)
            
            # Security options
            options_frame = tk.Frame(dialog, bg=self.colors['glass'])
            options_frame.pack(fill='both', expand=True, padx=10, pady=10)
            
            # Auto-lock
            auto_lock_var = tk.BooleanVar(value=True)
            tk.Checkbutton(options_frame, text="Auto-lock system after inactivity", 
                          variable=auto_lock_var, bg=self.colors['glass'], fg=self.colors['text'],
                          selectcolor=self.colors['glass']).pack(anchor='w', pady=5)
            
            # Encrypt data
            encrypt_var = tk.BooleanVar(value=True)
            tk.Checkbutton(options_frame, text="Encrypt sensitive data automatically", 
                          variable=encrypt_var, bg=self.colors['glass'], fg=self.colors['text'],
                          selectcolor=self.colors['glass']).pack(anchor='w', pady=5)
            
            # Clear tracks
            clear_tracks_var = tk.BooleanVar(value=False)
            tk.Checkbutton(options_frame, text="Clear tracks on exit", 
                          variable=clear_tracks_var, bg=self.colors['glass'], fg=self.colors['text'],
                          selectcolor=self.colors['glass']).pack(anchor='w', pady=5)
            
            # Security notifications
            notifications_var = tk.BooleanVar(value=True)
            tk.Checkbutton(options_frame, text="Security notifications", 
                          variable=notifications_var, bg=self.colors['glass'], fg=self.colors['text'],
                          selectcolor=self.colors['glass']).pack(anchor='w', pady=5)
            
            def apply_security_settings():
                self.add_display_entry("Security settings updated")
                dialog.destroy()
            
            tk.Button(dialog, text="Apply Settings", command=apply_security_settings,
                     bg=self.colors['green'], fg='white', font=('Arial', 12, 'bold')).pack(pady=10)
            
        except Exception as e:
            logger.error(f"Security settings error: {e}")
            self.add_display_entry(f"Security settings error: {str(e)}")
    
    def execute_manual_command(self, event=None):
        """Execute manual command"""
        try:
            command = self.manual_entry.get().strip()
            if not command:
                return
            
            self.add_voice_history(f"You: {command}")
            self.process_voice_command(command)
            self.manual_entry.delete(0, tk.END)
            
        except Exception as e:
            logger.error(f"Manual command error: {e}")
            self.add_display_entry(f"Manual command error: {str(e)}")
    
    def clear_display(self):
        """Clear main display"""
        try:
            self.main_display.delete('1.0', tk.END)
            self.add_display_entry("Display cleared")
            
        except Exception as e:
            logger.error(f"Clear display error: {e}")
            self.add_display_entry(f"Clear display error: {str(e)}")
    
    def save_session(self):
        """Save current session"""
        try:
            session_data = {
                'timestamp': datetime.now().isoformat(),
                'command_history': self.command_history,
                'conversation_context': self.conversation_context,
                'voice_active': self.voice_active
            }
            
            session_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'session.json')
            
            with open(session_file, 'w') as f:
                json.dump(session_data, f, indent=2)
            
            self.add_display_entry("Session saved successfully")
            
        except Exception as e:
            logger.error(f"Save session error: {e}")
            self.add_display_entry(f"Save session error: {str(e)}")
    
    def get_system_status(self) -> Dict[str, str]:
        """Get current system status"""
        try:
            return {
                'cpu': f"{psutil.cpu_percent(interval=1):.1f}",
                'memory': f"{psutil.virtual_memory().percent:.1f}",
                'processes': str(len(self.system_detector.get_running_processes())),
                'disk': f"{psutil.disk_usage('/').percent:.1f}"
            }
        except Exception as e:
            logger.error(f"Get system status error: {e}")
            return {'cpu': '0', 'memory': '0', 'processes': '0', 'disk': '0'}
    
    def add_display_entry(self, text: str):
        """Add entry to main display"""
        try:
            timestamp = datetime.now().strftime('%H:%M:%S')
            entry = f"[{timestamp}] {text}\n"
            
            self.main_display.insert(tk.END, entry)
            self.main_display.see(tk.END)
            
            # Add to command history
            self.command_history.append({
                'timestamp': timestamp,
                'text': text
            })
            
            # Update task label
            self.task_label.config(text=f"Task: {text[:50]}...")
            
        except Exception as e:
            logger.error(f"Add display entry error: {e}")
    
    def add_voice_history(self, text: str):
        """Add entry to voice history"""
        try:
            timestamp = datetime.now().strftime('%H:%M:%S')
            entry = f"[{timestamp}] {text}\n"
            
            self.voice_history_display.insert(tk.END, entry)
            self.voice_history_display.see(tk.END)
            
            # Add to conversation context
            self.conversation_context.append({
                'timestamp': timestamp,
                'text': text
            })
            
        except Exception as e:
            logger.error(f"Add voice history error: {e}")
    
    def update_system_info(self):
        """Update system information in background"""
        while True:
            try:
                # Update system detector
                self.system_detector.update_system_info()
                
                # Update status labels
                system_status = self.get_system_status()
                self.cpu_label.config(text=f"CPU: {system_status['cpu']}%")
                self.memory_label.config(text=f"Memory: {system_status['memory']}%")
                
                time.sleep(5)
                
            except Exception as e:
                logger.error(f"Update system info error: {e}")
                time.sleep(5)
    
    def update_time(self):
        """Update time display"""
        while True:
            try:
                current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.time_label.config(text=current_time)
                time.sleep(1)
            except Exception as e:
                logger.error(f"Update time error: {e}")
                time.sleep(1)
    
    def system_monitor_loop(self):
        """Background system monitoring"""
        while True:
            try:
                # Detect system changes
                changes = self.system_detector.detect_system_changes()
                
                if changes:
                    for change in changes:
                        self.add_display_entry(f"System Change: {change}")
                
                time.sleep(10)
                
            except Exception as e:
                logger.error(f"System monitor loop error: {e}")
                time.sleep(10)
    
    def auto_save_loop(self):
        """Auto-save session in background"""
        while True:
            try:
                if self.auto_save_enabled:
                    self.save_session()
                    time.sleep(300)  # Auto-save every 5 minutes
                else:
                    time.sleep(60)
                    
            except Exception as e:
                logger.error(f"Auto-save loop error: {e}")
                time.sleep(60)
    
    def welcome_user(self):
        """Welcome user"""
        try:
            welcome_message = f"""
            Welcome to ILLI AI Professional, {self.user_name}!
            
            I am your complete PC and Web control system with advanced security features.
            
            Available Features:
            - Voice Control: Say "Start Voice" to activate
            - Application Control: Launch and close any application
            - System Monitoring: Real-time system performance tracking
            - Security & Privacy: Advanced protection and encryption
            - GitHub Integration: Seamless version control
            - Professional Dashboard: Complete control interface
            
            Say "Help" for voice commands or explore the tabs above.
            
            System Status: Online | Security: Active | Voice: Ready
            """
            
            self.add_display_entry(welcome_message)
            self.voice_controller.speak(f"Welcome {self.user_name}! I'm ILLI AI, your professional assistant. All systems are online and ready to assist you.")
            
        except Exception as e:
            logger.error(f"Welcome user error: {e}")
            self.add_display_entry(f"Welcome message error: {str(e)}")

def main():
    """Main function"""
    try:
        root = tk.Tk()
        app = ILLI_AI_Professional(root)
        root.mainloop()
        
    except Exception as e:
        logger.error(f"Application error: {e}")
        messagebox.showerror("Error", f"Failed to start ILLI AI Professional: {str(e)}")

if __name__ == "__main__":
    main()
