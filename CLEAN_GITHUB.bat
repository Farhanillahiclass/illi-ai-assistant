@echo off
title Clean GitHub Repository
echo ===============================================
echo      CLEAN GITHUB REPOSITORY
echo ===============================================
echo.

cd /d "g:/Virtual Assistant"

echo Removing unnecessary files from Git...
git rm -f "GITHUB_PUBLISHING_GUIDE.md"
git rm -f "GITHUB_PUSH_COMMANDS.md" 
git rm -f "GITHUB_PUSH_COMMANDS_FINAL.md"
git rm -f "LINKEDIN_POST_MASTER_PROMPT.md"
git rm -f "LINKEDIN_POST_EXAMPLES.md"
git rm -f "VOSK_SETUP_GUIDE.md"
git rm -f "EMAIL_SETUP_GUIDE.txt"
git rm -f "PROJECT_CLEANUP_SUMMARY.txt"
git rm -f "PROJECT_STRUCTURE.txt"
git rm -f "QUICK_EMAIL_SETUP.bat"
git rm -f "PUSH_TO_GITHUB.bat"
git rm -f "CLEANUP_PROJECT.bat"
git rm -f "INSTALL_DEPENDENCIES.bat"
git rm -f "START_ILLI_HUD_FIXED.bat"
git rm -f "START_ILLI_STREAMLIT.bat"
git rm -f "START_ILLI_COMPLETE_FIXED.bat"
git rm -f "START_ILLI_ULTRA_FIXED.bat"
git rm -f "START_ILLI_LEARNING_AI.bat"
git rm -f "START_ILLI_COMPLETE_ALL_FEATURES.bat"
git rm -f "START_ILLI_MASTER_DASHBOARD_ULTRA.bat"
git rm -f "illi_complete_fixed.py"
git rm -f "illi_complete_ultra_fixed.py"
git rm -f "illi_hud_fixed.py"
git rm -f "illi_streamlit_dashboard.py"
git rm -f "illi_complete.py"
git rm -f "ILLI_AI_COMPLETE.py"
git rm -f "ILLI_AI_LEARNING.py"
git rm -f "hud_requirements.txt"
git rm -f "streamlit_requirements.txt"
git rm -f "requirements.txt"
git rm -f "whatsapp_contacts.json"
git rm -f "data" -r

echo Adding working files...
git add "ILLI_AI_WORKING_FIXED.py"
git add "START_ILLI_WORKING_FIXED.bat"

echo Committing changes...
git commit -m "Clean repository - Working ILLI AI

Fixed Issues:
- Removed sounddevice dependency
- Fixed batch file encoding
- Clean repository structure
- Only essential working files

Features:
- Voice recognition working
- App launching working  
- System scan working
- Time and date working
- 18+ applications supported
- Professional UI

Created by Muhammad Farhan
Email: farhanhomeschooling519@gmail.com"

echo Pushing to GitHub...
git push -u origin main

echo.
echo Success! GitHub repository cleaned and updated.
echo.
echo Run: START_ILLI_WORKING_FIXED.bat
echo.

pause
