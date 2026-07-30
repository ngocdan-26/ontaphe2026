from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schema import StudentCreate
from database import get_db
from services import add_new_student
router = APIRouter(
    prefix="/students",
    tags=["/students"]
)

@router.post("")
def add_student(student:StudentCreate,db:Session=Depends(get_db)):
    return add_new_student(student,db)