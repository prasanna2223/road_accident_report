# 🚦 Road Accident Report System

A web-based application developed using **Django** that allows users to report road accidents and enables administrators to analyze, manage, and update accident reports.

This project focuses on solving a real-world problem related to **road safety and accident management** with proper user and admin roles.

---

## 🛠️ Tech Stack
- **Backend:** Python, Django
- **Frontend:** HTML, CSS
- **Database:** SQLite
- **Authentication:** Django Authentication System
- **Version Control:** Git & GitHub

---

## ✨ Features

### 👤 User Module
- User registration and login
- Report road accidents with details:
  - Reporter name
  - Phone number
  - Location (city, state)
  - Vehicle details
  - Severity
  - Date and time
- View submitted accident reports
- Track accident status

### 🛡️ Admin Module
- Secure admin login
- View all accident reports
- Analyze accident data
- Update accident status
- Delete or manage accident records

---

## 📂 Project Structure

```text
road_accident_report/
│── manage.py
│── db.sqlite3
│── road_accident_report/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│── accident_app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   └── static/
