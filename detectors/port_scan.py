from scapy.all import TCP, IP

from config import (
    PORT_SCAN_THRESHOLD,
    HIGH
)

from core.tracker import scan_tracker
from core.alert_manager import can_alert
from core.logger import log_alert


def detect_port_scan(packet):

    if not packet.haslayer(TCP):
        return

    # Only SYN packets
    if packet[TCP].flags != "S":
        return

    src_ip = packet[IP].src
    dst_ip = packet[IP].dst
    dst_port = packet[TCP].dport

    key = ("PORTSCAN", src_ip, dst_ip)

    scan_tracker[key].add(dst_port)

    if (
        len(scan_tracker[key]) >= PORT_SCAN_THRESHOLD
        and can_alert(key)
    ):

        log_alert(
            "PORT_SCAN",
            src_ip,
            dst_ip,
            f"Ports={len(scan_tracker[key])}",
            HIGH
        )
