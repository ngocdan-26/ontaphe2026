from models import Students
from fastapi import HTTPException

def get_all_student(db):
    return db.query(Students).all()

def get_student_detail(stu_id:int,db):
    student = db.query(Students).filter(Students.id == stu_id).first()
    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Khong tim thay sinh vien"
        )
    return{
        "message":"tim thay sinh vien",
        "data": student
    }
