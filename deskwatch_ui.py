import tkinter as tk
from tkinter import ttk, scrolledtext
import pygetwindow as window_manager
import pyautogui
import datetime
import json
import threading
import activity

class DeskwatchUI:
    def __init__(self, root):
        self.root = root
        self.root.title("DeskWatch - Activity Tracker")
        self.root.geometry("700x500")
        self.root.configure(bg="#f5f5f5")  # Light gray-white background
        
        # Show splash screen before initializing main UI
        self.show_splash_screen()
        
        # Tracking state
        self.is_tracking = False
        self.activity_logs = {}
        self.active_window_title = ""
        self.activity_name = ""
        self.start_time = datetime.datetime.now()
        self.first_iteration = True
        
        # Tracking thread
        self.tracking_thread = None
        
    def show_splash_screen(self):
        # Create splash screen frame
        self.splash_frame = ttk.Frame(self.root, style="Splash.TFrame")
        self.splash_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Configure style for splash
        style = ttk.Style()
        style.configure("Splash.TFrame")
        style.configure("Splash.TLabel", font=("Helvetica", 24, "bold"))
        style.configure("SplashInfo.TLabel", font=("Helvetica", 12))
        
        # Splash screen content
        ttk.Label(self.splash_frame, text="🕒 DeskWatch", style="Splash.TLabel").pack(pady=20)
        ttk.Label(self.splash_frame, text="Loading your activity tracker...", style="SplashInfo.TLabel").pack(pady=10)
        
        # Schedule splash screen to close and load main UI after 3 seconds
        self.root.after(3000, self.load_main_ui)
        
    def load_main_ui(self):
        # Destroy splash screen
        self.splash_frame.destroy()
        
        # Create main UI widgets
        self.create_widgets()
        
    def create_widgets(self):
        # Main frame with white-based styling
        main_frame = ttk.Frame(self.root, padding="15", style="Main.TFrame")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure style
        style = ttk.Style()
        style.configure("Main.TFrame", background="#ffffff")  # Pure white frame
        style.configure("Accent.TButton", font=("Helvetica", 10, "bold"), background="#4a90e2")  # Blue for Start/Save
        style.configure("Danger.TButton", font=("Helvetica", 10, "bold"), background="#d9534f", foreground="white")  # Red for Stop
        style.configure("Info.TLabel", font=("Helvetica", 12), background="#ffffff", foreground="#333333")  # Dark gray text
        style.configure("Header.TLabel", font=("Helvetica", 16, "bold"), background="#ffffff", foreground="#4a90e2")  # Blue header
        
        # Header
        header = ttk.Label(main_frame, text="🕒 Deskwatch", style="Header.TLabel")
        header.grid(row=0, column=0, columnspan=2, pady=(0, 10))
        
        # Status frame
        status_frame = ttk.Frame(main_frame, style="Main.TFrame")
        status_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        # Current activity
        self.current_activity = ttk.Label(status_frame, text="Current Activity: None", style="Info.TLabel")
        self.current_activity.grid(row=0, column=0, sticky=tk.W, padx=5)
        
        # Time spent
        self.time_spent = ttk.Label(status_frame, text="Time Spent: 0h 0m 0s", style="Info.TLabel")
        self.time_spent.grid(row=1, column=0, sticky=tk.W, padx=5)
        
        # Control buttons frame
        button_frame = ttk.Frame(main_frame, style="Main.TFrame")
        button_frame.grid(row=2, column=0, columnspan=2, pady=10)
        
        self.start_button = ttk.Button(button_frame, text="▶ Start Tracking", command=self.start_tracking, style="Accent.TButton")
        self.start_button.grid(row=0, column=0, padx=5)
        
        self.stop_button = ttk.Button(button_frame, text="⏹ Stop Tracking", command=self.stop_tracking, style="Danger.TButton", state='disabled')
        self.stop_button.grid(row=0, column=1, padx=5)
        
        # Activity log display
        self.log_display = scrolledtext.ScrolledText(main_frame, height=12, width=70, bg="#f8f9fa", fg="#333333", font=("Helvetica", 10))
        self.log_display.grid(row=3, column=0, columnspan=2, pady=10)
        self.log_display.insert(tk.END, "📋 Welcome to Deskwatch! Start tracking to monitor your activities.\n")
        self.log_display.config(state='disabled')
        
        # Save button
        self.save_button = ttk.Button(main_frame, text="💾 Save Logs", command=self.save_logs, style="Accent.TButton")
        self.save_button.grid(row=4, column=0, columnspan=2, pady=5)
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        
    def start_tracking(self):
        if not self.is_tracking:
            self.is_tracking = True
            self.start_button.config(state='disabled')
            self.stop_button.config(state='normal')
            self.log_display.config(state='normal')
            self.log_display.insert(tk.END, "🚀 Tracking started...\n")
            self.log_display.config(state='disabled')
            self.tracking_thread = threading.Thread(target=self.track_activity, daemon=True)
            self.tracking_thread.start()
            
    def stop_tracking(self):
        self.is_tracking = False
        self.start_button.config(state='normal')
        self.stop_button.config(state='disabled')
        self.log_display.config(state='normal')
        self.log_display.insert(tk.END, "🛑 Tracking stopped.\n")
        self.update_log_display()
        self.log_display.config(state='disabled')
        
    def track_activity(self):
        while self.is_tracking:
            try:
                current_window_title = window_manager.getActiveWindow().title
                
                if "Brave" in current_window_title:
                    url = activity.get_current_url()
                    current_window_title = activity.extract_domain_name(url)
                
                if current_window_title != self.active_window_title:
                    if self.active_window_title and not self.first_iteration:
                        self.start_time = activity.extract_activity_logs(
                            self.activity_logs, 
                            self.active_window_title,
                            self.activity_name, 
                            self.start_time
                        )
                        self.log_display.config(state='normal')
                        self.update_log_display()
                        self.log_display.config(state='disabled')
                    
                    self.active_window_title = current_window_title
                    self.activity_name = current_window_title
                    self.first_iteration = False
                
                # Update UI
                self.current_activity.config(text=f"Current Activity: {self.active_window_title or 'None'}")
                time_spent = datetime.datetime.now() - self.start_time
                formatted_time = activity.format_time_delta(time_spent)
                self.time_spent.config(text=f"Time Spent: {formatted_time['hours']}h {formatted_time['minutes']}m {formatted_time['seconds']}s")
                
                self.root.update()
                pyautogui.sleep(1)
                
            except Exception as e:
                self.log_display.config(state='normal')
                self.log_display.insert(tk.END, f"⚠ Error: {str(e)}\n")
                self.log_display.config(state='disabled')
                break
                
    def update_log_display(self):
        self.log_display.config(state='normal')
        self.log_display.delete(1.0, tk.END)
        self.log_display.insert(tk.END, "📋 Deskwatch Activity Log\n\n")
        for activity_name, logs in self.activity_logs.items():
            self.log_display.insert(tk.END, f"🏷 {activity_name}\n")
            for log in logs:
                self.log_display.insert(tk.END, 
                    f"  ⏰ Start: {log['Start time']}\n"
                    f"  ⏰ End: {log['End time']}\n"
                    f"  ⏱ Time Spent: {log['Time spent']['hours']}h {log['Time spent']['minutes']}m {log['Time spent']['seconds']}s\n\n"
                )
        self.log_display.see(tk.END)
        
    def save_logs(self):
        with open('activity_log.json', 'w') as json_file:
            json.dump(self.activity_logs, json_file, indent=4)
        self.log_display.config(state='normal')
        self.log_display.insert(tk.END, "💾 Logs saved to activity_log.json\n")
        self.log_display.config(state='disabled')
        self.log_display.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = DeskwatchUI(root)
    root.mainloop()