@echo off
title ILLI AI - Push Latest Version
color 0A
echo.
echo ========================================
echo    ILLI AI - Push Latest Version
echo ========================================
echo.

echo [1/4] Adding latest files...
git add ILLI_AI_PROFESSIONAL_FINAL.py
git add START_ILLI_PROFESSIONAL_FINAL.bat
git add START_ILLI.cmd
git add QUICK_PUSH.cmd
git add SYNC_AND_MERGE.cmd
git add requirements.txt
git add .gitignore

echo [2/4] Committing latest version...
set commit_msg=Update ILLI AI Professional - %date% %time%
git commit -m "%commit_msg%"

echo [3/4] Pushing to main branch...
git push origin main
if %errorlevel% neq 0 (
    echo ERROR: Failed to push to main
    pause
    exit /b 1
)

echo [4/4] Success!
echo.
echo Latest version pushed to GitHub
echo Repository: https://github.com/Farhanillahiclass/illi-ai-assistant/tree/main
echo.
echo Files pushed:
echo - ILLI_AI_PROFESSIONAL_FINAL.py
echo - START_ILLI_PROFESSIONAL_FINAL.bat
echo - START_ILLI.cmd
echo - QUICK_PUSH.cmd
echo - SYNC_AND_MERGE.cmd
echo - requirements.txt
echo - .gitignore
echo.
pause
