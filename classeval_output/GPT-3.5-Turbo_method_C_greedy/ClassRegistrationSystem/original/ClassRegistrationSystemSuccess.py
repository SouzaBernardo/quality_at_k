
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
        """
        Register a student to the system, add the student to the students list. If the student is already registered, return 0, else return 1.
        """
        for existing_student in self.students:
            if existing_student['name'] == student['name']:
                return 0
        self.students.append(student)
        return 1
    

    def register_class(self, student_name, class_name):
        """
        Register a class to the student.
        :param student_name: str
        :param class_name: str
        :return: a list of class names that the student has registered
        """
        if student_name in self.students_registration_classes:
            self.students_registration_classes[student_name].append(class_name)
        else:
            self.students_registration_classes[student_name] = [class_name]
        return self.students_registration_classes[student_name]
    

    def get_students_by_major(self, major):
        """
        Get all students in the major
        :param major: str
        :return: a list of student names
        """
        students_in_major = []
        for student in self.students:
            if student["major"] == major:
                students_in_major.append(student["name"])
        return students_in_major
    

    def get_all_major(self):
        """
        get all majors in the system
        :return a list of majors
        """
        majors = []
        for student in self.students:
            major = student.get("major")
            if major not in majors:
                majors.append(major)
        return majors
    

    def get_most_popular_class_in_major(self, major):
        class_enrollment = {}
        
        for student in self.students:
            if student["major"] == major:
                for class_name in self.students_registration_classes.get(student["name"], []):
                    class_enrollment[class_name] = class_enrollment.get(class_name, 0) + 1
        
        most_popular_class = max(class_enrollment, key=class_enrollment.get)
        return most_popular_class
    