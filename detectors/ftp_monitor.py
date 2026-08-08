from scapy.all import TCP, IP
import time

from config import (
    FTP_THRESHOLD,
    FTP_WINDOW,
    HIGH
)

from core.tracker import ftp_tracker
from core.alert_manager import can_alert
from core.logger import log_alert


def detect_ftp(packet):

    if not packet.haslayer(TCP):
        return

    if packet[TCP].dport != 21:
        return

    # Count only SYN packets (connection attempts)
    if packet[TCP].flags != "S":
        return

    src_ip = packet[IP].src
    dst_ip = packet[IP].dst

    key = ("FTP", src_ip, dst_ip)

    current_time = time.time()

    ftp_tracker[key].append(current_time)

    # Keep only recent attempts
    ftp_tracker[key] = [
        t for t in ftp_tracker[key]
        if current_time - t <= FTP_WINDOW
    ]

    if (
        len(ftp_tracker[key]) >= FTP_THRESHOLD
        and can_alert(key)
    ):

        log_alert(
            "FTP_CONNECTION",
            src_ip,
            dst_ip,
            f"Connections={len(ftp_tracker[key])}",
            HIGH
        )
