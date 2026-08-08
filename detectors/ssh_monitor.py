from scapy.all import TCP, IP
import time

from config import (
    SSH_THRESHOLD,
    SSH_WINDOW,
    HIGH
)

from core.tracker import ssh_tracker
from core.alert_manager import can_alert
from core.logger import log_alert


def detect_ssh(packet):

    if not packet.haslayer(TCP):
        return

    if packet[TCP].dport != 22:
        return

    if packet[TCP].flags != "S":
        return

    src_ip = packet[IP].src
    dst_ip = packet[IP].dst

    key = ("SSH", src_ip, dst_ip)

    current_time = time.time()

    ssh_tracker[key].append(current_time)

    ssh_tracker[key] = [
        t for t in ssh_tracker[key]
        if current_time - t <= SSH_WINDOW
    ]

    if (
        len(ssh_tracker[key]) >= SSH_THRESHOLD
        and can_alert(key)
    ):

        log_alert(
            "SSH_CONNECTION",
            src_ip,
            dst_ip,
            f"Connections={len(ssh_tracker[key])}",
            HIGH
        )
