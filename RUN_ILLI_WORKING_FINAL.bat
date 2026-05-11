@echo off
chcp 65001 >nul
title ILLI AI - Working Final Version
echo ===============================================
echo      ILLI AI - WORKING FINAL VERSION
echo ===============================================
echo.
echo Created by: Muhammad Farhan
echo Email: farhanhomeschooling519@gmail.com
echo.
echo ===============================================
echo      COMPLETE PC AND WEB CONTROL SYSTEM
echo ===============================================
echo.
echo 1. COMPLETE PC CONTROL:
echo    - All desktop applications
echo    - All system utilities
echo    - All development tools
echo    - All graphics software
echo    - All gaming platforms
echo    - All security tools
echo.
echo 2. COMPLETE WEB CONTROL:
echo    - All websites and web apps
echo    - All social media platforms
echo    - All email services
echo    - All shopping sites
echo    - All entertainment platforms
echo    - All development platforms
echo.
echo 3. VOICE CONTROL:
echo    - Natural conversation
echo    - Complete command recognition
echo    - Voice feedback for all actions
echo    - Manual command input
echo    - Voice settings
echo.
echo 4. SYSTEM ADMINISTRATION:
echo    - Complete system monitoring
echo    - Performance optimization
echo    - Security scanning
echo    - Network management
echo    - Power management
echo    - File system management
echo.
echo 5. FILE MANAGEMENT:
echo    - Create, delete, copy, move, rename
echo    - Search and browse
echo    - File information
echo    - Batch operations
echo    - System cleanup
echo.
echo 6. PROFESSIONAL UI:
echo    - 6 organized tabs
echo    - Control Center dashboard
echo    - Applications by category
echo    - Web control panel
echo    - System monitoring
echo    - Voice control center
echo    - System utilities
echo.
echo ===============================================
echo      AUTOMATIC APP DETECTION:
echo ===============================================
echo.
echo - WhatsApp desktop (if installed)
echo - Chrome, Firefox, Edge (if installed)
echo - Office apps (if installed)
echo - Development tools (if installed)
echo - Graphics software (if installed)
echo - Gaming platforms (if installed)
echo.
echo ===============================================
echo      STARTING ILLI AI...
echo.
python "ILLI_AI_WORKING_FINAL.py"

if errorlevel 1 (
    echo.
    echo ERROR: Python script failed to run
    echo.
    echo POSSIBLE SOLUTIONS:
    echo 1. Install required packages:
    echo    pip install tkinter psutil speech_recognition pyttsx3
    echo.
    echo 2. Check Python installation:
    echo    python --version
    echo.
    echo 3. Install missing packages:
    echo    pip install pywin32
    echo.
    echo 4. Run as Administrator if needed
    echo.
    echo 5. Check file permissions
    echo.
)

pause
