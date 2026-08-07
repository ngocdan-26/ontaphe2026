from models import Students
from schema import StudentCreate
from fastapi import HTTPException

def add_new_student(student:StudentCreate,db):
    existing_email = db.query(Students).filter(Students.email == student.email).first()
    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="email da ton tai"
        )
        
    new_student = Students(
        full_name = student.full_name,
        email = student.email,
        age = student.age
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return{
        "message":"them sinh vien thanh cong",
        "data":student
    }

def get_all_student(db):
    return db.query(Students).all()

def get_student_detail(stu_id:int,db):
    student = db.query(Students).filter(Students.student_code == stu_id).first()
    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Khong tim thay sinh vien"
        )
    return{
        "message":"tim thay sinh vien",
        "data": student
    }

def update_student_by_id(stu_id:int,update_student:StudentCreate,db):
    student = db.query(Students).filter(Students.student_code == stu_id).first()
    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Khong tim thay sinh vien"
        )
    student.full_name = update_student.full_name
    student.age = update_student.age
    student.email = update_student.email
    db.commit()
    db.refresh(student)
    return{
        "message": "cap nhat thong tin sv thanh cong",
        "data": student
    }

def delete_student_by_id(stu_id:int,db):
    student = db.query(Students).filter(Students.student_code==stu_id).first()
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