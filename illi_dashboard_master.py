import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import os
import subprocess
import time
import webbrowser
import psutil
import threading
import queue
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from PIL import Image, ImageTk, ImageDraw, ImageFont
import math
import random
import json
import hashlib
import base64
import cv2
from datetime import datetime
import pyautogui
import glob
import win32gui
import win32con
import win32process

class ILLIMasterDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("ILLI AI - MASTER DASHBOARD")
        self.root.geometry("3840x1080")  # 32-inch ultra-wide
        self.root.configure(bg='#000000')
        self.root.attributes('-fullscreen', True)
        
        # System variables
        self.system_status = "ONLINE"
        self.user_name = os.getlogin()
        self.current_task = "System Monitoring"
        self.cpu_usage = 0
        self.memory_usage = 0
        self.gpu_temp = 0
        self.network_traffic = 0
        self.listening_state = False
        self.response_queue = queue.Queue()
        
        # Color scheme - Deep space black with electric blue and neon magenta
        self.colors = {
            'bg': '#000000',
            'glass': 'rgba(255, 255, 255, 0.05)',
            'glass_border': 'rgba(255, 255, 255, 0.1)',
            'accent': '#00D4FF',  # Electric blue
            'magenta': '#FF006E',  # Neon magenta
            'cyan': '#00FFFF',
            'text': '#FFFFFF',
            'text_dim': '#666666',
            'success': '#00FF00',
            'warning': '#FFAA00',
            'error': '#FF0000'
        }
        
        self.setup_ui()
        self.start_animations()
        self.start_system_monitoring()
        
    def setup_ui(self):
        # Create main container with glassmorphism effect
        main_frame = tk.Frame(self.root, bg=self.colors['bg'])
        main_frame.pack(fill='both', expand=True)
        
        # Header
        self.create_header(main_frame)
        
        # Main content area
        content_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        content_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Create modular grid system
        self.create_left_sidebar(content_frame)
        self.create_centerpiece(content_frame)
        self.create_right_sidebar(content_frame)
        self.create_bottom_panel(content_frame)
    
    def create_header(self, parent):
        """Create header with glassmorphism effect"""
        header_frame = tk.Frame(parent, bg=self.colors['glass'], height=80)
        header_frame.pack(fill='x', pady=(0, 20))
        header_frame.pack_propagate(False)
        
        # Title
        title_label = tk.Label(header_frame, text="ILLI AI - MASTER DASHBOARD", 
                          font=("Segoe UI", 24, "bold"), 
                          bg=self.colors['glass'], fg=self.colors['accent'])
        title_label.pack(side='left', padx=40, pady=20)
        
        # Status indicator
        self.status_label = tk.Label(header_frame, text=f"● {self.system_status}", 
                                 font=("Segoe UI", 16, "bold"),
                                 bg=self.colors['glass'], fg=self.colors['success'])
        self.status_label.pack(side='left', padx=40, pady=20)
        
        # User info
        user_info = f"USER: {self.user_name} | TASK: {self.current_task}"
        self.user_label = tk.Label(header_frame, text=user_info, 
                               font=("Segoe UI", 12), 
                               bg=self.colors['glass'], fg=self.colors['text_dim'])
        self.user_label.pack(side='right', padx=40, pady=20)
    
    def create_left_sidebar(self, parent):
        """Create left sidebar with system diagnostics"""
        left_frame = tk.Frame(parent, bg=self.colors['glass'], width=400)
        left_frame.pack(side='left', fill='y', padx=(0, 10))
        left_frame.pack_propagate(False)
        
        # System Diagnostics Title
        title = tk.Label(left_frame, text="SYSTEM DIAGNOSTICS", 
                       font=("Segoe UI", 14, "bold"),
                       bg=self.colors['glass'], fg=self.colors['accent'])
        title.pack(pady=20)
        
        # Temperature Gauges
        temp_frame = tk.Frame(left_frame, bg=self.colors['glass'])
        temp_frame.pack(fill='x', padx=20, pady=10)
        
        tk.Label(temp_frame, text="CPU TEMP", font=("Segoe UI", 10, "bold"),
                bg=self.colors['glass'], fg=self.colors['text']).pack(anchor='w')
        
        self.cpu_temp_canvas = tk.Canvas(temp_frame, width=350, height=30, 
                                     bg=self.colors['glass'], highlightthickness=0)
        self.cpu_temp_canvas.pack(fill='x', pady=5)
        
        tk.Label(temp_frame, text="GPU TEMP", font=("Segoe UI", 10, "bold"),
                bg=self.colors['glass'], fg=self.colors['text']).pack(anchor='w', pady=(10,0))
        
        self.gpu_temp_canvas = tk.Canvas(temp_frame, width=350, height=30, 
                                     bg=self.colors['glass'], highlightthickness=0)
        self.gpu_temp_canvas.pack(fill='x', pady=5)
        
        # Memory Usage Bar Chart
        mem_frame = tk.Frame(left_frame, bg=self.colors['glass'])
        mem_frame.pack(fill='x', padx=20, pady=20)
        
        tk.Label(mem_frame, text="MEMORY USAGE", font=("Segoe UI", 10, "bold"),
                bg=self.colors['glass'], fg=self.colors['text']).pack(anchor='w')
        
        self.memory_canvas = tk.Canvas(mem_frame, width=350, height=100, 
                                   bg=self.colors['glass'], highlightthickness=0)
        self.memory_canvas.pack(fill='x', pady=5)
        
        # System Log
        log_frame = tk.Frame(left_frame, bg=self.colors['glass'])
        log_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        tk.Label(log_frame, text="SYSTEM LOG", font=("Segoe UI", 10, "bold"),
                bg=self.colors['glass'], fg=self.colors['text']).pack(anchor='w')
        
        self.system_log = scrolledtext.ScrolledText(log_frame, height=15, width=40,
                                               bg='#0a0a0a', fg=self.colors['cyan'],
                                               font=("Consolas", 9), 
                                               insertbackground=self.colors['accent'])
        self.system_log.pack(fill='both', expand=True, pady=5)
        
        self.add_log_entry("System initialized", "info")
        self.add_log_entry("ILLI AI Dashboard loaded", "success")
        self.add_log_entry("Monitoring systems online", "info")
    
    def create_centerpiece(self, parent):
        """Create centerpiece with 3D particle nebula sphere"""
        center_frame = tk.Frame(parent, bg=self.colors['glass'])
        center_frame.pack(side='left', fill='both', expand=True, padx=10)
        
        # 3D Particle Nebula Sphere
        self.nebula_canvas = tk.Canvas(center_frame, width=800, height=600, 
                                   bg=self.colors['glass'], highlightthickness=0)
        self.nebula_canvas.pack(expand=True, pady=20)
        
        # Listening indicator
        self.listening_indicator = tk.Label(center_frame, text="● IDLE", 
                                       font=("Segoe UI", 16, "bold"),
                                       bg=self.colors['glass'], fg=self.colors['text_dim'])
        self.listening_indicator.pack(pady=10)
        
        # Control buttons
        control_frame = tk.Frame(center_frame, bg=self.colors['glass'])
        control_frame.pack(pady=20)
        
        tk.Button(control_frame, text="🎤 START LISTENING", 
                command=self.toggle_listening,
                bg=self.colors['accent'], fg=self.colors['text'], 
                font=("Segoe UI", 12, "bold"),
                width=20, height=2).pack(side='left', padx=10)
        
        tk.Button(control_frame, text="🔄 REFRESH SYSTEM", 
                command=self.refresh_system,
                bg=self.colors['magenta'], fg=self.colors['text'], 
                font=("Segoe UI", 12, "bold"),
                width=20, height=2).pack(side='left', padx=10)
    
    def create_right_sidebar(self, parent):
        """Create right sidebar with WhatsApp/Messaging integration"""
        right_frame = tk.Frame(parent, bg=self.colors['glass'], width=400)
        right_frame.pack(side='left', fill='y', padx=(10, 0))
        right_frame.pack_propagate(False)
        
        # Messaging Integration Title
        title = tk.Label(right_frame, text="MESSAGING INTEGRATION", 
                       font=("Segoe UI", 14, "bold"),
                       bg=self.colors['glass'], fg=self.colors['accent'])
        title.pack(pady=20)
        
        # WhatsApp Panel
        whatsapp_frame = tk.Frame(right_frame, bg=self.colors['glass'])
        whatsapp_frame.pack(fill='x', padx=20, pady=10)
        
        tk.Label(whatsapp_frame, text="📱 WHATSAPP", font=("Segoe UI", 12, "bold"),
                bg=self.colors['glass'], fg=self.colors['text']).pack(anchor='w')
        
        # Chat bubbles area
        self.chat_frame = tk.Frame(whatsapp_frame, bg='#0a0a0a')
        self.chat_frame.pack(fill='both', expand=True, pady=10)
        
        # Message input
        msg_input_frame = tk.Frame(whatsapp_frame, bg=self.colors['glass'])
        msg_input_frame.pack(fill='x', pady=10)
        
        self.message_entry = tk.Entry(msg_input_frame, width=30,
                                 bg='#0a0a0a', fg=self.colors['text'],
                                 font=("Segoe UI", 10), 
                                 insertbackground=self.colors['accent'])
        self.message_entry.pack(side='left', padx=(0, 10))
        self.message_entry.bind('<Return>', self.send_message)
        
        tk.Button(msg_input_frame, text="SEND", command=self.send_message,
                 bg=self.colors['success'], fg=self.colors['text'], 
                 font=("Segoe UI", 10, "bold")).pack(side='left')
        
        # File Transfer Progress
        transfer_frame = tk.Frame(right_frame, bg=self.colors['glass'])
        transfer_frame.pack(fill='x', padx=20, pady=20)
        
        tk.Label(transfer_frame, text="📁 FILE TRANSFER", font=("Segoe UI", 10, "bold"),
                bg=self.colors['glass'], fg=self.colors['text']).pack(anchor='w')
        
        self.transfer_canvas = tk.Canvas(transfer_frame, width=350, height=30, 
                                     bg=self.colors['glass'], highlightthickness=0)
        self.transfer_canvas.pack(fill='x', pady=5)
        
        self.transfer_label = tk.Label(transfer_frame, text="No active transfers", 
                                   font=("Segoe UI", 9),
                                   bg=self.colors['glass'], fg=self.colors['text_dim'])
        self.transfer_label.pack(anchor='w')
    
    def create_bottom_panel(self, parent):
        """Create bottom panel with Neural Map"""
        bottom_frame = tk.Frame(parent, bg=self.colors['glass'], height=300)
        bottom_frame.pack(side='bottom', fill='x', pady=(10, 0))
        bottom_frame.pack_propagate(False)
        
        # Neural Map Title
        title = tk.Label(bottom_frame, text="🧠 NEURAL MAP", 
                       font=("Segoe UI", 14, "bold"),
                       bg=self.colors['glass'], fg=self.colors['accent'])
        title.pack(pady=10)
        
        # Neural Network Visualization
        self.neural_canvas = tk.Canvas(bottom_frame, width=1200, height=200, 
                                    bg=self.colors['glass'], highlightthickness=0)
        self.neural_canvas.pack(fill='both', expand=True, padx=20, pady=10)
    
    def start_animations(self):
        """Start all animations"""
        threading.Thread(target=self.animate_nebula, daemon=True).start()
        threading.Thread(target=self.animate_neural_network, daemon=True).start()
        threading.Thread(target=self.animate_gauges, daemon=True).start()
    
    def animate_nebula(self):
        """Animate 3D particle nebula sphere"""
        angle = 0
        particles = []
        
        # Initialize particles
        for _ in range(100):
            particles.append({
                'x': random.uniform(-150, 150),
                'y': random.uniform(-150, 150),
                'z': random.uniform(-150, 150),
                'vx': random.uniform(-1, 1),
                'vy': random.uniform(-1, 1),
                'vz': random.uniform(-1, 1),
                'size': random.uniform(1, 3),
                'color': random.choice([self.colors['accent'], self.colors['magenta'], self.colors['cyan']])
            })
        
        while True:
            try:
                self.nebula_canvas.delete("all")
                
                # Draw particles
                cx, cy = 400, 300
                
                for particle in particles:
                    # Rotate particle
                    x = particle['x'] * math.cos(angle) - particle['z'] * math.sin(angle)
                    z = particle['x'] * math.sin(angle) + particle['z'] * math.cos(angle)
                    y = particle['y']
                    
                    # Project to 2D
                    scale = 200 / (200 + z)
                    px = cx + x * scale
                    py = cy + y * scale
                    
                    size = particle['size'] * scale
                    
                    self.nebula_canvas.create_oval(px-size, py-size, px+size, py+size, 
                                               fill=particle['color'], outline='')
                    
                    # Update particle position
                    particle['x'] += particle['vx']
                    particle['y'] += particle['vy']
                    particle['z'] += particle['vz']
                    
                    # Boundary check
                    if abs(particle['x']) > 150: particle['vx'] *= -1
                    if abs(particle['y']) > 150: particle['vy'] *= -1
                    if abs(particle['z']) > 150: particle['vz'] *= -1
                
                # Draw data rings
                for i in range(3):
                    radius = 100 + i * 50
                    self.nebula_canvas.create_oval(cx-radius, cy-radius, cx+radius, cy+radius, 
                                               outline=self.colors['accent'], width=1)
                
                # Draw orbiting labels
                labels = ["NLP", "NEURAL", "VISION", "AUDIO"]
                for i, label in enumerate(labels):
                    label_angle = angle * 2 + i * 90
                    lx = cx + (radius + 30) * math.cos(math.radians(label_angle))
                    ly = cy + (radius + 30) * math.sin(math.radians(label_angle))
                    
                    self.nebula_canvas.create_text(lx, ly, text=label, 
                                               fill=self.colors['text'], 
                                               font=("Segoe UI", 10, "bold"))
                    
                    # Connection line
                    self.nebula_canvas.create_line(cx, cy, lx, ly, 
                                               fill=self.colors['magenta'], width=1)
                
                # Center core
                core_size = 20 + 5 * math.sin(angle * 3)
                self.nebula_canvas.create_oval(cx-core_size, cy-core_size, cx+core_size, cy+core_size, 
                                           fill=self.colors['magenta'], outline=self.colors['accent'], width=2)
                
                # Pulsing effect when listening
                if self.listening_state:
                    pulse_size = 30 + 10 * math.sin(angle * 5)
                    self.nebula_canvas.create_oval(cx-pulse_size, cy-pulse_size, cx+pulse_size, cy+pulse_size, 
                                               outline=self.colors['cyan'], width=2)
                
                angle += 0.05
                time.sleep(0.03)
                
            except Exception as e:
                print(f"Nebula animation error: {e}")
    
    def animate_neural_network(self):
        """Animate neural network connections"""
        nodes = {
            'ILLI': (600, 100),
            'Local Files': (200, 150),
            'Cloud Services': (400, 50),
            'Home Automation': (800, 150),
            'WhatsApp': (1000, 100),
            'Email': (200, 50),
            'YouTube': (800, 50),
            'System': (600, 150)
        }
        
        connections = [
            ('ILLI', 'Local Files', 'active'),
            ('ILLI', 'Cloud Services', 'active'),
            ('ILLI', 'Home Automation', 'standby'),
            ('ILLI', 'WhatsApp', 'active'),
            ('ILLI', 'Email', 'active'),
            ('ILLI', 'YouTube', 'active'),
            ('ILLI', 'System', 'active'),
            ('Local Files', 'Cloud Services', 'data'),
            ('Home Automation', 'System', 'data')
        ]
        
        pulse_phase = 0
        
        while True:
            try:
                self.neural_canvas.delete("all")
                
                # Draw connections
                for conn in connections:
                    from_node, to_node, status = conn
                    x1, y1 = nodes[from_node]
                    x2, y2 = nodes[to_node]
                    
                    color_map = {
                        'active': self.colors['success'],
                        'standby': self.colors['warning'],
                        'data': self.colors['accent'],
                        'error': self.colors['error']
                    }
                    
                    color = color_map.get(status, self.colors['text_dim'])
                    
                    # Animated data flow
                    if status == 'data':
                        progress = (math.sin(pulse_phase) + 1) / 2
                        mid_x = x1 + (x2 - x1) * progress
                        mid_y = y1 + (y2 - y1) * progress
                        self.neural_canvas.create_oval(mid_x-3, mid_y-3, mid_x+3, mid_y+3, 
                                                   fill=self.colors['cyan'], outline='')
                    
                    self.neural_canvas.create_line(x1, y1, x2, y2, 
                                               fill=color, width=2)
                
                # Draw nodes
                for node_name, (x, y) in nodes.items():
                    size = 12 if node_name == 'ILLI' else 8
                    color = self.colors['magenta'] if node_name == 'ILLI' else self.colors['accent']
                    
                    self.neural_canvas.create_oval(x-size, y-size, x+size, y+size, 
                                               fill=color, outline=self.colors['text'], width=2)
                    
                    self.neural_canvas.create_text(x, y-20, text=node_name, 
                                               fill=self.colors['text'], 
                                               font=("Segoe UI", 9, "bold"))
                
                pulse_phase += 0.1
                time.sleep(0.05)
                
            except Exception as e:
                print(f"Neural network animation error: {e}")
    
    def animate_gauges(self):
        """Animate temperature gauges and memory usage"""
        while True:
            try:
                # Update CPU temperature gauge
                self.cpu_temp_canvas.delete("all")
                cpu_temp = random.uniform(40, 70)  # Simulated temperature
                self.draw_gauge(self.cpu_temp_canvas, cpu_temp, 0, 100, "CPU")
                
                # Update GPU temperature gauge
                self.gpu_temp_canvas.delete("all")
                gpu_temp = random.uniform(30, 60)  # Simulated temperature
                self.draw_gauge(self.gpu_temp_canvas, gpu_temp, 0, 100, "GPU")
                
                # Update memory usage
                self.memory_canvas.delete("all")
                memory = psutil.virtual_memory()
                self.draw_memory_chart(memory.percent)
                
                time.sleep(1)
                
            except Exception as e:
                print(f"Gauge animation error: {e}")
    
    def draw_gauge(self, canvas, value, min_val, max_val, label):
        """Draw temperature gauge"""
        width = 350
        height = 30
        
        # Background
        canvas.create_rectangle(0, 0, width, height, fill='#1a1a1a', outline='')
        
        # Color based on temperature
        if value < 50:
            color = self.colors['success']
        elif value < 70:
            color = self.colors['warning']
        else:
            color = self.colors['error']
        
        # Fill bar
        fill_width = (value / max_val) * width
        canvas.create_rectangle(0, 0, fill_width, height, fill=color, outline='')
        
        # Text
        canvas.create_text(width/2, height/2, text=f"{value:.1f}°C", 
                       fill=self.colors['text'], font=("Segoe UI", 10, "bold"))
    
    def draw_memory_chart(self, percent):
        """Draw memory usage bar chart"""
        width = 350
        height = 100
        
        # Background
        self.memory_canvas.create_rectangle(0, 0, width, height, fill='#1a1a1a', outline='')
        
        # Memory bars
        bar_width = width // 4
        bar_spacing = 10
        
        # Simulated memory data
        memory_data = [percent, random.uniform(20, 80), random.uniform(30, 70), random.uniform(40, 60)]
        
        for i, mem_percent in enumerate(memory_data):
            x = i * (bar_width + bar_spacing) + bar_spacing
            bar_height = (mem_percent / 100) * (height - 20)
            y = height - bar_height - 10
            
            # Color based on usage
            if mem_percent < 50:
                color = self.colors['success']
            elif mem_percent < 80:
                color = self.colors['warning']
            else:
                color = self.colors['error']
            
            self.memory_canvas.create_rectangle(x, y, x + bar_width, height - 10, 
                                          fill=color, outline='')
            
            # Label
            self.memory_canvas.create_text(x + bar_width/2, height - 5, text=f"{mem_percent:.0f}%", 
                                       fill=self.colors['text'], font=("Segoe UI", 8))
    
    def start_system_monitoring(self):
        """Start system monitoring"""
        threading.Thread(target=self.monitor_system, daemon=True).start()
    
    def monitor_system(self):
        """Monitor system resources"""
        while True:
            try:
                # Update system stats
                self.cpu_usage = psutil.cpu_percent(interval=1)
                memory = psutil.virtual_memory()
                self.memory_usage = memory.percent
                
                # Update user label
                self.current_task = "System Monitoring"
                user_info = f"USER: {self.user_name} | TASK: {self.current_task}"
                self.user_label.config(text=user_info)
                
                time.sleep(2)
                
            except Exception as e:
                print(f"System monitoring error: {e}")
    
    def toggle_listening(self):
        """Toggle listening state"""
        self.listening_state = not self.listening_state
        
        if self.listening_state:
            self.listening_indicator.config(text="● LISTENING", fg=self.colors['success'])
            self.add_log_entry("Voice recognition activated", "success")
        else:
            self.listening_indicator.config(text="● IDLE", fg=self.colors['text_dim'])
            self.add_log_entry("Voice recognition deactivated", "info")
    
    def refresh_system(self):
        """Refresh system information"""
        self.add_log_entry("System refresh initiated", "info")
        
        # Get current system info
        self.cpu_usage = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        self.memory_usage = memory.percent
        
        self.add_log_entry(f"CPU: {self.cpu_usage:.1f}%, Memory: {self.memory_usage:.1f}%", "info")
        self.add_log_entry("System refresh completed", "success")
    
    def send_message(self, event=None):
        """Send WhatsApp message"""
        message = self.message_entry.get().strip()
        if message:
            # Add message to chat
            self.add_chat_bubble("You", message, "user")
            
            # Clear input
            self.message_entry.delete(0, tk.END)
            
            # Simulate sending
            self.add_log_entry(f"Message sent: {message}", "info")
            
            # Simulate response
            self.root.after(2000, lambda: self.add_chat_bubble("ILLI", "Message received successfully!", "bot"))
    
    def add_chat_bubble(self, sender, message, msg_type):
        """Add chat bubble to chat frame"""
        bubble_frame = tk.Frame(self.chat_frame, bg='#0a0a0a')
        bubble_frame.pack(fill='x', pady=2)
        
        # Sender label
        sender_label = tk.Label(bubble_frame, text=f"{sender}:", 
                             font=("Segoe UI", 9, "bold"),
                             bg='#0a0a0a', fg=self.colors['accent'])
        sender_label.pack(anchor='w')
        
        # Message bubble
        bubble_color = self.colors['accent'] if msg_type == 'user' else self.colors['magenta']
        bubble = tk.Label(bubble_frame, text=message, 
                        font=("Segoe UI", 10),
                        bg=bubble_color, fg=self.colors['text'],
                        wraplength=300, justify='left')
        bubble.pack(anchor='w', pady=(0, 5))
    
    def add_log_entry(self, message, log_type):
        """Add entry to system log"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        color_map = {
            'info': self.colors['text'],
            'success': self.colors['success'],
            'warning': self.colors['warning'],
            'error': self.colors['error']
        }
        
        color = color_map.get(log_type, self.colors['text'])
        
        self.system_log.config(state='normal')
        self.system_log.insert('end', f"[{timestamp}] {message}\n")
        self.system_log.tag_add(log_type, f"end-2l", f"end-1l")
        self.system_log.tag_config(log_type, foreground=color)
        self.system_log.config(state='disabled')
        self.system_log.see('end')

if __name__ == "__main__":
    root = tk.Tk()
    app = ILLIMasterDashboard(root)
    root.mainloop()
