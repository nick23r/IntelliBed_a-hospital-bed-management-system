import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from auth.authentication import AuthenticationManager

class LoginWindow:
    """Login window for Hospital Bed Management System"""

    def __init__(self, root, on_login_success):
        self.root = root
        self.on_login_success = on_login_success
        self.auth_manager = AuthenticationManager()
        self.setup_ui()

    def setup_ui(self):
        """Setup login UI with superhero theme"""
        self.root.title("Hospital Bed Management System - Login")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        # Main frame
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill=BOTH, expand=True)

        # Title
        title_label = ttk.Label(
            main_frame,
            text="Hospital Bed Management",
            font=("Helvetica", 24, "bold")
        )
        title_label.pack(pady=20)

        subtitle_label = ttk.Label(
            main_frame,
            text="Login to Your Account",
            font=("Helvetica", 12)
        )
        subtitle_label.pack(pady=(0, 30))

        # Username field
        ttk.Label(main_frame, text="Username:", font=("Helvetica", 10)).pack(anchor=W, pady=(10, 5))
        self.username_entry = ttk.Entry(main_frame, width=40)
        self.username_entry.pack(fill=X, pady=(0, 15))
        self.username_entry.bind("<Return>", lambda e: self.login())

        # Password field
        ttk.Label(main_frame, text="Password:", font=("Helvetica", 10)).pack(anchor=W, pady=(10, 5))
        self.password_entry = ttk.Entry(main_frame, width=40, show="*")
        self.password_entry.pack(fill=X, pady=(0, 20))
        self.password_entry.bind("<Return>", lambda e: self.login())

        # Login button
        login_btn = ttk.Button(
            main_frame,
            text="Login",
            command=self.login,
            bootstyle="info"
        )
        login_btn.pack(fill=X, pady=10)

        # Info label
        info_label = ttk.Label(
            main_frame,
            text="Demo: admin_user / admin123 or dr_smith / doctor123",
            font=("Helvetica", 9),
            foreground="gray"
        )
        info_label.pack(pady=20)

    def login(self):
        """Handle login action"""
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not username or not password:
            messagebox.showerror("Error", "Please enter username and password")
            return

        user, error = self.auth_manager.authenticate_user(username, password)

        if error:
            messagebox.showerror("Login Failed", error)
            self.password_entry.delete(0, tk.END)
            return

        # Successful login
        self.on_login_success(user)
