
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
        else:
            self.students.append(student)
            if student['name'] in self.students_registration_classes:
                self.students_registration_classes[student['name']].append(student['major'])
            else:
                self.students_registration_classes[student['name']] = [student['major']]
            return 1

    def register_class(self, student_name, class_name):
        """
        register a class to the student.
        :param student_name: str
        :param class_name: str
        :return a list of class names that the student has registered
        """
        if student_name in self.students_registration_classes:
            if class_name in self.students_registration_classes[student_name]:
                return 0
            else:
                self.students_registration_classes[student_name].append(class_name)
                return 1
        else:
            self.students_registration_classes[student_name] = [class_name]
            return 1

    def get_students_by_major(self, major):
        """
        get all students in the major
        :param major: str
        :return a list of student name
        """
        return [student['name'] for student in self.students if student['major'] == major]

    def get_all_major(self):
        """
        get all majors in the system
        :return a list of majors
        """
        return list(set([student['major'] for student in self.students]))

    def get_most_popular_class_in_major(self, major):
        """
        get the class with the highest enrollment in the major.
        :return 

        """
        most_popular_class = ""
        max_enrollment = 0
        for student in self.students:
            if student['major'] == major:
                if len(self.students_registration_classes[student['name']]) > max_enrollment:
                    max_enrollment = len(self.students_registration_classes[student['name']])
                    most_popular_class = self.students_registration_classes[student['name']][0]
        return most_popular_class