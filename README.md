# Online Bus Ticket Reservation System

## Overview
The **Online Bus  Ticket Reservation System** is a web-based application built with Django to manage bus reservations efficiently. The system allows users to view bus schedules, book tickets, and manage their reservations through an intuitive interface.

## Features
- **User Authentication**: Secure login and registration for users.
- **Bus Management**: Add, update, and view bus schedules.
- **Ticket Booking**: Reserve tickets and manage bookings.
- **Language Support**: Option for selecting preferred language.
- **Admin Panel**: Manage buses, routes, and users.
- **Responsive Design**: Optimized for desktop and mobile devices.

## Tech Stack
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (default Django database)
- **Styling**: Bootstrap 5

## Folder Structure
BUS_3.1/ |— db.sqlite3 # Database file |— manage.py # Django management script |— myapp/ # Main application folder | |— admin.py # Admin site configurations | |— apps.py # Application configuration | |— forms.py # Forms for user input | |— models.py # Database models | |— static/ # Static files (CSS, JS, images) | |— templates/ # HTML templates | |— urls.py # App-specific URL routing | |— views.py # Application logic |— myproject/ # Project configuration folder |— settings.py # Project settings |— urls.py # Root URL configuration |— wsgi.py # WSGI configuration

## Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Virtual environment tool (optional but recommended)

### Steps
1. **Clone the repository**: <br>
   ```bash
   git clone <repository-url>
   cd BUS_3.1    <br>
2.**Set up a virtual environment (optional)**: <br>

python -m venv venv      <br>
source venv/bin/activate  # On Windows: venv\Scripts\activate  <br>

3.**Install dependencies**:    <br>

pip install -r requirements.txt   <br>

4.**Apply migrations:**   <br>

python manage.py migrate   <br>

5.**Run the development server**:  <br>

python manage.py runserver     <br>
 
6.**Access the application**: Open your browser and go to **http://127.0.0.1:8000/**.

**Usage**<br>

Register as a new user or log in if you already have an account. <br>
Explore bus schedules and make reservations. <br>
Admins can log in to manage buses, routes, and users.<br>

**Contributing**<br>

Contributions are welcome! Please follow these steps: <br>
Fork the repository. <br>
Create a new branch for your feature (git checkout -b feature-name). <br>
Commit your changes (git commit -m 'Add feature'). <br>
Push to the branch (git push origin feature-name). <br>
Create a pull request.<br>

**License** <br>

This project is licensed under the MIT License. See the LICENSE file for details.
