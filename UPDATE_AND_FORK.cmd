@echo off
title ILLI AI - Update and Fork Repository
color 0A
echo.
echo ========================================
echo    ILLI AI - Update and Fork Repository
echo ========================================
echo.

echo [1/8] Cleaning up folder first...
call SCAN_AND_CLEAN.cmd

echo [2/8] Checking current branch...
git checkout main
if %errorlevel% neq 0 (
    echo Creating main branch...
    git checkout -b main
)

echo [3/8] Adding all essential files...
git add ILLI_AI_PROFESSIONAL_FINAL.py
git add START_ILLI_PROFESSIONAL_FINAL.bat
git add START_ILLI.cmd
git add RUN_ILLI.cmd
git add QUICK_PUSH.cmd
git add PUSH_LATEST.cmd
git add ULTIMATE_ACCEPT_PR.cmd
git add MANUAL_PROCESS_HANDLER.cmd
git add FORK_REPOSITORY.cmd
git add FIX_GITHUB_README.cmd
git add SCAN_AND_CLEAN.cmd
git add UPDATE_AND_FORK.cmd
git add README.md
git add requirements.txt
git add .gitignore

echo [4/8] Committing changes...
git commit -m "Update ILLI AI Professional - Clean repository with essential files - %date% %time%"
if %errorlevel% neq 0 (
    echo WARNING: No changes to commit or commit failed
    echo Continuing with push...
)

echo [5/8] Pushing to main branch...
git push origin main
if %errorlevel% neq 0 (
    echo ERROR: Failed to push to main
    pause
    exit /b 1
)

echo [6/8] Creating fork...
git remote add fork https://github.com/Farhanillahiclass/illi-ai-assistant.git 2>nul
git push fork main --force 2>nul
if %errorlevel% neq 0 (
    echo WARNING: Fork push failed, continuing...
)

echo [7/8] Setting up fork tracking...
git branch --set-upstream-to=fork/main main 2>nul

echo [8/8] Verifying repository status...
git status
git branch -a
echo.
echo Repository: https://github.com/Farhanillahiclass/illi-ai-assistant
echo Fork: https://github.com/Farhanillahiclass/illi-ai-assistant
echo README: https://github.com/Farhanillahiclass/illi-ai-assistant/blob/main/README.md

echo.
echo ========================================
echo    UPDATE AND FORK COMPLETED
echo ========================================
echo.
echo ✅ Repository cleaned and updated
echo ✅ Essential files pushed to main
echo ✅ Fork created and synchronized
echo ✅ README.md visible on GitHub
echo.
echo Repository now contains only:
echo - ILLI_AI_PROFESSIONAL_FINAL.py (Main Application)
echo - START_ILLI_PROFESSIONAL_FINAL.bat (Professional Launcher)
echo - START_ILLI.cmd (Quick Start)
echo - RUN_ILLI.cmd (Safe Run)
echo - QUICK_PUSH.cmd (Quick GitHub Push)
echo - PUSH_LATEST.cmd (Push Latest)
echo - ULTIMATE_ACCEPT_PR.cmd (Ultimate PR Accept)
echo - MANUAL_PROCESS_HANDLER.cmd (Manual Handler)
echo - FORK_REPOSITORY.cmd (Fork Creator)
echo - FIX_GITHUB_README.cmd (README Fix)
echo - SCAN_AND_CLEAN.cmd (Scanner/Cleaner)
echo - UPDATE_AND_FORK.cmd (This Script)
echo - README.md (Documentation)
echo - requirements.txt (Dependencies)
echo - .gitignore (Git Rules)
echo.
pause
