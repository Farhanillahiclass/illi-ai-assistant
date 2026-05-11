@echo off
title ILLI AI - Manual Process Handler
color 0A
echo.
echo ========================================
echo    ILLI AI - Manual Process Handler
echo ========================================
echo.

:MENU
echo.
echo    SELECT PROCESS OPERATION
echo ========================================
echo.
echo 1. Check Repository Status
echo 2. Accept Pull Request (Safe)
echo 3. Accept Pull Request (Force)
echo 4. Accept Pull Request (Ultimate)
echo 5. Create Fork
echo 6. Sync Repository
echo 7. Push Latest Changes
echo 8. Clean Up Repository
echo 9. Run ILLI AI
echo 10. Test System
echo 11. Show All Commands
echo 0. Exit
echo.
set /p choice="Enter your choice (0-11): "

if "%choice%"=="1" goto CHECK_STATUS
if "%choice%"=="2" goto SAFE_PR
if "%choice%"=="3" goto FORCE_PR
if "%choice%"=="4" goto ULTIMATE_PR
if "%choice%"=="5" goto FORK
if "%choice%"=="6" goto SYNC
if "%choice%"=="7" goto PUSH
if "%choice%"=="8" goto CLEANUP
if "%choice%"=="9" goto RUN_ILLI
if "%choice%"=="10" goto TEST
if "%choice%"=="11" goto SHOW_COMMANDS
if "%choice%"=="0" goto EXIT
goto MENU

:CHECK_STATUS
echo.
echo Checking repository status...
git status
git branch -a
echo.
pause
goto MENU

:SAFE_PR
echo.
echo Safe Pull Request Acceptance...
call ACCEPT_PR.cmd
pause
goto MENU

:FORCE_PR
echo.
echo Force Pull Request Acceptance...
call FORCE_ACCEPT_PR.cmd
pause
goto MENU

:ULTIMATE_PR
echo.
echo Ultimate Pull Request Acceptance...
call ULTIMATE_ACCEPT_PR.cmd
pause
goto MENU

:FORK
echo.
echo Creating Repository Fork...
call FORK_REPOSITORY.cmd
pause
goto MENU

:SYNC
echo.
echo Syncing Repository...
call SYNC_AND_MERGE.cmd
pause
goto MENU

:PUSH
echo.
echo Pushing Latest Changes...
call PUSH_LATEST.cmd
pause
goto MENU

:CLEANUP
echo.
echo Cleaning Up Repository...
call CLEANUP_GITHUB.cmd
pause
goto MENU

:RUN_ILLI
echo.
echo Running ILLI AI...
call RUN_ILLI.cmd
pause
goto MENU

:TEST
echo.
echo Testing System...
python TEST_ILLI_PROFESSIONAL.py
pause
goto MENU

:SHOW_COMMANDS
echo.
echo ========================================
echo    AVAILABLE COMMANDS
echo ========================================
echo.
echo Repository Management:
echo   - CHECK_STATUS     : Check git status and branches
echo   - SAFE_PR          : Safe pull request acceptance
echo   - FORCE_PR         : Force pull request acceptance
echo   - ULTIMATE_PR      : Ultimate pull request acceptance
echo   - FORK             : Create repository fork
echo   - SYNC             : Sync repository with remote
echo   - PUSH             : Push latest changes
echo   - CLEANUP          : Clean up repository
echo.
echo Application:
echo   - RUN_ILLI         : Run ILLI AI with checks
echo   - TEST             : Test system functionality
echo.
echo Quick Access:
echo   - START_ILLI.cmd   : Quick start ILLI AI
echo   - RUN_ILLI.cmd     : Safe run ILLI AI
echo   - QUICK_PUSH.cmd    : Quick GitHub push
echo   - ULTIMATE_ACCEPT_PR.cmd : Ultimate PR acceptance
echo.
echo Manual Commands:
echo   git status         : Show repository status
echo   git branch -a      : Show all branches
echo   git checkout main    : Switch to main branch
echo   git pull origin main : Pull latest changes
echo   git push origin main : Push changes to main
echo   git merge master    : Merge master into current branch
echo   git add .          : Add all changes
echo   git commit -m "msg" : Commit with message
echo.
pause
goto MENU

:EXIT
echo.
echo Thank you for using ILLI AI Manual Process Handler!
echo.
echo Repository: https://github.com/Farhanillahiclass/illi-ai-assistant
echo Creator: Muhammad Farhan
echo Email: farhanhomeschooling519@gmail.com
echo.
pause
exit /b 0
