import re

def validate_student_id(student_id):
    if not student_id or student_id.strip() == "":
        raise ValueError("Mã sinh viên không được để trống")

def validate_name(name):
    if not name or name.strip() == "":
        raise ValueError("Tên không hợp lệ")

def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if not re.match(pattern, email):
        raise ValueError("Email không đúng định dạng")

def validate_age(age):
    if not isinstance(age, int):
        raise ValueError("Tuổi phải là số nguyên")

    if age < 18 or age > 100:
        raise ValueError("Tuổi phải từ 18 đến 100")