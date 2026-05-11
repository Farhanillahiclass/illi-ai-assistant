#!/usr/bin/env python3
"""
Safe runner for ILLI AI with error capture
"""

import sys
import traceback
import os

def main():
    print("ILLI AI Safe Runner")
    print("=" * 40)
    
    # Change to the correct directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    try:
        print("1. Testing basic imports...")
        import tkinter as tk
        from tkinter import ttk, scrolledtext, messagebox, filedialog, simpledialog
        import os, webbrowser, psutil, threading, time
        import speech_recognition as sr, pyttsx3
        from datetime import datetime
        import subprocess, shutil, platform, json, random, math, re
        from pathlib import Path
        print("   ✓ All imports successful")
        
        print("2. Testing application import...")
        # Import the main application
        from ILLI_AI_SIMPLE_WORKING import ILLI_AI_Simple_Working
        print("   ✓ Application class imported")
        
        print("3. Testing class instantiation...")
        # Create root window
        root = tk.Tk()
        print("   ✓ Root window created")
        
        # Create application instance
        app = ILLI_AI_Simple_Working(root)
        print("   ✓ Application instance created")
        
        print("4. Starting GUI...")
        print("   ✓ Application ready - GUI will open now")
        print("   Close the window to exit")
        
        # Start the GUI
        root.mainloop()
        
    except ImportError as e:
        print(f"✗ Import Error: {e}")
        print("   Please install missing packages:")
        print(f"   pip install {str(e).split()[-1]}")
        return False
        
    except Exception as e:
        print(f"✗ Runtime Error: {e}")
        print("\nFull traceback:")
        traceback.print_exc()
        return False
    
    print("✓ Application closed successfully")
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        input("\nPress Enter to exit...")
    sys.exit(0 if success else 1)
