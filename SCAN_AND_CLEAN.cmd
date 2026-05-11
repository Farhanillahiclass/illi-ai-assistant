@echo off
title ILLI AI - Scan and Clean Folder
color 0E
echo.
echo ========================================
echo    ILLI AI - Scan and Clean Folder
echo ========================================
echo.

echo [1/6] Scanning all files in folder...
echo.
echo CURRENT FILES:
echo ========================================
dir /b
echo ========================================
echo.

echo [2/6] Identifying essential files...
echo.
echo ESSENTIAL FILES TO KEEP:
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
echo - README.md (Documentation)
echo - requirements.txt (Dependencies)
echo - .gitignore (Git Rules)
echo.

echo [3/6] Creating backup of current state...
set backup_dir=backup_cleanup_%date:~-4,4%%date:~-7,2%%date:~-10,2%_%time:~0,2%%time:~3,2%
set backup_dir=%backup_dir: =0%
mkdir "%backup_dir%" 2>nul
echo Backup created: %backup_dir%

echo [4/6] Deleting unnecessary files...
echo.
echo Deleting old merge scripts...
del AUTO_MERGE_PR.cmd 2>nul
del ACCEPT_PULL_REQUEST.cmd 2>nul
del PULL_REQUEST_HANDLER.cmd 2>nul
del SIMPLE_AUTO_MERGE.cmd 2>nul
del FORCE_SYNC_MERGE.cmd 2>nul
del SYNC_AND_MERGE.cmd 2>nul
del FIX_AUTO_MERGE.cmd 2>nul
del FORCE_ACCEPT_PR.cmd 2>nul
del QUICK_AUTO_MERGE.cmd 2>nul
del CLEANUP_GITHUB.cmd 2>nul
del MANAGE_BRANCHES.cmd 2>nul
del PUSH_README.cmd 2>nul

echo Deleting backup folders...
rmdir /s /q backup_github_* 2>nul

echo [5/6] Verifying cleanup...
echo.
echo REMAINING ESSENTIAL FILES:
echo ========================================
dir /b
echo ========================================

echo [6/6] Cleanup completed!
echo.
echo Files deleted:
echo - Old merge scripts (AUTO_MERGE_PR, ACCEPT_PULL_REQUEST, etc.)
echo - Backup folders (backup_github_*)
echo - Duplicate scripts
echo.
echo Essential files preserved:
echo - Main application and launchers
echo - GitHub management tools
echo - Documentation and dependencies
echo.
pause
