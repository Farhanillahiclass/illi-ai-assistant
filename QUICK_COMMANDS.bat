@echo off
title ILLI AI - Quick Commands Menu
color 0E
echo.
echo ========================================
echo    ILLI AI - Quick Commands
echo ========================================
echo.
echo 1. Start ILLI AI
echo 2. Push to GitHub
echo 3. Pull from GitHub
echo 4. Test System
echo 5. Exit
echo.
set /p choice="Enter your choice (1-5): "

if "%choice%"=="1" goto START
if "%choice%"=="2" goto PUSH
if "%choice%"=="3" goto PULL
if "%choice%"=="4" goto TEST
if "%choice%"=="5" goto EXIT
goto MENU

:START
echo.
echo Starting ILLI AI Professional...
python ILLI_AI_PROFESSIONAL_FINAL.py
pause
goto MENU

:PUSH
echo.
echo Pushing to GitHub...
call PUSH_TO_GITHUB.cmd
pause
goto MENU

:PULL
echo.
echo Pulling from GitHub...
git pull origin main
pause
goto MENU

:TEST
echo.
echo Testing ILLI AI System...
python TEST_ILLI_PROFESSIONAL.py
pause
goto MENU

:EXIT
echo.
echo Thank you for using ILLI AI!
exit /b 0

:MENU
cls
goto :EOF
