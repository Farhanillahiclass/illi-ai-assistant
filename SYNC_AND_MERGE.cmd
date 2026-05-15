@echo off
title ILLI AI - Sync and Merge
color 0B
echo.
echo ========================================
echo    ILLI AI - Sync and Merge
echo ========================================
echo.

echo [1/5] Checking current branch...
for /f "tokens=*" %%i in ('git branch --show-current 2^>nul') do set current_branch=%%i
echo Current branch: %current_branch%

echo [2/5] Fetching latest changes from remote...
git fetch --all
if %errorlevel% neq 0 (
    echo ERROR: Failed to fetch from remote
    pause
    exit /b 1
)

echo [3/5] Pulling latest changes for main branch...
git checkout main
git pull origin main --rebase
if %errorlevel% neq 0 (
    echo WARNING: Pull failed, trying merge...
    git pull origin main --allow-unrelated-histories
)

echo [4/5] Merging %current_branch% into main...
git merge %current_branch% --no-edit --no-ff
if %errorlevel% neq 0 (
    echo CONFLICTS DETECTED - Auto-resolving...
    git merge %current_branch% --no-edit --no-ff --strategy-option=theirs
    if %errorlevel% neq 0 (
        echo ERROR: Cannot auto-resolve conflicts
        pause
        exit /b 1
    )
    echo Conflicts auto-resolved
)

echo [5/5] Pushing main branch to remote...
git push origin main
if %errorlevel% neq 0 (
    echo ERROR: Failed to push main branch
    pause
    exit /b 1
)

echo.
echo ========================================
echo    SYNC AND MERGE COMPLETED
echo ========================================
echo.
echo %current_branch% branch merged into main branch
echo Main branch pushed to remote
echo.
echo Repository: https://github.com/Farhanillahiclass/illi-ai-assistant/tree/main
echo.
echo Current branch status:
git branch -a
echo.
echo Recent commits:
git log --oneline -3
pause
