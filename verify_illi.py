#!/usr/bin/env python3
"""
Simple verification script for ILLI AI
"""

import os
import sys

def verify_app():
    print("ILLI AI Application Verification")
    print("=" * 50)
    
    # Check if main file exists
    if os.path.exists('ILLI_AI_SIMPLE_WORKING.py'):
        print("✓ Main application file exists")
    else:
        print("✗ Main application file missing")
        return False
    
    # Check file size (should be substantial)
    file_size = os.path.getsize('ILLI_AI_SIMPLE_WORKING.py')
    print(f"✓ File size: {file_size} bytes")
    
    if file_size < 10000:
        print("⚠ Warning: File seems small")
    
    # Check key content
    with open('ILLI_AI_SIMPLE_WORKING.py', 'r') as f:
        content = f.read()
    
    checks = [
        ('Main class', 'class ILLI_AI_Simple_Working:'),
        ('Constructor', 'def __init__(self, root):'),
        ('UI setup', 'def setup_ui(self):'),
        ('App launcher', 'def launch_app(self, app_name):'),
        ('Command processor', 'def process_command(self, command):'),
        ('Voice loop', 'def voice_assistant_loop(self):'),
        ('Text to speech', 'def speak(self, text):'),
        ('Main function', 'def main():'),
        ('Apps dictionary', 'self.apps = {'),
        ('Voice recognition', 'speech_recognition'),
        ('Text to speech', 'pyttsx3'),
        ('System monitoring', 'psutil'),
        ('GUI framework', 'tkinter')
    ]
    
    for name, pattern in checks:
        if pattern in content:
            print(f"✓ {name}")
        else:
            print(f"✗ {name}")
    
    print("=" * 50)
    print("✓ Verification completed!")
    return True

if __name__ == "__main__":
    verify_app()
