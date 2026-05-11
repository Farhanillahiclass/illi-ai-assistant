@echo off
title ILLI AI - Push to GitHub
color 0B
echo.
echo ========================================
echo    ILLI AI - Push to GitHub
echo ========================================
echo.

echo [1/4] Adding all changes...
git add .
if %errorlevel% neq 0 (
    echo ERROR: Failed to add changes
    pause
    exit /b 1
)

echo [2/4] Committing changes...
set commit_msg=Auto update %date% %time%
git commit -m "%commit_msg%"
if %errorlevel% neq 0 (
    echo ERROR: Failed to commit changes
    pause
    exit /b 1
)

echo [3/4] Pushing to GitHub...
git push origin main
if %errorlevel% neq 0 (
    echo ERROR: Failed to push to GitHub
    echo Make sure you have internet connection and proper permissions
    pause
    exit /b 1
)

echo [4/4] Success! Changes pushed to GitHub
echo.
echo Repository: https://github.com/Farhanillahiclass/illi-ai-assistant
pause
