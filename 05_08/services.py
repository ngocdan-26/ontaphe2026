from models import Students
from schema import StudentResponse
from fastapi import HTTPException

def update_student_by_id(stu_id:int,update_student:StudentResponse,db):
    student = db.query(Students).filter(Students.id == stu_id).first()
    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Khong tim thay sinh vien"
        )
    student.full_name = update_student.full_name
    student.email = update_student.email
    student.phone = update_student.phone
    db.commit()
    db.refresh(student)
    return{
        "message": "cap nhat thong tin sv thanh cong",
        "data": student
    }

def delete_student_by_id(stu_id:int,db):
    student = db.query(Students).filter(Students.id==stu_id).first()
    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Khong tim thay sinh vien"
        )
    db.delete(student)
    db.commit()
    return{
        "message":"xoa sinh vien thanh cong",
        "data":student
    }