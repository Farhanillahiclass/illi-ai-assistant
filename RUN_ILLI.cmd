@echo off
title ILLI AI - Run Application
color 0A
echo.
echo ========================================
echo    ILLI AI - Run Application
echo ========================================
echo.

echo Starting ILLI AI Professional...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed
    echo Please install Python from: https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Check if main file exists
if not exist "ILLI_AI_PROFESSIONAL_FINAL.py" (
    echo ERROR: ILLI_AI_PROFESSIONAL_FINAL.py not found
    echo Please ensure the file exists in current directory
    pause
    exit /b 1
)

echo Starting ILLI AI Professional...
echo.
python ILLI_AI_PROFESSIONAL_FINAL.py

if %errorlevel% neq 0 (
    echo.
    echo ERROR: ILLI AI failed to start
    echo Please check the error messages above
    pause
    exit /b 1
)

echo.
echo ILLI AI Professional closed successfully
pause
