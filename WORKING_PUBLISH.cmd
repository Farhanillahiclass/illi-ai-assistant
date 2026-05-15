@echo off
title ILLI AI - Working Package Publisher
color 0C
echo.
echo ========================================
echo    ILLI AI - Working Package Publisher
echo ========================================
echo.

echo [1/4] Installing required tools...
pip install --upgrade setuptools wheel twine
if %errorlevel% neq 0 (
    echo ERROR: Failed to install tools
    pause
    exit /b 1
)

echo [2/4] Creating package directory structure...
if not exist "illi_ai" mkdir "illi_ai"

echo [3/4] Creating setup.py in package directory...
echo from setuptools import setup > illi_ai\setup.py
echo. >> illi_ai\setup.py
echo setup( >> illi_ai\setup.py
echo     name="illi-ai-professional", >> illi_ai\setup.py
echo     version="1.0.0", >> illi_ai\setup.py
echo     author="Muhammad Farhan", >> illi_ai\setup.py
echo     author_email="farhanhomeschooling519@gmail.com", >> illi_ai\setup.py
echo     description="Complete PC & Web Control System with Voice Control and AI Features", >> illi_ai\setup.py
echo     url="https://github.com/Farhanillahiclass/illi-ai-assistant", >> illi_ai\setup.py
echo     py_modules=["illi_ai"], >> illi_ai\setup.py
echo     install_requires=[ >> illi_ai\setup.py
echo         "psutil>=5.9.0", >> illi_ai\setup.py
echo         "speechrecognition>=3.10.0", >> illi_ai\setup.py
echo         "pyttsx3>=2.90", >> illi_ai\setup.py
echo         "requests>=2.28.0", >> illi_ai\setup.py
echo         "GitPython>=3.1.0", >> illi_ai\setup.py
echo         "cryptography>=3.4.0", >> illi_ai\setup.py
echo         "numpy>=1.21.0" >> illi_ai\setup.py
echo     ], >> illi_ai\setup.py
echo     entry_points={ >> illi_ai\setup.py
echo         "console_scripts": [ >> illi_ai\setup.py
echo             "illi-ai=illi_ai:main", >> illi_ai\setup.py
echo         ], >> illi_ai\setup.py
echo     }, >> illi_ai\setup.py
echo     classifiers=[ >> illi_ai\setup.py
echo         "Development Status :: 5 - Production/Stable", >> illi_ai\setup.py
echo         "Intended Audience :: End Users/Desktop", >> illi_ai\setup.py
echo         "License :: OSI Approved :: MIT License", >> illi_ai\setup.py
echo         "Operating System :: Microsoft :: Windows", >> illi_ai\setup.py
echo         "Programming Language :: Python :: 3", >> illi_ai\setup.py
echo         "Topic :: Desktop Environment", >> illi_ai\setup.py
echo         "Topic :: System :: Monitoring", >> illi_ai\setup.py
echo         "Topic :: Utilities", >> illi_ai\setup.py
echo     ], >> illi_ai\setup.py
echo     python_requires=">=3.7", >> illi_ai\setup.py
echo ) >> illi_ai\setup.py

echo [4/4] Building and publishing package...
cd illi_ai
python setup.py sdist bdist_wheel
if %errorlevel% neq 0 (
    echo ERROR: Failed to build package
    cd ..
    pause
    exit /b 1
)

echo.
echo Package built successfully!
echo Distribution files:
dir /b dist\
echo.

echo Publishing to PyPI...
python -m twine upload dist/*
if %errorlevel% neq 0 (
    echo WARNING: PyPI upload failed
    echo.
    echo To publish manually:
    echo 1. Create PyPI account: https://pypi.org/account/register/
    echo 2. Generate API token: https://pypi.org/manage/account/token/
    echo 3. Configure twine: twine configure
    echo 4. Upload: python -m twine upload dist/*
) else (
    echo Package published successfully!
)

cd ..
echo.
echo ========================================
echo    PACKAGE PUBLISHING COMPLETED
echo ========================================
echo.
echo Package URL: https://pypi.org/project/illi-ai-professional/
echo Installation command:
echo   pip install illi-ai-professional
echo.
pause
