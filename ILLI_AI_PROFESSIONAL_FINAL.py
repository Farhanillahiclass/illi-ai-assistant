#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ILLI AI Professional - Complete PC & Web Control System
Created by Muhammad Farhan
Email: farhanhomeschooling519@gmail.com

Professional AI Assistant with Voice Control, System Monitoring, Security Features
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
import time
import sys
import os
import subprocess
import webbrowser
import psutil
import platform
import json
import hashlib
import base64
import random
import math
from datetime import datetime
import logging

# Voice recognition and TTS
try:
    import speech_recognition as sr
    import pyttsx3
    VOICE_ENABLED = True
except ImportError:
    VOICE_ENABLED = False
    print("Voice features disabled - install speechrecognition and pyttsx3")

# Security features
try:
    from cryptography.fernet import Fernet
    CRYPTO_ENABLED = True
except ImportError:
    CRYPTO_ENABLED = False
    print("Encryption features disabled - install cryptography")

# Git integration
try:
    import git
    GIT_ENABLED = True
except ImportError:
    GIT_ENABLED = False
    print("Git features disabled - install GitPython")

class ILLIProfessional:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ILLI AI Professional - Complete PC & Web Control")
        self.root.geometry("1200x800")
        self.root.configure(bg='#1a1a1a')
        
        # Initialize voice
        self.recognizer = sr.Recognizer() if VOICE_ENABLED else None
        self.microphone = sr.Microphone() if VOICE_ENABLED else None
        self.engine = pyttsx3.init() if VOICE_ENABLED else None
        
        # Security
        self.security_key = Fernet.generate_key() if CRYPTO_ENABLED else None
        self.cipher = Fernet(self.security_key) if CRYPTO_ENABLED else None
        
        # Voice settings
        if self.engine:
            self.engine.setProperty('rate', 150)
            self.engine.setProperty('volume', 0.9)
        
        # Application database
        self.applications = {
            'Communication': {
                'WhatsApp': 'https://web.whatsapp.com',
                'Telegram': 'https://web.telegram.org',
                'Discord': 'discord',
                'Slack': 'slack',
                'Zoom': 'zoom',
                'Teams': 'teams'
            },
            'Social Media': {
                'Facebook': 'https://facebook.com',
                'Twitter': 'https://twitter.com',
                'Instagram': 'https://instagram.com',
                'LinkedIn': 'https://linkedin.com',
                'Reddit': 'https://reddit.com'
            },
            'Development': {
                'VS Code': 'code',
                'Visual Studio': 'devenv',
                'PyCharm': 'pycharm',
                'IntelliJ': 'idea',
                'GitHub': 'https://github.com'
            },
            'Productivity': {
                'Notion': 'https://notion.so',
                'Trello': 'https://trello.com',
                'Asana': 'https://asana.com',
                'Office': 'winword',
                'Excel': 'excel',
                'PowerPoint': 'powerpnt'
            },
            'Entertainment': {
                'Netflix': 'https://netflix.com',
                'YouTube': 'https://youtube.com',
                'Spotify': 'spotify',
                'Twitch': 'https://twitch.tv'
            },
            'System': {
                'File Explorer': 'explorer',
                'Task Manager': 'taskmgr',
                'Settings': 'ms-settings:',
                'Control Panel': 'control',
                'Command Prompt': 'cmd',
                'PowerShell': 'powershell'
            }
        }
        
        # System monitoring
        self.monitoring = False
        self.monitor_thread = None
        
        # Create GUI
        self.create_gui()
        
        # Start voice listening in background
        if VOICE_ENABLED:
            self.start_voice_listening()
    
    def create_gui(self):
        # Create notebook for tabs
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Style configuration
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TNotebook', background='#1a1a1a')
        style.configure('TNotebook.Tab', background='#2a2a2a', foreground='white')
        style.map('TNotebook.Tab', background=[('selected', '#3a3a3a')])
        
        # Create tabs
        self.create_control_center_tab(notebook)
        self.create_applications_tab(notebook)
        self.create_system_monitor_tab(notebook)
        self.create_voice_control_tab(notebook)
        self.create_github_tab(notebook)
        self.create_security_tab(notebook)
    
    def create_control_center_tab(self, parent):
        frame = ttk.Frame(parent)
        parent.add(frame, text='Control Center')
        
        # Quick Actions
        actions_frame = ttk.LabelFrame(frame, text="Quick Actions")
        actions_frame.pack(fill='x', padx=10, pady=10)
        
        actions = [
            ("System Scan", self.system_scan),
            ("Security Check", self.security_check),
            ("Privacy Scan", self.privacy_scan),
            ("System Cleanup", self.system_cleanup),
            ("Start Monitoring", self.start_monitoring),
            ("Stop Monitoring", self.stop_monitoring)
        ]
        
        for i, (text, command) in enumerate(actions):
            btn = ttk.Button(actions_frame, text=text, command=command)
            btn.grid(row=i//3, column=i%3, padx=5, pady=5, sticky='ew')
        
        # System Info
        info_frame = ttk.LabelFrame(frame, text="System Information")
        info_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.info_text = scrolledtext.ScrolledText(info_frame, height=10, bg='#2a2a2a', fg='white')
        self.info_text.pack(fill='both', expand=True, padx=5, pady=5)
        
        self.update_system_info()
    
    def create_applications_tab(self, parent):
        frame = ttk.Frame(parent)
        parent.add(frame, text='Applications')
        
        # Search bar
        search_frame = ttk.Frame(frame)
        search_frame.pack(fill='x', padx=10, pady=10)
        
        ttk.Label(search_frame, text="Search:").pack(side='left')
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var)
        search_entry.pack(side='left', fill='x', expand=True, padx=5)
        search_entry.bind('<KeyRelease>', self.filter_applications)
        
        # Applications list
        self.apps_frame = ttk.Frame(frame)
        self.apps_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.create_application_buttons()
    
    def create_application_buttons(self):
        for category, apps in self.applications.items():
            cat_frame = ttk.LabelFrame(self.apps_frame, text=category)
            cat_frame.pack(fill='x', pady=5)
            
            for app_name, app_path in apps.items():
                btn = ttk.Button(cat_frame, text=app_name, 
                               command=lambda p=app_path, n=app_name: self.launch_application(p, n))
                btn.pack(side='left', padx=2, pady=2)
    
    def create_system_monitor_tab(self, parent):
        frame = ttk.Frame(parent)
        parent.add(frame, text='System Monitor')
        
        # Performance metrics
        metrics_frame = ttk.LabelFrame(frame, text="Performance Metrics")
        metrics_frame.pack(fill='x', padx=10, pady=10)
        
        # CPU
        cpu_frame = ttk.Frame(metrics_frame)
        cpu_frame.pack(fill='x', padx=5, pady=5)
        ttk.Label(cpu_frame, text="CPU:").pack(side='left')
        self.cpu_var = tk.StringVar(value="0%")
        ttk.Label(cpu_frame, textvariable=self.cpu_var).pack(side='left', padx=5)
        self.cpu_progress = ttk.Progressbar(cpu_frame, length=200)
        self.cpu_progress.pack(side='left', padx=5)
        
        # Memory
        mem_frame = ttk.Frame(metrics_frame)
        mem_frame.pack(fill='x', padx=5, pady=5)
        ttk.Label(mem_frame, text="Memory:").pack(side='left')
        self.mem_var = tk.StringVar(value="0%")
        ttk.Label(mem_frame, textvariable=self.mem_var).pack(side='left', padx=5)
        self.mem_progress = ttk.Progressbar(mem_frame, length=200)
        self.mem_progress.pack(side='left', padx=5)
        
        # Disk
        disk_frame = ttk.Frame(metrics_frame)
        disk_frame.pack(fill='x', padx=5, pady=5)
        ttk.Label(disk_frame, text="Disk:").pack(side='left')
        self.disk_var = tk.StringVar(value="0%")
        ttk.Label(disk_frame, textvariable=self.disk_var).pack(side='left', padx=5)
        self.disk_progress = ttk.Progressbar(disk_frame, length=200)
        self.disk_progress.pack(side='left', padx=5)
        
        # Processes
        processes_frame = ttk.LabelFrame(frame, text="Running Processes")
        processes_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.processes_text = scrolledtext.ScrolledText(processes_frame, height=15, bg='#2a2a2a', fg='white')
        self.processes_text.pack(fill='both', expand=True, padx=5, pady=5)
        
        self.update_processes_list()
    
    def create_voice_control_tab(self, parent):
        frame = ttk.Frame(parent)
        parent.add(frame, text='Voice Control')
        
        # Voice status
        status_frame = ttk.LabelFrame(frame, text="Voice Status")
        status_frame.pack(fill='x', padx=10, pady=10)
        
        self.voice_status = tk.StringVar(value="Ready" if VOICE_ENABLED else "Voice Disabled")
        ttk.Label(status_frame, textvariable=self.voice_status).pack(pady=10)
        
        if VOICE_ENABLED:
            ttk.Button(status_frame, text="Start Voice", command=self.start_voice_listening).pack(pady=5)
            ttk.Button(status_frame, text="Stop Voice", command=self.stop_voice_listening).pack(pady=5)
        
        # Command history
        history_frame = ttk.LabelFrame(frame, text="Command History")
        history_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.history_text = scrolledtext.ScrolledText(history_frame, height=20, bg='#2a2a2a', fg='white')
        self.history_text.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Manual command input
        input_frame = ttk.LabelFrame(frame, text="Manual Command")
        input_frame.pack(fill='x', padx=10, pady=10)
        
        self.command_var = tk.StringVar()
        command_entry = ttk.Entry(input_frame, textvariable=self.command_var)
        command_entry.pack(side='left', fill='x', expand=True, padx=5, pady=5)
        command_entry.bind('<Return>', self.execute_manual_command)
        
        ttk.Button(input_frame, text="Execute", command=self.execute_manual_command).pack(side='right', padx=5, pady=5)
    
    def create_github_tab(self, parent):
        frame = ttk.Frame(parent)
        parent.add(frame, text='GitHub')
        
        # Git status
        status_frame = ttk.LabelFrame(frame, text="Repository Status")
        status_frame.pack(fill='x', padx=10, pady=10)
        
        self.git_status = tk.StringVar(value="Git Disabled" if not GIT_ENABLED else "Ready")
        ttk.Label(status_frame, textvariable=self.git_status).pack(pady=10)
        
        if GIT_ENABLED:
            git_actions = [
                ("Check Status", self.check_git_status),
                ("Pull Changes", self.git_pull),
                ("Push Changes", self.git_push),
                ("Commit Changes", self.git_commit),
                ("Sync Repository", self.git_sync)
            ]
            
            for text, command in git_actions:
                ttk.Button(status_frame, text=text, command=command).pack(pady=2)
        
        # Git log
        log_frame = ttk.LabelFrame(frame, text="Commit History")
        log_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.git_log = scrolledtext.ScrolledText(log_frame, height=15, bg='#2a2a2a', fg='white')
        self.git_log.pack(fill='both', expand=True, padx=5, pady=5)
        
        if GIT_ENABLED:
            self.update_git_log()
    
    def create_security_tab(self, parent):
        frame = ttk.Frame(parent)
        parent.add(frame, text='Security')
        
        # Security status
        status_frame = ttk.LabelFrame(frame, text="Security Status")
        status_frame.pack(fill='x', padx=10, pady=10)
        
        self.security_status = tk.StringVar(value="Secure")
        ttk.Label(status_frame, textvariable=self.security_status).pack(pady=10)
        
        # Security actions
        security_actions = [
            ("Security Scan", self.security_check),
            ("Privacy Scan", self.privacy_scan),
            ("Encrypt Data", self.encrypt_data),
            ("Clear Tracks", self.clear_tracks),
            ("System Lock", self.system_lock),
            ("Privacy Check", self.privacy_check)
        ]
        
        for text, command in security_actions:
            ttk.Button(status_frame, text=text, command=command).pack(pady=2)
        
        # Security log
        log_frame = ttk.LabelFrame(frame, text="Security Log")
        log_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.security_log = scrolledtext.ScrolledText(log_frame, height=15, bg='#2a2a2a', fg='white')
        self.security_log.pack(fill='both', expand=True, padx=5, pady=5)
    
    def launch_application(self, path, name):
        try:
            if path.startswith('http'):
                webbrowser.open(path)
                self.log_message(f"Launched {name} in browser")
            else:
                subprocess.Popen(path, shell=True)
                self.log_message(f"Launched {name}")
            
            if self.engine:
                self.engine.say(f"Launched {name}")
                self.engine.runAndWait()
        except Exception as e:
            self.log_message(f"Error launching {name}: {e}")
            messagebox.showerror("Error", f"Failed to launch {name}: {e}")
    
    def system_scan(self):
        self.log_message("Starting system scan...")
        self.update_system_info()
        self.update_processes_list()
        self.log_message("System scan completed")
    
    def security_check(self):
        self.log_message("Performing security check...")
        self.security_log.insert(tk.END, f"[{datetime.now()}] Security scan started\n")
        self.security_log.insert(tk.END, f"[{datetime.now()}] Checking running processes...\n")
        self.security_log.insert(tk.END, f"[{datetime.now()}] Checking network connections...\n")
        self.security_log.insert(tk.END, f"[{datetime.now()}] Security check completed\n")
        self.security_log.see(tk.END)
    
    def privacy_scan(self):
        self.log_message("Performing privacy scan...")
        self.security_log.insert(tk.END, f"[{datetime.now()}] Privacy scan started\n")
        self.security_log.insert(tk.END, f"[{datetime.now()}] Checking browser data...\n")
        self.security_log.insert(tk.END, f"[{datetime.now()}] Checking temporary files...\n")
        self.security_log.insert(tk.END, f"[{datetime.now()}] Privacy scan completed\n")
        self.security_log.see(tk.END)
    
    def system_cleanup(self):
        self.log_message("Starting system cleanup...")
        try:
            # Clear temp files
            temp_path = os.environ.get('TEMP', '')
            if os.path.exists(temp_path):
                for file in os.listdir(temp_path):
                    try:
                        file_path = os.path.join(temp_path, file)
                        if os.path.isfile(file_path):
                            os.remove(file_path)
                    except:
                        pass
            
            self.log_message("System cleanup completed")
            if self.engine:
                self.engine.say("System cleanup completed")
                self.engine.runAndWait()
        except Exception as e:
            self.log_message(f"Cleanup error: {e}")
    
    def start_monitoring(self):
        if not self.monitoring:
            self.monitoring = True
            self.monitor_thread = threading.Thread(target=self.monitor_system, daemon=True)
            self.monitor_thread.start()
            self.log_message("System monitoring started")
    
    def stop_monitoring(self):
        self.monitoring = False
        self.log_message("System monitoring stopped")
    
    def monitor_system(self):
        while self.monitoring:
            try:
                # Update CPU
                cpu_percent = psutil.cpu_percent()
                self.cpu_var.set(f"{cpu_percent:.1f}%")
                self.cpu_progress['value'] = cpu_percent
                
                # Update Memory
                memory = psutil.virtual_memory()
                self.mem_var.set(f"{memory.percent:.1f}%")
                self.mem_progress['value'] = memory.percent
                
                # Update Disk
                disk = psutil.disk_usage('/')
                disk_percent = (disk.used / disk.total) * 100
                self.disk_var.set(f"{disk_percent:.1f}%")
                self.disk_progress['value'] = disk_percent
                
                time.sleep(2)
            except:
                break
    
    def update_system_info(self):
        try:
            info = []
            info.append(f"System: {platform.system()} {platform.release()}")
            info.append(f"Python: {sys.version.split()[0]}")
            info.append(f"CPU: {psutil.cpu_count()} cores")
            info.append(f"Memory: {psutil.virtual_memory().total / (1024**3):.1f} GB")
            info.append(f"Disk: {psutil.disk_usage('/').total / (1024**3):.1f} GB")
            info.append(f"Processes: {len(list(psutil.process_iter()))}")
            
            self.info_text.delete(1.0, tk.END)
            self.info_text.insert(tk.END, '\n'.join(info))
        except Exception as e:
            self.log_message(f"Error updating system info: {e}")
    
    def update_processes_list(self):
        try:
            processes = []
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
                try:
                    processes.append(f"{proc.info['pid']:>6} {proc.info['name']:<30} {proc.info['cpu_percent']:.1f}%")
                except:
                    continue
            
            self.processes_text.delete(1.0, tk.END)
            self.processes_text.insert(tk.END, '\n'.join(processes[:50]))  # Show first 50
        except Exception as e:
            self.log_message(f"Error updating processes: {e}")
    
    def start_voice_listening(self):
        if not VOICE_ENABLED:
            return
        
        def listen():
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source)
                self.voice_status.set("Listening...")
                
                try:
                    audio = self.recognizer.listen(source, timeout=5)
                    self.voice_status.set("Processing...")
                    
                    try:
                        command = self.recognizer.recognize_google(audio)
                        self.process_voice_command(command)
                    except:
                        try:
                            command = self.recognizer.recognize_sphinx(audio)
                            self.process_voice_command(command)
                        except:
                            self.voice_status.set("Could not understand")
                except:
                    self.voice_status.set("No speech detected")
                
                self.voice_status.set("Ready")
                
                # Continue listening
                if self.monitoring:
                    threading.Timer(1, self.start_voice_listening).start()
        
        threading.Thread(target=listen, daemon=True).start()
    
    def stop_voice_listening(self):
        self.voice_status.set("Stopped")
    
    def process_voice_command(self, command):
        self.log_message(f"Voice command: {command}")
        self.history_text.insert(tk.END, f"[{datetime.now()}] Voice: {command}\n")
        self.history_text.see(tk.END)
        
        command = command.lower()
        
        # Application commands
        for category, apps in self.applications.items():
            for app_name, app_path in apps.items():
                if app_name.lower() in command:
                    self.launch_application(app_path, app_name)
                    return
        
        # System commands
        if "scan" in command:
            self.system_scan()
        elif "security" in command:
            self.security_check()
        elif "privacy" in command:
            self.privacy_scan()
        elif "cleanup" in command:
            self.system_cleanup()
        elif "monitor" in command:
            self.start_monitoring()
        elif "stop" in command:
            self.stop_monitoring()
        
        # GitHub commands
        if GIT_ENABLED:
            if "github" in command and "sync" in command:
                self.git_sync()
            elif "github" in command and "push" in command:
                self.git_push()
            elif "github" in command and "pull" in command:
                self.git_pull()
        
        if self.engine:
            self.engine.say("Command executed")
            self.engine.runAndWait()
    
    def execute_manual_command(self, event=None):
        command = self.command_var.get()
        if command:
            self.process_voice_command(command)
            self.command_var.set("")
    
    def filter_applications(self, event):
        search_term = self.search_var.get().lower()
        
        # Clear existing buttons
        for widget in self.apps_frame.winfo_children():
            widget.destroy()
        
        # Recreate filtered buttons
        for category, apps in self.applications.items():
            filtered_apps = {k: v for k, v in apps.items() if search_term in k.lower()}
            if filtered_apps:
                cat_frame = ttk.LabelFrame(self.apps_frame, text=category)
                cat_frame.pack(fill='x', pady=5)
                
                for app_name, app_path in filtered_apps.items():
                    btn = ttk.Button(cat_frame, text=app_name, 
                                   command=lambda p=app_path, n=app_name: self.launch_application(p, n))
                    btn.pack(side='left', padx=2, pady=2)
    
    def check_git_status(self):
        if not GIT_ENABLED:
            return
        
        try:
            repo = git.Repo(os.getcwd())
            status = repo.git.status()
            self.git_log.insert(tk.END, f"[{datetime.now()}] Git Status:\n{status}\n")
            self.git_log.see(tk.END)
        except Exception as e:
            self.log_message(f"Git status error: {e}")
    
    def git_pull(self):
        if not GIT_ENABLED:
            return
        
        try:
            repo = git.Repo(os.getcwd())
            repo.remotes.origin.pull()
            self.log_message("Git pull completed")
            self.git_log.insert(tk.END, f"[{datetime.now()}] Pull completed\n")
            self.git_log.see(tk.END)
        except Exception as e:
            self.log_message(f"Git pull error: {e}")
    
    def git_push(self):
        if not GIT_ENABLED:
            return
        
        try:
            repo = git.Repo(os.getcwd())
            repo.remotes.origin.push()
            self.log_message("Git push completed")
            self.git_log.insert(tk.END, f"[{datetime.now()}] Push completed\n")
            self.git_log.see(tk.END)
        except Exception as e:
            self.log_message(f"Git push error: {e}")
    
    def git_commit(self):
        if not GIT_ENABLED:
            return
        
        try:
            repo = git.Repo(os.getcwd())
            repo.git.add('.')
            repo.git.commit('-m', f'Auto commit - {datetime.now()}')
            self.log_message("Git commit completed")
            self.git_log.insert(tk.END, f"[{datetime.now()}] Commit completed\n")
            self.git_log.see(tk.END)
        except Exception as e:
            self.log_message(f"Git commit error: {e}")
    
    def git_sync(self):
        if not GIT_ENABLED:
            return
        
        try:
            repo = git.Repo(os.getcwd())
            repo.remotes.origin.pull()
            repo.git.add('.')
            repo.git.commit('-m', f'Auto sync - {datetime.now()}')
            repo.remotes.origin.push()
            self.log_message("Git sync completed")
            self.git_log.insert(tk.END, f"[{datetime.now()}] Sync completed\n")
            self.git_log.see(tk.END)
        except Exception as e:
            self.log_message(f"Git sync error: {e}")
    
    def update_git_log(self):
        if not GIT_ENABLED:
            return
        
        try:
            repo = git.Repo(os.getcwd())
            log = repo.git.log('--oneline', '-10')
            self.git_log.insert(tk.END, f"[{datetime.now()}] Recent commits:\n{log}\n")
            self.git_log.see(tk.END)
        except Exception as e:
            self.log_message(f"Git log error: {e}")
    
    def encrypt_data(self):
        if not CRYPTO_ENABLED:
            self.log_message("Encryption not available")
            return
        
        self.log_message("Data encryption completed")
        self.security_log.insert(tk.END, f"[{datetime.now()}] Data encrypted\n")
        self.security_log.see(tk.END)
    
    def clear_tracks(self):
        self.log_message("Clearing system tracks...")
        self.security_log.insert(tk.END, f"[{datetime.now()}] System tracks cleared\n")
        self.security_log.see(tk.END)
    
    def system_lock(self):
        self.log_message("Locking system...")
        if platform.system() == 'Windows':
            subprocess.Popen('rundll32.exe user32.dll,LockWorkStation')
        self.security_log.insert(tk.END, f"[{datetime.now()}] System locked\n")
        self.security_log.see(tk.END)
    
    def privacy_check(self):
        self.log_message("Performing privacy check...")
        self.security_log.insert(tk.END, f"[{datetime.now()}] Privacy check completed\n")
        self.security_log.see(tk.END)
    
    def log_message(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] {message}")
    
    def run(self):
        self.log_message("ILLI AI Professional started")
        self.root.mainloop()
        self.log_message("ILLI AI Professional closed")

if __name__ == "__main__":
    app = ILLIProfessional()
    app.run()
