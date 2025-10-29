import csv
import os
from datetime import datetime

class CSVExporter:
    """Export data to CSV files"""

    @staticmethod
    def create_export_directory():
        """Create exports directory if it doesn't exist"""
        if not os.path.exists("exports"):
            os.makedirs("exports")
        return "exports"

    @staticmethod
    def export_audit_logs_to_csv(audit_data):
        """Export audit logs to CSV"""
        try:
            export_dir = CSVExporter.create_export_directory()
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(export_dir, f"audit_logs_{timestamp}.csv")

            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['Log ID', 'User', 'Action', 'Table', 'Record ID', 'Timestamp']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for row in audit_data:
                    writer.writerow({
                        'Log ID': row['log_id'],
                        'User': row['full_name'],
                        'Action': row['action'],
                        'Table': row['table_name'] or '',
                        'Record ID': row['record_id'] or '',
                        'Timestamp': row['timestamp'].strftime("%Y-%m-%d %H:%M:%S") if row['timestamp'] else ''
                    })

            print(f"[v0] Audit logs exported to {filename}")
            return filename
        except Exception as e:
            print(f"[v0] Error exporting audit logs: {e}")
            raise

    @staticmethod
    def export_admissions_to_csv(admissions_data):
        """Export admissions data to CSV"""
        try:
            export_dir = CSVExporter.create_export_directory()
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(export_dir, f"admissions_{timestamp}.csv")

            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['Admission ID', 'Patient Name', 'Age', 'Gender', 'Bed Number', 
                            'Ward', 'Admission Date', 'Discharge Date', 'Reason', 'Status', 'Doctor']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for row in admissions_data:
                    writer.writerow({
                        'Admission ID': row.get('admission_id', ''),
                        'Patient Name': row.get('patient_name', ''),
                        'Age': row.get('age', ''),
                        'Gender': row.get('gender', ''),
                        'Bed Number': row.get('bed_number', ''),
                        'Ward': row.get('ward', ''),
                        'Admission Date': row.get('admission_date', ''),
                        'Discharge Date': row.get('discharge_date', ''),
                        'Reason': row.get('admission_reason', ''),
                        'Status': row.get('status', ''),
                        'Doctor': row.get('doctor_name', '')
                    })

            print(f"[v0] Admissions exported to {filename}")
            return filename
        except Exception as e:
            print(f"[v0] Error exporting admissions: {e}")
            raise

    @staticmethod
    def export_beds_to_csv(beds_data):
        """Export beds data to CSV"""
        try:
            export_dir = CSVExporter.create_export_directory()
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(export_dir, f"beds_{timestamp}.csv")

            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['Bed ID', 'Bed Number', 'Ward', 'Type', 'Status']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for row in beds_data:
                    writer.writerow({
                        'Bed ID': row['bed_id'],
                        'Bed Number': row['bed_number'],
                        'Ward': row['ward'],
                        'Type': row['bed_type'],
                        'Status': row['status']
                    })

            print(f"[v0] Beds exported to {filename}")
            return filename
        except Exception as e:
            print(f"[v0] Error exporting beds: {e}")
            raise

    @staticmethod
    def export_alos_statistics_to_csv(alos_data):
        """Export ALOS statistics to CSV"""
        try:
            export_dir = CSVExporter.create_export_directory()
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(export_dir, f"alos_statistics_{timestamp}.csv")

            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['Bed Type', 'Average LOS (days)', 'Total Admissions', 'Total Days']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for row in alos_data:
                    writer.writerow({
                        'Bed Type': row['bed_type'],
                        'Average LOS (days)': f"{row['average_los']:.2f}" if row['average_los'] else 'N/A',
                        'Total Admissions': row['total_admissions'],
                        'Total Days': row['total_days']
                    })

            print(f"[v0] ALOS statistics exported to {filename}")
            return filename
        except Exception as e:
            print(f"[v0] Error exporting ALOS statistics: {e}")
            raise

    @staticmethod
    def export_bed_transfers_to_csv(transfers_data):
        """Export bed transfers to CSV"""
        try:
            export_dir = CSVExporter.create_export_directory()
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(export_dir, f"bed_transfers_{timestamp}.csv")

            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['Transfer ID', 'Admission ID', 'From Bed', 'To Bed', 'Transfer Date', 'Reason']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for row in transfers_data:
                    writer.writerow({
                        'Transfer ID': row['transfer_id'],
                        'Admission ID': row['admission_id'],
                        'From Bed': row['from_bed_number'],
                        'To Bed': row['to_bed_number'],
                        'Transfer Date': row['transfer_date'].strftime("%Y-%m-%d %H:%M:%S") if row['transfer_date'] else '',
                        'Reason': row['reason'] or ''
                    })

            print(f"[v0] Bed transfers exported to {filename}")
            return filename
        except Exception as e:
            print(f"[v0] Error exporting bed transfers: {e}")
            raise


# Convenience functions for direct use
def export_audit_logs_to_csv(audit_data):
    """Export audit logs to CSV"""
    return CSVExporter.export_audit_logs_to_csv(audit_data)

def export_admissions_to_csv(admissions_data):
    """Export admissions to CSV"""
    return CSVExporter.export_admissions_to_csv(admissions_data)

def export_beds_to_csv(beds_data):
    """Export beds to CSV"""
    return CSVExporter.export_beds_to_csv(beds_data)

def export_alos_statistics_to_csv(alos_data):
    """Export ALOS statistics to CSV"""
    return CSVExporter.export_alos_statistics_to_csv(alos_data)

def export_bed_transfers_to_csv(transfers_data):
    """Export bed transfers to CSV"""
    return CSVExporter.export_bed_transfers_to_csv(transfers_data)
