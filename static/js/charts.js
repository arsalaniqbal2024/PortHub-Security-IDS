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

                    "#FF6577",
                    "#22D3EE",
                    "#F5B942",
                    "#39F59A",
                    "#71899B"

                ],

                borderColor: "#0E1B2A",

                borderWidth: 2

            }]

        },

        options: {

            responsive: true,

            plugins: {

                legend: {

                    labels: {

                        color: "#C4D3DF"

                    }

                },

                tooltip: {

                    backgroundColor: "#102235",

                    titleColor: "#E5F0F7",

                    bodyColor: "#C4D3DF",

                    borderColor: "#31536A",

                    borderWidth: 1

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

                    "#39F59A",

                    "#54C7E8",

                    "#F5B942",

                    "#FF6577"

                ],

                borderColor: "#0E1B2A",

                borderWidth: 2

            }]

        },

        options: {

            responsive: true,

            plugins: {

                legend: {

                    labels: {

                        color: "#C4D3DF"

                    }

                },

                tooltip: {

                    backgroundColor: "#102235",

                    titleColor: "#E5F0F7",

                    bodyColor: "#C4D3DF",

                    borderColor: "#31536A",

                    borderWidth: 1

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

                data: attackerValues,

                backgroundColor: "#22D3EE",

                borderColor: "#22D3EE",

                borderWidth: 1,

                borderRadius: 3

            }]

        },

        options: {

            responsive: true,

            plugins: {

                legend: {

                    labels: {

                        color: "#C4D3DF"

                    }

                },

                tooltip: {

                    backgroundColor: "#102235",

                    titleColor: "#E5F0F7",

                    bodyColor: "#C4D3DF",

                    borderColor: "#31536A",

                    borderWidth: 1

                }

            },

            scales: {

                x: {

                    grid: {

                        color: "rgba(148,170,188,.14)"

                    },

                    border: {

                        color: "rgba(148,170,188,.28)"

                    },

                    ticks: {

                        color: "#C4D3DF"

                    }

                },

                y: {

                    beginAtZero: true,

                    grid: {

                        color: "rgba(148,170,188,.14)"

                    },

                    border: {

                        color: "rgba(148,170,188,.28)"

                    },

                    ticks: {

                        color: "#C4D3DF"

                    }

                }

            }

        }

    });

}
