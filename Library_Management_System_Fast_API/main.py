# from fastapi import FastAPI, Request, Form, Depends
# from fastapi.responses import RedirectResponse
# from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles
# from sqlalchemy.exc import IntegrityError
# from sqlalchemy.orm import Session
# from database import engine, Base, get_db
# from schemas import BookCreate
# from crud import create_book, get_books

# app = FastAPI()

# # Create database tables on startup
# @app.on_event("startup")
# def startup():
#     Base.metadata.create_all(bind=engine)

# templates = Jinja2Templates(directory="templates")
# app.mount("/static", StaticFiles(directory="static"), name="static")

# @app.get("/")
# async def home(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})

# @app.get("/about")
# async def about(request: Request):
#     return templates.TemplateResponse("about.html", {"request": request})

# @app.get("/contact")
# async def contact(request: Request):
#     return templates.TemplateResponse("contact.html", {"request": request})

# @app.get("/library")
# async def library_page(request: Request, db: Session = Depends(get_db)):
#     books = get_books(db)
#     return templates.TemplateResponse("library.html", {"request": request, "books": books})

# @app.post("/library")
# async def add_book(
#     title: str = Form(...),
#     author: str = Form(...),
#     isbn: str = Form(None),
#     db: Session = Depends(get_db)
# ):
#     book = BookCreate(title=title, author=author, isbn=isbn)
#     try:
#         create_book(db, book)
#     except IntegrityError:
#         # Handle unique ISBN violation (for simplicity, redirect without error message)
#         pass
#     return RedirectResponse(url="/library", status_code=303)


from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from schemas import BookCreate
from crud import create_book, get_books, delete_book

app = FastAPI()

# Create database tables on startup
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/about")
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.get("/contact")
async def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

@app.get("/library")
async def library_page(request: Request, db: Session = Depends(get_db)):
    books = get_books(db)
    return templates.TemplateResponse("library.html", {"request": request, "books": books})

@app.post("/library")
async def add_book(
    title: str = Form(...),
    author: str = Form(...),
    isbn: str = Form(None),
    db: Session = Depends(get_db)
):
    book = BookCreate(title=title, author=author, isbn=isbn)
    try:
        create_book(db, book)
    except IntegrityError:
        # Handle unique ISBN violation (for simplicity, redirect without error message)
        pass
    return RedirectResponse(url="/library", status_code=303)

@app.post("/library/delete/{book_id}")
async def delete_book_route(book_id: int, db: Session = Depends(get_db)):
    delete_book(db, book_id)
    return RedirectResponse(url="/library", status_code=303)