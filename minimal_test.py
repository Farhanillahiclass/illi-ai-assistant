#!/usr/bin/env python3
"""
Minimal test to identify ILLI AI issues
"""

import sys
import os

def test_basic():
    print("Basic ILLI AI Test")
    print("=" * 30)
    
    # Test 1: Check if file exists and is readable
    if not os.path.exists('ILLI_AI_SIMPLE_WORKING.py'):
        print("✗ File does not exist")
        return False
    
    try:
        with open('ILLI_AI_SIMPLE_WORKING.py', 'r') as f:
            content = f.read()
        print("✓ File readable")
    except Exception as e:
        print(f"✗ File read error: {e}")
        return False
    
    # Test 2: Check syntax
    try:
        compile(content, 'ILLI_AI_SIMPLE_WORKING.py', 'exec')
        print("✓ Syntax OK")
    except SyntaxError as e:
        print(f"✗ Syntax error: {e}")
        return False
    
    # Test 3: Try to import dependencies
    deps = ['tkinter', 'psutil', 'speech_recognition', 'pyttsx3']
    for dep in deps:
        try:
            __import__(dep)
            print(f"✓ {dep}")
        except ImportError as e:
            print(f"✗ {dep} missing: {e}")
            return False
    
    # Test 4: Try to execute the main function
    try:
        # Create a safe execution environment
        exec_globals = {}
        exec(content, exec_globals)
        
        # Check if main function exists
        if 'main' in exec_globals:
            print("✓ main function found")
        else:
            print("✗ main function not found")
            return False
            
        print("✓ Code executes without errors")
        return True
        
    except Exception as e:
        print(f"✗ Runtime error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_basic()
    print("=" * 30)
    if success:
        print("✓ All tests passed")
    else:
        print("✗ Issues found")
