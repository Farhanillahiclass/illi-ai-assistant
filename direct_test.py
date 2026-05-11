#!/usr/bin/env python3
"""
Direct test to run ILLI AI and capture errors
"""

import sys
import os

print("Direct ILLI AI Test")
print("=" * 40)

# Change to script directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

try:
    print("1. Importing required modules...")
    import tkinter as tk
    from tkinter import ttk, scrolledtext, messagebox, filedialog, simpledialog
    import os, webbrowser, psutil, threading, time
    import speech_recognition as sr, pyttsx3
    from datetime import datetime
    import subprocess, shutil, platform, json, random, math, re
    from pathlib import Path
    print("   ✓ All modules imported successfully")
    
    print("2. Creating main window...")
    root = tk.Tk()
    root.title("Test Window")
    root.geometry("400x300")
    print("   ✓ Main window created")
    
    print("3. Importing ILLI AI class...")
    from ILLI_AI_SIMPLE_WORKING import ILLI_AI_Simple_Working
    print("   ✓ ILLI AI class imported")
    
    print("4. Creating ILLI AI instance...")
    app = ILLI_AI_Simple_Working(root)
    print("   ✓ ILLI AI instance created")
    
    print("5. Application is ready!")
    print("   The GUI should now be visible.")
    print("   Close the window to exit.")
    
    # Run the GUI
    root.mainloop()
    
    print("✓ Application closed successfully")
    
except ImportError as e:
    print(f"✗ Import Error: {e}")
    print("\nSolution: Install missing packages:")
    print(f"pip install {str(e).split()[-1]}")
    
except Exception as e:
    print(f"✗ Error: {e}")
    print("\nFull error details:")
    import traceback
    traceback.print_exc()
    
    input("\nPress Enter to exit...")

print("\nTest completed.")
