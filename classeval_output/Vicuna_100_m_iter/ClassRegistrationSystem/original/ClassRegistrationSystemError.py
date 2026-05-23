
class ClassRegistrationSystem:  
    """
    This is a class as a class registration system, allowing to register students, register them for classes, retrieve students by major, get a list of all majors, and determine the most popular class within a specific major.
    """

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
        self.students.append(student)
        return 1

    def register_class(self, student_name, class_name):
        if student_name in self.students:
            return 0
        self.students.append(student_name)
        self.students_registration_classes[student_name].append(class_name)
        return 1

    def get_students_by_major(self, major):
        students = []
        for student in self.students:
            if student["major"] == major:
                students.append(student)
        return students

    def get_all_major(self):
        majors = []
        for student in self.students:
            major = student["major"]
            majors.append(major)
        return majors

    def get_most_popular_class_in_major(self, major):
        most_popular_class = ""
        enrollment = 0
        for student in self.get_students_by_major(major):
            class_names = self.students_registration_classes[student]
            for class_name in class_names:
                enrollment += 1
            if enrollment > most_popular_class:
                most_popular_class = class_name
        return most_popular_class