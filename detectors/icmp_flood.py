from scapy.all import ICMP, IP
import time

from config import (
    ICMP_THRESHOLD,
    ICMP_WINDOW,
    HIGH
)

from core.tracker import icmp_tracker
from core.alert_manager import can_alert
from core.logger import log_alert


def detect_icmp_flood(packet):

    if not packet.haslayer(ICMP):
        return

    src_ip = packet[IP].src
    dst_ip = packet[IP].dst

    key = ("ICMP", src_ip, dst_ip)

    current_time = time.time()

    icmp_tracker[key].append(current_time)

    # Remove old packets
    icmp_tracker[key] = [
        t for t in icmp_tracker[key]
        if current_time - t <= ICMP_WINDOW
    ]

    if (
        len(icmp_tracker[key]) >= ICMP_THRESHOLD
        and can_alert(key)
    ):

        log_alert(
            "ICMP_FLOOD",
            src_ip,
            dst_ip,
            f"Packets={len(icmp_tracker[key])}",
            HIGH
        )
