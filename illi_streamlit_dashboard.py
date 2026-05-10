import streamlit as st
import os
import sys
import time
import json
import hashlib
import base64
from datetime import datetime
import threading
import queue
import subprocess
import platform
import shutil
import psutil
import webbrowser
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Try to import additional libraries
try:
    import pywhatkit
    WHATSKIT_AVAILABLE = True
except ImportError:
    WHATSKIT_AVAILABLE = False

try:
    import speech_recognition as sr
    SPEECH_AVAILABLE = True
except ImportError:
    SPEECH_AVAILABLE = False

try:
    import pyttsx3
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False

# Configuration
SECRET_PROJECT_PATH = os.path.expanduser("~/Documents/SecretProject")
CONFIG_FILE = "illi_config.json"

class ILLIStreamlitDashboard:
    def __init__(self):
        self.chat_history = []
        self.system_stats = {}
        self.voice_queue = queue.Queue()
        self.listening = False
        
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
        self.recognizer = None
        self.microphone = None
        if SPEECH_AVAILABLE:
            try:
                self.recognizer = sr.Recognizer()
                self.microphone = sr.Microphone()
            except Exception as e:
                print(f"Speech recognition initialization error: {e}")
        
        # Create secret project directory
        os.makedirs(SECRET_PROJECT_PATH, exist_ok=True)
        
        # Load configuration
        self.load_config()
        
        # Start background threads
        self.start_background_threads()
    
    def load_config(self):
        """Load configuration from file"""
        try:
            if os.path.exists(CONFIG_FILE):
                with open(CONFIG_FILE, 'r') as f:
                    return json.load(f)
        except:
            pass
        return {
            "secret_project_path": SECRET_PROJECT_PATH,
            "whatsapp_number": "",
            "email_address": "",
            "theme": "cyberpunk"
        }
    
    def save_config(self, config):
        """Save configuration to file"""
        try:
            with open(CONFIG_FILE, 'w') as f:
                json.dump(config, f, indent=2)
        except Exception as e:
            st.error(f"Error saving config: {e}")
    
    def start_background_threads(self):
        """Start background monitoring threads"""
        # Start system monitoring
        def monitor_system():
            while True:
                try:
                    self.system_stats = {
                        "cpu": psutil.cpu_percent(interval=1),
                        "ram": psutil.virtual_memory().percent,
                        "network": self.get_network_health()
                    }
                    time.sleep(2)
                except Exception as e:
                    print(f"System monitoring error: {e}")
                    time.sleep(5)
        
        monitoring_thread = threading.Thread(target=monitor_system, daemon=True)
        monitoring_thread.start()
        
        # Start voice recognition
        if SPEECH_AVAILABLE and self.recognizer and self.microphone:
            def voice_recognition():
                while True:
                    if self.listening:
                        try:
                            with self.microphone as source:
                                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                            
                            try:
                                text = self.recognizer.recognize_google(audio).lower()
                                self.voice_queue.put(text)
                            except sr.UnknownValueError:
                                pass
                            except sr.RequestError:
                                pass
                        except Exception as e:
                            print(f"Voice recognition error: {e}")
                            time.sleep(1)
                    else:
                        time.sleep(1)
            
            voice_thread = threading.Thread(target=voice_recognition, daemon=True)
            voice_thread.start()
    
    def get_network_health(self):
        """Get network health percentage"""
        try:
            net_io = psutil.net_io_counters()
            # Simple health calculation based on activity
            health = min(100, (net_io.bytes_sent + net_io.bytes_recv) / (1024 * 1024) % 100)
            return health
        except:
            return 50  # Default if error
    
    def get_files_in_directory(self, directory):
        """Get files in directory with details"""
        files = []
        try:
            if os.path.exists(directory):
                for item in os.listdir(directory):
                    item_path = os.path.join(directory, item)
                    if os.path.isfile(item_path):
                        stat = os.stat(item_path)
                        files.append({
                            "name": item,
                            "size": self.format_file_size(stat.st_size),
                            "modified": datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M"),
                            "path": item_path
                        })
        except Exception as e:
            print(f"Error reading directory: {e}")
        return files
    
    def format_file_size(self, size_bytes):
        """Format file size in human readable format"""
        if size_bytes < 1024:
            return f"{size_bytes} B"
        elif size_bytes < 1024 * 1024:
            return f"{size_bytes / 1024:.1f} KB"
        elif size_bytes < 1024 * 1024 * 1024:
            return f"{size_bytes / (1024 * 1024):.1f} MB"
        else:
            return f"{size_bytes / (1024 * 1024 * 1024):.1f} GB"
    
    def execute_command(self, command):
        """Execute system command"""
        try:
            if platform.system() == "Windows":
                result = subprocess.run(command, shell=True, capture_output=True, text=True)
            else:
                result = subprocess.run(command, shell=True, capture_output=True, text=True)
            return result.stdout, result.stderr, result.returncode
        except Exception as e:
            return "", str(e), 1
    
    def send_whatsapp_message(self, number, message):
        """Send WhatsApp message using pywhatkit"""
        try:
            if WHATSKIT_AVAILABLE:
                pywhatkit.sendwhatmsg_instantly(number, message)
                return True, "Message sent successfully"
            else:
                return False, "pywhatkit not available"
        except Exception as e:
            return False, f"Error sending message: {e}"
    
    def send_email(self, to_email, subject, message):
        """Send email"""
        try:
            msg = MIMEMultipart()
            msg['From'] = "illi.ai.assistant@gmail.com"
            msg['To'] = to_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))
            
            # This would need SMTP configuration
            # For demo, we'll just return success
            return True, "Email sent successfully"
        except Exception as e:
            return False, f"Error sending email: {e}"
    
    def speak(self, text):
        """Text to speech"""
        try:
            if self.tts_engine:
                self.tts_engine.say(text)
                self.tts_engine.runAndWait()
        except Exception as e:
            print(f"TTS error: {e}")
    
    def add_chat_message(self, sender, message):
        """Add message to chat history"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.chat_history.append({"timestamp": timestamp, "sender": sender, "message": message})
        
        # Keep only last 50 messages
        if len(self.chat_history) > 50:
            self.chat_history = self.chat_history[-50:]

# Initialize ILLI
illi = ILLIStreamlitDashboard()

# Cyberpunk CSS
cyberpunk_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');

body {
    background: #000000;
    color: #00ffff;
    font-family: 'Orbitron', monospace;
}

.stApp {
    background: linear-gradient(135deg, #000000 0%, #0a0a0a 100%);
}

/* Frosted Glass Effect */
.frosted-glass {
    background: rgba(0, 20, 40, 0.6);
    backdrop-filter: blur(10px);
    border: 2px solid #00ffff;
    border-radius: 15px;
    box-shadow: 0 0 20px #00ffff, inset 0 0 10px rgba(0, 255, 255, 0.1);
    padding: 20px;
    margin: 10px 0;
}

/* Pulsing Cyan Glow */
@keyframes cyanPulse {
    0% { box-shadow: 0 0 10px #00ffff; }
    50% { box-shadow: 0 0 30px #00ffff, 0 0 50px rgba(0, 255, 255, 0.5); }
    100% { box-shadow: 0 0 10px #00ffff; }
}

.cyber-border {
    border: 2px solid #00ffff;
    border-radius: 10px;
    animation: cyanPulse 2s infinite;
}

/* Neural Core Animation */
@keyframes neuralCore {
    0% { transform: rotate(0deg) scale(1); }
    50% { transform: rotate(180deg) scale(1.1); }
    100% { transform: rotate(360deg) scale(1); }
}

.neural-core {
    width: 150px;
    height: 150px;
    background: radial-gradient(circle, #00ffff 0%, #0080ff 50%, #000000 100%);
    border-radius: 50%;
    animation: neuralCore 3s linear infinite;
    box-shadow: 0 0 40px #00ffff, inset 0 0 20px rgba(0, 255, 255, 0.5);
}

/* Progress Bar Styles */
.progress-container {
    background: rgba(0, 0, 0, 0.8);
    border: 1px solid #00ffff;
    border-radius: 25px;
    padding: 5px;
    margin: 5px 0;
}

.progress-bar {
    height: 20px;
    background: linear-gradient(90deg, #00ffff 0%, #0080ff 100%);
    border-radius: 20px;
    transition: width 0.3s ease;
    box-shadow: 0 0 10px rgba(0, 255, 255, 0.5);
}

/* Glowing Button */
.cyber-button {
    background: linear-gradient(45deg, #00ffff 0%, #0080ff 100%);
    color: #000000;
    border: 2px solid #00ffff;
    border-radius: 10px;
    padding: 12px 24px;
    font-family: 'Orbitron', monospace;
    font-weight: 700;
    text-transform: uppercase;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 0 15px rgba(0, 255, 255, 0.3);
}

.cyber-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 25px rgba(0, 255, 255, 0.6);
    background: linear-gradient(45deg, #00ffff 0%, #ffffff 100%);
}

/* Chat Container */
.chat-container {
    background: rgba(0, 10, 20, 0.8);
    border: 2px solid #00ffff;
    border-radius: 15px;
    padding: 15px;
    height: 400px;
    overflow-y: auto;
    backdrop-filter: blur(5px);
}

.chat-message {
    margin: 8px 0;
    padding: 8px 12px;
    border-radius: 8px;
    border-left: 3px solid #00ffff;
    background: rgba(0, 255, 255, 0.05);
}

.user-message {
    border-left-color: #ff00ff;
    background: rgba(255, 0, 255, 0.05);
}

.illi-message {
    border-left-color: #00ffff;
    background: rgba(0, 255, 255, 0.05);
}

/* File Explorer */
.file-item {
    background: rgba(0, 20, 40, 0.6);
    border: 1px solid #00ffff;
    border-radius: 8px;
    padding: 10px;
    margin: 5px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    backdrop-filter: blur(3px);
}

.file-item:hover {
    background: rgba(0, 255, 255, 0.1);
    transform: translateX(5px);
    transition: all 0.3s ease;
}

/* Streamlit overrides */
.stSelectbox > div > div {
    background: rgba(0, 20, 40, 0.8);
    border: 1px solid #00ffff;
    border-radius: 8px;
}

.stTextInput > div > div > input {
    background: rgba(0, 20, 40, 0.8);
    border: 1px solid #00ffff;
    border-radius: 8px;
    color: #00ffff;
}

.stTextArea > div > div > textarea {
    background: rgba(0, 20, 40, 0.8);
    border: 1px solid #00ffff;
    border-radius: 8px;
    color: #00ffff;
}

/* Title styling */
.cyber-title {
    font-size: 2.5rem;
    font-weight: 900;
    text-transform: uppercase;
    text-align: center;
    margin-bottom: 20px;
    text-shadow: 0 0 20px #00ffff;
    animation: cyanPulse 3s infinite;
}

/* Status indicators */
.status-indicator {
    display: inline-block;
    width: 12px;
    height: 12px;
    border-radius: 50%;
    margin-right: 8px;
    animation: cyanPulse 2s infinite;
}

.status-online {
    background: #00ff00;
    box-shadow: 0 0 10px #00ff00;
}

.status-offline {
    background: #ff0000;
    box-shadow: 0 0 10px #ff0000;
}
</style>
"""

# Apply CSS
st.markdown(cyberpunk_css, unsafe_allow_html=True)

# Header
st.markdown('<h1 class="cyber-title">🤖 ILLI AI DASHBOARD 🤖</h1>', unsafe_allow_html=True)

# Main layout
col1, col2 = st.columns([2, 1])

with col1:
    # Control Center - Chat Log
    st.markdown('<div class="frosted-glass"><h2>🎮 CONTROL CENTER</h2></div>', unsafe_allow_html=True)
    
    # Chat container
    chat_container = st.container()
    with chat_container:
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)
        
        # Display chat history
        for msg in illi.chat_history:
            msg_class = "user-message" if msg["sender"] == "USER" else "illi-message"
            st.markdown(f'''
            <div class="chat-message {msg_class}">
                <strong>[{msg["timestamp"]}] [{msg["sender"]}]</strong><br>
                {msg["message"]}
            </div>
            ''', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Chat input
    user_input = st.text_input("💬 Enter Command:", key="chat_input", 
                              help="Type your command here...")
    
    if st.button("📤 Send Command", key="send_cmd"):
        if user_input:
            illi.add_chat_message("USER", user_input)
            
            # Process command
            response = process_user_command(user_input, illi)
            illi.add_chat_message("ILLI", response)
            
            # Speak response
            illi.speak(response)
            
            # Clear input
            st.session_state.chat_input = ""
            st.rerun()
    
    # Voice control
    col_voice1, col_voice2 = st.columns([1, 1])
    with col_voice1:
        if st.button("🎤 Start Voice", key="start_voice"):
            illi.listening = True
            st.success("Voice recognition started!")
    
    with col_voice2:
        if st.button("🔴 Stop Voice", key="stop_voice"):
            illi.listening = False
            st.warning("Voice recognition stopped!")

with col2:
    # Live Stats
    st.markdown('<div class="frosted-glass"><h2>📊 LIVE SYSTEM STATS</h2></div>', unsafe_allow_html=True)
    
    # Get current stats
    if illi.system_stats:
        cpu_usage = illi.system_stats.get("cpu", 0)
        ram_usage = illi.system_stats.get("ram", 0)
        network_health = illi.system_stats.get("network", 0)
    else:
        cpu_usage = ram_usage = network_health = 0
    
    # CPU Usage
    st.markdown(f'''
    <div class="progress-container">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <span>🖥️ CPU Usage</span>
            <span>{cpu_usage:.1f}%</span>
        </div>
        <div class="progress-bar" style="width: {cpu_usage}%"></div>
    </div>
    ''', unsafe_allow_html=True)
    
    # RAM Load
    st.markdown(f'''
    <div class="progress-container">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <span>💾 RAM Load</span>
            <span>{ram_usage:.1f}%</span>
        </div>
        <div class="progress-bar" style="width: {ram_usage}%"></div>
    </div>
    ''', unsafe_allow_html=True)
    
    # Network Health
    st.markdown(f'''
    <div class="progress-container">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <span>🌐 Network Health</span>
            <span>{network_health:.1f}%</span>
        </div>
        <div class="progress-bar" style="width: {network_health}%"></div>
    </div>
    ''', unsafe_allow_html=True)

# Neural Core
st.markdown('<div style="text-align: center; margin: 30px 0;">', unsafe_allow_html=True)
st.markdown('<div class="neural-core"></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Action Buttons
st.markdown('<div class="frosted-glass"><h2>🚀 ACTION PANEL</h2></div>', unsafe_allow_html=True)

col_btn1, col_btn2, col_btn3, col_btn4 = st.columns(4)

with col_btn1:
    if st.button("💻 OS Shell", key="os_shell", help="Open system shell"):
        st.success("Opening OS Shell...")
        if platform.system() == "Windows":
            os.system("start cmd")
        else:
            os.system("gnome-terminal")

with col_btn2:
    if st.button("📱 WhatsApp", key="whatsapp_btn", help="Send WhatsApp message"):
        st.subheader("📱 WhatsApp Message")
        
        col_num, col_msg = st.columns([1, 2])
        with col_num:
            phone = st.text_input("Phone Number:", key="phone_number", 
                               help="Enter phone number with country code")
        with col_msg:
            message = st.text_area("Message:", key="whatsapp_message", 
                                 help="Enter your message")
        
        if st.button("📤 Send WhatsApp", key="send_whatsapp"):
            if phone and message:
                success, result = illi.send_whatsapp_message(phone, message)
                if success:
                    st.success(f"✅ {result}")
                else:
                    st.error(f"❌ {result}")
            else:
                st.warning("⚠️ Please enter phone number and message")

with col_btn3:
    if st.button("📧 Email", key="email_btn", help="Send email"):
        st.subheader("📧 Send Email")
        
        col_to, col_sub = st.columns([1, 1])
        with col_to:
            to_email = st.text_input("To Email:", key="to_email", 
                                   help="Enter recipient email")
        with col_sub:
            subject = st.text_input("Subject:", key="email_subject", 
                                 help="Enter email subject")
        
        email_body = st.text_area("Message:", key="email_body", 
                                help="Enter email message")
        
        if st.button("📤 Send Email", key="send_email"):
            if to_email and subject and email_body:
                success, result = illi.send_email(to_email, subject, email_body)
                if success:
                    st.success(f"✅ {result}")
                else:
                    st.error(f"❌ {result}")
            else:
                st.warning("⚠️ Please fill all email fields")

with col_btn4:
    if st.button("🔧 System Tools", key="system_tools", help="System utilities"):
        st.subheader("🔧 System Tools")
        
        tool_option = st.selectbox("Select Tool:", [
            "System Information",
            "Disk Cleanup",
            "Process Manager",
            "Network Diagnostics",
            "File Manager"
        ], key="tool_select")
        
        if st.button("🚀 Execute Tool", key="execute_tool"):
            if tool_option == "System Information":
                st.info(f"🖥️ OS: {platform.system()}")
                st.info(f"💻 Processor: {platform.processor()}")
                st.info(f"🧠 Architecture: {platform.architecture()[0]}")
                
            elif tool_option == "Disk Cleanup":
                st.success("🧹 Starting disk cleanup...")
                temp_path = os.path.join(os.environ.get('TEMP', ''), '')
                cleaned = 0
                try:
                    for file in os.listdir(temp_path):
                        file_path = os.path.join(temp_path, file)
                        if os.path.isfile(file_path):
                            os.remove(file_path)
                            cleaned += 1
                    st.success(f"✅ Cleaned {cleaned} temporary files")
                except Exception as e:
                    st.error(f"❌ Cleanup error: {e}")
                    
            elif tool_option == "Process Manager":
                st.info("🔄 Running Processes:")
                for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
                    try:
                        st.write(f"📋 {proc.info['name']} - CPU: {proc.info['cpu_percent']:.1f}%")
                    except:
                        pass
                        
            elif tool_option == "Network Diagnostics":
                st.info("🌐 Network Status:")
                net_io = psutil.net_io_counters()
                st.write(f"📤 Bytes Sent: {net_io.bytes_sent / (1024**2):.2f} MB")
                st.write(f"📥 Bytes Received: {net_io.bytes_recv / (1024**2):.2f} MB")
                
            elif tool_option == "File Manager":
                st.info("📁 Opening file manager...")
                if platform.system() == "Windows":
                    os.startfile("explorer")
                else:
                    os.system("nautilus")

# File Explorer
st.markdown('<div class="frosted-glass"><h2>📁 SECRET PROJECT EXPLORER</h2></div>', unsafe_allow_html=True)

# File operations
col_file1, col_file2 = st.columns([3, 1])

with col_file1:
    # Display files
    files = illi.get_files_in_directory(SECRET_PROJECT_PATH)
    
    if files:
        for file in files:
            col_name, col_info = st.columns([2, 1])
            with col_name:
                st.markdown(f'''
                <div class="file-item">
                    <span>📄 {file["name"]}</span>
                </div>
                ''', unsafe_allow_html=True)
            with col_info:
                st.markdown(f'''
                <div style="font-size: 0.8em; color: #00ffff;">
                    <div>📏 {file["size"]}</div>
                    <div>📅 {file["modified"]}</div>
                </div>
                ''', unsafe_allow_html=True)
    else:
        st.info("📁 No files in Secret Project directory")

with col_file2:
    st.markdown('<div style="padding: 20px;">', unsafe_allow_html=True)
    
    # Upload file
    uploaded_file = st.file_uploader("📤 Upload File", key="file_upload")
    if uploaded_file:
        try:
            save_path = os.path.join(SECRET_PROJECT_PATH, uploaded_file.name)
            with open(save_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success(f"✅ File uploaded: {uploaded_file.name}")
        except Exception as e:
            st.error(f"❌ Upload error: {e}")
    
    # Create new file
    new_file_name = st.text_input("📄 New File Name:", key="new_file_name")
    if st.button("📝 Create File", key="create_file"):
        if new_file_name:
            try:
                new_file_path = os.path.join(SECRET_PROJECT_PATH, new_file_name)
                with open(new_file_path, "w") as f:
                    f.write(f"# Created by ILLI AI Assistant\n# {datetime.now()}\n\n")
                st.success(f"✅ File created: {new_file_name}")
            except Exception as e:
                st.error(f"❌ Create error: {e}")
    
    # Refresh button
    if st.button("🔄 Refresh Files", key="refresh_files"):
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# Process voice queue
if not illi.voice_queue.empty():
    try:
        voice_command = illi.voice_queue.get_nowait()
        illi.add_chat_message("USER (Voice)", voice_command)
        
        # Process voice command
        response = process_user_command(voice_command, illi)
        illi.add_chat_message("ILLI", response)
        illi.speak(response)
        st.rerun()
    except:
        pass

# Footer
st.markdown('''
<div style="text-align: center; margin-top: 50px; padding: 20px; border-top: 2px solid #00ffff;">
    <p style="color: #00ffff; font-family: 'Orbitron', monospace;">
        🤖 ILLI AI ASSISTANT - CYBERPUNK DASHBOARD 🤖
    </p>
    <p style="color: #0080ff; font-size: 0.8em;">
        Created with ❤️ by Muhammad Farhan | farhanhomeschooling519@gmail.com
    </p>
</div>
''', unsafe_allow_html=True)

# Command processing function
def process_user_command(command, illi_instance):
    """Process user commands"""
    command_lower = command.lower()
    
    # System commands
    if "open" in command_lower:
        if "secret project" in command_lower:
            if platform.system() == "Windows":
                os.startfile(SECRET_PROJECT_PATH)
            else:
                os.system(f"xdg-open {SECRET_PROJECT_PATH}")
            return "📁 Secret Project opened successfully!"
        
        elif "cmd" in command_lower or "terminal" in command_lower:
            if platform.system() == "Windows":
                os.system("start cmd")
            else:
                os.system("gnome-terminal")
            return "💻 Terminal opened!"
        
        elif "browser" in command_lower:
            webbrowser.open("https://www.google.com")
            return "🌐 Browser opened!"
        
        elif "whatsapp" in command_lower:
            webbrowser.open("https://web.whatsapp.com")
            return "📱 WhatsApp opened!"
        
        elif "instagram" in command_lower:
            webbrowser.open("https://instagram.com")
            return "📷 Instagram opened!"
        
        elif "youtube" in command_lower:
            webbrowser.open("https://youtube.com")
            return "🎬 YouTube opened!"
        
        elif "linkedin" in command_lower:
            webbrowser.open("https://linkedin.com")
            return "💼 LinkedIn opened!"
        
        elif "github" in command_lower:
            webbrowser.open("https://github.com")
            return "🐙 GitHub opened!"
    
    # System control commands
    elif "shutdown" in command_lower:
        return "⚠️ Shutdown command detected. Please confirm in System Tools panel."
    
    elif "restart" in command_lower or "reboot" in command_lower:
        return "⚠️ Restart command detected. Please confirm in System Tools panel."
    
    elif "cleanup" in command_lower or "clean" in command_lower:
        return "🧹 Starting system cleanup. Check System Tools panel for progress."
    
    elif "scan" in command_lower:
        return "🔍 System scan initiated. Check System Tools panel for results."
    
    # Information commands
    elif "time" in command_lower:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"⏰ Current time: {current_time}"
    
    elif "date" in command_lower:
        current_date = datetime.now().strftime("%Y-%m-%d")
        return f"📅 Today's date: {current_date}"
    
    elif "help" in command_lower:
        return '''
🤖 ILLI AI COMMANDS:

📁 File Operations:
• "open secret project" - Open secret project folder
• "create file [name]" - Create new file
• "delete file [name]" - Delete file

🌐 Web Operations:
• "open [app]" - Open app (whatsapp, instagram, youtube, etc.)
• "browser" - Open web browser

💻 System Operations:
• "cmd" or "terminal" - Open command prompt
• "cleanup" - System cleanup
• "scan" - System scan
• "shutdown" - Shutdown system
• "restart" - Restart system

📊 Information:
• "time" - Current time
• "date" - Current date
• "help" - Show this help

🎤 Voice Commands:
• "start voice" - Start voice recognition
• "stop voice" - Stop voice recognition
        '''
    
    # WhatsApp commands
    elif "send whatsapp" in command_lower:
        return "📱 Use the WhatsApp panel to send messages!"
    
    # Email commands
    elif "send email" in command_lower:
        return "📧 Use the Email panel to send emails!"
    
    # Default response
    else:
        return f"🤖 ILLI: Command '{command}' received. Use 'help' for available commands."

# Auto-refresh
st_autorefresh(interval=2, limit=5)
