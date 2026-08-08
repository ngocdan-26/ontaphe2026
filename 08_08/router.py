from fastapi import APIRouter, Depends,Query
from sqlalchemy.orm import Session
from schema import StudentCreate
from database import get_db
from services import add_new_student,get_student_detail,update_student_by_id,delete_student,get_students
router = APIRouter(
    prefix="/students",
    tags=["/students"]
)

@router.post("")
def add_student(student:StudentCreate,db:Session=Depends(get_db)):
    return add_new_student(student,db)

@router.get("")
def get_all_students(
    keyword: str | None = None,
    min_age: int | None = None,
    max_age: int | None = None,
    is_active: bool | None = None,
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    return get_students(db,keyword,min_age,max_age,is_active,page,page_size)

@router.get("/{stu_id}")
def get_studnet_by_id(stu_id:int,db:Session=Depends(get_db)):
    return get_student_detail(stu_id,db)

@router.put("/{stu_id}")
def update_student(stu_id:int,student:StudentCreate,db:Session=Depends(get_db)):
    return update_student_by_id(stu_id,student,db) 

@router.delete("/{stu_id}")
def delete_student_by_id(stu_id:int,db:Session=Depends(get_db)):
    return delete_student(stu_id,db)
