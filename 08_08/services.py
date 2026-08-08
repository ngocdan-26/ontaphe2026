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

def get_student_detail(stu_id:int,db):
    student = db.query(Students).filter(Students.id == stu_id).first()
    if student is None:
        raise HTTPException(
            status_code=404,
            detail="khong tim thay nhan vien"
        )
    return{
        "message" : "tim thay sinh vien",
        "data" : student
    }

def update_student_by_id(stu_id:int,update_student:StudentCreate,db):
    student = db.query(Students).filter(Students.id == stu_id).first()
    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Khong tim thay sinh vien"
        )
    student.full_name = update_student.full_name
    student.age = update_student.age
    student.email = update_student.email
    student.is_active = update_student.is_active
    db.commit()
    db.refresh(student)
    return{
        "message": "cap nhat thong tin sv thanh cong",
        "data": student
    }

def delete_student(stu_id:int,db):
    student = db.query(Students).filter(Students.id == stu_id).first()
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

def get_students(db,keyword=None,min_age=None,max_age=None,is_active=None,page=1,page_size=10):
    query = db.query(Students)
    if keyword:
        query = query.filter(Students.full_name.contains(keyword))

    if min_age is not None:
        query = query.filter(Students.age >= min_age)

    if max_age is not None:
        query = query.filter(Students.age <= max_age)

    if is_active is not None:
        query = query.filter( Students.is_active == is_active )

    total = query.count()
    data = (query.order_by(Students.id).offset((page - 1) * page_size).limit(page_size).all())

    return {
        "total": total,
        "page": page,
        "page_size": page_size,
        "data": data
    }