@echo off
title ILLI AI - Fork Repository
color 0B
echo.
echo ========================================
echo    ILLI AI - Fork Repository
echo ========================================
echo.

echo [1/6] Setting up Git configuration...
git config user.name "Muhammad Farhan"
git config user.email "farhanhomeschooling519@gmail.com"

echo [2/6] Adding remote for fork...
git remote add fork https://github.com/Farhanillahiclass/illi-ai-assistant.git
if %errorlevel% neq 0 (
    echo Fork remote already exists, continuing...
)

echo [3/6] Fetching from original repository...
git fetch origin
git fetch fork

echo [4/6] Creating fork branch if not exists...
git show-ref --verify --quiet refs/heads/fork-main
if %errorlevel% neq 0 (
    echo Creating fork-main branch...
    git checkout -b fork-main origin/main
) else (
    echo Switching to fork-main branch...
    git checkout fork-main
)

echo [5/6] Syncing fork with original...
git pull origin main
git push fork fork-main

echo [6/6] Setting up fork tracking...
git branch --set-upstream-to=fork/fork-main fork-main

echo.
echo ========================================
echo    FORK COMPLETED SUCCESSFULLY
echo ========================================
echo.
echo Original Repository: https://github.com/Farhanillahiclass/illi-ai-assistant
echo Fork Repository: https://github.com/Farhanillahiclass/illi-ai-assistant
echo.
echo Fork branch: fork-main
echo Original branch: main
echo.
echo To sync fork with original:
echo   git checkout fork-main
echo   git pull origin main
echo   git push fork fork-main
echo.
pause
