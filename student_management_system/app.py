from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'super_secret_key'  # Required for flash messages

# Database connection function
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Initialize database if not exists
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS STUDENTS (
            STUDENT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            FULL_NAME TEXT NOT NULL,
            EMAIL TEXT UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

init_db()  # Run on app start

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/students', methods=['GET', 'POST'])
def students():
    conn = get_db_connection()
    
    if request.method == 'POST':
        if 'add_student' in request.form:
            full_name = request.form['full_name'].strip()
            email = request.form['email'].strip() or None  # Allow empty email
            
            if not full_name:
                flash('Full name is required!', 'error')
            else:
                try:
                    conn.execute('INSERT INTO STUDENTS (FULL_NAME, EMAIL) VALUES (?, ?)', (full_name, email))
                    conn.commit()
                    flash('Student added successfully!', 'success')
                except sqlite3.IntegrityError:
                    flash('Email must be unique if provided!', 'error')
        
        elif 'delete_student' in request.form:
            student_id = request.form['student_id']
            conn.execute('DELETE FROM STUDENTS WHERE STUDENT_ID = ?', (student_id,))
            conn.commit()
            flash('Student deleted successfully!', 'success')
    
    # Search functionality
    search_query = request.args.get('search', '').strip()
    if search_query:
        cursor = conn.execute('SELECT * FROM STUDENTS WHERE FULL_NAME LIKE ? ORDER BY FULL_NAME', (f'%{search_query}%',))
    else:
        cursor = conn.execute('SELECT * FROM STUDENTS ORDER BY FULL_NAME')
    
    students_list = cursor.fetchall()
    conn.close()
    
    return render_template('students.html', students=students_list, search_query=search_query)

if __name__ == '__main__':
    app.run(debug=True)