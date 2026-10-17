from core.database import database


def get_dashboard_statistics():

    stats = {}

    # Basic Statistics
    stats["total_alerts"] = database.get_total_alerts()
    stats["today_alerts"] = database.get_today_alerts()
    stats["new_alerts"] = database.get_status_count("NEW")
    stats["acknowledged_alerts"] = database.get_status_count("ACKNOWLEDGED")

    # Alert Counts
    stats["port_scans"] = database.get_alert_count("PORT_SCAN")
    stats["ssh_alerts"] = database.get_alert_count("SSH_CONNECTION")
    stats["ftp_alerts"] = database.get_alert_count("FTP_CONNECTION")
    stats["icmp_alerts"] = database.get_alert_count("ICMP_FLOOD")
    stats["telnet_alerts"] = database.get_alert_count("TELNET_ACCESS")

    # Analytics
    stats["top_attacker"] = database.get_top_attacker()
    stats["top_target"] = database.get_top_target()
    stats["top_attackers"] = database.get_top_attackers()

    return stats


def get_chart_data():

    return {

        "Port Scan": database.get_alert_count("PORT_SCAN"),

        "SSH": database.get_alert_count("SSH_CONNECTION"),

        "FTP": database.get_alert_count("FTP_CONNECTION"),

        "ICMP": database.get_alert_count("ICMP_FLOOD"),

        "Telnet": database.get_alert_count("TELNET_ACCESS")

    }

def get_severity_chart():

    severity = {
        "LOW": 0,
        "MEDIUM": 0,
        "HIGH": 0,
        "CRITICAL": 0
    }

    results = database.get_severity_counts()

    for level, count in results:
        severity[level] = count

    return severity

def get_top_attackers_chart():

    attackers = database.get_top_attackers()

    labels = []
    values = []

    for ip, count in attackers:

        labels.append(ip)
        values.append(count)

    return {
        "attacker_ips": labels,
        "alert_counts": values
    }
