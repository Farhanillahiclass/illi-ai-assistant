@echo off
title ILLI AI - Accept Pull Request
color 0E
echo.
echo ========================================
echo    ILLI AI - Accept Pull Request
echo ========================================
echo.

echo [1/4] Fetching latest changes...
git fetch --all
if %errorlevel% neq 0 (
    echo ERROR: Failed to fetch from remote
    pause
    exit /b 1
)

echo [2/4] Switching to main branch...
git checkout main
if %errorlevel% neq 0 (
    echo ERROR: Failed to switch to main branch
    pause
    exit /b 1
)

echo [3/4] Pulling latest changes...
git pull origin main
if %errorlevel% neq 0 (
    echo WARNING: Pull failed, continuing anyway
)

echo [4/4] Merging any changes...
git merge master --no-edit
if %errorlevel% neq 0 (
    echo WARNING: Merge conflicts, forcing...
    git merge master --no-edit --strategy-option=theirs
)

echo [5/4] Pushing to remote...
git push origin main
if %errorlevel% neq 0 (
    echo ERROR: Failed to push to remote
    pause
    exit /b 1
)

echo.
echo ========================================
echo    PULL REQUEST ACCEPTED
echo ========================================
echo.
echo Repository: https://github.com/Farhanillahiclass/illi-ai-assistant/tree/main
echo.
pause
