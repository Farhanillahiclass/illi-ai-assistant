@echo off
title ILLI AI Professional - Complete PC & Web Control System
color 0A
echo.
echo ================================================
echo    ILLI AI PROFESSIONAL LAUNCHER
echo    Complete PC & Web Control System
echo    Created by Muhammad Farhan
echo    Email: farhanhomeschooling519@gmail.com
echo ================================================
echo.
echo [+] Initializing ILLI AI Professional...
echo [+] Checking system requirements...
echo.

REM Check Python installation
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python 3.7 or higher
    echo Download from: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [+] Python found: 
python --version

REM Check if required modules are installed
echo [+] Checking required modules...
python -c "import tkinter, psutil, speech_recognition, pyttsx3, requests, git" >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Some required modules are missing
    echo [+] Installing required modules...
    pip install psutil speechrecognition pyttsx3 requests GitPython cryptography
    if %errorlevel% neq 0 (
        echo [ERROR] Failed to install required modules
        pause
        exit /b 1
    )
)

echo [+] All requirements satisfied
echo [+] Starting ILLI AI Professional...
echo.

REM Start the application
python "ILLI_AI_PROFESSIONAL_FINAL.py"

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Application failed to start
    echo [!] Check error messages above
    pause
)

echo.
echo [+] ILLI AI Professional closed
pause
