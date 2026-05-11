@echo off
chcp 65001 >nul
title Complete Git Reset
echo ===============================================
echo      COMPLETE GIT RESET
echo ===============================================
echo.

cd /d "g:/Virtual Assistant"

echo Step 1: Remove all Git files...
if exist .git (
    rmdir /s /q .git
    echo Removed .git directory
)

echo Step 2: Remove temporary files...
if exist .gitignore del .gitignore
if exist .gitattributes del .gitattributes

echo Step 3: Initialize fresh Git repository...
git init
git config --global user.name "Muhammad Farhan"
git config --global user.email "farhanhomeschooling519@gmail.com"

echo Step 4: Add remote origin...
git remote add origin https://github.com/Farhanillahiclass/illi-ai-assistant.git

echo Step 5: Add all files...
git add .

echo Step 6: Initial commit...
git commit -m "Complete Git Reset - Fresh Start

- Removed corrupted configuration
- Clean repository initialization
- All files ready for GitHub
- Professional ILLI AI project

Created by Muhammad Farhan
Email: farhanhomeschooling519@gmail.com
GitHub: https://github.com/Farhanillahiclass/illi-ai-assistant"

echo Step 7: Push to GitHub...
git push -u origin main --force

echo.
echo SUCCESS! Git completely reset and pushed to GitHub
echo.
echo Repository: https://github.com/Farhanillahiclass/illi-ai-assistant
echo.

pause
