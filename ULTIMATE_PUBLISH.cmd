@echo off
title ILLI AI - Ultimate Package Publisher
color 0F
echo.
echo ========================================
echo    ILLI AI - Ultimate Package Publisher
echo ========================================
echo.

echo [1/8] Cleaning all previous builds...
if exist "dist" rmdir /s /q "dist"
if exist "build" rmdir /s /q "build"
if exist "*.egg-info" rmdir /s /q "*.egg-info"
if exist "illi_ai" rmdir /s /q "illi_ai"

echo [2/8] Creating minimal package structure...
mkdir "illi_ai"

echo [3/8] Creating simple __init__.py...
(
echo #!/usr/bin/env python3
echo # -*- coding: utf-8 -*-
echo """
echo ILLI AI Professional - Complete PC ^& Web Control System
echo Created by Muhammad Farhan
echo Email: farhanhomeschooling519@gmail.com
echo """
echo.
echo import tkinter as tk
echo from tkinter import ttk
echo import sys
echo import os
echo import subprocess
echo import webbrowser
echo import psutil
echo import platform
echo from datetime import datetime
echo.
echo class ILLIProfessional:
echo     def __init__(self):
echo         self.root = tk.Tk()
echo         self.root.title("ILLI AI Professional")
echo         self.root.geometry("800x600")
echo         
echo         # Create simple GUI
echo         label = ttk.Label(self.root, text="ILLI AI Professional", font=("Arial", 24))
echo         label.pack(pady=50)
echo         
echo         info = ttk.Label(self.root, text="Complete PC ^& Web Control System\nVoice Control, System Monitoring, Security")
echo         info.pack(pady=20)
echo         
echo         button = ttk.Button(self.root, text="Launch ILLI AI", command=self.launch_main_app)
echo         button.pack(pady=20)
echo     
echo     def launch_main_app(self):
echo         try:
echo             # Launch the main ILLI AI application
echo             if os.path.exists("ILLI_AI_PROFESSIONAL_FINAL.py"):
echo                 subprocess.Popen([sys.executable, "ILLI_AI_PROFESSIONAL_FINAL.py"])
echo                 self.root.quit()
echo             else:
echo                 ttk.messagebox.showinfo("Info", "Main application not found. Please install from GitHub.")
echo         except Exception as e:
echo             ttk.messagebox.showerror("Error", f"Failed to launch: {e}")
echo     
echo     def run(self):
echo         self.root.mainloop()
echo.
echo def main():
echo     """Main entry point for package"""
echo     app = ILLIProfessional()
echo     app.run()
echo.
echo if __name__ == "__main__":
echo     main()
) > "illi_ai\__init__.py"

echo [4/8] Creating setup.py...
(
echo from setuptools import setup, find_packages
echo.
echo setup(
echo     name="illi-ai-professional",
echo     version="1.0.0",
echo     author="Muhammad Farhan",
echo     author_email="farhanhomeschooling519@gmail.com",
echo     description="Complete PC ^& Web Control System with Voice Control and AI Features",
echo     long_description="ILLI AI Professional - Complete PC ^& Web Control System with Voice Control, AI Features, and Security",
echo     long_description_content_type="text/plain",
echo     url="https://github.com/Farhanillahiclass/illi-ai-assistant",
echo     packages=["illi_ai"],
echo     classifiers=[
echo         "Development Status :: 5 - Production/Stable",
echo         "Intended Audience :: End Users/Desktop",
echo         "License :: OSI Approved :: MIT License",
echo         "Operating System :: Microsoft :: Windows",
echo         "Programming Language :: Python :: 3",
echo         "Programming Language :: Python :: 3.7",
echo         "Programming Language :: Python :: 3.8",
echo         "Programming Language :: Python :: 3.9",
echo         "Programming Language :: Python :: 3.10",
echo         "Programming Language :: Python :: 3.11",
echo         "Programming Language :: Python :: 3.12",
echo         "Programming Language :: Python :: 3.13",
echo         "Topic :: Desktop Environment",
echo         "Topic :: System :: Monitoring",
echo         "Topic :: Utilities",
echo     ],
echo     python_requires=">=3.7",
echo     install_requires=[
echo         "psutil>=5.9.0",
echo         "speechrecognition>=3.10.0",
echo         "pyttsx3>=2.90",
echo         "requests>=2.28.0",
echo         "GitPython>=3.1.0",
echo         "cryptography>=3.4.0",
echo         "numpy>=1.21.0"
echo     ],
echo     entry_points={
echo         "console_scripts": [
echo             "illi-ai=illi_ai:main",
echo         ],
echo     },
echo     keywords=[
echo         "ai assistant",
echo         "voice control",
echo         "system monitoring",
echo         "pc control",
echo         "web control",
echo         "automation",
echo         "security",
echo         "professional",
echo         "desktop assistant"
echo     ],
echo     project_urls={
echo         "Bug Reports": "https://github.com/Farhanillahiclass/illi-ai-assistant/issues",
echo         "Source": "https://github.com/Farhanillahiclass/illi-ai-assistant",
echo         "Documentation": "https://github.com/Farhanillahiclass/illi-ai-assistant/blob/main/README.md",
echo         "Changelog": "https://github.com/Farhanillahiclass/illi-ai-assistant/releases",
echo     },
echo )
) > "illi_ai\setup.py"

echo [5/8] Building package...
cd illi_ai
python setup.py sdist bdist_wheel
if %errorlevel% neq 0 (
    echo ERROR: Failed to build package
    cd ..
    pause
    exit /b 1
)

echo [6/8] Checking build results...
if exist "dist" (
    echo Build successful! Distribution files:
    dir /b dist\
) else (
    echo ERROR: No distribution files created
    cd ..
    pause
    exit /b 1
)

echo [7/8] Testing package installation...
pip install --quiet dist/*.whl
if %errorlevel% neq 0 (
    echo WARNING: Package installation test failed
) else (
    echo Package installation test successful
    pip uninstall -y illi-ai-professional
)

echo [8/8] Publishing to PyPI...
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
echo    ULTIMATE PACKAGE PUBLISHING COMPLETED
echo ========================================
echo.
echo Package URL: https://pypi.org/project/illi-ai-professional/
echo Installation command:
echo   pip install illi-ai-professional
echo.
pause
