import tkinter as tk
import os
import glob
from utils.pillow_patch import *  # Apply PIL patch before importing ttkbootstrap
import ttkbootstrap as ttk
from ttkbootstrap.constants import (
    BOTH, LEFT, RIGHT, X, Y, VERTICAL, HORIZONTAL
)
from ui.login_window import LoginWindow
from ui.doctor_dashboard import DoctorDashboard
from ui.admin_dashboard import AdminDashboard
from database.connection import db
from database.init_db import initialize_database
from analytics.alos_calculator import ALOSCalculator

class HospitalBedManagementApp:
    """Main application controller"""

    def cleanup_graphs(self):
        """Delete all files in the graphs folder"""
        graph_folder = os.path.join(os.path.dirname(__file__), 'graphs')
        if os.path.exists(graph_folder):
            files = glob.glob(os.path.join(graph_folder, '*'))
            for file in files:
                try:
                    os.remove(file)
                    print(f"[v0] Cleaned up: {file}")
                except Exception as e:
                    print(f"[v0] Error cleaning up {file}: {e}")

    def __init__(self, root):
        self.root = root
        self.current_user = None
        self.current_window = None
        self.cleanup_graphs()  # Clean up existing graphs
        self.setup_theme()
        self.initialize_database()
        self.show_login()

    def setup_theme(self):
        """Setup ttkbootstrap theme"""
        # Using superhero theme as requested
        self.style = ttk.Style(theme="superhero")

    def initialize_database(self):
        """Initialize database connection"""
        try:
            db.connect()
            print("[v0] Database connection established")
        except Exception as e:
            print(f"[v0] Database connection failed: {e}")
            # Try to initialize database
            try:
                initialize_database()
                db.connect()
                print("[v0] Database initialized and connected")
            except Exception as init_error:
                print(f"[v0] Database initialization failed: {init_error}")

    def show_login(self):
        """Show login window"""
        self.clear_window()
        LoginWindow(self.root, self.on_login_success)

    def on_login_success(self, user_data):
        """Handle successful login"""
        self.current_user = user_data
        
        # Update ALOS statistics
        ALOSCalculator.update_alos_statistics()

        if user_data['role'] == 'admin':
            self.show_admin_dashboard()
        elif user_data['role'] == 'doctor':
            self.show_doctor_dashboard()

    def show_doctor_dashboard(self):
        """Show doctor dashboard"""
        self.clear_window()
        DoctorDashboard(self.root, self.current_user)

    def show_admin_dashboard(self):
        """Show admin dashboard"""
        self.clear_window()
        admin_dashboard = AdminDashboard(self.root, self.current_user)
        admin_dashboard.load_data()

    def clear_window(self):
        """Clear all widgets from window"""
        for widget in self.root.winfo_children():
            widget.destroy()

    def on_closing(self):
        """Handle window closing"""
        db.close()
        self.root.destroy()


def main():
    """Main entry point"""
    root = tk.Tk()
    # Configure window for full screen
    root.state('zoomed')  # This will maximize the window
    root.minsize(1024, 768)  # Set minimum window size
    app = HospitalBedManagementApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()


if __name__ == "__main__":
    main()
