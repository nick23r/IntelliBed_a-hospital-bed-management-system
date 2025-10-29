import mysql.connector
from mysql.connector import Error
from contextlib import contextmanager
import os

class DatabaseConnection:
    """Singleton database connection manager"""
    _instance = None
    _connection = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
        return cls._instance

    def connect(self, host='localhost', user='root', password='', database='hospital_bed_management'):
        """Establish database connection"""
        try:
            self._connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            print("[v0] Database connected successfully")
            return self._connection
        except Error as e:
            print(f"[v0] Error connecting to database: {e}")
            raise

    def get_connection(self):
        """Get current connection"""
        if self._connection is None or not self._connection.is_connected():
            self.connect()
        return self._connection

    @contextmanager
    def get_cursor(self):
        """Context manager for database cursor"""
        connection = self.get_connection()
        cursor = connection.cursor(dictionary=True)
        try:
            yield cursor
            connection.commit()
        except Error as e:
            connection.rollback()
            print(f"[v0] Database error: {e}")
            raise
        finally:
            cursor.close()

    def close(self):
        """Close database connection"""
        if self._connection and self._connection.is_connected():
            self._connection.close()
            print("[v0] Database connection closed")

# Global instance
db = DatabaseConnection()
