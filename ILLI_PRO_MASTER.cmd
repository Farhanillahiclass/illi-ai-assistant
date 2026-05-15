@echo off
title ILLI AI PRO MASTER
color 0B

:menu
cls
echo ====================================================
echo    ILLI AI PROFESSIONAL - MASTER CONTROL PANEL
echo ====================================================
echo 1. Start ILLI AI Professional
echo 2. Clean Project Clutter (Remove temp/extra files)
echo 3. Push to GitHub (Professional Mode)
echo 4. Exit
echo ====================================================
set /p choice="Enter choice (1-4): "

if "%choice%"=="1" (
    python ILLI_AI_PROFESSIONAL_FINAL.py
    pause
    goto menu
)

if "%choice%"=="2" (
    echo Cleaning unnecessary files...
    del /q *.log *.tmp 2>nul
    del /q PUSH_LATEST.cmd QUICK_PUSH.cmd RUN_ILLI.cmd START_ILLI.cmd 2>nul
    echo Done.
    pause
    goto menu
)

if "%choice%"=="3" (
    echo [GitHub Sync] Securing secrets and pushing essential files...
    git add ILLI_AI_PROFESSIONAL_FINAL.py
    git add requirements.txt
    git add README.md
    git add setup.py
    git add ILLI_PRO_MASTER.cmd
    git commit -m "Production Build: Consolidated features and cleaned workspace"
    git push origin main
    echo Repository Updated Successfully.
    pause
    goto menu
)

if "%choice%"=="4" exit