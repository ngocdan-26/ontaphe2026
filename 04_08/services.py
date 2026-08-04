from models import Students
from schema import StudentResponse
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

def add_new_student(student:StudentResponse,db):
    existing_email = db.query(Students).filter(Students.email == student.email).first()
    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="email da ton tai"
        )
    new_student = Students(
        full_name = student.full_name,
        email = student.email,
        phone = student.phone
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return{
        "message":"them sinh vien thanh cong",
        "data":student
    }