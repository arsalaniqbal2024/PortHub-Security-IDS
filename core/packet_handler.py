"""
==========================================================
PortHub Security IDS - Packet Handler
==========================================================

This module acts as the central dispatcher for all captured
network packets. Each packet is validated and then forwarded
to the appropriate detection modules.
"""

from scapy.all import IP

from detectors.ftp_monitor import detect_ftp
from detectors.icmp_flood import detect_icmp_flood
from detectors.port_scan import detect_port_scan
from detectors.ssh_monitor import detect_ssh
from detectors.telnet_monitor import detect_telnet


def process_packet(packet):
    """
    Process a captured network packet.

    Every packet captured by Scapy passes through this function.
    If the packet contains an IP layer, it is forwarded to each
    detection module for analysis.

    Args:
        packet: A Scapy packet object.
    """

    # Ignore packets without an IP layer
    if not packet.haslayer(IP):
        return

    # Run all enabled detection modules
    detect_port_scan(packet)
    detect_ssh(packet)
    detect_ftp(packet)
    detect_icmp_flood(packet)
    detect_telnet(packet)
