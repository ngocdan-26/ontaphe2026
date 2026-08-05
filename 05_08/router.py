from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schema import StudentResponse
from database import get_db
from services import update_student_by_id
router = APIRouter(
    prefix="/students",
    tags=["/students"]
)

@router.put("/{stu_id}")
def update_student(stu_id:int,student:StudentResponse,db:Session=Depends(get_db)):
    return update_student_by_id(stu_id,student,db)

@router.delete("/{stu_id}")
def delete_student(stu_id:int,db:Session=Depends(get_db)):
    return delete_student(stu_id,db)