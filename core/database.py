import sqlite3

from config import DATABASE_NAME


class DatabaseManager:
    """Handles all SQLite database operations for PortHub Security IDS."""

    def __init__(self):
        """Initialize the database manager."""
        self.database = DATABASE_NAME

    def connect(self):
        """Create and return a SQLite database connection."""
        return sqlite3.connect(self.database)

    def initialize(self):
        """Create the alerts table if it does not already exist."""

        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS alerts (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            timestamp TEXT NOT NULL,

            alert_type TEXT NOT NULL,

            src_ip TEXT NOT NULL,

            dst_ip TEXT NOT NULL,

            severity TEXT NOT NULL,

            details TEXT NOT NULL

        )
        """)
                  # Add status column to existing databases if needed
        cursor.execute("PRAGMA table_info(alerts)")
        columns = [row[1] for row in cursor.fetchall()]

        if "status" not in columns:
            cursor.execute("""
                ALTER TABLE alerts
                ADD COLUMN status TEXT NOT NULL DEFAULT 'NEW'
            """)
        conn.commit()
        conn.close()

    def insert_alert(
        self,
        timestamp,
        alert_type,
        src_ip,
        dst_ip,
        severity,
        details
    ):
        """Insert a new IDS alert into the database."""

        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO alerts
            (
                timestamp,
                alert_type,
                src_ip,
                dst_ip,
                severity,
                details
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                timestamp,
                alert_type,
                src_ip,
                dst_ip,
                severity,
                details
            )
        )

        conn.commit()
        conn.close()

    def get_all_alerts(self):
        """Return all alerts ordered by newest first."""

        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM alerts
        ORDER BY id DESC
        """)

        alerts = cursor.fetchall()

        conn.close()

        return alerts
   
 
    def acknowledge_alert(self, alert_id):
        """Mark an alert as acknowledged."""

        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE alerts
            SET status = ?
            WHERE id = ?
            """,
            ("ACKNOWLEDGED", alert_id)
        )

        updated = cursor.rowcount > 0

        conn.commit()
        conn.close()

        return updated

    def get_total_alerts(self):
        """Return the total number of alerts."""

        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT COUNT(*)
        FROM alerts
        """)

        count = cursor.fetchone()[0]

        conn.close()

        return count

    def get_alert_count(self, alert_type):
        """Return the total number of alerts for a specific alert type."""

        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM alerts
            WHERE alert_type = ?
            """,
            (alert_type,)
        )

        count = cursor.fetchone()[0]

        conn.close()

        return count

    def get_today_alerts(self):
        """Return the number of alerts generated today."""

        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT COUNT(*)
        FROM alerts
        WHERE DATE(timestamp) = DATE('now')
        """)

        count = cursor.fetchone()[0]

        conn.close()

        return count

    def get_top_attacker(self):
        """Return the source IP with the highest number of alerts."""

        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT src_ip, COUNT(*) AS total
        FROM alerts
        GROUP BY src_ip
        ORDER BY total DESC
        LIMIT 1
        """)

        result = cursor.fetchone()

        conn.close()

        return result

    def get_top_target(self):
        """Return the most frequently targeted destination IP."""

        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT dst_ip, COUNT(*) AS total
        FROM alerts
        GROUP BY dst_ip
        ORDER BY total DESC
        LIMIT 1
        """)

        result = cursor.fetchone()

        conn.close()

        return result

    def get_top_attackers(self):
        """Return the top five attacker IP addresses."""

        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT src_ip, COUNT(*) AS total
        FROM alerts
        GROUP BY src_ip
        ORDER BY total DESC
        LIMIT 5
        """)

        results = cursor.fetchall()

        conn.close()

        return results

    def get_severity_counts(self):
        """Return the number of alerts grouped by severity."""

        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT severity, COUNT(*)
        FROM alerts
        GROUP BY severity
        """)

        results = cursor.fetchall()

        conn.close()

        return results

    def clear_database(self):
        """Delete all records from the alerts table."""

        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM alerts")

        conn.commit()
        conn.close()


database = DatabaseManager()
