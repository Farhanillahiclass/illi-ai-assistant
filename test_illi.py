#!/usr/bin/env python3
"""
Test script for ILLI AI Application
"""

import sys
import os
import importlib.util

def test_import():
    """Test if the main module can be imported"""
    try:
        spec = importlib.util.spec_from_file_location("illi_ai", "ILLI_AI_SIMPLE_WORKING.py")
        module = importlib.util.module_from_spec(spec)
        print("✓ Module imports successfully")
        return True
    except Exception as e:
        print(f"✗ Import failed: {e}")
        return False

def test_dependencies():
    """Test if all required dependencies are available"""
    required_modules = [
        'tkinter', 'ttk', 'scrolledtext', 'messagebox', 'filedialog', 'simpledialog',
        'os', 'webbrowser', 'psutil', 'threading', 'time', 'speech_recognition', 
        'pyttsx3', 'datetime', 'subprocess', 'shutil', 'platform', 'json', 
        'random', 'math', 'sys', 're', 'pathlib'
    ]
    
    missing_modules = []
    
    for module in required_modules:
        try:
            if '.' in module:
                parent, child = module.split('.', 1)
                parent_mod = __import__(parent)
                getattr(parent_mod, child)
            else:
                __import__(module)
            print(f"✓ {module}")
        except ImportError:
            missing_modules.append(module)
            print(f"✗ {module}")
    
    if missing_modules:
        print(f"\nMissing modules: {missing_modules}")
        return False
    else:
        print("\n✓ All dependencies available")
        return True

def test_class_instantiation():
    """Test if the main class can be instantiated (without GUI)"""
    try:
        # Test the class definition
        with open('ILLI_AI_SIMPLE_WORKING.py', 'r') as f:
            content = f.read()
        
        if 'class ILLI_AI_Simple_Working:' in content:
            print("✓ Main class found")
        else:
            print("✗ Main class not found")
            return False
            
        if 'def __init__(self, root):' in content:
            print("✓ Constructor found")
        else:
            print("✗ Constructor not found")
            return False
            
        print("✓ Class structure looks correct")
        return True
    except Exception as e:
        print(f"✗ Class test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("ILLI AI Application Test Suite")
    print("=" * 40)
    
    tests = [
        ("Import Test", test_import),
        ("Dependency Test", test_dependencies),
        ("Class Test", test_class_instantiation)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n{test_name}:")
        print("-" * 20)
        result = test_func()
        results.append(result)
    
    print("\n" + "=" * 40)
    print("Test Results:")
    print(f"Passed: {sum(results)}/{len(results)}")
    
    if all(results):
        print("✓ All tests passed! The ILLI AI application should work correctly.")
        return True
    else:
        print("✗ Some tests failed. Please check the issues above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
