def add_student(students_list):
    id = input("Nhập vào mã số: ")
    full_name = input("Nhập vào họ tên: ")
    gender = input("Nhập vào giới tính: ")
    province = input("Nhập vào tỉnh/thành phố: ")
    theory = input("Nhập vào điểm lý thuyết: ")
    practice = input("Nhập vào điểm thực hành: ")
    # Validation
    students_list += f'\n{id}, {full_name}, {gender}, {province}, {theory}, {practice}'
    return students_list

def edit_student():
    pass

def show_header():
    print(f"{'Mã số':<10}{'Họ tên':^20}{'giới tính':^10}{'tỉnh/Thành phố':<20}{'Điểm thi lý thuyết':>20}{'Điểm thi thực hành':>20}")


def show_students(condition, students_list):
    show_header()
    lst = students_list.split("\n")
    for std in lst:
        if std == "":
            continue

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

def show_students_list(students_list):
    show_students(get_all_condition, students_list)


def show_passed_students(students_list):
    show_students(get_passed_condition, students_list)


def show_failed_students(students_list):
    show_students(get_failed_condition, students_list)

def remove_student(students_list):
    remove_id = input("Hãy nhập vào mã số của học viên muốn xóa khỏi bộ nhớ: ")
    lst = students_list.split("\n")
    new_students_list = ""
    for std in lst:
        info = std.split(",")
        id = info[0]
        if id != remove_id:
            new_students_list += std + "\n"

    return new_students_list
