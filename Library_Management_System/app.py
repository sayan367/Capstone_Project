# # app.py

# from flask import Flask, render_template, request, redirect, url_for, flash
# import sqlite3

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'  # For flash messages

# # Database connection function
# def get_db_connection():
#     conn = sqlite3.connect('library.db')
#     conn.row_factory = sqlite3.Row
#     return conn

# # Initialize database if not exists
# def init_db():
#     conn = get_db_connection()
#     conn.execute('''
#         CREATE TABLE IF NOT EXISTS BOOKS (
#             BOOK_ID INTEGER PRIMARY KEY AUTOINCREMENT,
#             TITLE TEXT NOT NULL,
#             AUTHOR TEXT NOT NULL,
#             ISBN TEXT UNIQUE
#         )
#     ''')
#     conn.commit()
#     conn.close()

# init_db()  # Call to initialize DB on app start

# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/contact')
# def contact():
#     return render_template('contact.html')

# @app.route('/library', methods=['GET', 'POST'])
# def library():
#     conn = get_db_connection()
    
#     if request.method == 'POST':
#         title = request.form['title'].strip()
#         author = request.form['author'].strip()
#         isbn = request.form['isbn'].strip() if request.form['isbn'] else None
        
#         # Basic validation
#         if not title or not author:
#             flash('Title and Author are required!', 'error')
#         else:
#             try:
#                 conn.execute('INSERT INTO BOOKS (TITLE, AUTHOR, ISBN) VALUES (?, ?, ?)',
#                              (title, author, isbn))
#                 conn.commit()
#                 flash('Book added successfully!', 'success')
#             except sqlite3.IntegrityError:
#                 flash('ISBN must be unique if provided!', 'error')
    
#     # Fetch all books
#     books = conn.execute('SELECT * FROM BOOKS').fetchall()
#     conn.close()
    
#     return render_template('library.html', books=books)

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # For flash messages

# Database connection function
def get_db_connection():
    conn = sqlite3.connect('library.db')
    conn.row_factory = sqlite3.Row
    return conn

# Initialize database if not exists
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS BOOKS (
            BOOK_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            TITLE TEXT NOT NULL,
            AUTHOR TEXT NOT NULL,
            ISBN TEXT UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

init_db()  # Call to initialize DB on app start

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/library', methods=['GET', 'POST'])
def library():
    conn = get_db_connection()
    
    if request.method == 'POST':
        title = request.form['title'].strip()
        author = request.form['author'].strip()
        isbn = request.form['isbn'].strip() if request.form['isbn'] else None
        
        # Basic validation
        if not title or not author:
            flash('Title and Author are required!', 'error')
        else:
            try:
                conn.execute('INSERT INTO BOOKS (TITLE, AUTHOR, ISBN) VALUES (?, ?, ?)',
                             (title, author, isbn))
                conn.commit()
                flash('Book added successfully!', 'success')
            except sqlite3.IntegrityError:
                flash('ISBN must be unique if provided!', 'error')
    
    # Fetch all books
    books = conn.execute('SELECT * FROM BOOKS').fetchall()
    conn.close()
    
    return render_template('library.html', books=books)

@app.route('/delete_book/<int:book_id>', methods=['GET'])
def delete_book(book_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM BOOKS WHERE BOOK_ID = ?', (book_id,))
    conn.commit()
    conn.close()
    flash('Book deleted successfully!', 'success')
    return redirect(url_for('library'))

if __name__ == '__main__':
    app.run(debug=True)