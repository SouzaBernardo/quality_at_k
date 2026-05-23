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
            return 1


    def register_class(self, class_name, class_capacity, enrolled_students):


    def register_class(self, student_name, class_name):
        
        if student_name in self.students_registration_classes:
            self.students_registration_classes[student_name].append(class_name)
        else:
            self.students_registration_classes[student_name] = [class_name]

        return self.students_registration_classes[student_name]


    def get_students_by_major(self, major_name):


    def get_students_by_major(self, major):
        

        students_by_major = []
        for student in self.students:
            if student["major"] == major:
                students_by_major.append(student["name"])
        return students_by_major


    def get_all_majors(self):


    def get_all_majors(self):


    def get_all_major(self):


    def get_most_popular_class_in_major(self, major):