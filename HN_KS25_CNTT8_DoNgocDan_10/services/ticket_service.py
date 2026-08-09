from fastapi import HTTPException

from models.movie import Movie
from models.ticket import Ticket


def get_all_tickets(db):
    return db.query(Ticket).all()

def create_ticket(ticket, db):
    movie = db.query(Movie).filter(Movie.id == ticket.movie_id).first()
    if movie is None:
        raise HTTPException(
            status_code=404,
            detail="Phim không tồn tại"
        )

    existed_ticket = db.query(Ticket).filter(
        Ticket.ticket_code == ticket.ticket_code).first()
    
    if existed_ticket:
        raise HTTPException(
            status_code=400,
            detail="Mã vé đã tồn tại"
        )

    new_ticket = Ticket(
        ticket_code=ticket.ticket_code,
        seat_number=ticket.seat_number,
        price=ticket.price,
        movie_id=ticket.movie_id
    )

    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)

    return new_ticket