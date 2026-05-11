@echo off
title ILLI AI - GitHub Manual Commands
color 0B
echo.
echo ===============================================
echo    ILLI AI - GITHUB MANUAL COMMANDS
echo    Complete Repository Management
echo    Created by Muhammad Farhan
echo    Email: farhanhomeschooling519@gmail.com
echo ===============================================
echo.
echo [+] GitHub Repository: https://github.com/Farhanillahiclass/illi-ai-assistant
echo [+] Local Path: %CD%
echo.

:MENU
echo.
echo ===============================================
echo    SELECT GITHUB OPERATION
echo ===============================================
echo.
echo 1. Initialize Repository (First Time Setup)
echo 2. Add All Changes to Staging
echo 3. Commit Changes
echo 4. Push to GitHub
echo 5. Pull Latest Changes
echo 6. Check Repository Status
echo 7. View Commit History
echo 8. Create New Branch
echo 9. Switch Branch
echo 10. Merge Branches
echo 11. Clone Repository
echo 12. Create Backup
echo 13. Sync Repository (Pull + Add + Commit + Push)
echo 14. View Remote Information
echo 15. Reset Repository
echo 0. Exit
echo.
set /p choice="Enter your choice (0-15): "

if "%choice%"=="1" goto INIT_REPO
if "%choice%"=="2" goto ADD_CHANGES
if "%choice%"=="3" goto COMMIT_CHANGES
if "%choice%"=="4" goto PUSH_CHANGES
if "%choice%"=="5" goto PULL_CHANGES
if "%choice%"=="6" goto CHECK_STATUS
if "%choice%"=="7" goto VIEW_HISTORY
if "%choice%"=="8" goto CREATE_BRANCH
if "%choice%"=="9" goto SWITCH_BRANCH
if "%choice%"=="10" goto MERGE_BRANCHES
if "%choice%"=="11" goto CLONE_REPO
if "%choice%"=="12" goto CREATE_BACKUP
if "%choice%"=="13" goto SYNC_REPO
if "%choice%"=="14" goto VIEW_REMOTE
if "%choice%"=="15" goto RESET_REPO
if "%choice%"=="0" goto EXIT
goto MENU

:INIT_REPO
echo.
echo [+] Initializing Git repository...
git init
if %errorlevel% neq 0 (
    echo [ERROR] Failed to initialize repository
    pause
    goto MENU
)
echo [+] Adding remote origin...
git remote add origin https://github.com/Farhanillahiclass/illi-ai-assistant.git
echo [+] Repository initialized successfully
pause
goto MENU

:ADD_CHANGES
echo.
echo [+] Adding all changes to staging...
git add .
if %errorlevel% neq 0 (
    echo [ERROR] Failed to add changes
    pause
    goto MENU
)
echo [+] Changes added to staging successfully
pause
goto MENU

:COMMIT_CHANGES
echo.
set /p commit_msg="Enter commit message: "
if "%commit_msg%"=="" (
    echo [ERROR] Commit message cannot be empty
    pause
    goto MENU
)
echo [+] Committing changes...
git commit -m "%commit_msg%"
if %errorlevel% neq 0 (
    echo [ERROR] Failed to commit changes
    pause
    goto MENU
)
echo [+] Changes committed successfully
pause
goto MENU

:PUSH_CHANGES
echo.
echo [+] Pushing changes to GitHub...
git push -u origin main
if %errorlevel% neq 0 (
    echo [ERROR] Failed to push changes
    echo [!] Check if you have proper permissions and internet connection
    pause
    goto MENU
)
echo [+] Changes pushed to GitHub successfully
pause
goto MENU

:PULL_CHANGES
echo.
echo [+] Pulling latest changes from GitHub...
git pull origin main
if %errorlevel% neq 0 (
    echo [ERROR] Failed to pull changes
    pause
    goto MENU
)
echo [+] Latest changes pulled successfully
pause
goto MENU

:CHECK_STATUS
echo.
echo [+] Checking repository status...
git status
pause
goto MENU

:VIEW_HISTORY
echo.
echo [+] Viewing commit history...
git log --oneline -10
pause
goto MENU

:CREATE_BRANCH
echo.
set /p branch_name="Enter new branch name: "
if "%branch_name%"=="" (
    echo [ERROR] Branch name cannot be empty
    pause
    goto MENU
)
echo [+] Creating new branch: %branch_name%
git checkout -b %branch_name%
if %errorlevel% neq 0 (
    echo [ERROR] Failed to create branch
    pause
    goto MENU
)
echo [+] Branch created successfully
pause
goto MENU

:SWITCH_BRANCH
echo.
echo [+] Available branches:
git branch
echo.
set /p branch_name="Enter branch name to switch to: "
if "%branch_name%"=="" (
    echo [ERROR] Branch name cannot be empty
    pause
    goto MENU
)
echo [+] Switching to branch: %branch_name%
git checkout %branch_name%
if %errorlevel% neq 0 (
    echo [ERROR] Failed to switch branch
    pause
    goto MENU
)
echo [+] Switched to branch successfully
pause
goto MENU

:MERGE_BRANCHES
echo.
echo [+] Available branches:
git branch
echo.
set /p source_branch="Enter source branch name: "
set /p target_branch="Enter target branch name: "
if "%source_branch%"=="" or "%target_branch%"=="" (
    echo [ERROR] Branch names cannot be empty
    pause
    goto MENU
)
echo [+] Switching to target branch: %target_branch%
git checkout %target_branch%
echo [+] Merging %source_branch% into %target_branch%
git merge %source_branch%
if %errorlevel% neq 0 (
    echo [ERROR] Failed to merge branches
    pause
    goto MENU
)
echo [+] Branches merged successfully
pause
goto MENU

:CLONE_REPO
echo.
set /p clone_path="Enter path to clone repository (or press Enter for current directory): "
if "%clone_path%"=="" set clone_path=%CD%
echo [+] Cloning repository to: %clone_path%
git clone https://github.com/Farhanillahiclass/illi-ai-assistant.git "%clone_path%"
if %errorlevel% neq 0 (
    echo [ERROR] Failed to clone repository
    pause
    goto MENU
)
echo [+] Repository cloned successfully
pause
goto MENU

:CREATE_BACKUP
echo.
echo [+] Creating backup...
set backup_dir=backup_%date:~-4,4%%date:~-7,2%%date:~-10,2%_%time:~0,2%%time:~3,2%
set backup_dir=%backup_dir: =0%
mkdir "%backup_dir%" 2>nul
echo [+] Copying files to backup...
xcopy /E /I /Y * "%backup_dir%" >nul 2>&1
echo [+] Backup created: %backup_dir%
pause
goto MENU

:SYNC_REPO
echo.
echo [+] Syncing repository (Pull + Add + Commit + Push)...
echo [+] Step 1: Pulling latest changes...
git pull origin main
echo [+] Step 2: Adding all changes...
git add .
echo [+] Step 3: Committing changes...
set commit_msg=Auto-sync %date% %time%
git commit -m "%commit_msg%"
echo [+] Step 4: Pushing to GitHub...
git push origin main
if %errorlevel% neq 0 (
    echo [ERROR] Failed to sync repository
    pause
    goto MENU
)
echo [+] Repository synchronized successfully
pause
goto MENU

:VIEW_REMOTE
echo.
echo [+] Viewing remote information...
git remote -v
echo.
echo [+] Viewing remote branches...
git branch -r
pause
goto MENU

:RESET_REPO
echo.
echo [!] WARNING: This will reset the repository to the last commit
echo [!] All uncommitted changes will be lost
set /p confirm="Are you sure you want to continue? (Y/N): "
if /i not "%confirm%"=="Y" goto MENU
echo [+] Resetting repository...
git reset --hard HEAD
echo [+] Repository reset successfully
pause
goto MENU

:EXIT
echo.
echo [+] Thank you for using ILLI AI GitHub Manager!
echo [+] Created by Muhammad Farhan
echo [+] Email: farhanhomeschooling519@gmail.com
pause
exit /b 0
