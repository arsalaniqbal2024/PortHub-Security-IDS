console.log("PortHub Security Dashboard Loaded");
// Alert search and filters
const alertSearch = document.getElementById("alertSearch");
const severityFilter = document.getElementById("severityFilter");
const typeFilter = document.getElementById("typeFilter");

function filterAlerts() {
    const searchText = alertSearch.value.trim().toLowerCase();
    const selectedSeverity = severityFilter.value;
    const selectedType = typeFilter.value;

    const rows = document.querySelectorAll("#alertsTable tbody tr");

    rows.forEach((row) => {
        // Handle the "No alerts detected" placeholder row
        if (row.cells.length < 7) {
            row.style.display =
                (!searchText && !selectedSeverity && !selectedType)
                    ? ""
                    : "none";
            return;
        }

        const alertType = row.cells[2].textContent.trim().toUpperCase();
        const severity = row.cells[3].textContent.trim().toUpperCase();
        const rowText = row.textContent.toLowerCase();

        const matchesSearch = rowText.includes(searchText);
        const matchesSeverity =
            !selectedSeverity || severity === selectedSeverity;
        const matchesType =
            !selectedType || alertType === selectedType;

        row.style.display =
            matchesSearch && matchesSeverity && matchesType ? "" : "none";
    });
}

if (alertSearch && severityFilter && typeFilter) {
    alertSearch.addEventListener("input", filterAlerts);
    severityFilter.addEventListener("change", filterAlerts);
    typeFilter.addEventListener("change", filterAlerts);
}
