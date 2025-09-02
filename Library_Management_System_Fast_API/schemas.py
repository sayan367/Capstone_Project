from typing import Optional
from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author: str
    isbn: Optional[str] = None

class Book(BaseModel):
    book_id: int
    title: str
    author: str
    isbn: Optional[str] = None

    class Config:
        from_attributes = True