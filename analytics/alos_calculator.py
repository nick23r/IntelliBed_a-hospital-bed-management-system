from database.connection import db
from datetime import datetime, timedelta
from decimal import Decimal

class ALOSCalculator:
    """Calculate Average Length of Stay (ALOS) and provide predictions"""

    @staticmethod
    def calculate_los_for_admission(admission_id):
        """Calculate length of stay for a specific admission"""
        try:
            with db.get_cursor() as cursor:
                cursor.execute("""
                    SELECT admission_date, discharge_date FROM admissions 
                    WHERE admission_id = %s
                """, (admission_id,))
                result = cursor.fetchone()

                if not result:
                    return None

                admission_date = result['admission_date']
                discharge_date = result['discharge_date']

                if discharge_date is None:
                    # Still admitted, calculate from admission to now
                    discharge_date = datetime.now()

                los_days = (discharge_date - admission_date).days
                return max(los_days, 1)  # Minimum 1 day
        except Exception as e:
            print(f"[v0] Error calculating LOS: {e}")
            return None

    @staticmethod
    def update_alos_statistics():
        """Update ALOS statistics for all bed types"""
        try:
            with db.get_cursor() as cursor:
                bed_types = ['general', 'icu', 'isolation']

                for bed_type in bed_types:
                    # Get all discharged admissions for this bed type
                    cursor.execute("""
                        SELECT a.admission_id, a.admission_date, a.discharge_date, b.bed_type
                        FROM admissions a
                        JOIN beds b ON a.bed_id = b.bed_id
                        WHERE b.bed_type = %s AND a.status = 'discharged' AND a.discharge_date IS NOT NULL
                    """, (bed_type,))

                    admissions = cursor.fetchall()

                    if not admissions:
                        continue

                    total_days = 0
                    for admission in admissions:
                        los = (admission['discharge_date'] - admission['admission_date']).days
                        total_days += max(los, 1)

                    average_los = Decimal(total_days) / Decimal(len(admissions))

                    # Update ALOS statistics
                    cursor.execute("""
                        UPDATE alos_statistics 
                        SET average_los = %s, total_admissions = %s, total_days = %s
                        WHERE bed_type = %s
                    """, (float(average_los), len(admissions), total_days, bed_type))

                print("[v0] ALOS statistics updated successfully")
        except Exception as e:
            print(f"[v0] Error updating ALOS statistics: {e}")

    @staticmethod
    def predict_discharge_date(admission_id):
        """Predict discharge date based on ALOS for the bed type"""
        try:
            with db.get_cursor() as cursor:
                # Get admission and bed type
                cursor.execute("""
                    SELECT a.admission_date, b.bed_type
                    FROM admissions a
                    JOIN beds b ON a.bed_id = b.bed_id
                    WHERE a.admission_id = %s
                """, (admission_id,))

                result = cursor.fetchone()
                if not result:
                    return None

                admission_date = result['admission_date']
                bed_type = result['bed_type']

                # Get average LOS for this bed type
                cursor.execute("""
                    SELECT average_los FROM alos_statistics WHERE bed_type = %s
                """, (bed_type,))

                alos_result = cursor.fetchone()
                if not alos_result or alos_result['average_los'] is None:
                    return None

                average_los = int(alos_result['average_los'])
                predicted_discharge = admission_date + timedelta(days=average_los)

                return predicted_discharge
        except Exception as e:
            print(f"[v0] Error predicting discharge date: {e}")
            return None

    @staticmethod
    def get_bed_type_statistics():
        """Get ALOS statistics for all bed types"""
        try:
            with db.get_cursor() as cursor:
                cursor.execute("""
                    SELECT bed_type, average_los, total_admissions, total_days
                    FROM alos_statistics
                    ORDER BY bed_type
                """)
                return cursor.fetchall()
        except Exception as e:
            print(f"[v0] Error getting statistics: {e}")
            return []

    @staticmethod
    def get_occupancy_rate():
        """Calculate current bed occupancy rate"""
        try:
            with db.get_cursor() as cursor:
                cursor.execute("SELECT COUNT(*) as total FROM beds")
                total_beds = cursor.fetchone()['total']

                cursor.execute("SELECT COUNT(*) as occupied FROM beds WHERE status = 'occupied'")
                occupied_beds = cursor.fetchone()['occupied']

                if total_beds == 0:
                    return 0

                occupancy_rate = (occupied_beds / total_beds) * 100
                return round(occupancy_rate, 2)
        except Exception as e:
            print(f"[v0] Error calculating occupancy rate: {e}")
            return 0

    @staticmethod
    def get_occupancy_by_bed_type():
        """Get occupancy statistics by bed type"""
        try:
            with db.get_cursor() as cursor:
                cursor.execute("""
                    SELECT 
                        b.bed_type,
                        COUNT(*) as total_beds,
                        SUM(CASE WHEN b.status = 'occupied' THEN 1 ELSE 0 END) as occupied_beds,
                        ROUND(SUM(CASE WHEN b.status = 'occupied' THEN 1 ELSE 0 END) / COUNT(*) * 100, 2) as occupancy_rate
                    FROM beds b
                    GROUP BY b.bed_type
                """)
                return cursor.fetchall()
        except Exception as e:
            print(f"[v0] Error getting occupancy by type: {e}")
            return []

    @staticmethod
    def get_admission_trends(days=30):
        """Get admission trends for the last N days"""
        try:
            with db.get_cursor() as cursor:
                cursor.execute("""
                    SELECT 
                        DATE(admission_date) as admission_day,
                        COUNT(*) as admission_count
                    FROM admissions
                    WHERE admission_date >= DATE_SUB(NOW(), INTERVAL %s DAY)
                    GROUP BY DATE(admission_date)
                    ORDER BY admission_day
                """, (days,))
                return cursor.fetchall()
        except Exception as e:
            print(f"[v0] Error getting admission trends: {e}")
            return []
