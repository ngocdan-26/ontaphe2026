from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base
class Movie(Base):
    __tablename__ = "movie"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100),nullable=False,unique=True)
    director = Column(String(100),nullable=False)
    tickets = relationship("Ticket",back_populates="movie")