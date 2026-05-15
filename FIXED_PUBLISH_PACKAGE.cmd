@echo off
title ILLI AI - Fixed Package Publisher
color 0B
echo.
echo ========================================
echo    ILLI AI - Fixed Package Publisher
echo ========================================
echo.

echo [1/5] Installing build tools...
pip install --upgrade build setuptools wheel twine
if %errorlevel% neq 0 (
    echo ERROR: Failed to install build tools
    pause
    exit /b 1
)

echo [2/5] Creating simple package structure...
if not exist "illi_ai" mkdir "illi_ai"

echo [3/5] Copying main application...
copy "ILLI_AI_PROFESSIONAL_FINAL.py" "illi_ai\__init__.py"
copy "requirements.txt" "illi_ai\requirements.txt"

echo [4/5] Building simple package...
cd illi_ai
python -c "
import setuptools
setuptools.setup(
    name='illi-ai-professional',
    version='1.0.0',
    author='Muhammad Farhan',
    author_email='farhanhomeschooling519@gmail.com',
    description='Complete PC & Web Control System with Voice Control and AI Features',
    long_description='ILLI AI Professional - Complete PC & Web Control System with Voice Control, AI Features, and Security',
    url='https://github.com/Farhanillahiclass/illi-ai-assistant',
    py_modules=['__init__'],
    install_requires=[
        'psutil>=5.9.0',
        'speechrecognition>=3.10.0', 
        'pyttsx3>=2.90',
        'requests>=2.28.0',
        'GitPython>=3.1.0',
        'cryptography>=3.4.0',
        'numpy>=1.21.0'
    ],
    entry_points={
        'console_scripts': [
            'illi-ai=__init__:main',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Topic :: Desktop Environment',
        'Topic :: Multimedia :: Sound/Audio :: Speech',
        'Topic :: System :: Monitoring',
        'Topic :: Utilities',
    ],
    python_requires='>=3.7',
)
"
if %errorlevel% neq 0 (
    echo ERROR: Failed to build package
    cd ..
    pause
    exit /b 1
)

echo [5/5] Publishing to PyPI...
python -m twine upload dist/*
if %errorlevel% neq 0 (
    echo WARNING: PyPI upload failed
    echo You may need to:
    echo 1. Create PyPI account: https://pypi.org/account/register/
    echo 2. Generate API token: https://pypi.org/manage/account/token/
    echo 3. Configure twine: twine configure
    echo.
    echo Or publish to Test PyPI:
    python -m twine upload --repository testpypi dist/*
)

cd ..
echo.
echo ========================================
echo    PACKAGE PUBLISHING COMPLETED
echo ========================================
echo.
echo Package URL: https://pypi.org/project/illi-ai-professional/
echo.
echo Installation command:
echo   pip install illi-ai-professional
echo.
pause
