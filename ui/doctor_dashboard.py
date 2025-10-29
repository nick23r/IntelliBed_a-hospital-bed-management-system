import tkinter as tk
from tkinter import messagebox, ttk as tk_ttk
from tkinter.constants import W, END, VERTICAL, HORIZONTAL  # Add missing constants
from utils.pillow_patch import *  # Apply PIL patch before importing ttkbootstrap
import ttkbootstrap as ttk
from ttkbootstrap.constants import (
    BOTH, LEFT, RIGHT, X, Y
)
from datetime import datetime
from database.connection import db
from auth.authentication import AuthenticationManager

class DoctorDashboard:
    """Doctor dashboard for managing patient admissions and bed transfers"""

    def __init__(self, root, user_data):
        self.root = root
        self.user_data = user_data
        self.auth_manager = AuthenticationManager()
        self.setup_ui()
        self.load_data()

    def setup_ui(self):
        """Setup doctor dashboard UI"""
        self.root.title(f"Doctor Dashboard - {self.user_data['full_name']}")
        self.root.geometry("1200x700")

        # Main container
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill=BOTH, expand=True)

        # Header
        header_frame = ttk.Frame(main_frame)
        header_frame.pack(fill=X, pady=(0, 10))

        ttk.Label(header_frame, text=f"Welcome, {self.user_data['full_name']}", font=("Helvetica", 16, "bold")).pack(side=LEFT)
        ttk.Button(header_frame, text="Logout", command=self.logout, bootstyle="danger").pack(side=RIGHT)

        # Search and Filter Panel
        search_frame = ttk.LabelFrame(main_frame, text="Search & Filter", padding=10)
        search_frame.pack(fill=X, pady=(0, 10))

        ttk.Label(search_frame, text="Search by Patient Name:").pack(side=LEFT, padx=5)
        self.search_entry = ttk.Entry(search_frame, width=20)
        self.search_entry.pack(side=LEFT, padx=5)
        self.search_entry.bind("<KeyRelease>", lambda e: self.apply_filters())

        ttk.Label(search_frame, text="Bed ID:").pack(side=LEFT, padx=5)
        self.bed_filter_entry = ttk.Entry(search_frame, width=15)
        self.bed_filter_entry.pack(side=LEFT, padx=5)
        self.bed_filter_entry.bind("<KeyRelease>", lambda e: self.apply_filters())

        ttk.Label(search_frame, text="Admission Reason:").pack(side=LEFT, padx=5)
        self.reason_filter_entry = ttk.Entry(search_frame, width=20)
        self.reason_filter_entry.pack(side=LEFT, padx=5)
        self.reason_filter_entry.bind("<KeyRelease>", lambda e: self.apply_filters())

        ttk.Button(search_frame, text="Clear Filters", command=self.clear_filters, bootstyle="secondary").pack(side=LEFT, padx=5)

        # Admissions Table
        table_frame = ttk.LabelFrame(main_frame, text="Active Admissions", padding=10)
        table_frame.pack(fill=BOTH, expand=True, pady=(0, 10))

        # Create treeview
        columns = ("Admission ID", "Patient Name", "Bed ID", "Admission Date", "Reason", "Status")
        self.tree = tk_ttk.Treeview(table_frame, columns=columns, height=15, show="headings")

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)

        scrollbar = tk_ttk.Scrollbar(table_frame, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)

        self.tree.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Action buttons frame
        action_frame = ttk.Frame(main_frame)
        action_frame.pack(fill=X, pady=10)

        ttk.Button(action_frame, text="New Admission", command=self.open_admission_form, bootstyle="success").pack(side=LEFT, padx=5)
        ttk.Button(action_frame, text="Discharge Patient", command=self.discharge_patient, bootstyle="warning").pack(side=LEFT, padx=5)
        ttk.Button(action_frame, text="Transfer Bed", command=self.transfer_bed, bootstyle="info").pack(side=LEFT, padx=5)
        ttk.Button(action_frame, text="Refresh", command=self.load_data, bootstyle="secondary").pack(side=LEFT, padx=5)

    def load_data(self):
        """Load admissions data from database"""
        try:
            with db.get_cursor() as cursor:
                cursor.execute("""
                    SELECT a.admission_id, p.patient_name, b.bed_number, 
                           a.admission_date, a.admission_reason, a.status
                    FROM admissions a
                    JOIN patients p ON a.patient_id = p.patient_id
                    JOIN beds b ON a.bed_id = b.bed_id
                    WHERE a.doctor_id = %s AND a.status = 'active'
                    ORDER BY a.admission_date DESC
                """, (self.user_data['user_id'],))
                
                self.all_data = cursor.fetchall()
                self.display_data(self.all_data)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {str(e)}")

    def display_data(self, data):
        """Display data in treeview"""
        for item in self.tree.get_children():
            self.tree.delete(item)

        for row in data:
            self.tree.insert("", END, values=(
                row['admission_id'],
                row['patient_name'],
                row['bed_number'],
                row['admission_date'].strftime("%Y-%m-%d %H:%M") if row['admission_date'] else "",
                row['admission_reason'],
                row['status']
            ))

    def apply_filters(self):
        """Apply search and filter criteria"""
        search_term = self.search_entry.get().lower()
        bed_filter = self.bed_filter_entry.get().lower()
        reason_filter = self.reason_filter_entry.get().lower()

        filtered_data = [
            row for row in self.all_data
            if (search_term in row['patient_name'].lower() and
                bed_filter in row['bed_number'].lower() and
                reason_filter in row['admission_reason'].lower())
        ]

        self.display_data(filtered_data)

    def clear_filters(self):
        """Clear all filters"""
        self.search_entry.delete(0, tk.END)
        self.bed_filter_entry.delete(0, tk.END)
        self.reason_filter_entry.delete(0, tk.END)
        self.display_data(self.all_data)

    def open_admission_form(self):
        """Open new admission form"""
        AdmissionForm(self.root, self.user_data, self.load_data)

    def discharge_patient(self):
        """Discharge selected patient"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select an admission to discharge")
            return

        item = self.tree.item(selection[0])
        admission_id = item['values'][0]

        try:
            with db.get_cursor() as cursor:
                cursor.execute(
                    "UPDATE admissions SET status = 'discharged', discharge_date = NOW() WHERE admission_id = %s",
                    (admission_id,)
                )
                self.auth_manager.log_audit(
                    self.user_data['user_id'],
                    "Discharged patient",
                    "admissions",
                    admission_id
                )
            messagebox.showinfo("Success", "Patient discharged successfully")
            self.load_data()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to discharge patient: {str(e)}")

    def transfer_bed(self):
        """Transfer patient to different bed"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select an admission to transfer")
            return

        item = self.tree.item(selection[0])
        admission_id = item['values'][0]

        BedTransferForm(self.root, admission_id, self.user_data, self.load_data)

    def logout(self):
        """Logout and return to login"""
        self.root.quit()


class AdmissionForm:
    """Form for new patient admission"""

    def __init__(self, parent, user_data, callback):
        self.user_data = user_data
        self.callback = callback
        self.window = tk.Toplevel(parent)
        self.window.title("New Admission")
        self.window.geometry("500x500")
        self.setup_form()

    def setup_form(self):
        """Setup admission form"""
        frame = ttk.Frame(self.window, padding=20)
        frame.pack(fill=BOTH, expand=True)

        ttk.Label(frame, text="Patient Name:").pack(anchor=W, pady=(10, 5))
        self.patient_name = ttk.Entry(frame, width=40)
        self.patient_name.pack(fill=X, pady=(0, 10))

        ttk.Label(frame, text="Age:").pack(anchor=W, pady=(10, 5))
        self.age = ttk.Entry(frame, width=40)
        self.age.pack(fill=X, pady=(0, 10))

        ttk.Label(frame, text="Gender:").pack(anchor=W, pady=(10, 5))
        self.gender = ttk.Combobox(frame, values=["M", "F", "Other"], state="readonly", width=37)
        self.gender.pack(fill=X, pady=(0, 10))

        ttk.Label(frame, text="Contact Number:").pack(anchor=W, pady=(10, 5))
        self.contact = ttk.Entry(frame, width=40)
        self.contact.pack(fill=X, pady=(0, 10))

        ttk.Label(frame, text="Medical History:").pack(anchor=W, pady=(10, 5))
        self.history = tk.Text(frame, height=4, width=40)
        self.history.pack(fill=X, pady=(0, 10))

        ttk.Label(frame, text="Bed ID:").pack(anchor=W, pady=(10, 5))
        self.bed_id = ttk.Combobox(frame, state="readonly", width=37)
        self.bed_id.pack(fill=X, pady=(0, 10))
        self.load_available_beds()

        ttk.Label(frame, text="Admission Reason:").pack(anchor=W, pady=(10, 5))
        self.reason = ttk.Entry(frame, width=40)
        self.reason.pack(fill=X, pady=(0, 20))

        ttk.Button(frame, text="Submit", command=self.submit, bootstyle="success").pack(fill=X, pady=5)
        ttk.Button(frame, text="Cancel", command=self.window.destroy, bootstyle="danger").pack(fill=X)

    def load_available_beds(self):
        """Load available beds"""
        try:
            with db.get_cursor() as cursor:
                cursor.execute("SELECT bed_id, bed_number FROM beds WHERE status = 'available'")
                beds = cursor.fetchall()
                self.bed_id.configure(values=[f"{b['bed_id']} - {b['bed_number']}" for b in beds])
                self.beds_data = beds
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load beds: {str(e)}")

    def submit(self):
        """Submit admission form"""
        try:
            bed_selection = self.bed_id.get()
            if not bed_selection:
                messagebox.showwarning("Warning", "Please select a bed")
                return

            bed_id = int(bed_selection.split(" - ")[0])

            with db.get_cursor() as cursor:
                # Insert patient
                cursor.execute(
                    """INSERT INTO patients (patient_name, age, gender, contact_number, medical_history)
                    VALUES (%s, %s, %s, %s, %s)""",
                    (self.patient_name.get(), int(self.age.get()), self.gender.get(),
                     self.contact.get(), self.history.get("1.0", tk.END))
                )
                patient_id = cursor.lastrowid

                # Insert admission
                cursor.execute(
                    """INSERT INTO admissions (patient_id, bed_id, doctor_id, admission_date, admission_reason, status)
                    VALUES (%s, %s, %s, NOW(), %s, 'active')""",
                    (patient_id, bed_id, self.user_data['user_id'], self.reason.get())
                )

                # Update bed status
                cursor.execute("UPDATE beds SET status = 'occupied' WHERE bed_id = %s", (bed_id,))

                # Log audit
                AuthenticationManager.log_audit(
                    self.user_data['user_id'],
                    "Admitted new patient",
                    "admissions",
                    cursor.lastrowid
                )

            messagebox.showinfo("Success", "Patient admitted successfully")
            self.callback()
            self.window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to admit patient: {str(e)}")


class BedTransferForm:
    """Form for bed transfer"""

    def __init__(self, parent, admission_id, user_data, callback):
        self.admission_id = admission_id
        self.user_data = user_data
        self.callback = callback
        self.window = tk.Toplevel(parent)
        self.window.title("Transfer Bed")
        self.window.geometry("400x300")
        self.setup_form()

    def setup_form(self):
        """Setup transfer form"""
        frame = ttk.Frame(self.window, padding=20)
        frame.pack(fill=BOTH, expand=True)

        ttk.Label(frame, text="Select New Bed:").pack(anchor=W, pady=(10, 5))
        self.new_bed = ttk.Combobox(frame, state="readonly", width=37)
        self.new_bed.pack(fill=X, pady=(0, 10))
        self.load_available_beds()

        ttk.Label(frame, text="Transfer Reason:").pack(anchor=W, pady=(10, 5))
        self.reason = ttk.Entry(frame, width=40)
        self.reason.pack(fill=X, pady=(0, 20))

        ttk.Button(frame, text="Transfer", command=self.submit, bootstyle="success").pack(fill=X, pady=5)
        ttk.Button(frame, text="Cancel", command=self.window.destroy, bootstyle="danger").pack(fill=X)

    def load_available_beds(self):
        """Load available beds"""
        try:
            with db.get_cursor() as cursor:
                cursor.execute("SELECT bed_id, bed_number FROM beds WHERE status = 'available'")
                beds = cursor.fetchall()
                self.new_bed.configure(values=[f"{b['bed_id']} - {b['bed_number']}" for b in beds])
                self.beds_data = beds
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load beds: {str(e)}")

    def submit(self):
        """Submit transfer"""
        try:
            bed_selection = self.new_bed.get()
            if not bed_selection:
                messagebox.showwarning("Warning", "Please select a bed")
                return

            new_bed_id = int(bed_selection.split(" - ")[0])

            with db.get_cursor() as cursor:
                # Get current bed
                cursor.execute("SELECT bed_id FROM admissions WHERE admission_id = %s", (self.admission_id,))
                result = cursor.fetchone()
                old_bed_id = result['bed_id']

                # Insert transfer record
                cursor.execute(
                    """INSERT INTO bed_transfers (admission_id, from_bed_id, to_bed_id, transfer_date, reason)
                    VALUES (%s, %s, %s, NOW(), %s)""",
                    (self.admission_id, old_bed_id, new_bed_id, self.reason.get())
                )

                # Update admission
                cursor.execute("UPDATE admissions SET bed_id = %s WHERE admission_id = %s", (new_bed_id, self.admission_id))

                # Update bed statuses
                cursor.execute("UPDATE beds SET status = 'available' WHERE bed_id = %s", (old_bed_id,))
                cursor.execute("UPDATE beds SET status = 'occupied' WHERE bed_id = %s", (new_bed_id,))

                # Log audit
                AuthenticationManager.log_audit(
                    self.user_data['user_id'],
                    "Transferred patient bed",
                    "bed_transfers",
                    cursor.lastrowid
                )

            messagebox.showinfo("Success", "Patient transferred successfully")
            self.callback()
            self.window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to transfer patient: {str(e)}")
