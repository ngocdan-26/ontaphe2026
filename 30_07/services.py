from fastapi import HTTPException
from models import Students
from sqlalchemy import func

def get_all_student(db):
    return db.query(Students).all()

def get_student_detail(stu_id:int,db):
    student = db.query(Students).filter(Students.id == stu_id).first()
    if not student:
        raise HTTPException(
            status_code=404,
            detail="khong tim thay sinh vien"
        )
    return{
        "message": "tim thay sinh vien",
        "data":student
    }

def search_student(stu_name:str,db):
    student = db.query(Students).filter(func.lower(Students.name) == stu_name.lower()).all()
    if not student:
        raise HTTPException(
            status_code=404,
            detail="khong tim thay sinh vien"
        )
    return{
        "message":"tim thay sinh vien",
        "data":student
    }

def filter_student(max_age: int, db):
    students = db.query(Students).filter(Students.age <= max_age).all()
    if not students:
        raise HTTPException(
            status_code=404,
            detail="khong tim thay sinh vien"
        )
    return {
        "message": "danh sach sinh vien",
        "data": students
    }