import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, scrolledtext
import os
import sys
import time
import threading
import queue
import math
import psutil
import json
from datetime import datetime
import pyautogui
import subprocess
import platform

# Try to import vosk for offline speech recognition
try:
    import vosk
    import json
    VOSK_AVAILABLE = True
except ImportError:
    VOSK_AVAILABLE = False
    print("Vosk not available. Install with: pip install vosk")

# Text-to-speech
try:
    import pyttsx3
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False
    print("pyttsx3 not available. Install with: pip install pyttsx3")

# Speech recognition
try:
    import speech_recognition as sr
    SPEECH_AVAILABLE = True
except ImportError:
    SPEECH_AVAILABLE = False
    print("speech_recognition not available. Install with: pip install SpeechRecognition")

class ILLIHUDDashboardFixed:
    def __init__(self):
        # Set up CustomTkinter
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        
        # Create main window
        self.root = ctk.CTk()
        self.root.title("ILLI AI - HUD Dashboard Fixed")
        self.root.geometry("1200x800")
        self.root.configure(fg_color="#1a1a1a")
        
        # Initialize TTS if available
        self.tts_engine = None
        if TTS_AVAILABLE:
            try:
                self.tts_engine = pyttsx3.init()
                self.tts_engine.setProperty('rate', 150)
                self.tts_engine.setProperty('volume', 0.9)
            except Exception as e:
                print(f"TTS initialization error: {e}")
        
        # Initialize speech recognition
        self.speech_queue = queue.Queue()
        self.listening = False
        
        # Initialize online speech recognition as fallback
        self.speech_recognizer = None
        self.microphone = None
        if SPEECH_AVAILABLE:
            try:
                self.speech_recognizer = sr.Recognizer()
                self.microphone = sr.Microphone()
            except Exception as e:
                print(f"Speech recognition initialization error: {e}")
        
        # System monitoring
        self.cpu_usage = 0
        self.ram_usage = 0
        self.monitoring_active = True
        
        # Chat history
        self.chat_history = []
        
        # Secret project path (customize this)
        self.secret_project_path = "C:\\Users\\{user}\\Documents\\SecretProject".format(user=os.getlogin())
        
        # App paths for launching
        self.app_paths = {
            'whatsapp': 'https://web.whatsapp.com',
            'instagram': 'https://instagram.com',
            'linkedin': 'https://linkedin.com',
            'github': 'https://github.com',
            'gmail': 'https://gmail.com',
            'chatgpt': 'https://chat.openai.com',
            'spotify': 'https://open.spotify.com',
            'discord': 'https://discord.com',
            'youtube': 'https://youtube.com',
            'facebook': 'https://facebook.com',
            'twitter': 'https://twitter.com',
            'reddit': 'https://reddit.com'
        }
        
        # Create main container
        self.setup_ui()
        
        # Start background threads
        self.start_system_monitoring()
        if SPEECH_AVAILABLE:
            self.start_speech_recognition()
        
        # Start the GUI
        self.root.mainloop()
    
    def setup_ui(self):
        """Set up the main UI with modular design"""
        
        # Main container frame
        self.main_frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color="#1a1a1a")
        self.main_frame.pack(fill="both", expand=True)
        
        # Top section - System monitoring
        self.create_system_monitoring()
        
        # Center section - Chat module
        self.create_chat_module()
        
        # Bottom section - Navigation bar
        self.create_navigation_bar()
    
    def create_system_monitoring(self):
        """Create circular progress bars for CPU and RAM monitoring"""
        
        # System monitoring frame
        monitoring_frame = ctk.CTkFrame(self.main_frame, corner_radius=15, 
                                       fg_color="#2a2a2a", border_width=2, 
                                       border_color="#00ffff")
        monitoring_frame.pack(pady=20, padx=20, fill="x")
        
        # Title
        title_label = ctk.CTkLabel(monitoring_frame, text="SYSTEM MONITORING", 
                                   font=ctk.CTkFont(size=18, weight="bold"),
                                   text_color="#00ffff")
        title_label.pack(pady=10)
        
        # Progress bars container
        progress_container = ctk.CTkFrame(monitoring_frame, fg_color="transparent")
        progress_container.pack(pady=10)
        
        # CPU Monitor
        cpu_frame = ctk.CTkFrame(progress_container, fg_color="transparent")
        cpu_frame.pack(side="left", padx=30)
        
        self.cpu_canvas = tk.Canvas(cpu_frame, width=150, height=150, 
                                 bg="#1a1a1a", highlightthickness=0)
        self.cpu_canvas.pack()
        
        cpu_label = ctk.CTkLabel(cpu_frame, text="CPU", 
                                 font=ctk.CTkFont(size=14, weight="bold"),
                                 text_color="#00ffff")
        cpu_label.pack(pady=5)
        
        self.cpu_percentage_label = ctk.CTkLabel(cpu_frame, text="0%", 
                                               font=ctk.CTkFont(size=12),
                                               text_color="#ffffff")
        self.cpu_percentage_label.pack()
        
        # RAM Monitor
        ram_frame = ctk.CTkFrame(progress_container, fg_color="transparent")
        ram_frame.pack(side="left", padx=30)
        
        self.ram_canvas = tk.Canvas(ram_frame, width=150, height=150, 
                                 bg="#1a1a1a", highlightthickness=0)
        self.ram_canvas.pack()
        
        ram_label = ctk.CTkLabel(ram_frame, text="RAM", 
                                 font=ctk.CTkFont(size=14, weight="bold"),
                                 text_color="#00ffff")
        ram_label.pack(pady=5)
        
        self.ram_percentage_label = ctk.CTkLabel(ram_frame, text="0%", 
                                               font=ctk.CTkFont(size=12),
                                               text_color="#ffffff")
        self.ram_percentage_label.pack()
        
        # Initialize circular progress bars
        self.draw_circular_progress(self.cpu_canvas, 0, "#00ffff")
        self.draw_circular_progress(self.ram_canvas, 0, "#ff00ff")
    
    def draw_circular_progress(self, canvas, percentage, color):
        """Draw a circular progress bar"""
        canvas.delete("all")
        
        # Canvas dimensions
        width = 150
        height = 150
        center_x = width // 2
        center_y = height // 2
        radius = 60
        
        # Draw background circle
        canvas.create_oval(center_x - radius, center_y - radius,
                         center_x + radius, center_y + radius,
                         outline="#333333", width=8, fill="")
        
        # Draw progress arc
        if percentage > 0:
            extent = (percentage / 100) * 360
            canvas.create_arc(center_x - radius, center_y - radius,
                           center_x + radius, center_y + radius,
                           start=90, extent=-extent, outline=color, 
                           width=8, style="arc", fill="")
        
        # Draw center text
        canvas.create_text(center_x, center_y, text=f"{percentage:.1f}%",
                        fill=color, font=("Arial", 16, "bold"))
    
    def create_chat_module(self):
        """Create central glassmorphic chat module"""
        
        # Chat frame with glassmorphic effect
        chat_frame = ctk.CTkFrame(self.main_frame, corner_radius=20,
                                  fg_color="#2a2a2a", border_width=2,
                                  border_color="#00ffff")
        chat_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Chat title
        chat_title = ctk.CTkLabel(chat_frame, text="ILLI AI ASSISTANT",
                                 font=ctk.CTkFont(size=20, weight="bold"),
                                 text_color="#00ffff")
        chat_title.pack(pady=10)
        
        # Chat display area with glassmorphic effect
        chat_container = ctk.CTkFrame(chat_frame, corner_radius=15,
                                    fg_color="#1a1a1a", border_width=1,
                                    border_color="#00ffff")
        chat_container.pack(pady=10, padx=15, fill="both", expand=True)
        
        # Chat text widget
        self.chat_display = ctk.CTkTextbox(chat_container, corner_radius=10,
                                        fg_color="#0a0a0a", text_color="#00ffff",
                                        font=ctk.CTkFont(size=12),
                                        wrap="word")
        self.chat_display.pack(pady=10, padx=10, fill="both", expand=True)
        
        # Input frame
        input_frame = ctk.CTkFrame(chat_frame, fg_color="transparent")
        input_frame.pack(pady=10, padx=15, fill="x")
        
        # Text input
        self.chat_input = ctk.CTkEntry(input_frame, corner_radius=10,
                                     fg_color="#2a2a2a", border_width=1,
                                     border_color="#00ffff", text_color="#ffffff",
                                     placeholder_text="Type your message or say 'Open Secret Project'...",
                                     font=ctk.CTkFont(size=12),
                                     height=40)
        self.chat_input.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.chat_input.bind("<Return>", self.process_text_input)
        
        # Send button
        send_button = ctk.CTkButton(input_frame, text="SEND", corner_radius=10,
                                   fg_color="#00ffff", text_color="#1a1a1a",
                                   font=ctk.CTkFont(size=12, weight="bold"),
                                   width=80, command=self.process_text_input)
        send_button.pack(side="right")
        
        # Voice button
        voice_button = ctk.CTkButton(input_frame, text="🎤", corner_radius=10,
                                   fg_color="#ff00ff", text_color="#ffffff",
                                   font=ctk.CTkFont(size=16),
                                   width=50, command=self.toggle_voice_recognition)
        voice_button.pack(side="right", padx=(0, 10))
        
        # Add welcome message
        self.add_chat_message("ILLI", "Hello! I'm ILLI, your AI assistant. How can I help you today?")
    
    def create_navigation_bar(self):
        """Create bottom navigation bar with icons"""
        
        # Navigation frame
        nav_frame = ctk.CTkFrame(self.main_frame, corner_radius=15,
                                fg_color="#2a2a2a", border_width=2,
                                border_color="#00ffff")
        nav_frame.pack(side="bottom", fill="x", padx=20, pady=20)
        
        # Navigation buttons container
        button_container = ctk.CTkFrame(nav_frame, fg_color="transparent")
        button_container.pack(pady=15)
        
        # Navigation buttons with icons
        buttons_data = [
            ("🔌", "Shutdown", self.shutdown_system),
            ("🌐", "Browser", self.open_browser),
            ("📁", "File Explorer", self.open_file_explorer),
            ("🔄", "Network Sync", self.network_sync),
            ("🔧", "Settings", self.open_settings),
            ("📊", "Performance", self.show_performance),
            ("🎯", "Secret Project", self.open_secret_project)
        ]
        
        for icon, text, command in buttons_data:
            button_frame = ctk.CTkFrame(button_container, fg_color="transparent")
            button_frame.pack(side="left", padx=10)
            
            button = ctk.CTkButton(button_frame, text=icon, corner_radius=10,
                                 fg_color="#00ffff", text_color="#1a1a1a",
                                 font=ctk.CTkFont(size=16),
                                 width=60, height=60, command=command)
            button.pack()
            
            label = ctk.CTkLabel(button_frame, text=text,
                                font=ctk.CTkFont(size=10),
                                text_color="#00ffff")
            label.pack(pady=(5, 0))
    
    def add_chat_message(self, sender, message):
        """Add message to chat display"""
        timestamp = datetime.now().strftime("%H:%M")
        formatted_message = f"[{timestamp}] [{sender}]: {message}\n"
        
        self.chat_display.insert("end", formatted_message)
        self.chat_display.see("end")
        
        # Store in history
        self.chat_history.append({"timestamp": timestamp, "sender": sender, "message": message})
    
    def process_text_input(self, event=None):
        """Process text input from chat"""
        user_input = self.chat_input.get().strip()
        if not user_input:
            return
        
        # Add user message to chat
        self.add_chat_message("USER", user_input)
        
        # Clear input
        self.chat_input.delete(0, "end")
        
        # Process command
        self.process_command(user_input)
    
    def process_command(self, command):
        """Process user commands"""
        command_lower = command.lower()
        
        if "open secret project" in command_lower:
            self.open_secret_project()
        elif "shutdown" in command_lower:
            self.shutdown_system()
        elif "browser" in command_lower:
            self.open_browser()
        elif "file explorer" in command_lower:
            self.open_file_explorer()
        elif "network sync" in command_lower:
            self.network_sync()
        elif "settings" in command_lower:
            self.open_settings()
        elif "performance" in command_lower:
            self.show_performance()
        elif "open" in command_lower:
            # Check for app opening commands
            for app_name, url in self.app_paths.items():
                if app_name in command_lower:
                    self.launch_app(app_name)
                    return
            self.add_chat_message("ILLI", f"I don't know how to open: {command}")
        elif "hello" in command_lower or "hi" in command_lower:
            self.add_chat_message("ILLI", "Hello! How can I assist you today?")
        elif "help" in command_lower:
            self.show_help()
        elif "time" in command_lower:
            self.tell_time()
        elif "clear" in command_lower:
            self.chat_display.delete("1.0", "end")
            self.chat_history.clear()
        else:
            self.add_chat_message("ILLI", f"I received your command: '{command}'. I'm still learning!")
    
    def launch_app(self, app_name):
        """Launch application"""
        try:
            url = self.app_paths.get(app_name)
            if url:
                import webbrowser
                webbrowser.open(url)
                self.add_chat_message("ILLI", f"Opened {app_name}")
                
                # Speak response if TTS is available
                if self.tts_engine:
                    self.speak(f"Opened {app_name}")
            else:
                self.add_chat_message("ILLI", f"App '{app_name}' not found")
        except Exception as e:
            self.add_chat_message("ILLI", f"Error opening {app_name}: {str(e)}")
    
    def open_secret_project(self):
        """Open secret project folder"""
        try:
            # Create the directory if it doesn't exist
            if not os.path.exists(self.secret_project_path):
                os.makedirs(self.secret_project_path)
            
            # Open the folder
            os.startfile(self.secret_project_path)
            
            self.add_chat_message("ILLI", f"Secret Project opened at: {self.secret_project_path}")
            
            # Speak response if TTS is available
            if self.tts_engine:
                self.speak("Secret Project opened")
                
        except Exception as e:
            self.add_chat_message("ILLI", f"Error opening Secret Project: {str(e)}")
    
    def shutdown_system(self):
        """Shutdown the system"""
        self.add_chat_message("ILLI", "Shutting down system in 5 seconds...")
        
        if self.tts_engine:
            self.speak("Shutting down system")
        
        # Shutdown after delay
        self.root.after(5000, self.root.quit)
        
        # Actual system shutdown (platform specific)
        try:
            if platform.system() == "Windows":
                os.system("shutdown /s /t 5")
            elif platform.system() == "Darwin":  # macOS
                os.system("sudo shutdown -h +5")
            else:  # Linux
                os.system("shutdown -h +5")
        except:
            pass
    
    def open_browser(self):
        """Open default web browser"""
        try:
            import webbrowser
            webbrowser.open("https://www.google.com")
            self.add_chat_message("ILLI", "Browser opened")
            
            if self.tts_engine:
                self.speak("Browser opened")
        except Exception as e:
            self.add_chat_message("ILLI", f"Error opening browser: {str(e)}")
    
    def open_file_explorer(self):
        """Open file explorer"""
        try:
            if platform.system() == "Windows":
                os.startfile("explorer")
            elif platform.system() == "Darwin":  # macOS
                os.system("open .")
            else:  # Linux
                os.system("xdg-open .")
            
            self.add_chat_message("ILLI", "File Explorer opened")
            
            if self.tts_engine:
                self.speak("File Explorer opened")
        except Exception as e:
            self.add_chat_message("ILLI", f"Error opening File Explorer: {str(e)}")
    
    def network_sync(self):
        """Simulate network synchronization"""
        self.add_chat_message("ILLI", "Starting network synchronization...")
        
        # Simulate sync process
        for i in range(1, 6):
            self.root.after(i * 1000, lambda i=i: self.add_chat_message("ILLI", f"Syncing... {i*20}%"))
        
        self.root.after(6000, lambda: self.add_chat_message("ILLI", "Network synchronization complete!"))
        
        if self.tts_engine:
            self.speak("Network synchronization complete")
    
    def open_settings(self):
        """Open settings dialog"""
        settings_window = ctk.CTkToplevel(self.root)
        settings_window.title("ILLI Settings")
        settings_window.geometry("400x300")
        settings_window.configure(fg_color="#1a1a1a")
        
        # Settings title
        title = ctk.CTkLabel(settings_window, text="ILLI Settings",
                           font=ctk.CTkFont(size=18, weight="bold"),
                           text_color="#00ffff")
        title.pack(pady=20)
        
        # Secret project path setting
        path_frame = ctk.CTkFrame(settings_window, fg_color="transparent")
        path_frame.pack(pady=20, padx=20, fill="x")
        
        path_label = ctk.CTkLabel(path_frame, text="Secret Project Path:",
                                font=ctk.CTkFont(size=12),
                                text_color="#ffffff")
        path_label.pack(anchor="w")
        
        path_entry = ctk.CTkEntry(path_frame, corner_radius=10,
                                 fg_color="#2a2a2a", border_width=1,
                                 border_color="#00ffff", text_color="#ffffff",
                                 font=ctk.CTkFont(size=12))
        path_entry.pack(fill="x", pady=5)
        path_entry.insert(0, self.secret_project_path)
        
        # Save button
        save_button = ctk.CTkButton(settings_window, text="Save Settings",
                                  corner_radius=10, fg_color="#00ffff",
                                  text_color="#1a1a1a",
                                  font=ctk.CTkFont(size=12, weight="bold"),
                                  command=lambda: self.save_settings(path_entry.get()))
        save_button.pack(pady=20)
    
    def save_settings(self, path):
        """Save settings to file"""
        try:
            settings = {"secret_project_path": path}
            with open("illi_settings.json", "w") as f:
                json.dump(settings, f)
            
            self.secret_project_path = path
            self.add_chat_message("ILLI", "Settings saved successfully!")
            
            if self.tts_engine:
                self.speak("Settings saved")
        except Exception as e:
            self.add_chat_message("ILLI", f"Error saving settings: {str(e)}")
    
    def show_performance(self):
        """Show detailed performance information"""
        self.add_chat_message("ILLI", f"CPU Usage: {self.cpu_usage:.1f}%")
        self.add_chat_message("ILLI", f"RAM Usage: {self.ram_usage:.1f}%")
        
        # Get additional system info
        try:
            disk_usage = psutil.disk_usage('/').percent
            self.add_chat_message("ILLI", f"Disk Usage: {disk_usage:.1f}%")
            
            # Get network info
            network = psutil.net_io_counters()
            self.add_chat_message("ILLI", f"Network Sent: {network.bytes_sent / (1024**2):.1f} MB")
            self.add_chat_message("ILLI", f"Network Received: {network.bytes_recv / (1024**2):.1f} MB")
        except:
            pass
    
    def show_help(self):
        """Show help information"""
        help_text = """
Available Commands:
• Open Secret Project - Opens your secret project folder
• Open [app] - Opens WhatsApp, Instagram, Gmail, etc.
• Shutdown - Shuts down the system
• Browser - Opens web browser
• File Explorer - Opens file manager
• Network Sync - Simulates network synchronization
• Settings - Opens settings dialog
• Performance - Shows system performance
• Time - Shows current time
• Clear - Clears chat history
• Help - Shows this help message
        """
        self.add_chat_message("ILLI", help_text)
    
    def tell_time(self):
        """Tell current time"""
        current_time = datetime.now().strftime("%I:%M %p")
        self.add_chat_message("ILLI", f"Current time: {current_time}")
        
        if self.tts_engine:
            self.speak(f"The current time is {current_time}")
    
    def speak(self, text):
        """Text-to-speech function"""
        try:
            if self.tts_engine:
                self.tts_engine.say(text)
                self.tts_engine.runAndWait()
        except Exception as e:
            print(f"TTS Error: {e}")
    
    def toggle_voice_recognition(self):
        """Toggle voice recognition on/off"""
        if not SPEECH_AVAILABLE:
            self.add_chat_message("ILLI", "Speech recognition not available. Install SpeechRecognition library.")
            return
        
        self.listening = not self.listening
        
        if self.listening:
            self.add_chat_message("ILLI", "Voice recognition activated. Say your command!")
            if self.tts_engine:
                self.speak("Voice recognition activated")
        else:
            self.add_chat_message("ILLI", "Voice recognition deactivated.")
            if self.tts_engine:
                self.speak("Voice recognition deactivated")
    
    def start_system_monitoring(self):
        """Start system monitoring thread"""
        def monitor():
            while self.monitoring_active:
                try:
                    # Get CPU usage
                    self.cpu_usage = psutil.cpu_percent(interval=1)
                    
                    # Get RAM usage
                    memory = psutil.virtual_memory()
                    self.ram_usage = memory.percent
                    
                    # Update UI (must be done in main thread)
                    self.root.after(0, self.update_system_display)
                    
                    time.sleep(2)
                except Exception as e:
                    print(f"Monitoring error: {e}")
                    time.sleep(5)
        
        monitoring_thread = threading.Thread(target=monitor, daemon=True)
        monitoring_thread.start()
    
    def update_system_display(self):
        """Update system monitoring display"""
        try:
            # Update CPU progress
            self.draw_circular_progress(self.cpu_canvas, self.cpu_usage, "#00ffff")
            self.cpu_percentage_label.configure(text=f"{self.cpu_usage:.1f}%")
            
            # Update RAM progress
            self.draw_circular_progress(self.ram_canvas, self.ram_usage, "#ff00ff")
            self.ram_percentage_label.configure(text=f"{self.ram_usage:.1f}%")
        except:
            pass
    
    def start_speech_recognition(self):
        """Start speech recognition thread"""
        def recognize_speech():
            while True:
                if self.listening and self.speech_recognizer and self.microphone:
                    try:
                        with self.microphone as source:
                            # Adjust for ambient noise
                            self.speech_recognizer.adjust_for_ambient_noise(source, duration=1)
                            
                            # Listen for audio
                            audio = self.speech_recognizer.listen(source, timeout=5, phrase_time_limit=10)
                        
                        # Recognize speech using Google Speech Recognition
                        try:
                            text = self.speech_recognizer.recognize_google(audio).lower()
                            self.speech_queue.put(text)
                        except sr.UnknownValueError:
                            pass
                        except sr.RequestError:
                            self.add_chat_message("ILLI", "Speech recognition service unavailable")
                            
                    except Exception as e:
                        print(f"Speech recognition error: {e}")
                        time.sleep(1)
                else:
                    time.sleep(1)
        
        speech_thread = threading.Thread(target=recognize_speech, daemon=True)
        speech_thread.start()
        
        # Process speech queue
        def process_speech_queue():
            while True:
                try:
                    if not self.speech_queue.empty():
                        command = self.speech_queue.get()
                        self.add_chat_message("USER (Voice)", command)
                        self.process_command(command)
                    time.sleep(0.1)
                except:
                    pass
        
        queue_thread = threading.Thread(target=process_speech_queue, daemon=True)
        queue_thread.start()

def main():
    """Main function to run the dashboard"""
    try:
        app = ILLIHUDDashboardFixed()
    except Exception as e:
        print(f"Error starting dashboard: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
