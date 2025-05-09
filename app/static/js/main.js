document.addEventListener("DOMContentLoaded", () => {
    fetch("/api/data")
        .then(response => response.json())
        .then(data => {
            console.log("Datos desde Flask:", data);
        });
});