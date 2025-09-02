# import sqlite3
# from flask import Flask, render_template, request, redirect, url_for, flash

# app = Flask(__name__)
# app.secret_key = "dev-secret"  # for flash messages
# DB = "books.db"

# def init_db():
#     with sqlite3.connect(DB) as conn:
#         c = conn.cursor()
#         c.execute("""
#         CREATE TABLE IF NOT EXISTS books (
#             book_id INTEGER PRIMARY KEY AUTOINCREMENT,
#             title TEXT NOT NULL,
#             author TEXT NOT NULL,
#             isbn TEXT UNIQUE
#         )
#         """)
#         conn.commit()

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/about")
# def about():
#     return render_template("about.html")

# @app.route("/contact")
# def contact():
#     return render_template("contact.html")

# @app.route("/library", methods=["GET", "POST"])
# def library():
#     conn = sqlite3.connect(DB)
#     c = conn.cursor()

#     if request.method == "POST":
#         title = request.form["title"].strip()
#         author = request.form["author"].strip()
#         isbn = request.form["isbn"].strip()

#         if not title or not author:
#             flash("Title and Author are required!", "danger")
#         else:
#             try:
#                 c.execute("INSERT INTO books (title, author, isbn) VALUES (?, ?, ?)",
#                           (title, author, isbn if isbn else None))
#                 conn.commit()
#                 flash("Book added successfully!", "success")
#             except sqlite3.IntegrityError:
#                 flash("ISBN must be unique!", "danger")

#     c.execute("SELECT * FROM books")
#     books = c.fetchall()
#     conn.close()
#     return render_template("library.html", books=books)

# if __name__ == "__main__":
#     init_db()
#     app.run(debug=True)


import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "dev-secret"
DB = "books.db"

def get_connection():
    return sqlite3.connect(DB)

def init_db():
    with get_connection() as conn:
        c = conn.cursor()
        c.execute("""
        CREATE TABLE IF NOT EXISTS books (
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            isbn TEXT UNIQUE
        )
        """)
        conn.commit()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/library", methods=["GET", "POST"])
def library():
    conn = get_connection()
    c = conn.cursor()

    if request.method == "POST":
        title = request.form["title"].strip()
        author = request.form["author"].strip()
        isbn = request.form["isbn"].strip()

        if not title or not author:
            flash("Title and Author are required!", "danger")
        else:
            try:
                c.execute("INSERT INTO books (title, author, isbn) VALUES (?, ?, ?)",
                          (title, author, isbn if isbn else None))
                conn.commit()
                flash("✅ Book added successfully!", "success")
            except sqlite3.IntegrityError:
                flash("❌ ISBN must be unique!", "danger")

    c.execute("SELECT * FROM books")
    books = c.fetchall()
    conn.close()
    return render_template("library.html", books=books)

@app.route("/delete/<int:book_id>")
def delete_book(book_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute("DELETE FROM books WHERE book_id=?", (book_id,))
    conn.commit()
    conn.close()
    flash("🗑️ Book deleted successfully!", "warning")
    return redirect(url_for("library"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)

