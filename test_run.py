#!/usr/bin/env python3
"""
Test runner to capture ILLI AI errors
"""

import sys
import os
import traceback

def test_app():
    print("Testing ILLI AI Application...")
    print("=" * 50)
    
    # Change to the correct directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    try:
        print("Step 1: Importing modules...")
        import tkinter as tk
        from tkinter import ttk, scrolledtext, messagebox, filedialog, simpledialog
        import os, webbrowser, psutil, threading, time
        import speech_recognition as sr, pyttsx3
        from datetime import datetime
        import subprocess, shutil, platform, json, random, math, re
        from pathlib import Path
        print("   ✓ All modules imported")
        
        print("Step 2: Reading application file...")
        with open('ILLI_AI_SIMPLE_WORKING.py', 'r') as f:
            app_code = f.read()
        print("   ✓ Application file read")
        
        print("Step 3: Compiling application...")
        compile(app_code, 'ILLI_AI_SIMPLE_WORKING.py', 'exec')
        print("   ✓ Application compiles successfully")
        
        print("Step 4: Creating GUI environment...")
        root = tk.Tk()
        root.withdraw()  # Hide the window initially
        print("   ✓ GUI environment created")
        
        print("Step 5: Executing application...")
        exec_globals = {
            '__name__': '__main__',
            'tk': tk, 'ttk': ttk, 'scrolledtext': scrolledtext,
            'messagebox': messagebox, 'filedialog': filedialog, 'simpledialog': simpledialog,
            'os': os, 'webbrowser': webbrowser, 'psutil': psutil, 'threading': threading,
            'time': time, 'sr': sr, 'pyttsx3': pyttsx3, 'datetime': datetime,
            'subprocess': subprocess, 'shutil': shutil, 'platform': platform,
            'json': json, 'random': random, 'math': math, 'sys': sys, 're': re,
            'Path': Path
        }
        
        exec(app_code, exec_globals)
        print("   ✓ Application executed successfully")
        
        root.destroy()
        return True
        
    except ImportError as e:
        print(f"   ✗ Import Error: {e}")
        print("   Solution: Install missing package with pip")
        return False
        
    except SyntaxError as e:
        print(f"   ✗ Syntax Error: {e}")
        print(f"   Line {e.lineno}: {e.text}")
        return False
        
    except Exception as e:
        print(f"   ✗ Runtime Error: {e}")
        print("   Full traceback:")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_app()
    print("=" * 50)
    if success:
        print("✓ Application test completed successfully!")
    else:
        print("✗ Application test failed!")
        input("Press Enter to exit...")
    sys.exit(0 if success else 1)
