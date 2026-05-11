@echo off
title ILLI AI - Force Push to GitHub
color 0C
echo.
echo ========================================
echo    ILLI AI - Force Push to GitHub
echo ========================================
echo.

echo [1/4] Checking current branch...
git branch
echo.

echo [2/4] Adding only working files (excluding .md and backup files)...
git add ILLI_AI_PROFESSIONAL_FINAL.py
git add START_ILLI_PROFESSIONAL_FINAL.bat
git add START_ILLI.cmd
git add PUSH_TO_GITHUB.cmd
git add PUSH_TO_GITHUB_CLEAN.cmd
git add FORCE_PUSH.cmd
git add QUICK_COMMANDS.bat
git add requirements.txt
git add GITHUB_MANUAL_COMMANDS.cmd
git add TEST_ILLI_PROFESSIONAL.py

echo [3/4] Force committing changes...
set commit_msg=Force update ILLI AI Professional - %date% %time%
git commit --allow-empty -m "%commit_msg%"

echo [4/4] Force pushing to GitHub...
git push origin master --force
if %errorlevel% neq 0 (
    echo ERROR: Failed to push to GitHub
    echo Trying alternative push...
    git push origin master
    if %errorlevel% neq 0 (
        echo ERROR: Both push attempts failed
        pause
        exit /b 1
    )
)

echo Success! Force pushed to GitHub
echo.
echo Repository: https://github.com/Farhanillahiclass/illi-ai-assistant
pause
