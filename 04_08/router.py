from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schema import StudentResponse
from database import get_db
from services import get_all_student,get_student_detail,add_new_student
router = APIRouter(
    prefix="/students",
    tags=["/students"]
)

@router.get("")
def get_student(db:Session=Depends(get_db)):
    return{
        "data":get_all_student(db)
    }

@router.get("/{stu_id}")
def get_student_by_id(stu_id:int,db:Session=Depends(get_db)):
    return get_student_detail(stu_id,db)

@router.post("")
def add_student(student:StudentResponse,db:Session=Depends(get_db)):
    return add_new_student(student,db)