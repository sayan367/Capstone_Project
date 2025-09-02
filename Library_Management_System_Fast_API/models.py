from sqlalchemy import Column, Integer, String
from database import Base

class Book(Base):
    __tablename__ = "books"

    book_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    isbn = Column(String, unique=True)