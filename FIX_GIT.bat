@echo off
chcp 65001 >nul
title Fix Git Configuration
echo ===============================================
echo      FIX GIT CONFIGURATION
echo ===============================================
echo.

cd /d "g:/Virtual Assistant"

echo Step 1: Reset Git configuration...
git config --global user.name "Muhammad Farhan"
git config --global user.email "farhanhomeschooling519@gmail.com"

echo Step 2: Remove corrupted config...
if exist .git/config (
    del .git/config
    echo Removed corrupted config file
)

echo Step 3: Initialize fresh Git repository...
git init
git remote add origin https://github.com/Farhanillahiclass/illi-ai-assistant.git

echo Step 4: Add all files...
git add .

echo Step 5: Commit changes...
git commit -m "Fixed Git configuration and updated ILLI AI

- Fixed corrupted Git configuration
- Added final ILLI AI version
- All files working properly
- Ready for GitHub push

Created by Muhammad Farhan
Email: farhanhomeschooling519@gmail.com"

echo Step 6: Push to GitHub...
git push -u origin main --force

echo.
echo SUCCESS! Git configuration fixed and pushed to GitHub
echo.
echo Now you can run: RUN_ILLI.bat
echo.

pause
