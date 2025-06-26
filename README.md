# 🚌 Online Bus Ticket Reservation System

A web-based Django application that enables users to browse bus schedules, book tickets, and manage their bookings online. Built for ease of use and administrative control, this system streamlines the bus reservation process.

---

## 📌 Overview

The **Online Bus Ticket Reservation System** is designed to:
- Allow users to register, log in, and reserve bus tickets.
- Help admins manage buses, routes, and user data.
- Deliver a responsive, language-friendly, and intuitive booking experience.

---

## ✨ Features

✅ Secure User Registration & Login  
✅ Search & Book Bus Tickets  
✅ Admin Dashboard for Bus & Route Management  
✅ View and Manage Reservations  
✅ Language Selection Support  
✅ Mobile-Friendly Responsive UI  

---

## 🧰 Tech Stack

| Layer      | Technology          |
|------------|---------------------|
| Backend    | Python, Django       |
| Frontend   | HTML5, CSS3, JavaScript |
| Styling    | Bootstrap 5          |
| Database   | SQLite (Django default) |

---

## 📁 Folder Structure
BUS_3.1/
│
├── db.sqlite3 # SQLite database
├── manage.py # Django management script
│
├── myproject/ # Project configuration
│ ├── settings.py # Project settings
│ ├── urls.py # Root URL routing
│ └── wsgi.py # WSGI configuration
│
└── myapp/ # Main app
├── admin.py # Admin interface
├── apps.py # App config
├── forms.py # Custom forms
├── models.py # Database models
├── views.py # View logic
├── urls.py # App-specific routes
├── templates/ # HTML templates
└── static/ # CSS, JS, images

## ⚙️ Installation & Setup

### ✅ Prerequisites
- Python 3.8+
- pip (Python package manager)
- Virtualenv (recommended)

### 🧪 Steps

1. **Clone the Repository**
git clone https://github.com/your-username/bus-reservation-system.git
cd BUS_3.1

**2.Set Up Virtual Environment (optional)**
python -m venv venv
# Activate it:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
**Install Dependencies**
pip install -r requirements.txt
**Apply Migrations**
python manage.py migrate
**Run the Development Server**
python manage.py runserver
**Access the Application**
Open your browser:
👉 http://127.0.0.1:8000/



