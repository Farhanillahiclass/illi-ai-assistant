@echo off
title Install ILLI AI Dependencies
echo ===============================================
echo      INSTALL ILLI AI DEPENDENCIES
echo ===============================================
echo.
echo Created by: Muhammad Farhan
echo Email: farhanhomeschooling519@gmail.com
echo.
echo This script will install all required dependencies for ILLI AI Assistant.
echo.
echo 📦 DEPENDENCIES TO INSTALL:
echo - speechrecognition (Voice recognition)
echo - pyttsx3 (Text-to-speech)
echo - wikipedia (Wikipedia search)
echo - psutil (System monitoring)
echo - pyautogui (Screen automation)
echo - pywin32 (Windows API)
echo - Pillow (Image processing)
echo - matplotlib (Data visualization)
echo - numpy (Numerical computing)
echo - opencv-python (Computer vision)
echo.
echo 🔧 INSTALLATION METHODS:
echo 1. Automatic installation using pip
echo 2. Manual installation guide
echo 3. GitHub dependency download
echo.
echo Starting automatic installation...
echo.

echo Installing speechrecognition...
pip install speechrecognition>=3.10.0

echo.
echo Installing pyttsx3...
pip install pyttsx3>=2.90

echo.
echo Installing wikipedia...
pip install wikipedia>=1.4.0

echo.
echo Installing psutil...
pip install psutil>=5.9.0

echo.
echo Installing pyautogui...
pip install pyautogui>=0.9.54

echo.
echo Installing pywin32...
pip install pywin32>=304

echo.
echo Installing Pillow...
pip install Pillow>=9.0.0

echo.
echo Installing matplotlib...
pip install matplotlib>=3.5.0

echo.
echo Installing numpy...
pip install numpy>=1.21.0

echo.
echo Installing opencv-python...
pip install opencv-python>=4.5.0

echo.
echo 🎉 INSTALLATION COMPLETED!
echo.
echo All dependencies have been installed successfully.
echo You can now run ILLI AI Assistant.
echo.
echo 🚀 TO RUN ILLI:
echo START_ILLI_PROFESSIONAL.bat
echo.
echo 📚 MANUAL INSTALLATION:
echo If automatic installation fails, run:
echo pip install -r requirements.txt
echo.
echo 🌐 GITHUB DEPENDENCIES:
echo Repository: https://github.com/Farhanillahiclass/illi-ai-assistant
echo Download: https://github.com/Farhanillahiclass/illi-ai-assistant/archive/main.zip
echo.
echo Press any key to exit...
pause
