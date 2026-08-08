"""
==========================================================
PortHub Security IDS - Runtime Trackers
==========================================================

This module stores in-memory data structures used by the
IDS detection engine. These trackers maintain temporary
state while the application is running and are not
persisted to the database.
"""

from collections import defaultdict

# ==========================================================
# Port Scan Tracker
# ==========================================================
# Stores unique destination ports accessed by each source IP.
# Format:
# {
#     "192.168.1.10": {22, 80, 443}
# }
scan_tracker = defaultdict(set)

# ==========================================================
# SSH Brute Force Tracker
# ==========================================================
# Stores timestamps of SSH connection attempts per source IP.
# Format:
# {
#     "192.168.1.10": [timestamp1, timestamp2, ...]
# }
ssh_tracker = defaultdict(list)

# ==========================================================
# FTP Brute Force Tracker
# ==========================================================
# Stores timestamps of FTP connection attempts per source IP.
ftp_tracker = defaultdict(list)

# ==========================================================
# ICMP Flood Tracker
# ==========================================================
# Stores timestamps of ICMP packets received per source IP.
icmp_tracker = defaultdict(list)

# ==========================================================
# Alert Cooldown Tracker
# ==========================================================
# Stores the timestamp of the most recent alert for each
# alert key to prevent duplicate alerts.
#
# Format:
# {
#     "PORT_SCAN_192.168.1.10": 1752938517.63
# }
last_alert_time = {}
