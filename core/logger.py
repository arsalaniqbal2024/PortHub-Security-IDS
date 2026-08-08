from datetime import datetime

from config import ALERT_LOG_FILE
from core.database import database


def log_alert(alert_type, src_ip, dst_ip, details, severity):
    """
    Log an IDS alert to the console, log file, and SQLite database.

    Args:
        alert_type (str): Type of detected attack.
        src_ip (str): Source IP address.
        dst_ip (str): Destination IP address.
        details (str): Additional information about the alert.
        severity (str): Alert severity level.
    """

    timestamp = datetime.now()

    # ==========================================
    # Console Output
    # ==========================================

    print("\n" + "=" * 60)
    print(f"ALERT: {alert_type}")
    print("=" * 60)
    print(f"Time      : {timestamp}")
    print(f"Source IP : {src_ip}")
    print(f"Target IP : {dst_ip}")
    print(f"Details   : {details}")
    print(f"Severity  : {severity}")
    print("=" * 60)

    # ==========================================
    # Write to alerts.log
    # ==========================================

    with open(ALERT_LOG_FILE, "a", encoding="utf-8") as logfile:
        logfile.write(
            f"{timestamp} | "
            f"{alert_type} | "
            f"{src_ip} -> {dst_ip} | "
            f"{details} | "
            f"Severity={severity}\n"
        )

    # ==========================================
    # Write to SQLite Database
    # ==========================================

    database.insert_alert(
        str(timestamp),
        alert_type,
        src_ip,
        dst_ip,
        severity,
        details
    )
