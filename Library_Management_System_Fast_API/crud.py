from sqlalchemy.orm import Session
from models import Book
from schemas import BookCreate

def create_book(db: Session, book: BookCreate):
    db_book = Book(title=book.title, author=book.author, isbn=book.isbn)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session):
    return db.query(Book).all()

def delete_book(db: Session, book_id: int):
    db_book = db.query(Book).filter(Book.book_id == book_id).first()
    if db_book:
        db.delete(db_book)
        db.commit()
        return True
    return False