from flask import render_template

from app import app

from core.database import database

from services.statistics_service import (
    get_dashboard_statistics,
    get_chart_data,
    get_severity_chart,
    get_top_attackers_chart
)

from services.risk_service import calculate_risk


@app.route("/")
def dashboard():

    # Dashboard Statistics
    stats = get_dashboard_statistics()

    # Risk Score
    risk_score, status = calculate_risk()

    # Chart Data
    chart_data = get_chart_data()

    severity_chart = get_severity_chart()

    top_attackers_chart = get_top_attackers_chart()

    # Recent Alerts
    alerts = database.get_all_alerts()

    formatted_alerts = []

    for alert in alerts:

        formatted_alerts.append({

            "id": alert[0],
            "timestamp": alert[1],
            "alert_type": alert[2],
            "src_ip": alert[3],
            "dst_ip": alert[4],
            "severity": alert[5],
            "details": alert[6]

        })

    return render_template(

        "dashboard.html",

        stats=stats,

        alerts=formatted_alerts,

        risk={
            "score": risk_score,
            "status": status
        },

        chart_data=chart_data,
        severity_chart=severity_chart,
        top_attackers_chart=top_attackers_chart

    )
