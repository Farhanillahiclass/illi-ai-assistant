#!/usr/bin/env python3
"""
Comprehensive test to identify and fix ILLI AI errors
"""

import sys
import os
import traceback

def main():
    print("ILLI AI Comprehensive Error Detection")
    print("=" * 50)
    
    # Change to correct directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Test 1: Basic file and syntax check
    print("1. File and Syntax Check:")
    try:
        with open('ILLI_AI_SIMPLE_WORKING.py', 'r') as f:
            content = f.read()
        compile(content, 'ILLI_AI_SIMPLE_WORKING.py', 'exec')
        print("   ✓ File exists and syntax is correct")
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False
    
    # Test 2: Import all dependencies
    print("\n2. Dependency Check:")
    deps = {
        'tkinter': 'tkinter',
        'ttk': 'tkinter.ttk',
        'scrolledtext': 'tkinter.scrolledtext',
        'messagebox': 'tkinter.messagebox',
        'filedialog': 'tkinter.filedialog',
        'simpledialog': 'tkinter.simpledialog',
        'psutil': 'psutil',
        'speech_recognition': 'speech_recognition',
        'pyttsx3': 'pyttsx3',
        'webbrowser': 'webbrowser',
        'threading': 'threading',
        'time': 'time',
        'datetime': 'datetime',
        'subprocess': 'subprocess',
        'shutil': 'shutil',
        'platform': 'platform',
        'json': 'json',
        'random': 'random',
        'math': 'math',
        're': 're',
        'pathlib': 'pathlib'
    }
    
    missing_deps = []
    for name, module in deps.items():
        try:
            __import__(module)
            print(f"   ✓ {name}")
        except ImportError as e:
            print(f"   ✗ {name}: {e}")
            missing_deps.append(name)
    
    if missing_deps:
        print(f"\n   Missing dependencies: {missing_deps}")
        print("   Install with: pip install " + " ".join(missing_deps))
        return False
    
    # Test 3: Try to create the GUI environment
    print("\n3. GUI Environment Test:")
    try:
        import tkinter as tk
        from tkinter import ttk, scrolledtext, messagebox, filedialog, simpledialog
        root = tk.Tk()
        root.withdraw()  # Hide it for now
        root.destroy()
        print("   ✓ GUI environment works")
    except Exception as e:
        print(f"   ✗ GUI error: {e}")
        return False
    
    # Test 4: Try to import and instantiate the class
    print("\n4. Class Instantiation Test:")
    try:
        # Import the module
        sys.path.insert(0, '.')
        import ILLI_AI_SIMPLE_WORKING
        
        # Create a minimal root
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()  # Hide initially
        
        # Try to create the app
        app = ILLI_AI_SIMPLE_WORKING.ILLI_AI_Simple_Working(root)
        print("   ✓ Class instantiation successful")
        
        # Clean up
        root.destroy()
        
    except Exception as e:
        print(f"   ✗ Class error: {e}")
        print("   Full traceback:")
        traceback.print_exc()
        return False
    
    # Test 5: Try to run the main function
    print("\n5. Main Function Test:")
    try:
        # We won't actually call main() as it opens GUI
        # Just check if it exists
        if hasattr(ILLI_AI_SIMPLE_WORKING, 'main'):
            print("   ✓ Main function exists")
        else:
            print("   ✗ Main function missing")
            return False
    except Exception as e:
        print(f"   ✗ Main function error: {e}")
        return False
    
    print("\n" + "=" * 50)
    print("✓ ALL TESTS PASSED!")
    print("The ILLI AI application should work correctly.")
    print("\nTo run the application:")
    print("python ILLI_AI_SIMPLE_WORKING.py")
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        input("\nPress Enter to exit...")
    sys.exit(0 if success else 1)
