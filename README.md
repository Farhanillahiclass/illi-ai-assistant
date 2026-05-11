# ILLI AI Assistant - Professional Cyberpunk Dashboard

## 🌟 Overview

ILLI AI Assistant is a comprehensive, professional-grade AI assistant created by Muhammad Farhan. This project features multiple interfaces including a cutting-edge Streamlit cyberpunk dashboard, complete desktop applications, and advanced system control capabilities.

## 🚀 Versions Available

### 1. ILLI Streamlit Dashboard (Recommended)
**File:** `illi_streamlit_dashboard.py` | **Launcher:** `START_ILLI_STREAMLIT.bat`

**🌟 Cyberpunk Features:**
- ✅ Deep black background (#000000) with neon cyan (#00ffff) borders
- ✅ 2-column grid layout with Control Center chat log
- ✅ Neural Core with glowing rotating sphere animation
- ✅ Live stats with CPU, RAM, Network circular progress bars
- ✅ Action buttons for OS Shell, WhatsApp, Email, System Tools
- ✅ File Explorer for Secret Project directory with technical details
- ✅ Frosted glass CSS effects with backdrop-filter blur(10px)
- ✅ Pulsing cyan glow animations
- ✅ Monospaced technical fonts (Orbitron/Consolas)
- ✅ Real-time system monitoring with psutil
- ✅ Voice recognition and TTS capabilities
- ✅ WhatsApp integration with pywhatkit
- ✅ Complete OS control with os and shutil libraries
- ✅ Professional web-based interface with Streamlit

### 2. ILLI Complete Fixed (Desktop)
**File:** `illi_complete_fixed.py` | **Launcher:** `START_ILLI_COMPLETE_FIXED.bat`

**🔧 Features:**
- ✅ Complete voice recognition with enhanced accuracy and error handling
- ✅ 20+ app launching (WhatsApp, Instagram, Gmail, ChatGPT, etc.)
- ✅ App closing functionality with process detection
- ✅ YouTube control with search and video name extraction
- ✅ LinkedIn integration with profile, jobs, and network access
- ✅ System monitoring and control with real-time updates
- ✅ WhatsApp messaging with contact memory system
- ✅ Professional dashboard UI with fixed animations
- ✅ Enhanced error handling and crash prevention
- ✅ All features tested and working perfectly

### 3. ILLI HUD Dashboard Fixed (Futuristic)
**File:** `illi_hud_fixed.py` | **Launcher:** `START_ILLI_HUD_FIXED.bat`

**🎮 Features:**
- ✅ Futuristic HUD interface with CustomTkinter (fixed)
- ✅ Dark theme (#1a1a1a) with neon cyan (#00ffff) borders
- ✅ Circular progress bars for CPU and RAM monitoring (working)
- ✅ Glassmorphic chat module with message history
- ✅ Bottom navigation bar with 7 icon functions
- ✅ Online speech recognition with Google Speech API
- ✅ Text-to-speech (pyttsx3) with voice feedback
- ✅ "Open Secret Project" system integration
- ✅ Modular design for future features
- ✅ All UI components tested and working

## 🛠️ Installation

### Prerequisites
- Python 3.7 or higher
- Windows/macOS/Linux support

### Install Dependencies
```bash
# For ILLI Complete
pip install -r requirements.txt

# For ILLI HUD Dashboard
pip install -r hud_requirements.txt
```

### Quick Start
```bash
# Run ILLI Complete Fixed (Recommended)
START_ILLI_COMPLETE_FIXED.bat

# Run ILLI HUD Dashboard Fixed
START_ILLI_HUD_FIXED.bat
```

## 📋 Available Commands

### ILLI Complete Commands
**App Launching:**
- `open whatsapp` - Launch WhatsApp
- `open instagram` - Launch Instagram
- `open gmail` - Open Gmail
- `open chatgpt` - Open ChatGPT
- `open spotify` - Launch Spotify
- `open discord` - Launch Discord
- And 15+ more apps...

**App Closing:**
- `close whatsapp` - Close WhatsApp
- `close instagram` - Close Instagram
- `close chrome` - Close Chrome
- And more...

**System Control:**
- `system scan` - Scan system resources
- `system cleanup` - Clean temporary files
- `system optimize` - Optimize performance
- `system monitor` - Start monitoring

**Communication:**
- `send message to [contact] saying [message]` - Send WhatsApp message
- `linkedin connect` - Send connection request

**Entertainment:**
- `play [video name]` - Search and play YouTube
- `next video` / `previous video` - YouTube controls

### ILLI HUD Commands
**Voice Commands:**
- `Open Secret Project` - Opens your secret project folder
- `Shutdown` - System shutdown
- `Browser` - Open web browser
- `File Explorer` - Open file manager
- `Network Sync` - Simulate network sync
- `Settings` - Opens configuration dialog
- `Performance` - Shows system information
- `Time` - Displays current time
- `Clear` - Clears chat history
- `Help` - Shows commands

**Navigation:**
- Bottom navigation bar with 7 main functions
- Icon-based interface
- Quick access to all features

## 🎨 Features

### Voice Recognition
- Enhanced speech recognition with Google Speech API
- Offline support with Vosk (HUD version)
- Natural language processing
- Multiple language support
- Noise reduction

### System Monitoring
- Real-time CPU usage monitoring
- RAM usage tracking
- Disk space monitoring
- Network statistics
- Process management
- Circular progress indicators (HUD)

### App Integration
- 20+ application integrations
- Desktop app detection
- Web version fallbacks
- Process management
- Cross-platform support

### Communication
- WhatsApp messaging integration
- LinkedIn connection requests
- Email support
- Social media integration
- Message history

### User Interface
- Professional dashboard design
- Futuristic HUD aesthetic
- Glassmorphic effects
- Smooth animations
- Responsive layout
- Customizable themes

## 🔧 Technical Details

### Dependencies
**Core Libraries:**
- `customtkinter` - Modern GUI framework
- `psutil` - System monitoring
- `pyttsx3` - Text-to-speech
- `vosk` - Offline speech recognition
- `speechrecognition` - Online speech recognition
- `pyautogui` - Screen automation
- `webbrowser` - Web integration

**System Requirements:**
- Python 3.7+
- 4GB RAM minimum
- 100MB disk space
- Microphone for voice commands
- Internet for online features

### Architecture
- Modular design for easy extension
- Plugin-ready architecture
- Cross-platform compatibility
- Configuration management
- Error handling and logging

## 📁 Project Structure

```
Virtual Assistant/
├── illi_complete_fixed.py        # Main AI assistant (fixed version)
├── illi_hud_fixed.py           # Futuristic HUD dashboard (fixed)
├── START_ILLI_COMPLETE_FIXED.bat # Launcher for complete fixed version
├── START_ILLI_HUD_FIXED.bat     # Launcher for HUD fixed version
├── INSTALL_DEPENDENCIES.bat        # Dependency installer
├── requirements.txt               # Dependencies for complete version
├── hud_requirements.txt           # Dependencies for HUD version
├── VOSK_SETUP_GUIDE.md          # Vosk setup guide
├── README.md                     # This file
└── data/                         # Data storage folder
    └── whatsapp_contacts.json     # Contact memory
```

## 🔐 Security & Privacy

### Data Protection
- Local data storage only
- No cloud data transmission
- Encrypted configuration files
- User consent for all features

### Permissions
- Minimal system permissions required
- Transparent data usage
- User-controlled settings
- No background tracking

## 🌟 Advanced Features

### AI Capabilities
- Natural language understanding
- Context-aware responses
- Learning from user interactions
- Predictive assistance
- Multi-modal interaction

### System Integration
- Deep system integration
- Native file operations
- System service management
- Network configuration
- Hardware control

### Customization
- Custom command creation
- Personalized responses
- Theme customization
- Layout configuration
- Plugin development

## 🚀 Getting Started

### 1. Clone Repository
```bash
git clone https://github.com/Farhanillahiclass/illi-ai-assistant.git
cd illi-ai-assistant
```

### 2. Install Dependencies
```bash
# For complete version
pip install -r requirements.txt

# For HUD version
pip install -r hud_requirements.txt
```

### 3. Setup Vosk (HUD only)
```bash
# Follow VOSK_SETUP_GUIDE.md
# Download and configure Vosk model
```

### 4. Run Application
```bash
# Complete version
START_ILLI_COMPLETE.bat

# HUD version
START_ILLI_HUD.bat
```

## 🤝 Contributing

### Development Setup
1. Fork repository
2. Create feature branch
3. Make changes
4. Test thoroughly
5. Submit pull request

### Code Standards
- Follow PEP 8 guidelines
- Add documentation
- Include error handling
- Test all features
- Update README

## 📞 Support

### Contact
- **Creator:** Muhammad Farhan
- **Email:** farhanhomeschooling519@gmail.com
- **GitHub:** https://github.com/Farhanillahiclass/illi-ai-assistant

### Troubleshooting
- Check dependencies installation
- Verify Python version
- Review setup guides
- Check system permissions
- Test microphone (voice features)

## 📜 License

This project is open source and available under the MIT License.

## 🔮 Future Roadmap

### Planned Features
- Advanced AI responses
- Machine learning integration
- Web interface
- Mobile app
- Cloud synchronization
- Advanced automation
- Multi-language support
- Plugin marketplace

### Development Goals
- Enhanced user experience
- Improved performance
- Better accessibility
- Expanded compatibility
- Advanced security
- Community features

---

**🎉 Thank you for using ILLI AI Assistant!**

*Created with ❤️ by Muhammad Farhan*
*Email: farhanhomeschooling519@gmail.com*
