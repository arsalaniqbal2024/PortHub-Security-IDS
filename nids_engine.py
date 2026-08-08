from scapy.all import sniff

from config import INTERFACE
from core.packet_handler import process_packet
from core.database import database

print("\n" + "=" * 60)
print("        PortHub Security IDS Engine")
print("=" * 60)

print("[+] Initializing Database...")
database.initialize()

print(f"[+] Monitoring Interface : {INTERFACE}")
print("[+] Status               : RUNNING")
print("[+] Press CTRL+C to stop")
print("=" * 60 + "\n")

sniff(
    iface=INTERFACE,
    prn=process_packet,
    store=False
)
