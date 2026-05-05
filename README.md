# 📋 Log Monitoring SaaS Dashboard

<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"/>
</p>

> A full-stack real-time log monitoring system with a modern SaaS-style dashboard — ingest, filter, search, and analyze application logs through a clean web UI.

---

## 🚨 The Problem

When applications break in production, engineers waste hours grepping through raw log files with no structure, no filtering, and no visibility. This system turns chaotic log streams into a queryable, visual dashboard.

---

## ✨ Features

- ⚡ **Real-time log streaming** — new logs appear instantly without page refresh
- 🔍 **Advanced filtering** — filter by severity (ERROR, WARN, INFO), timestamp range, and keywords
- 📊 **Dashboard with live stats** — log counts, error rates, severity breakdown
- 🚨 **Alerts panel** — surface critical errors automatically
- 🧪 **Built-in log generator** — simulate log traffic for testing
- 🐳 **Dockerized** — consistent deployment across any environment

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend API | FastAPI + Uvicorn |
| Database | SQLite + SQLAlchemy ORM |
| Frontend | Vanilla HTML, CSS, JavaScript |
| Containerization | Docker |
| API Style | RESTful |

---

## 📁 Project Structure

```
log-monitor/
├── main.py           # FastAPI app + API routes
├── models.py         # SQLAlchemy database models
├── schemas.py        # Pydantic request/response schemas
├── database.py       # DB connection & session management
├── log_generator.py  # Simulates log traffic for testing
├── static/           # Frontend HTML, CSS, JS
└── .gitignore
```

---

## 🚀 Run Locally

**Without Docker:**
```bash
git clone https://github.com/Sumithkokkula/log-monitor.git
cd log-monitor
pip install -r requirements.txt
uvicorn main:app --reload
```

**With Docker:**
```bash
docker build -t log-monitor .
docker run -p 8000:8000 log-monitor
```

Open `http://localhost:8000` in your browser.

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/logs` | Ingest a new log entry |
| `GET` | `/logs` | Retrieve logs with optional filters |
| `GET` | `/logs?severity=ERROR` | Filter by severity level |
| `GET` | `/logs?keyword=timeout` | Search logs by keyword |
| `GET` | `/logs?start=...&end=...` | Filter by timestamp range |
| `GET` | `/stats` | Get dashboard statistics |

---

## 🔮 Future Improvements

- [ ] Add WebSocket support for true real-time streaming
- [ ] Export logs to CSV / JSON
- [ ] Role-based access control (RBAC)
- [ ] Migrate from SQLite to PostgreSQL for production scale
- [ ] Email/Slack alerts for critical errors

---

## 👤 Author

**Sumith Kokkula** · [LinkedIn](https://www.linkedin.com/in/sumith-kokkula-6a240b329) · [GitHub](https://github.com/Sumithkokkula)
