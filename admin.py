from user import User


class Admin(User):
    def __init__(self, user_id, pin):
        super().__init__(user_id, pin)

    def show_roster(self, c_list):
        print("List of courses:")
        for c in c_list:
            print(c.get_course_code())
        course_to_see = input("Which roster would you like to see?").upper()
        for course in c_list:
            if course_to_see == course.get_course_code():
                course.display_roster()
                break
        else:
            print("That course is not offered")

    def change_max_size(self, c_list):
        print("List of courses and max size:")
        for course in c_list:
            print(course.get_course_code(), course.get_max_size())
        course_to_change = input("Which course's max size would you like to change?").upper()
        for course in c_list:
            if course_to_change == course.get_course_code():
                course.change_max_size()
                break
        else:
            print("That course is not offered")
