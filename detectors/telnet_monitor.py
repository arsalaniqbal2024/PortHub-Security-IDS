from scapy.all import TCP, IP

from config import MEDIUM

from core.alert_manager import can_alert
from core.logger import log_alert


def detect_telnet(packet):

    if not packet.haslayer(TCP):
        return

    # Only Telnet traffic
    if packet[TCP].dport != 23:
        return

    # Ignore SYN packets (prevents Nmap scans from triggering)
    if packet[TCP].flags == "S":
        return

    # Require actual payload
    if len(packet[TCP].payload) == 0:
        return

    src_ip = packet[IP].src
    dst_ip = packet[IP].dst

    key = ("TELNET", src_ip, dst_ip)

    if can_alert(key):

        log_alert(
            "TELNET_ACCESS",
            src_ip,
            dst_ip,
            "Established Telnet Session",
            MEDIUM
        )
