@echo off
title ILLI AI - Simple Package Publisher
color 0A
echo.
echo ========================================
echo    ILLI AI - Simple Package Publisher
echo ========================================
echo.

echo [1/6] Installing required tools...
pip install --upgrade setuptools wheel twine
if %errorlevel% neq 0 (
    echo ERROR: Failed to install tools
    pause
    exit /b 1
)

echo [2/6] Cleaning previous builds...
if exist "dist" rmdir /s /q "dist"
if exist "build" rmdir /s /q "build"
if exist "*.egg-info" rmdir /s /q "*.egg-info"

echo [3/6] Creating package structure...
mkdir "illi_ai" 2>nul

echo [4/6] Creating package files...
echo # ILLI AI Professional Package > "illi_ai\__init__.py"
echo. >> "illi_ai\__init__.py"
echo def main(): >> "illi_ai\__init__.py"
echo     """Main entry point for ILLI AI Professional package""" >> "illi_ai\__init__.py"
echo     print("ILLI AI Professional - Complete PC ^& Web Control System") >> "illi_ai\__init__.py"
echo     print("Features: Voice Control, System Monitoring, Security") >> "illi_ai\__init__.py"
echo     print("Visit: https://github.com/Farhanillahiclass/illi-ai-assistant") >> "illi_ai\__init__.py"
echo. >> "illi_ai\__init__.py"
echo if __name__ == "__main__": >> "illi_ai\__init__.py"
echo     main() >> "illi_ai\__init__.py"

echo from setuptools import setup > "illi_ai\setup.py"
echo setup( >> "illi_ai\setup.py"
echo     name="illi-ai-professional", >> "illi_ai\setup.py"
echo     version="1.0.0", >> "illi_ai\setup.py"
echo     author="Muhammad Farhan", >> "illi_ai\setup.py"
echo     author_email="farhanhomeschooling519@gmail.com", >> "illi_ai\setup.py"
echo     description="Complete PC ^& Web Control System with Voice Control and AI Features", >> "illi_ai\setup.py"
echo     url="https://github.com/Farhanillahiclass/illi-ai-assistant", >> "illi_ai\setup.py"
echo     packages=["illi_ai"], >> "illi_ai\setup.py"
echo     install_requires=[ >> "illi_ai\setup.py"
echo         "psutil>=5.9.0", >> "illi_ai\setup.py"
echo         "speechrecognition>=3.10.0", >> "illi_ai\setup.py"
echo         "pyttsx3>=2.90", >> "illi_ai\setup.py"
echo         "requests>=2.28.0", >> "illi_ai\setup.py"
echo         "GitPython>=3.1.0", >> "illi_ai\setup.py"
echo         "cryptography>=3.4.0", >> "illi_ai\setup.py"
echo         "numpy>=1.21.0" >> "illi_ai\setup.py"
echo     ], >> "illi_ai\setup.py"
echo     entry_points={ >> "illi_ai\setup.py"
echo         "console_scripts": [ >> "illi_ai\setup.py"
echo             "illi-ai=illi_ai:main", >> "illi_ai\setup.py"
echo         ], >> "illi_ai\setup.py"
echo     }, >> "illi_ai\setup.py"
echo     classifiers=[ >> "illi_ai\setup.py"
echo         "Development Status :: 5 - Production/Stable", >> "illi_ai\setup.py"
echo         "Intended Audience :: End Users/Desktop", >> "illi_ai\setup.py"
echo         "License :: OSI Approved :: MIT License", >> "illi_ai\setup.py"
echo         "Operating System :: Microsoft :: Windows", >> "illi_ai\setup.py"
echo         "Programming Language :: Python :: 3", >> "illi_ai\setup.py"
echo         "Programming Language :: Python :: 3.7", >> "illi_ai\setup.py"
echo         "Programming Language :: Python :: 3.8", >> "illi_ai\setup.py"
echo         "Programming Language :: Python :: 3.9", >> "illi_ai\setup.py"
echo         "Programming Language :: Python :: 3.10", >> "illi_ai\setup.py"
echo         "Programming Language :: Python :: 3.11", >> "illi_ai\setup.py"
echo         "Programming Language :: Python :: 3.12", >> "illi_ai\setup.py"
echo         "Programming Language :: Python :: 3.13", >> "illi_ai\setup.py"
echo         "Topic :: Desktop Environment", >> "illi_ai\setup.py"
echo         "Topic :: System :: Monitoring", >> "illi_ai\setup.py"
echo         "Topic :: Utilities", >> "illi_ai\setup.py"
echo     ], >> "illi_ai\setup.py"
echo     python_requires=">=3.7", >> "illi_ai\setup.py"
echo ) >> "illi_ai\setup.py"

echo [5/6] Building package...
cd illi_ai
python setup.py sdist bdist_wheel
if %errorlevel% neq 0 (
    echo ERROR: Failed to build package
    cd ..
    pause
    exit /b 1
)

echo [6/6] Package build completed!
echo.
echo Distribution files created:
dir /b dist\
echo.
echo Package ready for publishing!
echo.
echo To publish to PyPI:
echo   python -m twine upload dist/*
echo.
echo To publish to Test PyPI:
echo   python -m twine upload --repository testpypi dist/*
echo.
pause
