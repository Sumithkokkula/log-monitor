let allLogs = [];

async function loadLogs() {
    const res = await fetch("http://127.0.0.1:8000/logs");
    const data = await res.json();

    allLogs = data;
    displayLogs(allLogs);
}

function displayLogs(logs) {
    const container = document.getElementById("logs");
    container.innerHTML = "";

    logs.forEach(log => {
        const div = document.createElement("div");
        div.className = "log " + log.level;

        div.innerHTML = `
            <strong>${log.level}</strong> - ${log.message}<br>
            <small>${new Date(log.timestamp).toLocaleString()}</small>
        `;

        container.appendChild(div);
    });
}


function filterLogs(level) {
    const filtered = allLogs.filter(log => log.level === level);
    displayLogs(filtered);

    document.getElementById("totalLogs").innerText = filtered.length;
    document.getElementById("errorLogs").innerText = filtered.filter(l => l.level === "ERROR").length;
    document.getElementById("infoLogs").innerText = filtered.filter(l => l.level === "INFO").length;
}


async function searchLogs() {
    const keyword = document.getElementById("search").value;

    const res = await fetch(`http://127.0.0.1:8000/logs/search?keyword=${keyword}`);
    const data = await res.json();

    displayLogs(data);
}

// Auto refresh
setInterval(loadLogs, 5000);

function showSection(section) {
    document.querySelectorAll(".sidebar li").forEach(li => li.classList.remove("active"));

    event.target.classList.add("active");

    document.getElementById("dashboardSection").style.display = "none";
    document.getElementById("logsSection").style.display = "none";
    document.getElementById("alertsSection").style.display = "none";

    document.getElementById(section + "Section").style.display = "block";
}
