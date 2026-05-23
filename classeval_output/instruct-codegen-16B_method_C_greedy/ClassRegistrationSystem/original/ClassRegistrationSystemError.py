
class ClassRegistrationSystem: 
    def __init__(self):
        """
        Initialize the registration system with the attribute students and students_registration_class.
        students is a list of student dictionaries, each student dictionary has the key of name and major.
        students_registration_class is a dictionaries, key is the student name, value is a list of class names
        """
        self.students = []
        self.students_registration_classes = {}



    def register_student(self, student):
        if student in self.students:
            return 0
        else:
            self.students.append(student)
            self.students_registration_classes[student['name']] = []
            return 1



    def get_students_by_major(self, major):
        """
        get all students in the major
        :param major: str
        :return a list of student name
        >>> registration_system = ClassRegistrationSystem()
        >>> student1 = {"name": "John", "major": "Computer Science"}
        >>> registration_system.register_student(student1)
        >>> registration_system.get_students_by_major("Computer Science")
        ["John"]
        """
        return [student['name'] for student in self.students if student['major'] == major]

    def get_all_major(self):
        """
        get all majors in the system
        :return a list of majors
        """
        return list(set([student["major"] for student in self.students]))

    def get_most_popular_class_in_major(self, major):
        """
        get the class with the highest enrollment in the major.
        :return 
        """