from core.database import database


def get_dashboard_statistics():

    stats = {}

    stats["total_alerts"] = database.get_total_alerts()

    stats["today_alerts"] = database.get_today_alerts()

    stats["port_scans"] = database.get_alert_count("PORT_SCAN")

    stats["ssh_alerts"] = database.get_alert_count("SSH_CONNECTION")

    stats["ftp_alerts"] = database.get_alert_count("FTP_CONNECTION")

    stats["icmp_alerts"] = database.get_alert_count("ICMP_FLOOD")

    stats["telnet_alerts"] = database.get_alert_count("TELNET_ACCESS")

    stats["top_attacker"] = database.get_top_attacker()

    stats["top_target"] = database.get_top_target()

    stats["top_attackers"] = database.get_top_attackers()

    return stats
