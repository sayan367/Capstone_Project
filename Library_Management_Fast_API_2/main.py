from fastapi import FastAPI, Request, Form, status, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from database import get_connection, create_table
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="your-secret-key")

templates = Jinja2Templates(directory="templates")

# Mount static files (CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize DB table
create_table()

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/about")
def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.get("/contact")
def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

@app.get("/library")
def library(request: Request):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM BOOKS ORDER BY BOOK_ID DESC")
    books = cursor.fetchall()
    conn.close()
    return templates.TemplateResponse("library.html", {"request": request, "books": books, "error": None})

# @app.post("/library")
# def add_book(request: Request, title: str = Form(...), author: str = Form(...), isbn: str = Form(None)):
#     error = None
#     title = title.strip()
#     author = author.strip()
#     isbn = isbn.strip() if isbn else None

#     if not title or not author:
#         error = "Title and Author are required."
#     else:
#         try:
#             conn = get_connection()
#             cursor = conn.cursor()
#             if isbn:
#                 cursor.execute("INSERT INTO BOOKS (TITLE, AUTHOR, ISBN) VALUES (?, ?, ?)", (title, author, isbn))
#             else:
#                 cursor.execute("INSERT INTO BOOKS (TITLE, AUTHOR) VALUES (?, ?)", (title, author))
#             conn.commit()
#             conn.close()
#             return RedirectResponse(url="/library", status_code=status.HTTP_303_SEE_OTHER)
#         except Exception as e:
#             if "UNIQUE constraint failed: BOOKS.ISBN" in str(e):
#                 error = "ISBN must be unique."
#             else:
#                 error = "An error occurred while adding the book."

#     # On error, reload books and show error message
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM BOOKS ORDER BY BOOK_ID DESC")
#     books = cursor.fetchall()
#     conn.close()
#     return templates.TemplateResponse("library.html", {"request": request, "books": books, "error": error})


import logging

# Configure logging (at the top of your file)
logging.basicConfig(level=logging.INFO)

@app.post("/library")
def add_book(request: Request, title: str = Form(...), author: str = Form(...), isbn: str = Form(None)):
    error = None
    title = title.strip()
    author = author.strip()
    isbn = isbn.strip() if isbn else None

    if not title or not author:
        error = "Title and Author are required."
    else:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            if isbn:
                cursor.execute("INSERT INTO BOOKS (TITLE, AUTHOR, ISBN) VALUES (?, ?, ?)", (title, author, isbn))
            else:
                cursor.execute("INSERT INTO BOOKS (TITLE, AUTHOR) VALUES (?, ?)", (title, author))
            conn.commit()
            conn.close()
            return RedirectResponse(url="/library", status_code=status.HTTP_303_SEE_OTHER)
        except Exception as e:
            logging.error(f"Error adding book: {e}")
            if "UNIQUE constraint failed: BOOKS.ISBN" in str(e):
                error = "ISBN must be unique."
            else:
                error = f"An error occurred while adding the book: {e}"

    # On error, reload books and show error message
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM BOOKS ORDER BY BOOK_ID DESC")
    books = cursor.fetchall()
    conn.close()
    return templates.TemplateResponse("library.html", {"request": request, "books": books, "error": error})

@app.post("/library/delete/{book_id}")
def delete_book(request: Request, book_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM BOOKS WHERE BOOK_ID = ?", (book_id,))
    book = cursor.fetchone()
    if not book:
        conn.close()
        raise HTTPException(status_code=404, detail="Book not found")
    cursor.execute("DELETE FROM BOOKS WHERE BOOK_ID = ?", (book_id,))
    conn.commit()
    conn.close()
    return RedirectResponse(url="/library", status_code=status.HTTP_303_SEE_OTHER)
