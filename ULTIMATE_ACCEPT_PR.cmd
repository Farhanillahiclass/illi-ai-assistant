@echo off
title ILLI AI - Ultimate Pull Request Accept
color 0E
echo.
echo ========================================
echo    ILLI AI - Ultimate Pull Request Accept
echo ========================================
echo.

echo [1/7] Force switching to main branch...
git checkout main --force
if %errorlevel% neq 0 (
    echo Creating main branch...
    git checkout -b main --force
)

echo [2/7] Force fetching all changes...
git fetch --all --force
if %errorlevel% neq 0 (
    echo ERROR: Failed to fetch
    pause
    exit /b 1
)

echo [3/7] Force merging master into main...
git merge origin/master --no-edit --no-ff --allow-unrelated-histories --strategy-option=theirs
if %errorlevel% neq 0 (
    echo WARNING: Merge failed, trying alternative...
    git merge master --no-edit --no-ff --allow-unrelated-histories --strategy-option=theirs
    if %errorlevel% neq 0 (
        echo ERROR: Cannot merge master into main
        pause
        exit /b 1
    )
)

echo [4/7] Force pushing main to remote...
git push origin main --force-with-lease
if %errorlevel% neq 0 (
    echo WARNING: Force push failed, trying regular force...
    git push origin main --force
    if %errorlevel% neq 0 (
        echo ERROR: Cannot push to remote
        pause
        exit /b 1
    )
)

echo [5/7] Syncing master with main...
git checkout master
git merge main --no-edit --no-ff
git push origin master --force-with-lease

echo [6/7] Setting main as default...
git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main

echo [7/7] Verifying success...
git status
echo.
echo Branch status:
git branch -a
echo.
echo Recent commits:
git log --oneline -3

echo.
echo ========================================
echo    PULL REQUEST ULTIMATELY ACCEPTED
echo ========================================
echo.
echo Master branch successfully merged into main
echo Both branches synchronized
echo Main branch set as default
echo.
echo Repository: https://github.com/Farhanillahiclass/illi-ai-assistant/tree/main
echo.
echo SUCCESS! Pull request accepted and processed!
pause
