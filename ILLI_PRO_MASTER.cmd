@echo off
title ILLI AI PRO MASTER | GHOST-PROTOCOL
color 0A

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
    streamlit run ILLI_AI_PROFESSIONAL_FINAL.py
    pause
    goto menu
)

if "%choice%"=="2" (
    echo Cleaning artifacts...
    del /q *.whl *.tar.gz 2>nul
    rmdir /s /q dist build *.egg-info 2>nul
    del /f /q ILLI_AI_ENHANCED.py ILLI_AI_FIXED.py 2>nul
    git add .
    git commit -m "Production: Ghost-Protocol Modular Structure v1.2.2"
    git push origin main --force
    pause
    goto menu
)

if "%choice%"=="3" (
    echo Building...
    python -m build --sdist --wheel
    python -m twine upload dist/*
    pause
    goto menu
)

if "%choice%"=="4" exit