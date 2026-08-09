from sqlalchemy import Column,Integer,String,Float,ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer,primary_key=True,index=True)
    ticket_code = Column(String(20),nullable=False,unique=True)
    seat_number = Column(String(10),nullable=False)
    price = Column(Float,nullable=False)
    movie_id = Column(Integer,ForeignKey("movie.id"),nullable=False)
    movie = relationship("Movie",back_populates="tickets")