@echo off
title ILLI AI - Final Package Publisher
color 0E
echo.
echo ========================================
echo    ILLI AI - Final Package Publisher
echo ========================================
echo.

echo [1/6] Cleaning previous builds...
if exist "dist" rmdir /s /q "dist"
if exist "build" rmdir /s /q "build"
if exist "*.egg-info" rmdir /s /q "*.egg-info"

echo [2/6] Building with simple setup...
python setup_simple.py sdist bdist_wheel
if %errorlevel% neq 0 (
    echo ERROR: Failed to build package
    pause
    exit /b 1
)

echo [3/6] Checking build results...
if exist "dist" (
    echo Build successful! Distribution files:
    dir /b dist\
) else (
    echo ERROR: No distribution files created
    pause
    exit /b 1
)

echo [4/6] Testing package installation...
pip install --quiet dist/*.whl
if %errorlevel% neq 0 (
    echo WARNING: Package installation test failed
) else (
    echo Package installation test successful
    pip uninstall -y illi-ai-professional
)

echo [5/6] Publishing to Test PyPI...
python -m twine upload --repository testpypi dist/*
if %errorlevel% neq 0 (
    echo WARNING: Test PyPI upload failed
) else (
    echo Test PyPI upload successful
)

echo [6/6] Publishing to Main PyPI...
python -m twine upload dist/*
if %errorlevel% neq 0 (
    echo WARNING: Main PyPI upload failed
    echo.
    echo To publish manually:
    echo 1. Create PyPI account: https://pypi.org/account/register/
    echo 2. Generate API token: https://pypi.org/manage/account/token/
    echo 3. Configure twine: twine configure
    echo 4. Upload: python -m twine upload dist/*
) else (
    echo Main PyPI upload successful!
)

echo.
echo ========================================
echo    PACKAGE PUBLISHING COMPLETED
echo ========================================
echo.
echo Package URL: https://pypi.org/project/illi-ai-professional/
echo Test Package: https://test.pypi.org/project/illi-ai-professional/
echo.
echo Installation commands:
echo   pip install illi-ai-professional
echo   pip install --index-url https://test.pypi.org/simple/ illi-ai-professional
echo.
pause
