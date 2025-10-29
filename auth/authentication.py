import hashlib
from database.connection import db

class AuthenticationManager:
    """Handle user authentication and authorization"""

    @staticmethod
    def hash_password(password):
        """Hash password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def verify_password(stored_hash, provided_password):
        """Verify password against stored hash"""
        return stored_hash == AuthenticationManager.hash_password(provided_password)

    @staticmethod
    def authenticate_user(username, password):
        """Authenticate user and return user data if valid"""
        try:
            with db.get_cursor() as cursor:
                cursor.execute(
                    "SELECT user_id, username, role, full_name, email FROM users WHERE username = %s",
                    (username,)
                )
                user = cursor.fetchone()

                if user is None:
                    return None, "Invalid username or password"

                # Get stored password
                cursor.execute("SELECT password FROM users WHERE user_id = %s", (user['user_id'],))
                result = cursor.fetchone()
                stored_password = result['password']

                if not AuthenticationManager.verify_password(stored_password, password):
                    return None, "Invalid username or password"

                return user, None
        except Exception as e:
            return None, f"Authentication error: {str(e)}"

    @staticmethod
    def log_audit(user_id, action, table_name=None, record_id=None, old_value=None, new_value=None):
        """Log user actions for audit trail"""
        try:
            with db.get_cursor() as cursor:
                cursor.execute(
                    """INSERT INTO audit_logs 
                    (user_id, action, table_name, record_id, old_value, new_value) 
                    VALUES (%s, %s, %s, %s, %s, %s)""",
                    (user_id, action, table_name, record_id, old_value, new_value)
                )
        except Exception as e:
            print(f"[v0] Error logging audit: {e}")
