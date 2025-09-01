# Student Management System

## Overview
This is a web-based Student Management System built with Flask (Python) and SQLite. It includes pages for Homepage, About Us, Contact Us, and Student Management (add, list, delete, search students). Bonus features: delete functionality, search by name, and flash messages.

## Setup Steps
1. **Prerequisites**:
   - Python 3.x installed.
   - Install dependencies: `pip install -r requirements.txt`

2. **Run the Application**:
   - Execute `python app.py`
   - Open a browser and go to `http://127.0.0.1:5000/`

3. **Database**:
   - SQLite database (`database.db`) is created automatically on first run.
   - Schema: STUDENTS table with STUDENT_ID (PK, auto-inc), FULL_NAME (required), EMAIL (unique).

4. **Features**:
   - Add students via form (name required, email optional/unique).
   - List students in a table.
   - Delete students.
   - Search by name.
   - Flash notifications for actions.

5. **Technology Stack**:
   - Backend: Flask
   - Database: SQLite
   - Frontend: HTML, Bootstrap CSS

## Notes
- No external database setup needed.
- For production, consider using a more robust server (e.g., Gunicorn).