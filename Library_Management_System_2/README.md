
---

# 📘 README.md (Modern Blue Theme)

```markdown
# 📚 Library Management System (Modern Blue Theme)

A web-based **Library Management System** built with **Flask (Python)** and **SQLite**.  
This version uses a **modern design with a blue navigation bar, smooth animations, and page transitions**.

---

## 🚀 Features
- Homepage with smooth fade-in animations.
- About Us & Contact Us pages with modern transitions.
- Library Management Page with:
  - ➕ Add new books
  - 📖 List all books
  - ✏️ Edit books
  - ❌ Delete books
- Blue-themed navigation bar with spacing & hover animations.
- Background gradients for a modern look.

---

## 🗄️ Database
SQLite database with one table:

```sql
CREATE TABLE books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    isbn TEXT UNIQUE
);
project/
│── app.py
│── schema.sql
│── README.md
│
├── static/
│   ├── style.css
│   
│
└── templates/
    ├── base.html
    ├── index.html
    ├── about.html
    ├── contact.html
    └── library.html


python app.py
