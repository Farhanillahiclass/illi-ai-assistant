@echo off
title ILLI AI - Publish Package
color 0B
echo.
echo ========================================
echo    ILLI AI - Publish Package
echo ========================================
echo.

echo [1/6] Installing build tools...
pip install --upgrade build setuptools wheel twine
if %errorlevel% neq 0 (
    echo ERROR: Failed to install build tools
    pause
    exit /b 1
)

echo [2/6] Building package...
python -m build
if %errorlevel% neq 0 (
    echo ERROR: Failed to build package
    pause
    exit /b 1
)

echo [3/6] Checking package...
python -m twine check dist/*
if %errorlevel% neq 0 (
    echo WARNING: Package check failed, continuing...
)

echo [4/6] Creating PyPI account info...
echo.
echo To publish to PyPI, you need:
echo 1. PyPI account: https://pypi.org/account/register/
echo 2. API Token: https://pypi.org/manage/account/token/
echo.
echo If you have API token, press any key to continue...
pause

echo [5/6] Publishing to Test PyPI...
python -m twine upload --repository testpypi dist/*
if %errorlevel% neq 0 (
    echo WARNING: Test PyPI upload failed, trying main PyPI...
    goto MAIN_PYPI
)

echo [6/6] Publishing to Main PyPI...
:MAIN_PYPI
python -m twine upload dist/*
if %errorlevel% neq 0 (
    echo ERROR: Failed to publish to PyPI
    echo.
    echo Possible solutions:
    echo 1. Check your PyPI credentials
    echo 2. Verify package name is available
    echo 3. Check internet connection
    pause
    exit /b 1
)

echo.
echo ========================================
echo    PACKAGE PUBLISHED SUCCESSFULLY
echo ========================================
echo.
echo Package URL: https://pypi.org/project/illi-ai-professional/
echo Test Package: https://test.pypi.org/project/illi-ai-professional/
echo.
echo Installation command:
echo   pip install illi-ai-professional
echo.
echo To install from GitHub:
echo   pip install git+https://github.com/Farhanillahiclass/illi-ai-assistant.git
echo.
pause
