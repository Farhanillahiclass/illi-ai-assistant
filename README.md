# ILLI Virtual Assistant

Created by: Muhammad Farhan

## Description
ILLI is an advanced virtual assistant with Islamic greetings and enhanced features. It can help you with various tasks using voice commands.

## Features
- Islamic greeting (Assalam o Alaikum) on startup
- Enhanced WhatsApp desktop app detection and launching
- Video selection feature (first, second, third)
- Introduction system - tells who created ILLI
- YouTube video search and play
- Universal app launcher
- Wikipedia search
- System controls (shutdown, restart)
- Screenshot capability
- File search functionality
- Modern dashboard interface
- Enhanced voice recognition

## Files
- `illi.py` - Main voice assistant
- `illi_advanced.py` - Advanced version with more features
- `illi_dashboard.py` - Modern GUI dashboard
- `START_ILLI.bat` - Easy launcher

## How to Run

### Option 1: Using Launcher (Recommended)
Double-click `START_ILLI.bat`

### Option 2: Command Line
```bash
python "g:/Virtual Assistant/illi.py"
```

### Option 3: Advanced Version
```bash
python "g:/Virtual Assistant/illi_advanced.py"
```

### Option 4: Dashboard
```bash
python "g:/Virtual Assistant/illi_dashboard.py"
```

## Available Commands

### Introduction
- "who created you" - Tells who made ILLI
- "who are you" - Introduction

### YouTube
- "open youtube" - Opens YouTube
- "play [song/video]" - Searches and asks which video to play

### Apps
- "open whatsapp" - Launches WhatsApp desktop app
- "open [app name]" - Launches any app

### Information
- "what is [topic]" - Searches Wikipedia
- "time" - Tells current time

### System
- "shutdown" - Shuts down computer
- "restart" - Restarts computer
- "screenshot" - Takes screenshot

### Files
- "find file [name]" - Searches computer for files

### Help
- "help" - Shows all commands

## Requirements
- Python 3.7+
- pyttsx3
- speech_recognition
- wikipedia
- webbrowser
- os
- subprocess
- time
- pyautogui
- glob
- psutil
- smtplib
- json
- winreg
- tkinter (for dashboard)

## Notes
- ILLI starts with Islamic greeting "Assalam o Alaikum"
- Enhanced WhatsApp detection finds desktop app before falling back to web
- Video selection allows choosing first, second, or third video
- Created by Muhammad Farhan
- Modern dashboard available for GUI control
