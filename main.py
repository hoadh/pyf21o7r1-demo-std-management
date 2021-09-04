
students_list = '''001, Huy Hoà, Nam, Đà Nẵng, 50, 50
002, Thế Anh, Nam, Vũng Tàu, 80, 90
003, Duy Luân, Nam, New York, 90, 90'''

def add_student():
    pass

def edit_student():
    pass

def show_header():
    print(f"{'Mã số':<10}{'Họ tên':^20}{'giới tính':^10}{'tỉnh/Thành phố':<20}{'Điểm thi lý thuyết':>20}{'Điểm thi thực hành':>20}")


def show_students(condition):
    show_header()
    lst = students_list.split("\n")
    for std in lst:
        info = std.split(",")
        id = info[0]
        full_name = info[1]
        gender = info[2]
        province = info[3]
        theory = info[4]
        practice = info[5]
        is_valid = condition(theory, practice)
        if is_valid:
            print(f"{id:<10}{full_name:^20}{gender:^10}{province:<20}{theory:>20}{practice:>20}")

def get_all_condition(theory, practice):
    return True

def get_passed_condition(theory, practice):
    return get_average_point(theory, practice) >= 75

def get_failed_condition(theory, practice):
    return get_average_point(theory, practice) < 75

def get_average_point(theory, practice):
    return (int(theory) + int(practice)) // 2

def show_students_list():
    show_students(get_all_condition)


def show_passed_students():
    show_students(get_passed_condition)


def show_failed_students():
    show_students(get_failed_condition)

def remove_student():
    pass

def show_menu():
    print('''
Hãy chọn tính năng muốn thực hiện theo danh sách dưới đây:
1) Thêm thông tin học viên vào bộ nhớ
2) Cập nhật thông tin học viên
3) Hiển thị danh sách tất cả học viên
4) Hiển thị danh sách học viên thi đỗ (Điểm trung bình >= 75)
5) Hiển thị danh sách học viên thi trượt (Điểm trung bình < 75)
6) Xóa thông tin của học viên
7) Thoát chương trình
    ''')

def get_choice():
    return input("Lựa chọn của bạn: ")


while True:
    show_menu()
    user_choice = get_choice()
    print("Bạn đã chọn " + user_choice)

    if user_choice == "7":
        break
    elif user_choice == "1":
        add_student()
    elif user_choice == "2":
        edit_student()
    elif user_choice == "3":
        show_students_list()
    elif user_choice == "4":
        show_passed_students()
    elif user_choice == "5":
        show_failed_students()
    elif user_choice == "6":
        remove_student()


# Top-Down
# Bottom-Up