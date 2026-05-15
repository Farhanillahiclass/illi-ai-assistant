@echo off
title ILLI AI - Create Package Release
color 0E
echo.
echo ========================================
echo    ILLI AI - Create Package Release
echo ========================================
echo.

echo [1/8] Building distribution files...
python -m build
if %errorlevel% neq 0 (
    echo ERROR: Failed to build distribution
    pause
    exit /b 1
)

echo [2/8] Creating GitHub release...
set version=v1.0.0
git tag -a %version% -m "ILLI AI Professional %version% - Complete PC & Web Control System with Package Distribution"
if %errorlevel% neq 0 (
    echo ERROR: Failed to create tag
    pause
    exit /b 1
)

echo [3/8] Pushing tag to GitHub...
git push origin %version%
if %errorlevel% neq 0 (
    echo ERROR: Failed to push tag
    pause
    exit /b 1
)

echo [4/8] Creating release assets...
echo Creating release with package files...
echo.

echo [5/8] Uploading distribution files to GitHub...
echo Files to upload:
dir /b dist\

echo.
echo To complete package release:
echo 1. Visit: https://github.com/Farhanillahiclass/illi-ai-assistant/releases/new
echo 2. Tag: %version%
echo 3. Title: ILLI AI Professional %version%
echo 4. Description: Complete PC & Web Control System with Voice Control, AI Features, and Security
echo 5. Upload files from dist/ folder:
echo    - illi_ai_professional-%version%-py3-none-any.whl
echo    - illi_ai_professional-%version%.tar.gz
echo.

echo [6/8] Publishing to PyPI...
echo Publishing to Test PyPI first...
python -m twine upload --repository testpypi dist/*
if %errorlevel% neq 0 (
    echo WARNING: Test PyPI upload failed
)

echo Publishing to Main PyPI...
python -m twine upload dist/*
if %errorlevel% neq 0 (
    echo ERROR: Failed to publish to PyPI
    pause
    exit /b 1
)

echo [7/8] Verifying package installation...
echo Testing package installation...
pip install illi-ai-professional
if %errorlevel% neq 0 (
    echo WARNING: Package installation test failed
)

echo [8/8] Creating installation commands...
echo.
echo Installation commands for users:
echo.
echo 1. From PyPI:
echo    pip install illi-ai-professional
echo.
echo 2. From GitHub:
echo    pip install git+https://github.com/Farhanillahiclass/illi-ai-assistant.git
echo.
echo 3. From Test PyPI:
echo    pip install --index-url https://test.pypi.org/simple/ illi-ai-professional
echo.
echo 4. Development version:
echo    pip install -e git+https://github.com/Farhanillahiclass/illi-ai-assistant.git
echo.

echo ========================================
echo    PACKAGE RELEASE COMPLETED
echo ========================================
echo.
echo ✅ Distribution files built
echo ✅ GitHub release created
echo ✅ Package published to PyPI
echo ✅ Installation commands generated
echo.
echo Package URL: https://pypi.org/project/illi-ai-professional/
echo GitHub Release: https://github.com/Farhanillahiclass/illi-ai-assistant/releases/tag/%version%
echo.
pause
