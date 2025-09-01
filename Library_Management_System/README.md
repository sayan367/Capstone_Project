# README.md

## Library Management System

This is a simple web-based Library Management System built using Python Flask and SQLite.

### Setup Steps

1. **Prerequisites**:
   - Python 3.x installed.
   - Install Flask: `pip install flask`

2. **Project Structure**:
   - `app.py`: Main Flask application.
   - `templates/`: Folder containing HTML templates (base.html, home.html, about.html, contact.html, library.html).
   - `library.db`: SQLite database file (auto-created on first run).
   - `db_schema.sql`: Database schema script (for reference or manual creation).

3. **Running the Application**:
   - Place all files in a project directory.
   - Run `python app.py` from the command line.
   - Open a web browser and navigate to `http://127.0.0.1:5000/`.
   - Access pages:
     - Homepage: `/`
     - About Us: `/about`
     - Contact Us: `/contact`
     - Library Management: `/library`

4. **Notes**:
   - The database is initialized automatically on app start.
   - For Oracle PL/SQL alternative: Replace SQLite with Oracle connections using `cx_Oracle` library. Create a PL/SQL package for CRUD operations. Install `pip install cx_Oracle` and configure Oracle XE connection details in `app.py`.
   - Bootstrap is used via CDN for styling.
   - Validation is basic; title and author are required, ISBN is optional but unique.

### Screenshots
(As this is a text-based response, run the app locally to view and capture screenshots:
- Homepage: Welcome message.
- About Us: System description.
- Contact Us: Dummy details.
- Library Management: Form and empty table initially; after adding books, table populated.)