from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=False)
    author = Column(String(50), nullable=False)
    genre = Column(String(50), nullable=False)
    price = Column(DECIMAL(12,2), nullable=False)