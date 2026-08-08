// ======================================
// Alert Type Pie Chart
// ======================================

const pieCanvas = document.getElementById("alertPieChart");

if (pieCanvas) {

    new Chart(pieCanvas, {

        type: "pie",

        data: {

            labels: [
                "Port Scan",
                "SSH",
                "FTP",
                "ICMP",
                "Telnet"
            ],

            datasets: [{

                data: chartValues,

                backgroundColor: [

                    "#dc3545",
                    "#0d6efd",
                    "#ffc107",
                    "#198754",
                    "#6c757d"

                ]

            }]

        },

        options: {

            responsive: true,

            plugins: {

                legend: {

                    labels: {

                        color: "white"

                    }

                }

            }

        }

    });

}



// ======================================
// Severity Doughnut Chart
// ======================================

const severityCanvas = document.getElementById("severityChart");

if (severityCanvas) {

    new Chart(severityCanvas, {

        type: "doughnut",

        data: {

            labels: [

                "Low",

                "Medium",

                "High",

                "Critical"

            ],

            datasets: [{

                data: severityValues,

                backgroundColor: [

                    "#28a745",

                    "#17a2b8",

                    "#ffc107",

                    "#dc3545"

                ]

            }]

        },

        options: {

            responsive: true,

            plugins: {

                legend: {

                    labels: {

                        color: "white"

                    }

                }

            }

        }

    });

}



// ======================================
// Top Attackers Bar Chart
// ======================================

const attackerCanvas = document.getElementById("attackerChart");

if (attackerCanvas) {

    new Chart(attackerCanvas, {

        type: "bar",

        data: {

            labels: attackerLabels,

            datasets: [{

                label: "Alerts",

                data: attackerValues

            }]

        },

        options: {

            responsive: true,

            plugins: {

                legend: {

                    labels: {

                        color: "white"

                    }

                }

            },

            scales: {

                x: {

                    ticks: {

                        color: "white"

                    }

                },

                y: {

                    beginAtZero: true,

                    ticks: {

                        color: "white"

                    }

                }

            }

        }

    });

}
