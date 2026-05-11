import tkinter as tk 
from tkinter import ttk, scrolledtext, messagebox, filedialog 
import os 
import webbrowser 
import psutil 
import threading 
import time 
import speech_recognition as sr 
import pyttsx3 
from datetime import datetime 
 
class ILLI_AI: 
    def __init__(self, root): 
        self.root = root 
        self.root.title("ILLI AI - Working Version") 
        self.root.geometry("1200x800") 
        self.root.configure(bg='#000000') 
 
        # Initialize voice 
        self.recognizer = sr.Recognizer() 
        self.engine = pyttsx3.init() 
        self.engine.setProperty('rate', 150) 
        self.listening = False 
 
        # App paths 
        self.apps = { 
            'whatsapp': 'https://web.whatsapp.com', 
            'chrome': 'https://google.com', 
            'youtube': 'https://youtube.com', 
            'files': 'explorer.exe', 
            'notepad': 'notepad.exe', 
            'calculator': 'calc.exe', 
            'cmd': 'cmd.exe' 
