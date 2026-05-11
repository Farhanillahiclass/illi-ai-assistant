#!/usr/bin/env python3
"""
Simple test to run ILLI AI and capture exact errors
"""

import sys
import os
import traceback

def test_run():
    print("Running ILLI AI Application Test...")
    print("=" * 50)
    
    # Ensure we're in the right directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    try:
        print("Step 1: Importing all required modules...")
        import tkinter as tk
        from tkinter import ttk, scrolledtext, messagebox, filedialog, simpledialog
        import os, webbrowser, psutil, threading, time
        import speech_recognition as sr, pyttsx3
        from datetime import datetime
        import subprocess, shutil, platform, json, random, math, re
        from pathlib import Path
        print("   ✓ All modules imported successfully")
        
        print("Step 2: Creating main window...")
        root = tk.Tk()
        root.title("ILLI AI - Test Run")
        root.geometry("800x600")
        print("   ✓ Main window created")
        
        print("Step 3: Importing ILLI AI module...")
        # Add current directory to path
        if script_dir not in sys.path:
            sys.path.insert(0, script_dir)
        
        # Import the module
        import ILLI_AI_SIMPLE_WORKING
        print("   ✓ Module imported")
        
        print("Step 4: Creating ILLI AI instance...")
        app = ILLI_AI_SIMPLE_WORKING.ILLI_AI_Simple_Working(root)
        print("   ✓ ILLI AI instance created successfully")
        
        print("Step 5: Application is ready!")
        print("   The GUI should now be visible and functional.")
        print("   You can test all features:")
        print("   - Click 'Start Voice' to enable voice control")
        print("   - Use tabs to access different features")
        print("   - Click buttons to launch applications")
        print("   - Close the window to exit")
        
        # Run the application
        root.mainloop()
        
        print("✓ Application closed successfully")
        return True
        
    except ImportError as e:
        print(f"   ✗ Import Error: {e}")
        print("\nSOLUTION: Install missing packages:")
        print(f"pip install {str(e).split()[-1]}")
        return False
        
    except Exception as e:
        print(f"   ✗ Runtime Error: {e}")
        print("\nFULL ERROR DETAILS:")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_run()
    print("=" * 50)
    if success:
        print("✓ ILLI AI is working perfectly!")
    else:
        print("✗ ILLI AI has issues that need to be fixed")
        input("Press Enter to exit...")
    sys.exit(0 if success else 1)
