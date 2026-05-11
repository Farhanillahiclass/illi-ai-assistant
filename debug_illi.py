#!/usr/bin/env python3
"""
Debug script to identify all issues in ILLI AI
"""

import sys
import traceback
import importlib.util

def test_imports():
    """Test all required imports"""
    print("Testing imports...")
    try:
        import tkinter as tk
        from tkinter import ttk, scrolledtext, messagebox, filedialog, simpledialog
        print("✓ tkinter imports OK")
    except ImportError as e:
        print(f"✗ tkinter error: {e}")
        return False
    
    try:
        import os
        import webbrowser
        import psutil
        import threading
        import time
        import speech_recognition as sr
        import pyttsx3
        from datetime import datetime
        import subprocess
        import shutil
        import platform
        import json
        import random
        import math
        import sys
        import re
        from pathlib import Path
        print("✓ All standard imports OK")
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False
    
    return True

def test_class_structure():
    """Test class structure"""
    print("\nTesting class structure...")
    try:
        with open('ILLI_AI_SIMPLE_WORKING.py', 'r') as f:
            content = f.read()
        
        # Check for syntax errors
        try:
            compile(content, 'ILLI_AI_SIMPLE_WORKING.py', 'exec')
            print("✓ No syntax errors")
        except SyntaxError as e:
            print(f"✗ Syntax error: {e}")
            return False
        
        # Check for required methods
        required_methods = [
            '__init__',
            'setup_ui',
            'get_user_app_paths',
            'launch_app',
            'process_command',
            'voice_assistant_loop',
            'speak',
            'main'
        ]
        
        for method in required_methods:
            if f'def {method}(' in content:
                print(f"✓ Method {method} found")
            else:
                print(f"✗ Method {method} missing")
                return False
        
        return True
    except Exception as e:
        print(f"✗ Structure test error: {e}")
        return False

def test_class_instantiation():
    """Test class instantiation without GUI"""
    print("\nTesting class instantiation...")
    try:
        # Import the module
        spec = importlib.util.spec_from_file_location("illi_ai", "ILLI_AI_SIMPLE_WORKING.py")
        module = importlib.util.module_from_spec(spec)
        
        # Create a mock root to avoid GUI
        class MockRoot:
            def __init__(self):
                self.title = lambda x: None
                self.geometry = lambda x: None
                self.configure = lambda **kwargs: None
        
        # Try to create the class
        sys.modules['tkinter'] = type('MockTkinter', (), {
            'Tk': MockRoot,
            'Frame': object,
            'Label': object,
            'Button': object,
            'Entry': object,
            'Text': object,
            'ScrolledText': object,
            'Notebook': object,
            'ttk': type('MockTtk', (), {'Notebook': object})(),
            'scrolledtext': type('MockScrolled', (), {'ScrolledText': object})(),
            'messagebox': type('MockMsg', (), {'showinfo': lambda *args: None, 'askyesno': lambda *args: True})(),
            'filedialog': type('MockFile', (), {'asksaveasfilename': lambda **kwargs: '', 'askopenfilename': lambda **kwargs: '', 'askdirectory': lambda **kwargs: ''})(),
            'simpledialog': type('MockSimple', (), {'askstring': lambda *args: ''})(),
            'END': 'end',
            'BOTH': 'both',
            'X': 'x',
            'LEFT': 'left',
            'RIGHT': 'right',
            'BOTTOM': 'bottom'
        })()
        
        spec.loader.exec_module(module)
        
        # Test basic class creation
        mock_root = MockRoot()
        app = module.ILLI_AI_Simple_Working(mock_root)
        print("✓ Class instantiation successful")
        
        return True
    except Exception as e:
        print(f"✗ Instantiation error: {e}")
        traceback.print_exc()
        return False

def main():
    """Run all tests"""
    print("ILLI AI Debug Test Suite")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_class_structure,
        test_class_instantiation
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"✗ Test failed: {e}")
            results.append(False)
    
    print("\n" + "=" * 50)
    print(f"Results: {sum(results)}/{len(results)} tests passed")
    
    if all(results):
        print("✓ All tests passed!")
    else:
        print("✗ Some tests failed - issues detected")
    
    return all(results)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
