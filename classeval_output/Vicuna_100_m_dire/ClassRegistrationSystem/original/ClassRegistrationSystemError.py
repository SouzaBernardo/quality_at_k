
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
        if student.name in self.students_registration_classes:
            return 0
        self.students.append(student)
        self.students_registration_classes[student.name] = student.major
        return 1

    def register_class(self, student_name, class_name):
        """
        register a class to the student.
        :param student_name: str
        :param class_name: str
        :return a list of class names that the student has registered
        >>> registration_system = ClassRegistrationSystem()
        >>> registration_system.register_class(student_name="John", class_name="CS101")
        >>> registration_system.register_class(student_name="John", class_name="CS102")
        ["CS101", "CS102"]

    def get_students_by_major(self, major):
        students_by_major = {}
        for student in self.students:
            if student["major"] == major:
                students_by_major[student["name"]] = student
        return students_by_major



    def get_most_popular_class_in_major(self, major):
        most_enrolled_class = max(self.students_registration_classes.values(), key=lambda x: len(x))
        return most_enrolled_class[0]