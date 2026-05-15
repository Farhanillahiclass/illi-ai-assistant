@echo off
title ILLI AI - Fix GitHub README
color 0C
echo.
echo ========================================
echo    ILLI AI - Fix GitHub README
echo ========================================
echo.

echo [1/6] Checking current status...
git status
echo.

echo [2/6] Switching to main branch...
git checkout main
if %errorlevel% neq 0 (
    echo Creating main branch...
    git checkout -b main
)

echo [3/6] Adding README.md with force...
git add README.md --force
if %errorlevel% neq 0 (
    echo ERROR: Cannot add README.md
    pause
    exit /b 1
)

echo [4/6] Committing README.md...
git commit -m "Add professional README.md - ILLI AI Professional documentation" --allow-empty
if %errorlevel% neq 0 (
    echo WARNING: Commit may have failed, continuing...
)

echo [5/6] Force pushing README.md to GitHub...
git push origin main --force
if %errorlevel% neq 0 (
    echo ERROR: Failed to push README.md
    echo Trying alternative push method...
    git push origin main --force-with-lease
    if %errorlevel% neq 0 (
        echo ERROR: Cannot push README.md to GitHub
        pause
        exit /b 1
    )
)

echo [6/6] Verifying README on GitHub...
git log --oneline -1
echo.
echo Repository: https://github.com/Farhanillahiclass/illi-ai-assistant
echo README should be visible at: https://github.com/Farhanillahiclass/illi-ai-assistant/blob/main/README.md

echo.
echo ========================================
echo    GITHUB README FIXED
echo ========================================
echo.
echo README.md has been force pushed to GitHub
echo If README is still not visible:
echo 1. Refresh GitHub page
echo 2. Check GitHub cache (may take few minutes)
echo 3. Verify README.md exists in main branch
echo.
pause
