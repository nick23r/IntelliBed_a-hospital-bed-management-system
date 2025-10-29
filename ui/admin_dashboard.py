import tkinter as tk
from tkinter import messagebox, ttk as tk_ttk
from tkinter.constants import W, END, VERTICAL, HORIZONTAL
from utils.pillow_patch import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import (
    BOTH, LEFT, RIGHT, X, Y
)
from datetime import datetime, timedelta
from database.connection import db
from auth.authentication import AuthenticationManager

class AdminDashboard:
    """Admin dashboard for system configuration and analytics"""

    def __init__(self, root, user_data):
        self.root = root
        self.user_data = user_data
        self.auth_manager = AuthenticationManager()
        self.setup_ui()
        self.load_data()

    def setup_ui(self):
        """Setup admin dashboard UI"""
        self.root.title(f"Admin Dashboard - {self.user_data['full_name']}")
        self.root.geometry("1400x800")

        # Main container with notebook (tabs)
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill=BOTH, expand=True)

        # Header
        header_frame = ttk.Frame(main_frame)
        header_frame.pack(fill=X, pady=(0, 10))

        ttk.Label(header_frame, text=f"Admin Dashboard - {self.user_data['full_name']}", font=("Helvetica", 16, "bold")).pack(side=LEFT)
        ttk.Button(header_frame, text="Logout", command=self.logout, bootstyle="danger").pack(side=RIGHT)

        # Notebook for tabs
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=BOTH, expand=True)

        # Tab 1: Audit Logs
        self.audit_tab = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(self.audit_tab, text="Audit Logs")
        self.setup_audit_tab()

        # Tab 2: Bed Management
        self.bed_tab = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(self.bed_tab, text="Bed Management")
        self.setup_bed_tab()

        # Tab 3: System Statistics
        self.stats_tab = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(self.stats_tab, text="Statistics")
        self.setup_stats_tab()

    def setup_audit_tab(self):
        """Setup audit logs tab with filtering"""
        # Filter panel
        filter_frame = ttk.LabelFrame(self.audit_tab, text="Filter Audit Logs", padding=10)
        filter_frame.pack(fill=X, pady=(0, 10))

        ttk.Label(filter_frame, text="User:").pack(side=LEFT, padx=5)
        self.user_filter = ttk.Combobox(filter_frame, state="readonly", width=20)
        self.user_filter.pack(side=LEFT, padx=5)
        self.user_filter.bind("<<ComboboxSelected>>", lambda e: self.apply_audit_filters())
        self.load_users_for_filter()

        ttk.Label(filter_frame, text="Date From:").pack(side=LEFT, padx=5)
        self.date_from = ttk.Entry(filter_frame, width=15)
        self.date_from.pack(side=LEFT, padx=5)
        self.date_from.insert(0, (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d"))
        self.date_from.bind("<KeyRelease>", lambda e: self.apply_audit_filters())

        ttk.Label(filter_frame, text="Date To:").pack(side=LEFT, padx=5)
        self.date_to = ttk.Entry(filter_frame, width=15)
        self.date_to.pack(side=LEFT, padx=5)
        self.date_to.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.date_to.bind("<KeyRelease>", lambda e: self.apply_audit_filters())

        ttk.Button(filter_frame, text="Clear Filters", command=self.clear_audit_filters, bootstyle="secondary").pack(side=LEFT, padx=5)

        # Audit logs table
        table_frame = ttk.LabelFrame(self.audit_tab, text="Audit Log Records", padding=10)
        table_frame.pack(fill=BOTH, expand=True, pady=(0, 10))

        columns = ("Log ID", "User", "Action", "Table", "Record ID", "Timestamp")
        self.audit_tree = tk_ttk.Treeview(table_frame, columns=columns, height=20, show="headings")

        for col in columns:
            self.audit_tree.heading(col, text=col)
            self.audit_tree.column(col, width=200)

        scrollbar = tk_ttk.Scrollbar(table_frame, orient=VERTICAL, command=self.audit_tree.yview)
        self.audit_tree.configure(yscroll=scrollbar.set)

        self.audit_tree.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Action buttons
        action_frame = ttk.Frame(self.audit_tab)
        action_frame.pack(fill=X, pady=10)

        ttk.Button(action_frame, text="Export to CSV", command=self.export_audit_csv, bootstyle="info").pack(side=LEFT, padx=5)
        ttk.Button(action_frame, text="Refresh", command=self.load_audit_logs, bootstyle="secondary").pack(side=LEFT, padx=5)

    def setup_bed_tab(self):
        """Setup bed management tab"""
        # Add bed form
        form_frame = ttk.LabelFrame(self.bed_tab, text="Add New Bed", padding=10)
        form_frame.pack(fill=X, pady=(0, 10))

        ttk.Label(form_frame, text="Bed Number:").pack(side=LEFT, padx=5)
        self.bed_number = ttk.Entry(form_frame, width=15)
        self.bed_number.pack(side=LEFT, padx=5)

        ttk.Label(form_frame, text="Ward:").pack(side=LEFT, padx=5)
        self.bed_ward = ttk.Entry(form_frame, width=15)
        self.bed_ward.pack(side=LEFT, padx=5)

        ttk.Label(form_frame, text="Type:").pack(side=LEFT, padx=5)
        self.bed_type = ttk.Combobox(form_frame, values=["general", "icu", "isolation"], state="readonly", width=12)
        self.bed_type.pack(side=LEFT, padx=5)

        ttk.Button(form_frame, text="Add Bed", command=self.add_bed, bootstyle="success").pack(side=LEFT, padx=5)

        # Beds table
        table_frame = ttk.LabelFrame(self.bed_tab, text="All Beds", padding=10)
        table_frame.pack(fill=BOTH, expand=True, pady=(0, 10))

        columns = ("Bed ID", "Bed Number", "Ward", "Type", "Status")
        self.bed_tree = tk_ttk.Treeview(table_frame, columns=columns, height=20, show="headings")

        for col in columns:
            self.bed_tree.heading(col, text=col)
            self.bed_tree.column(col, width=200)

        scrollbar = tk_ttk.Scrollbar(table_frame, orient=VERTICAL, command=self.bed_tree.yview)
        self.bed_tree.configure(yscroll=scrollbar.set)

        self.bed_tree.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Action buttons
        action_frame = ttk.Frame(self.bed_tab)
        action_frame.pack(fill=X, pady=10)

        ttk.Button(action_frame, text="Export to CSV", command=self.export_beds_csv, bootstyle="info").pack(side=LEFT, padx=5)
        ttk.Button(action_frame, text="Refresh", command=self.load_beds, bootstyle="secondary").pack(side=LEFT, padx=5)

    def setup_stats_tab(self):
        """Setup statistics tab with enhanced details and graphs"""
        # Create scrollable frame for statistics
        canvas = tk.Canvas(self.stats_tab, bg='white', highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.stats_tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Main statistics frame
        stats_frame = ttk.LabelFrame(scrollable_frame, text="System Statistics", padding=20)
        stats_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Key metrics section
        metrics_frame = ttk.LabelFrame(stats_frame, text="Key Metrics", padding=15)
        metrics_frame.pack(fill=X, pady=(0, 15))

        self.total_beds_label = ttk.Label(metrics_frame, text="Total Beds: 0", font=("Helvetica", 12, "bold"))
        self.total_beds_label.pack(anchor=W, pady=5)

        self.occupied_beds_label = ttk.Label(metrics_frame, text="Occupied Beds: 0", font=("Helvetica", 12, "bold"))
        self.occupied_beds_label.pack(anchor=W, pady=5)

        self.available_beds_label = ttk.Label(metrics_frame, text="Available Beds: 0", font=("Helvetica", 12, "bold"))
        self.available_beds_label.pack(anchor=W, pady=5)

        self.occupancy_rate_label = ttk.Label(metrics_frame, text="Occupancy Rate: 0%", font=("Helvetica", 12, "bold"))
        self.occupancy_rate_label.pack(anchor=W, pady=5)

        self.active_admissions_label = ttk.Label(metrics_frame, text="Active Admissions: 0", font=("Helvetica", 12, "bold"))
        self.active_admissions_label.pack(anchor=W, pady=5)

        self.total_admissions_label = ttk.Label(metrics_frame, text="Total Admissions (All Time): 0", font=("Helvetica", 12, "bold"))
        self.total_admissions_label.pack(anchor=W, pady=5)

        ttk.Separator(stats_frame, orient=HORIZONTAL).pack(fill=X, pady=15)

        # ALOS section
        alos_frame = ttk.LabelFrame(stats_frame, text="Average Length of Stay (ALOS)", padding=15)
        alos_frame.pack(fill=X, pady=(0, 15))

        self.alos_tree = tk_ttk.Treeview(alos_frame, columns=("Bed Type", "ALOS (days)", "Total Admissions", "Total Days"), height=5, show="headings")
        self.alos_tree.heading("Bed Type", text="Bed Type")
        self.alos_tree.heading("ALOS (days)", text="ALOS (days)")
        self.alos_tree.heading("Total Admissions", text="Total Admissions")
        self.alos_tree.heading("Total Days", text="Total Days")

        self.alos_tree.column("Bed Type", width=120)
        self.alos_tree.column("ALOS (days)", width=120)
        self.alos_tree.column("Total Admissions", width=150)
        self.alos_tree.column("Total Days", width=120)

        self.alos_tree.pack(fill=X, pady=10)

        ttk.Separator(stats_frame, orient=HORIZONTAL).pack(fill=X, pady=15)

        # Bed type distribution section
        bed_dist_frame = ttk.LabelFrame(stats_frame, text="Bed Distribution by Type", padding=15)
        bed_dist_frame.pack(fill=X, pady=(0, 15))

        self.bed_dist_tree = tk_ttk.Treeview(bed_dist_frame, columns=("Bed Type", "Count", "Occupied", "Available"), height=5, show="headings")
        self.bed_dist_tree.heading("Bed Type", text="Bed Type")
        self.bed_dist_tree.heading("Count", text="Total Count")
        self.bed_dist_tree.heading("Occupied", text="Occupied")
        self.bed_dist_tree.heading("Available", text="Available")

        self.bed_dist_tree.column("Bed Type", width=120)
        self.bed_dist_tree.column("Count", width=120)
        self.bed_dist_tree.column("Occupied", width=120)
        self.bed_dist_tree.column("Available", width=120)

        self.bed_dist_tree.pack(fill=X, pady=10)

        ttk.Separator(stats_frame, orient=HORIZONTAL).pack(fill=X, pady=15)

        # Action buttons
        button_frame = ttk.Frame(stats_frame)
        button_frame.pack(fill=X, pady=10)

        ttk.Button(button_frame, text="Refresh Statistics", command=self.load_statistics, bootstyle="secondary").pack(side=LEFT, padx=5)
        ttk.Button(button_frame, text="Export Statistics to CSV", command=self.export_statistics_csv, bootstyle="info").pack(side=LEFT, padx=5)
        ttk.Button(button_frame, text="Generate Graphs", command=self.generate_statistics_graphs, bootstyle="success").pack(side=LEFT, padx=5)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def load_users_for_filter(self):
        """Load users for audit filter dropdown"""
        try:
            with db.get_cursor() as cursor:
                cursor.execute("SELECT user_id, full_name FROM users")
                users = cursor.fetchall()
                user_list = ["All"] + [f"{u['user_id']} - {u['full_name']}" for u in users]
                self.user_filter.configure(values=user_list)
                self.user_filter.current(0)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load users: {str(e)}")

    def load_audit_logs(self):
        """Load audit logs from database"""
        try:
            with db.get_cursor() as cursor:
                cursor.execute("""
                    SELECT al.log_id, u.full_name, al.action, al.table_name, al.record_id, al.timestamp
                    FROM audit_logs al
                    JOIN users u ON al.user_id = u.user_id
                    ORDER BY al.timestamp DESC
                    LIMIT 1000
                """)
                self.all_audit_data = cursor.fetchall()
                self.display_audit_logs(self.all_audit_data)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load audit logs: {str(e)}")

    def display_audit_logs(self, data):
        """Display audit logs in treeview"""
        for item in self.audit_tree.get_children():
            self.audit_tree.delete(item)

        for row in data:
            self.audit_tree.insert("", END, values=(
                row['log_id'],
                row['full_name'],
                row['action'],
                row['table_name'] or "",
                row['record_id'] or "",
                row['timestamp'].strftime("%Y-%m-%d %H:%M:%S") if row['timestamp'] else ""
            ))

    def apply_audit_filters(self):
        """Apply audit log filters"""
        user_filter = self.user_filter.get()
        date_from = self.date_from.get()
        date_to = self.date_to.get()

        filtered_data = self.all_audit_data

        if user_filter != "All":
            user_id = int(user_filter.split(" - ")[0])
            filtered_data = [row for row in filtered_data if row['user_id'] == user_id]

        try:
            if date_from:
                date_from_obj = datetime.strptime(date_from, "%Y-%m-%d")
                filtered_data = [row for row in filtered_data if row['timestamp'].date() >= date_from_obj.date()]

            if date_to:
                date_to_obj = datetime.strptime(date_to, "%Y-%m-%d")
                filtered_data = [row for row in filtered_data if row['timestamp'].date() <= date_to_obj.date()]
        except ValueError:
            messagebox.showwarning("Warning", "Invalid date format. Use YYYY-MM-DD")
            return

        self.display_audit_logs(filtered_data)

    def clear_audit_filters(self):
        """Clear audit filters"""
        self.user_filter.current(0)
        self.date_from.delete(0, tk.END)
        self.date_from.insert(0, (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d"))
        self.date_to.delete(0, tk.END)
        self.date_to.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.display_audit_logs(self.all_audit_data)

    def load_beds(self):
        """Load beds from database"""
        try:
            with db.get_cursor() as cursor:
                cursor.execute("SELECT bed_id, bed_number, ward, bed_type, status FROM beds ORDER BY bed_number")
                beds = cursor.fetchall()

            for item in self.bed_tree.get_children():
                self.bed_tree.delete(item)

            for bed in beds:
                self.bed_tree.insert("", END, values=(
                    bed['bed_id'],
                    bed['bed_number'],
                    bed['ward'],
                    bed['bed_type'],
                    bed['status']
                ))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load beds: {str(e)}")

    def add_bed(self):
        """Add new bed"""
        try:
            bed_number = self.bed_number.get().strip()
            ward = self.bed_ward.get().strip()
            bed_type = self.bed_type.get()

            if not bed_number or not ward or not bed_type:
                messagebox.showwarning("Warning", "Please fill all fields")
                return

            with db.get_cursor() as cursor:
                cursor.execute(
                    "INSERT INTO beds (bed_number, ward, bed_type, status) VALUES (%s, %s, %s, 'available')",
                    (bed_number, ward, bed_type)
                )
                self.auth_manager.log_audit(
                    self.user_data['user_id'],
                    "Added new bed",
                    "beds",
                    cursor.lastrowid
                )

            messagebox.showinfo("Success", "Bed added successfully")
            self.bed_number.delete(0, tk.END)
            self.bed_ward.delete(0, tk.END)
            self.bed_type.set("")
            self.load_beds()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add bed: {str(e)}")

    def load_statistics(self):
        """Load system statistics"""
        try:
            with db.get_cursor() as cursor:
                # Total beds
                cursor.execute("SELECT COUNT(*) as count FROM beds")
                total_beds = cursor.fetchone()['count']

                # Occupied beds
                cursor.execute("SELECT COUNT(*) as count FROM beds WHERE status = 'occupied'")
                occupied_beds = cursor.fetchone()['count']

                # Available beds
                cursor.execute("SELECT COUNT(*) as count FROM beds WHERE status = 'available'")
                available_beds = cursor.fetchone()['count']

                # Active admissions
                cursor.execute("SELECT COUNT(*) as count FROM admissions WHERE status = 'active'")
                active_admissions = cursor.fetchone()['count']

                # Total admissions (all time)
                cursor.execute("SELECT COUNT(*) as count FROM admissions")
                total_admissions = cursor.fetchone()['count']

                # Calculate occupancy rate
                occupancy_rate = (occupied_beds / total_beds * 100) if total_beds > 0 else 0

                # Update labels
                self.total_beds_label.configure(text=f"Total Beds: {total_beds}")
                self.occupied_beds_label.configure(text=f"Occupied Beds: {occupied_beds}")
                self.available_beds_label.configure(text=f"Available Beds: {available_beds}")
                self.occupancy_rate_label.configure(text=f"Occupancy Rate: {occupancy_rate:.1f}%")
                self.active_admissions_label.configure(text=f"Active Admissions: {active_admissions}")
                self.total_admissions_label.configure(text=f"Total Admissions (All Time): {total_admissions}")

                # Load ALOS data
                cursor.execute("SELECT bed_type, average_los, total_admissions, total_days FROM alos_statistics")
                alos_data = cursor.fetchall()

                for item in self.alos_tree.get_children():
                    self.alos_tree.delete(item)

                for row in alos_data:
                    self.alos_tree.insert("", END, values=(
                        row['bed_type'],
                        f"{row['average_los']:.2f}",
                        row['total_admissions'],
                        row['total_days']
                    ))

                cursor.execute("""
                    SELECT bed_type, COUNT(*) as count,
                           SUM(CASE WHEN status = 'occupied' THEN 1 ELSE 0 END) as occupied,
                           SUM(CASE WHEN status = 'available' THEN 1 ELSE 0 END) as available
                    FROM beds
                    GROUP BY bed_type
                """)
                bed_dist_data = cursor.fetchall()

                for item in self.bed_dist_tree.get_children():
                    self.bed_dist_tree.delete(item)

                for row in bed_dist_data:
                    self.bed_dist_tree.insert("", END, values=(
                        row['bed_type'],
                        row['count'],
                        row['occupied'],
                        row['available']
                    ))

                # Store data for export
                self.current_alos_data = alos_data
                self.current_bed_dist_data = bed_dist_data

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load statistics: {str(e)}")

    def export_audit_csv(self):
        """Export audit logs to CSV"""
        from utils.csv_export import export_audit_logs_to_csv
        try:
            filename = export_audit_logs_to_csv(self.all_audit_data)
            messagebox.showinfo("Success", f"Audit logs exported to {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export: {str(e)}")

    def export_beds_csv(self):
        """Export beds to CSV"""
        from utils.csv_export import export_beds_to_csv
        try:
            # Get current beds data
            with db.get_cursor() as cursor:
                cursor.execute("SELECT bed_id, bed_number, ward, bed_type, status FROM beds ORDER BY bed_number")
                beds_data = cursor.fetchall()
            
            filename = export_beds_to_csv(beds_data)
            messagebox.showinfo("Success", f"Beds exported to {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export: {str(e)}")

    def export_statistics_csv(self):
        """Export statistics to CSV"""
        from utils.csv_export import export_alos_statistics_to_csv
        try:
            filename = export_alos_statistics_to_csv(self.current_alos_data)
            messagebox.showinfo("Success", f"Statistics exported to {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export: {str(e)}")

    def generate_statistics_graphs(self):
        """Generate statistics graphs"""
        from utils.statistics_graphs import StatisticsGraphs
        try:
            with db.get_cursor() as cursor:
                # Get bed status data
                cursor.execute("SELECT COUNT(*) as count FROM beds WHERE status = 'occupied'")
                occupied_beds = cursor.fetchone()['count']
                
                cursor.execute("SELECT COUNT(*) as count FROM beds WHERE status = 'available'")
                available_beds = cursor.fetchone()['count']
                
                cursor.execute("SELECT COUNT(*) as count FROM beds")
                total_beds = cursor.fetchone()['count']

                # Generate bed status pie chart
                StatisticsGraphs.generate_bed_status_pie_chart(total_beds, occupied_beds, available_beds)

                # Generate ALOS bar chart
                StatisticsGraphs.generate_alos_bar_chart(self.current_alos_data)

                # Generate bed type distribution chart
                StatisticsGraphs.generate_bed_type_distribution_chart(self.current_bed_dist_data)

                # Get admissions trend data
                cursor.execute("""
                    SELECT DATE(admission_date) as date, COUNT(*) as count
                    FROM admissions
                    WHERE admission_date >= DATE_SUB(NOW(), INTERVAL 30 DAY)
                    GROUP BY DATE(admission_date)
                    ORDER BY date
                """)
                admissions_trend = cursor.fetchall()

                if admissions_trend:
                    StatisticsGraphs.generate_admissions_trend_chart(admissions_trend)

            messagebox.showinfo("Success", "Graphs generated successfully! Check the 'graphs' folder.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate graphs: {str(e)}")

    def load_data(self):
        """Load all data"""
        self.load_audit_logs()
        self.load_beds()
        self.load_statistics()

    def logout(self):
        """Logout and return to login"""
        self.root.quit()
