class Course:
    def __init__(self, c_code, m_size):
        self._course_code = c_code
        self._max_size = m_size
        self._roster = []

    def add_student(self, id):
        if id in self._roster:
            print("You are already in the course")
        elif len(self._roster) == self._max_size:
            print("This class is full")
        else:
            self._roster.append(id)
            print(id, "has been added to the course")

    def drop_student(self, id):
        if id not in self._roster:
            print("You are not enrolled in this course")
        else:
            self._roster.remove(id)

    def display_roster(self):
        print(self._roster)

    def change_max_size(self):
        print("Current enrollment count is", len(self._roster))
        print("Current maximum class size is", self._max_size)
        while True:
            new_size = int(input("What would you like the new max class size to be?"))
            if new_size < len(self._roster):
                print("That size is too small, enter another size")
            else:
                self._max_size = new_size
                break

    def get_max_size(self):
        return self._max_size

    def get_course_code(self):
        return self._course_code

    def student_in_course(self, id):
        if id in self._roster:
            return True
        else:
            return False


