@echo off
title ILLI AI - Push to GitHub (Clean)
color 0B
echo.
echo ========================================
echo    ILLI AI - Push to GitHub (Clean)
echo ========================================
echo.

echo [1/5] Checking repository status...
git status
echo.

echo [2/5] Adding only working files...
git add ILLI_AI_PROFESSIONAL_FINAL.py
git add START_ILLI_PROFESSIONAL_FINAL.bat
git add START_ILLI.cmd
git add PUSH_TO_GITHUB.cmd
git add QUICK_COMMANDS.bat
git add requirements.txt
git add GITHUB_MANUAL_COMMANDS.cmd
git add TEST_ILLI_PROFESSIONAL.py

echo [3/5] Committing changes...
set commit_msg=Update ILLI AI Professional - %date% %time%
git commit -m "%commit_msg%"
if %errorlevel% neq 0 (
    echo No changes to commit or commit failed
    echo Continuing to push...
)

echo [4/5] Pushing to GitHub...
git push origin master
if %errorlevel% neq 0 (
    echo ERROR: Failed to push to GitHub
    echo Make sure you have internet connection and proper permissions
    pause
    exit /b 1
)

echo [5/5] Success! Working files pushed to GitHub
echo.
echo Repository: https://github.com/Farhanillahiclass/illi-ai-assistant
echo.
echo Pushed files:
echo - ILLI_AI_PROFESSIONAL_FINAL.py
echo - START_ILLI_PROFESSIONAL_FINAL.bat
echo - START_ILLI.cmd
echo - PUSH_TO_GITHUB.cmd
echo - QUICK_COMMANDS.bat
echo - requirements.txt
echo - GITHUB_MANUAL_COMMANDS.cmd
echo - TEST_ILLI_PROFESSIONAL.py
echo.
echo Excluded files: .md files, backup files, temporary files
pause
