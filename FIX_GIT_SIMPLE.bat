@echo off
title Fix Git Simple
echo Removing corrupted Git files...
if exist .git rmdir /s /q .git
echo Initializing new Git repository...
git init
git config --global user.name "Muhammad Farhan"
git config --global user.email "farhanhomeschooling519@gmail.com"
git remote add origin https://github.com/Farhanillahiclass/illi-ai-assistant.git
git add .
git commit -m "Fixed Git and updated ILLI AI"
git push -u origin main --force
echo Git fixed and pushed!
pause
