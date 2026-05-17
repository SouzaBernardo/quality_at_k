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
        register a student to the system, add the student to the students list, if the student is already registered, return 0, else return 1
        """
        for existing_student in self.students:
            if existing_student['name'] == student['name']:
                return 0
        self.students.append(student)
        self.students_registration_classes[student['name']] = []
        return 1
    def register_class(self, student_name, class_name):
        """
        register a class to the student.
        :param student_name: str
        :param class_name: str
        :return a list of class names that the student has registered
        """
        if student_name in self.students_registration_classes:
            self.students_registration_classes[student_name].append(class_name)
        return self.students_registration_classes[student_name]
    def get_students_by_major(self, major):
        """
        get all students in the major
        :param major: str
        :return a list of student name
        """
        students_in_major = []
        for student in self.students:
            if student['major'] == major:
                students_in_major.append(student['name'])
        return students_in_major
    def get_all_major(self):
        """
        get all majors in the system
        :return a list of majors
        """
        all_majors = []
        for student in self.students:
            if student['major'] not in all_majors:
                all_majors.append(student['major'])
        return all_majors
    def get_most_popular_class_in_major(self, major):
        """
        get the class with the highest enrollment in the major.
        :return  a string of the most popular class in this major
        """
        students_in_major = self.get_students_by_major(major)
        classes_in_major = []
        for student in students_in_major:
            classes_in_major.extend(self.students_registration_classes[student])
        class_counter = Counter(classes_in_major)
        most_common_class = class_counter.most_common(1)
        if most_common_class:
            return most_common_class[0][0]
        else:
            return None