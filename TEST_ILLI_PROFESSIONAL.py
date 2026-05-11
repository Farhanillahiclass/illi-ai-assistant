#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ILLI AI Professional - Comprehensive Test Suite
Created by Muhammad Farhan
Email: farhanhomeschooling519@gmail.com

This script tests all major features of ILLI AI Professional
"""

import sys
import os
import time
import psutil
import platform
import subprocess
import threading
from datetime import datetime

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test all required imports"""
    print("🔍 Testing Imports...")
    
    tests = [
        ("tkinter", "GUI Framework"),
        ("psutil", "System Monitoring"),
        ("speech_recognition", "Voice Recognition"),
        ("pyttsx3", "Text-to-Speech"),
        ("requests", "HTTP Requests"),
        ("git", "Git Operations"),
        ("hashlib", "Security Hashing"),
        ("base64", "Base64 Encoding"),
        ("json", "JSON Processing"),
        ("threading", "Threading"),
        ("subprocess", "System Commands"),
        ("platform", "Platform Detection"),
        ("pathlib", "Path Operations"),
        ("logging", "Logging"),
        ("re", "Regular Expressions"),
        ("math", "Math Operations"),
        ("random", "Random Generation"),
        ("time", "Time Operations"),
        ("datetime", "Date/Time")
    ]
    
    passed = 0
    failed = 0
    
    for module, description in tests:
        try:
            __import__(module)
            print(f"  ✅ {module} - {description}")
            passed += 1
        except ImportError as e:
            print(f"  ❌ {module} - {description} - ERROR: {e}")
            failed += 1
    
    print(f"\n📊 Import Tests: {passed} passed, {failed} failed")
    return failed == 0

def test_system_requirements():
    """Test system requirements"""
    print("\n🔍 Testing System Requirements...")
    
    # Test Python version
    python_version = sys.version_info
    if python_version >= (3, 7):
        print(f"  ✅ Python Version: {python_version.major}.{python_version.minor}.{python_version.micro}")
    else:
        print(f"  ❌ Python Version: {python_version.major}.{python_version.minor}.{python_version.micro} (Requires 3.7+)")
        return False
    
    # Test system resources
    memory = psutil.virtual_memory()
    if memory.total >= 4 * 1024**3:  # 4GB
        print(f"  ✅ RAM: {memory.total / (1024**3):.1f} GB")
    else:
        print(f"  ⚠️  RAM: {memory.total / (1024**3):.1f} GB (Recommended: 4GB+)")
    
    # Test disk space
    disk = psutil.disk_usage('/')
    if disk.free >= 500 * 1024**2:  # 500MB
        print(f"  ✅ Disk Space: {disk.free / (1024**3):.1f} GB free")
    else:
        print(f"  ❌ Disk Space: {disk.free / (1024**3):.1f} GB free (Requires 500MB+)")
        return False
    
    # Test platform
    print(f"  ✅ Platform: {platform.system()} {platform.release()}")
    
    return True

def test_voice_system():
    """Test voice system components"""
    print("\n🔍 Testing Voice System...")
    
    try:
        import speech_recognition as sr
        recognizer = sr.Recognizer()
        print("  ✅ Speech Recognition initialized")
        
        # Test microphone availability
        try:
            mic = sr.Microphone()
            print("  ✅ Microphone available")
        except:
            print("  ⚠️  Microphone not available (Voice commands may not work)")
        
        # Test TTS
        try:
            import pyttsx3
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            print(f"  ✅ Text-to-Speech initialized ({len(voices)} voices available)")
        except Exception as e:
            print(f"  ❌ Text-to-Speech failed: {e}")
            return False
        
        return True
        
    except Exception as e:
        print(f"  ❌ Voice system failed: {e}")
        return False

def test_system_monitoring():
    """Test system monitoring capabilities"""
    print("\n🔍 Testing System Monitoring...")
    
    try:
        # Test CPU monitoring
        cpu_percent = psutil.cpu_percent(interval=1)
        print(f"  ✅ CPU Monitoring: {cpu_percent}%")
        
        # Test memory monitoring
        memory = psutil.virtual_memory()
        print(f"  ✅ Memory Monitoring: {memory.percent}% ({memory.available / (1024**3):.1f} GB available)")
        
        # Test disk monitoring
        disk = psutil.disk_usage('/')
        print(f"  ✅ Disk Monitoring: {disk.percent}% used")
        
        # Test process monitoring
        processes = list(psutil.process_iter())
        print(f"  ✅ Process Monitoring: {len(processes)} processes detected")
        
        # Test network monitoring
        try:
            network = psutil.net_io_counters()
            print(f"  ✅ Network Monitoring: {network.bytes_sent / (1024**2):.1f} MB sent, {network.bytes_recv / (1024**2):.1f} MB received")
        except:
            print("  ⚠️  Network monitoring not available")
        
        return True
        
    except Exception as e:
        print(f"  ❌ System monitoring failed: {e}")
        return False

def test_security_features():
    """Test security features"""
    print("\n🔍 Testing Security Features...")
    
    try:
        # Test encryption
        from cryptography.fernet import Fernet
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        
        test_data = "Hello, ILLI AI!"
        encrypted_data = cipher_suite.encrypt(test_data.encode())
        decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
        
        if test_data == decrypted_data:
            print("  ✅ Encryption/Decryption working")
        else:
            print("  ❌ Encryption/Decryption failed")
            return False
        
        # Test hashing
        import hashlib
        hash_value = hashlib.sha256(test_data.encode()).hexdigest()
        print(f"  ✅ Hash generation working ({hash_value[:16]}...)")
        
        # Test base64 encoding
        import base64
        encoded = base64.b64encode(test_data.encode()).decode()
        decoded = base64.b64decode(encoded).decode()
        
        if test_data == decoded:
            print("  ✅ Base64 encoding/decoding working")
        else:
            print("  ❌ Base64 encoding/decoding failed")
            return False
        
        return True
        
    except Exception as e:
        print(f"  ❌ Security features failed: {e}")
        return False

def test_git_integration():
    """Test Git integration"""
    print("\n🔍 Testing Git Integration...")
    
    try:
        import git
        
        # Check if we're in a git repository
        try:
            repo = git.Repo(os.getcwd())
            print(f"  ✅ Git repository detected: {repo.remotes.origin.url}")
            
            # Test git status
            is_dirty = repo.is_dirty()
            print(f"  ✅ Git status working (dirty: {is_dirty})")
            
            # Test branch info
            current_branch = repo.active_branch.name
            print(f"  ✅ Branch detection working: {current_branch}")
            
            return True
            
        except git.InvalidGitRepositoryError:
            print("  ⚠️  Not in a Git repository (Git features limited)")
            return True  # Not a failure, just limited functionality
        
    except ImportError:
        print("  ❌ GitPython not installed")
        return False
    except Exception as e:
        print(f"  ❌ Git integration failed: {e}")
        return False

def test_application_detection():
    """Test application detection"""
    print("\n🔍 Testing Application Detection...")
    
    try:
        # Test common applications
        common_apps = [
            'chrome.exe',
            'firefox.exe',
            'msedge.exe',
            'explorer.exe',
            'notepad.exe',
            'calc.exe',
            'cmd.exe'
        ]
        
        detected_apps = []
        running_processes = list(psutil.process_iter(['name']))
        
        for proc in running_processes:
            try:
                proc_name = proc.info['name'].lower()
                if proc_name in common_apps:
                    detected_apps.append(proc_name)
            except:
                continue
        
        print(f"  ✅ Process detection working ({len(detected_apps)} common apps detected)")
        
        # Test installed applications (Windows only)
        if platform.system() == 'Windows':
            try:
                import winreg
                app_count = 0
                
                registry_paths = [
                    r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
                    r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
                ]
                
                for registry_path in registry_paths:
                    try:
                        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, registry_path) as key:
                            app_count += winreg.QueryInfoKey(key)[0]
                    except:
                        continue
                
                print(f"  ✅ Installed apps detection working ({app_count} apps found)")
                
            except Exception as e:
                print(f"  ⚠️  Registry access limited: {e}")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Application detection failed: {e}")
        return False

def test_file_operations():
    """Test file operations"""
    print("\n🔍 Testing File Operations...")
    
    try:
        # Test file creation
        test_file = "test_illi_ai_temp.txt"
        with open(test_file, 'w') as f:
            f.write("ILLI AI Professional Test File")
        print("  ✅ File creation working")
        
        # Test file reading
        with open(test_file, 'r') as f:
            content = f.read()
        if content == "ILLI AI Professional Test File":
            print("  ✅ File reading working")
        else:
            print("  ❌ File reading failed")
            return False
        
        # Test file operations
        import shutil
        test_file_copy = "test_illi_ai_temp_copy.txt"
        shutil.copy2(test_file, test_file_copy)
        print("  ✅ File copying working")
        
        # Test directory operations
        test_dir = "test_illi_ai_temp_dir"
        os.makedirs(test_dir, exist_ok=True)
        print("  ✅ Directory creation working")
        
        # Cleanup
        os.remove(test_file)
        os.remove(test_file_copy)
        shutil.rmtree(test_dir)
        print("  ✅ File cleanup working")
        
        return True
        
    except Exception as e:
        print(f"  ❌ File operations failed: {e}")
        return False

def test_network_connectivity():
    """Test network connectivity"""
    print("\n🔍 Testing Network Connectivity...")
    
    try:
        import requests
        
        # Test basic HTTP request
        try:
            response = requests.get('https://www.google.com', timeout=5)
            if response.status_code == 200:
                print("  ✅ Internet connectivity working")
            else:
                print(f"  ⚠️  Internet connectivity limited (Status: {response.status_code})")
        except requests.exceptions.RequestException:
            print("  ⚠️  No internet connectivity (offline mode)")
        
        # Test DNS resolution
        try:
            import socket
            socket.gethostbyname('github.com')
            print("  ✅ DNS resolution working")
        except:
            print("  ⚠️  DNS resolution limited")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Network connectivity test failed: {e}")
        return False

def test_gui_components():
    """Test GUI components"""
    print("\n🔍 Testing GUI Components...")
    
    try:
        import tkinter as tk
        
        # Test basic GUI creation
        root = tk.Tk()
        root.withdraw()  # Hide the window
        
        # Test widgets
        label = tk.Label(root, text="Test")
        button = tk.Button(root, text="Test")
        entry = tk.Entry(root)
        text = tk.Text(root)
        
        print("  ✅ Basic widgets working")
        
        # Test styling
        style = tk.ttk.Style()
        style.theme_use('default')
        print("  ✅ Style system working")
        
        # Test notebook
        notebook = tk.ttk.Notebook(root)
        print("  ✅ Notebook widget working")
        
        root.destroy()
        print("  ✅ GUI cleanup working")
        
        return True
        
    except Exception as e:
        print(f"  ❌ GUI components failed: {e}")
        return False

def run_comprehensive_test():
    """Run comprehensive test suite"""
    print("🚀 ILLI AI Professional - Comprehensive Test Suite")
    print("=" * 60)
    print(f"📅 Test Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🖥️  System: {platform.system()} {platform.release()}")
    print(f"🐍 Python: {sys.version}")
    print("=" * 60)
    
    # Run all tests
    tests = [
        ("Import Tests", test_imports),
        ("System Requirements", test_system_requirements),
        ("Voice System", test_voice_system),
        ("System Monitoring", test_system_monitoring),
        ("Security Features", test_security_features),
        ("Git Integration", test_git_integration),
        ("Application Detection", test_application_detection),
        ("File Operations", test_file_operations),
        ("Network Connectivity", test_network_connectivity),
        ("GUI Components", test_gui_components)
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        try:
            if test_func():
                passed += 1
                print(f"✅ {test_name}: PASSED")
            else:
                failed += 1
                print(f"❌ {test_name}: FAILED")
        except Exception as e:
            failed += 1
            print(f"❌ {test_name}: ERROR - {e}")
        print()
    
    # Summary
    print("=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)
    print(f"✅ Passed: {passed}")
    print(f"❌ Failed: {failed}")
    print(f"📈 Success Rate: {(passed / (passed + failed) * 100):.1f}%")
    
    if failed == 0:
        print("\n🎉 ALL TESTS PASSED! ILLI AI Professional is ready to use!")
        print("🚀 You can now run: START_ILLI_PROFESSIONAL_FINAL.bat")
    else:
        print(f"\n⚠️  {failed} test(s) failed. Please check the issues above.")
        print("🔧 Some features may not work correctly.")
    
    print("\n📞 For support: farhanhomeschooling519@gmail.com")
    print("🌐 GitHub: https://github.com/Farhanillahiclass/illi-ai-assistant")
    
    return failed == 0

if __name__ == "__main__":
    success = run_comprehensive_test()
    
    # Keep window open if running from batch file
    if len(sys.argv) > 1 and sys.argv[1] == "--pause":
        input("\nPress Enter to exit...")
    
    sys.exit(0 if success else 1)
