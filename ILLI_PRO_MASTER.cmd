@echo off
title ILLI AI PRO MASTER
color 0B

:menu
cls
echo ====================================================
echo    ILLI AI PROFESSIONAL - MASTER CONTROL PANEL
echo ====================================================
echo 1. Start ILLI AI Professional
echo 2. Sync to GitHub (Clean Mode)
echo 3. Exit
echo ====================================================
set /p choice="Enter choice (1-3): "

if "%choice%"=="1" (
    python ILLI_AI_PROFESSIONAL_FINAL.py
    pause
    goto menu
)

if "%choice%"=="2" (
    git add .
    git commit -m "Restore professional repository state"
    git push origin main --force
    pause
    goto menu
)

if "%choice%"=="3" exit