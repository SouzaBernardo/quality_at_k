
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
            self.students_registration_classes[student] = []
            return 1

    def register_class(self, student_name, class_name):





    def get_students_by_major(self, major):


    def get_all_major(self):


    def get_most_popular_class_in_major(self, major):
