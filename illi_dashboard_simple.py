import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog
import os
import subprocess
import time
import webbrowser
import psutil

class ILLIDashboardSimple:
    def __init__(self, root):
        self.root = root
        self.root.title("ILLI Dashboard - Simple Version")
        self.root.geometry("800x600")
        self.root.configure(bg='#1e1e1e')
        
        # Title
        title_label = tk.Label(root, text="ILLI DASHBOARD", 
                              font=("Arial", 20, "bold"), 
                              bg='#1e1e1e', fg='#00ff00')
        title_label.pack(pady=20)
        
        subtitle_label = tk.Label(root, text="Created by Muhammad Farhan", 
                                 font=("Arial", 12), 
                                 bg='#1e1e1e', fg='#ffffff')
        subtitle_label.pack(pady=5)
        
        # Main container
        main_frame = tk.Frame(root, bg='#2d2d2d', relief=tk.RAISED, borderwidth=2)
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Quick Launch Section
        launch_frame = tk.LabelFrame(main_frame, text="QUICK LAUNCH", 
                                   font=("Arial", 12, "bold"),
                                   bg='#2d2d2d', fg='#ffffff')
        launch_frame.pack(fill='x', padx=10, pady=10)
        
        # App buttons
        button_frame = tk.Frame(launch_frame, bg='#2d2d2d')
        button_frame.pack(pady=10)
        
        # Row 1
        row1 = tk.Frame(button_frame, bg='#2d2d2d')
        row1.pack(pady=5)
        
        tk.Button(row1, text="WhatsApp", command=self.launch_whatsapp,
                 bg='#25d366', fg='white', font=("Arial", 10, "bold"),
                 width=12, height=2).pack(side='left', padx=5)
        
        tk.Button(row1, text="Instagram", command=self.launch_instagram,
                 bg='#E4405F', fg='white', font=("Arial", 10, "bold"),
                 width=12, height=2).pack(side='left', padx=5)
        
        tk.Button(row1, text="YouTube", command=self.launch_youtube,
                 bg='#FF0000', fg='white', font=("Arial", 10, "bold"),
                 width=12, height=2).pack(side='left', padx=5)
        
        # Row 2
        row2 = tk.Frame(button_frame, bg='#2d2d2d')
        row2.pack(pady=5)
        
        tk.Button(row2, text="Chrome", command=self.launch_chrome,
                 bg='#4285F4', fg='white', font=("Arial", 10, "bold"),
                 width=12, height=2).pack(side='left', padx=5)
        
        tk.Button(row2, text="VS Code", command=self.launch_vscode,
                 bg='#007ACC', fg='white', font=("Arial", 10, "bold"),
                 width=12, height=2).pack(side='left', padx=5)
        
        tk.Button(row2, text="File Manager", command=self.launch_file_manager,
                 bg='#FFA500', fg='white', font=("Arial", 10, "bold"),
                 width=12, height=2).pack(side='left', padx=5)
        
        # System Info Section
        info_frame = tk.LabelFrame(main_frame, text="SYSTEM INFO", 
                                 font=("Arial", 12, "bold"),
                                 bg='#2d2d2d', fg='#ffffff')
        info_frame.pack(fill='x', padx=10, pady=10)
        
        self.info_text = tk.Text(info_frame, height=8, width=70, 
                               bg='#1a1a1a', fg='#ffffff', 
                               font=("Courier", 9))
        self.info_text.pack(padx=10, pady=10)
        
        # Refresh button
        tk.Button(info_frame, text="Refresh System Info", 
                command=self.refresh_system_info,
                bg='#4CAF50', fg='white', font=("Arial", 10, "bold")).pack(pady=5)
        
        # Status bar
        self.status_var = tk.StringVar(value="ILLI Dashboard Ready")
        status_bar = tk.Label(main_frame, textvariable=self.status_var, 
                            relief=tk.SUNKEN, bg='#333333', fg='#ffffff')
        status_bar.pack(fill='x', side='bottom', pady=5)
        
        # Initialize system info
        self.refresh_system_info()
    
    def launch_whatsapp(self):
        """Launch WhatsApp"""
        self.status_var.set("Launching WhatsApp...")
        try:
            # Try multiple methods
            whatsapp_paths = [
                f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\WhatsApp\\WhatsApp.exe",
                f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\WhatsApp\\WhatsApp\\WhatsApp.exe",
                f"C:\\Users\\{os.getlogin()}\\Desktop\\WhatsApp.lnk"
            ]
            
            for path in whatsapp_paths:
                if os.path.exists(path):
                    os.startfile(path)
                    self.status_var.set("WhatsApp launched successfully!")
                    return
            
            # Fallback to web
            webbrowser.open("https://web.whatsapp.com")
            self.status_var.set("WhatsApp Web opened")
            
        except Exception as e:
            self.status_var.set(f"Error launching WhatsApp: {e}")
    
    def launch_instagram(self):
        """Launch Instagram"""
        self.status_var.set("Launching Instagram...")
        try:
            # Try multiple methods
            instagram_paths = [
                f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Instagram\\Instagram.exe",
                f"C:\\Users\\{os.getlogin()}\\Desktop\\Instagram.lnk"
            ]
            
            for path in instagram_paths:
                if os.path.exists(path):
                    os.startfile(path)
                    self.status_var.set("Instagram launched successfully!")
                    return
            
            # Fallback to web
            webbrowser.open("https://www.instagram.com")
            self.status_var.set("Instagram website opened")
            
        except Exception as e:
            self.status_var.set(f"Error launching Instagram: {e}")
    
    def launch_youtube(self):
        """Launch YouTube"""
        self.status_var.set("Opening YouTube...")
        try:
            webbrowser.open("https://www.youtube.com")
            self.status_var.set("YouTube opened successfully!")
        except Exception as e:
            self.status_var.set(f"Error opening YouTube: {e}")
    
    def launch_chrome(self):
        """Launch Chrome"""
        self.status_var.set("Launching Chrome...")
        try:
            chrome_paths = [
                f"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
                f"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            ]
            
            for path in chrome_paths:
                if os.path.exists(path):
                    os.startfile(path)
                    self.status_var.set("Chrome launched successfully!")
                    return
            
            self.status_var.set("Chrome not found")
            
        except Exception as e:
            self.status_var.set(f"Error launching Chrome: {e}")
    
    def launch_vscode(self):
        """Launch VS Code"""
        self.status_var.set("Launching VS Code...")
        try:
            vscode_path = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            if os.path.exists(vscode_path):
                os.startfile(vscode_path)
                self.status_var.set("VS Code launched successfully!")
            else:
                self.status_var.set("VS Code not found")
                
        except Exception as e:
            self.status_var.set(f"Error launching VS Code: {e}")
    
    def launch_file_manager(self):
        """Launch File Manager"""
        self.status_var.set("Opening File Manager...")
        try:
            subprocess.run(["explorer"], shell=True)
            self.status_var.set("File Manager opened successfully!")
        except Exception as e:
            self.status_var.set(f"Error opening File Manager: {e}")
    
    def refresh_system_info(self):
        """Refresh system information"""
        try:
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('C:')
            
            info = "SYSTEM INFORMATION\n"
            info += "=" * 50 + "\n"
            info += f"CPU Usage: {cpu_percent}%\n"
            info += f"Memory Usage: {memory.percent}% ({memory.used//1024//1024}MB/{memory.total//1024//1024}MB)\n"
            info += f"Disk C Usage: {disk.percent}% ({disk.used//1024//1024}GB/{disk.total//1024//1024}GB)\n"
            info += f"Available Memory: {memory.available//1024//1024}MB\n"
            info += f"Available Disk Space: {disk.free//1024//1024}GB\n"
            info += f"Current Time: {time.strftime('%Y-%m-%d %H:%M:%S')}\n"
            info += f"User: {os.getlogin()}\n"
            
            self.info_text.delete('1.0', 'end')
            self.info_text.insert('1.0', info)
            self.status_var.set("System info refreshed")
            
        except Exception as e:
            self.status_var.set(f"Error getting system info: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ILLIDashboardSimple(root)
    root.mainloop()
