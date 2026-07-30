from models import Students
from schema import StudentCreate
from fastapi import HTTPException

def add_new_student(student:StudentCreate,db):
    existing_student = db.query(Students).filter(Students.student_code == student.student_code).first()
    if existing_student:
        raise HTTPException(
            status_code=400,
            detail="sinh vien da ton tai"
        )
    existing_email = db.query(Students).filter(Students.email == student.email).first()
    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="email da ton tai"
        )
        
    new_student = Students(
        student_code = student.student_code,
        full_name = student.full_name,
        email = student.email,
        age = student.age,
        is_active = student.is_active
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return{
        "message":"them sinh vien thanh cong",
        "data":student
    }