from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from services import get_all_student,get_student_detail
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