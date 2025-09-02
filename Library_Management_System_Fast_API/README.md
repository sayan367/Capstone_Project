# Library Management System

## Overview
A web-based system for managing library books using FastAPI, SQLite, and Bootstrap.

## Setup Steps
1. Clone the repository or copy the files into a directory.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `uvicorn main:app --reload`
4. Access the app at http://127.0.0.1:8000/
5. Navigate to pages: Home (/), About (/about), Contact (/contact), Library (/library)
6. On the Library page, add books via the form and view the updated table.

## Notes
- Database is auto-created on startup.
- Validation: Title and Author are required; ISBN is optional but unique (enforced by DB).
- For production, consider using a more robust DB like Oracle and add error handling for duplicates.

## Screenshots
- Homepage: Shows welcome message and introduction.
- About Us: Displays system description.
- Contact Us: Lists dummy contact details.
- Library Management (before adding): Empty table with form.
- Library Management (after adding): Table populated with book entries (e.g., ID:1, Title:"Book1", Author:"Author1", ISBN:"123456").