from user import User


class Student(User):
    def __init__(self, student_id, pin):
        super().__init__(student_id, pin)

    def add_course(self, c_list):
        print("List of courses:")
        for c in c_list:
            print(c.get_course_code())
        course_to_add = input("Which class do you want to add?").upper()
        for course in c_list:
            if course_to_add == course.get_course_code():
                print("That course is offered")
                course.add_student(self._id)
                break
        else:
            print("That course is not offered")

    def drop_course(self, c_list):
        print("List of courses:")
        for c in c_list:
            print(c.get_course_code())
        course_to_drop = input("Which class do you want to drop?").upper()
        for course in c_list:
            if course_to_drop == course.get_course_code():
                print("That course is offered")
                course.drop_student(self._id)
                print("This course has been dropped.")
                break
        else:
            print("That course is not offered.")

    def list_courses(self, c_list):
        num = 0
        for course in c_list:
            if course.student_in_course(self._id):
                print(course.get_course_code())
                num += 1
        print("The student is in", num, "courses")
