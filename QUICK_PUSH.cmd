@echo off
title ILLI AI - Quick Push
color 0A
echo.
echo ========================================
echo    ILLI AI - Quick Push
echo ========================================
echo.

echo Adding only working files...
git add ILLI_AI_PROFESSIONAL_FINAL.py
git add START_ILLI_PROFESSIONAL_FINAL.bat
git add START_ILLI.cmd
git add QUICK_PUSH.cmd
git add requirements.txt

echo Committing changes...
git commit -m "Update ILLI AI Professional %date% %time%"

echo Pushing to GitHub...
git push origin master

echo Done!
pause
