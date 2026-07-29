from student_service import (
    add_student,
    show_students,
    find_student_by_id,
    filter_students_by_age
)


while True:
    print("\n===== QUẢN LÝ SINH VIÊN =====")
    print("1. Thêm sinh viên")
    print("2. Hiển thị danh sách")
    print("3. Tìm sinh viên theo mã")
    print("4. Lọc sinh viên theo tuổi")
    print("5. Thoát")


    choice = input("Nhập lựa chọn (1-5): ")
    if choice == "1":
        try:
            student_id = input("Mã sinh viên: ")
            name = input("Tên sinh viên: ")
            email = input("Email: ")
            age = int(input("Tuổi: "))

            result = add_student(
                student_id,
                name,
                email,
                age
            )

            print(result)

        except ValueError as e:
            print("Lỗi: ",e)
    elif choice == "2":
        students = show_students()
        if not students:
            print("Danh sách trống")
        else:
            for student in students:
                print(student)
    elif choice == "3":
        student_id = input("Nhập mã cần tìm: ")
        student = find_student_by_id(student_id)
        if student:
            print(student)
        else:
            print("Không tìm thấy")
    elif choice == "4":
        try:
            age = int(input("Nhập tuổi tối thiểu: "))

            result = filter_students_by_age(age)
            if result:
                for student in result:
                    print(student)
            else:
                print("Không có sinh viên phù hợp")
        except ValueError:
            print("Tuổi phải là số")
    elif choice == "5":
        print("Thoát chương trình")
        break
    else:
        print("Lựa chọn không hợp lệ")