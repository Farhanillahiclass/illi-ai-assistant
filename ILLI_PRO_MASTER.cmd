@echo off
title ILLI AI PRO v1.2.1 - MASTER
color 0B

:menu
cls
echo ====================================================
echo    ILLI AI PROFESSIONAL - MASTER CONTROL PANEL
echo ====================================================
echo 1. Start ILLI AI Professional
echo 2. Clean ^& Sync to GitHub
echo 3. Build ^& Publish to PyPI
echo 4. Exit
echo ====================================================
set /p choice="Enter choice (1-4): "

if "%choice%"=="1" (
    python ILLI_AI_PROFESSIONAL_FINAL.py
    pause
    goto menu
)

if "%choice%"=="2" (
    echo Cleaning artifacts...
    del /q *.whl *.tar.gz 2>nul
    rmdir /s /q dist build *.egg-info 2>nul
    git rm LICENSE.md 2>nul
    git add .
    git commit -m "UI/UX Update: v1.2.1 - Implemented Typewriter Feed and Fixed Build"
    git push origin main --force
    pause
    goto menu
)

if "%choice%"=="3" (
    echo Building Version 1.2.1...
    python setup.py sdist bdist_wheel
    python -m twine upload dist/*
    pause
    goto menu
)

if "%choice%"=="4" exit