from validators import (
    validate_student_id,
    validate_name,
    validate_email,
    validate_age
)

students = []

def is_duplicate_id(student_id):
    return any(student["id"] == student_id for student in students)

def is_duplicate_email(email):
    return any(student["email"] == email for student in students)

def add_student(student_id, name, email, age):
    validate_student_id(student_id)
    validate_name(name)
    validate_email(email)
    validate_age(age)

    if is_duplicate_id(student_id):
        raise ValueError("Mã sinh viên đã tồn tại")

    if is_duplicate_email(email):
        raise ValueError("Email đã tồn tại")

    student = {
        "id": student_id,
        "name": name.strip(),
        "email": email,
        "age": age
    }
    students.append(student)
    return "Thêm sinh viên thành công"

def show_students():
    return students

def find_student_by_id(student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None

def filter_students_by_age(min_age):
    return [
        student
        for student in students
        if student["age"] >= min_age
    ]