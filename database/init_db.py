import mysql.connector
from mysql.connector import Error
import hashlib

def hash_password(password):
    """Hash password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def initialize_database(host='localhost', user='root', password=''):
    """Initialize database with schema and sample data"""
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        cursor = connection.cursor()

        # Read and execute schema
        with open('database/schema.sql', 'r') as f:
            schema = f.read()
            for statement in schema.split(';'):
                if statement.strip():
                    cursor.execute(statement)

        connection.commit()
        print("[v0] Database schema created successfully")

        # Insert sample data
        cursor.execute("USE hospital_bed_management")

        # Insert sample users
        users = [
            ('admin_user', hash_password('admin123'), 'admin', 'Admin User', 'admin@hospital.com'),
            ('dr_smith', hash_password('doctor123'), 'doctor', 'Dr. Smith', 'smith@hospital.com'),
            ('dr_jones', hash_password('doctor123'), 'doctor', 'Dr. Jones', 'jones@hospital.com'),
        ]
        for user in users:
            cursor.execute(
                "INSERT INTO users (username, password, role, full_name, email) VALUES (%s, %s, %s, %s, %s)",
                user
            )

        # Insert sample beds
        beds = [
            ('BED-001', 'Ward A', 'general', 'available'),
            ('BED-002', 'Ward A', 'general', 'available'),
            ('BED-003', 'Ward B', 'icu', 'available'),
            ('BED-004', 'Ward B', 'icu', 'occupied'),
            ('BED-005', 'Ward C', 'isolation', 'available'),
        ]
        for bed in beds:
            cursor.execute(
                "INSERT INTO beds (bed_number, ward, bed_type, status) VALUES (%s, %s, %s, %s)",
                bed
            )

        # Insert sample patients
        patients = [
            ('John Doe', 45, 'M', '555-0001', 'Hypertension, Diabetes'),
            ('Jane Smith', 32, 'F', '555-0002', 'Asthma'),
            ('Robert Johnson', 68, 'M', '555-0003', 'Heart Disease'),
        ]
        for patient in patients:
            cursor.execute(
                "INSERT INTO patients (patient_name, age, gender, contact_number, medical_history) VALUES (%s, %s, %s, %s, %s)",
                patient
            )

        # Insert sample ALOS statistics
        alos_data = [
            ('general', 5.5, 100, 550),
            ('icu', 8.2, 50, 410),
            ('isolation', 6.0, 30, 180),
        ]
        for data in alos_data:
            cursor.execute(
                "INSERT INTO alos_statistics (bed_type, average_los, total_admissions, total_days) VALUES (%s, %s, %s, %s)",
                data
            )

        connection.commit()
        print("[v0] Sample data inserted successfully")
        cursor.close()
        connection.close()

    except Error as e:
        print(f"[v0] Error initializing database: {e}")
        raise

if __name__ == "__main__":
    initialize_database()
