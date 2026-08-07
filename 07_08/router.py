from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schema import StudentCreate
from database import get_db
from services import add_new_student,get_all_student,get_student_detail,update_student_by_id,delete_student_by_id
router = APIRouter(
    prefix="/students",
    tags=["/students"]
)

@router.post("")
def add_student(student:StudentCreate,db:Session=Depends(get_db)):
    return add_new_student(student,db)

@router.get("")
def get_student(db:Session=Depends(get_db)):
    return{
        "data": get_all_student(db)
    }

@router.get("/{stu_id}")
def get_student_by_id(stu_id:int,db:Session=Depends(get_db)):
    return get_student_detail(stu_id,db)

@router.put("/{stu_id}")
def update_student(stu_id:int,student:StudentCreate,db:Session=Depends(get_db)):
    return update_student_by_id(stu_id,student,db)

@router.delete("/{stu_id}")
def delete_student(stu_id:int,db:Session=Depends(get_db)):
    return delete_student_by_id(stu_id,db)