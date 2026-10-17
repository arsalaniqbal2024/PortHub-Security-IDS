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
// Dynamic export button and CSV export
const exportButton = document.getElementById("exportFilteredAlerts");
const exportButtonLabel = document.getElementById("exportButtonLabel");

const searchInputForExport = document.getElementById("alertSearch");
const severitySelectForExport = document.getElementById("severityFilter");
const typeSelectForExport = document.getElementById("typeFilter");

if (
    exportButton &&
    exportButtonLabel &&
    searchInputForExport &&
    severitySelectForExport &&
    typeSelectForExport
) {
    function updateExportButtonLabel() {
        const filtersApplied =
            searchInputForExport.value.trim() !== "" ||
            severitySelectForExport.value !== "" ||
            typeSelectForExport.value !== "";

        exportButtonLabel.textContent = filtersApplied
            ? "Export Filtered Alerts"
            : "Export Alerts";
    }

    [
        searchInputForExport,
        severitySelectForExport,
        typeSelectForExport
    ].forEach((control) => {
        control.addEventListener("input", updateExportButtonLabel);
        control.addEventListener("change", updateExportButtonLabel);
    });

    exportButton.addEventListener("click", function () {
        const table = document.getElementById("alertsTable");

        const headers = Array.from(table.querySelectorAll("thead th"))
            .map((cell) => cell.innerText.trim());

        const visibleRows = Array.from(
            table.querySelectorAll("tbody tr")
        ).filter((row) => {
            return row.cells.length === 7 &&
                   row.style.display !== "none";
        });

        const escapeCSV = (value) =>
            '"' + String(value).replace(/"/g, '""') + '"';

        const csvRows = [
            headers,
            ...visibleRows.map((row) =>
                Array.from(row.cells).map((cell) => cell.innerText.trim())
            )
        ];

        const csvContent = csvRows
            .map((row) => row.map(escapeCSV).join(","))
            .join("\r\n");

        const blob = new Blob(["\uFEFF", csvContent], {
            type: "text/csv;charset=utf-8;"
        });

        const downloadURL = URL.createObjectURL(blob);
        const downloadLink = document.createElement("a");

        const filtersApplied =
            searchInputForExport.value.trim() !== "" ||
            severitySelectForExport.value !== "" ||
            typeSelectForExport.value !== "";

        downloadLink.href = downloadURL;
        downloadLink.download = filtersApplied
            ? "porthub_filtered_alerts.csv"
            : "porthub_alerts.csv";

        document.body.appendChild(downloadLink);
        downloadLink.click();
        downloadLink.remove();

        setTimeout(() => URL.revokeObjectURL(downloadURL), 1000);
    });

    updateExportButtonLabel();
}