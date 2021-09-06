
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