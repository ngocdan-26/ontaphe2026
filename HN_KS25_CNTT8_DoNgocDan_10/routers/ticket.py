from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas.ticket import TicketCreate
from services.ticket_service import create_ticket
from services.ticket_service import get_all_tickets

router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)


@router.get("")
def get_tickets(
    db: Session = Depends(get_db)
):
    tickets = get_all_tickets(db)

    return {
        "statusCode": 200,
        "error": None,
        "message": "Lấy danh sách vé thành công",
        "data": tickets
    }


@router.post("")
def add_ticket(
    ticket: TicketCreate,
    db: Session = Depends(get_db)
):
    new_ticket = create_ticket(ticket, db)

    return {
        "statusCode": 201,
        "error": None,
        "message": "Thêm vé thành công",
        "data": new_ticket
    }