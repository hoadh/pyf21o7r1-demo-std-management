from user_interface import *
from student_management import *

students_list = '''001, Huy Hoà, Nam, Đà Nẵng, 50, 50
002, Thế Anh, Nam, Vũng Tàu, 80, 90
003, Duy Luân, Nam, New York, 90, 90'''

while True:
    show_menu()
    user_choice = get_choice()
    print("Bạn đã chọn " + user_choice)

    if user_choice == "7":
        break
    elif user_choice == "1":
        students_list = add_student(students_list)
    elif user_choice == "2":
        edit_student()
    elif user_choice == "3":
        show_students_list(students_list)
    elif user_choice == "4":
        show_passed_students(students_list)
    elif user_choice == "5":
        show_failed_students(students_list)
    elif user_choice == "6":
        students_list = remove_student(students_list)
