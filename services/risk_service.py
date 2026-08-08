from services.statistics_service import get_dashboard_statistics


def calculate_risk():

    stats = get_dashboard_statistics()

    risk_score = 0

    risk_score += stats["port_scans"] * 30
    risk_score += stats["ssh_alerts"] * 50
    risk_score += stats["ftp_alerts"] * 50
    risk_score += stats["icmp_alerts"] * 40
    risk_score += stats["telnet_alerts"] * 20

    if risk_score >= 100:
        status = "CRITICAL"

    elif risk_score >= 50:
        status = "HIGH"

    else:
        status = "MEDIUM"

    return risk_score, status
