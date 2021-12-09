from admin import Admin
from course import Course
from student import Student


def main():
    course_list = []
    student_list = []
    admin_list = []
    init_lists(course_list, student_list, admin_list)

    while True:
        start = input("Enter 1 if you are student \n"
                      "2 if you are admin\n"
                      "0 to quit: ")

        if start == "1":
            student_session(c_list=course_list, s_list=student_list)
        elif start == "2":
            admin_session(c_list=course_list, a_list=admin_list)
        else:
            print("Exiting Registration System")
            break


def student_session(c_list, s_list):
    is_valid, index = login(u_list=s_list)
    if not is_valid:
        return
    student = s_list[index]
    while True:
        choice = input("Enter 1 to add course\n"
                       "      2 to drop course\n"
                       "      3 to see your registered courses\n"
                       "      0 to exit")
        if choice == "1":
            student.add_course(c_list)
        elif choice == "2":
            student.drop_course(c_list)
        elif choice == "3":
            student.list_courses(c_list)
        elif choice == "0":
            print("\n Student session ended.")
            break


def admin_session(c_list, a_list):
    is_valid, index = login(u_list=a_list)
    if not is_valid:
        return
    admin = a_list[index]
    while True:
        choice = input("Enter 1 to show class roster\n"
                       "      2 to change max class size\n"
                       "      0 to exit")
        if choice == "1":
            admin.show_roster(c_list)
        elif choice == "2":
            admin.change_max_size(c_list)
        elif choice == "0":
            print("\n Administrator session ended.")
            break


def login(u_list):
    user_id = input("Enter ID: ")
    pin = input("Enter PIN: ")
    for i, user in enumerate(u_list):
        if user_id == user.get_id():
            if pin in user.get_pin():
                print("ID and PIN verified")
                return True, i
    else:
        print("ID or PIN incorrect")
        return False, -1


def init_lists(c_list, s_list, a_list):
    course1 = Course("CSC121", 2)
    course1.add_student("1004")
    course1.add_student("1003")
    c_list.append(course1)
    course2 = Course("CSC122", 2)
    course2.add_student("1001")
    c_list.append(course2)
    course3 = Course("CSC221", 1)
    course3.add_student("1002")
    c_list.append(course3)

    student1 = Student("1001", "111")
    s_list.append(student1)
    student2 = Student("1002", "222")
    s_list.append(student2)
    student3 = Student("1003", "333")
    s_list.append(student3)
    student4 = Student("1004", "444")
    s_list.append(student4)

    admin1 = Admin("7001", "777")
    a_list.append(admin1)
    admin2 = Admin("8001", "888")
    a_list.append(admin2)


main()
