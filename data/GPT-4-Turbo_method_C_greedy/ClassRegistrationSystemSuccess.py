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
        else:
            self.students_registration_classes[student_name] = [class_name]
        return self.students_registration_classes[student_name]
    def get_students_by_major(self, major):
        """
        get all students in the major
        :param major: str
        :return a list of student name
        """
        students_in_major = [student['name'] for student in self.students if student['major'] == major]
        return students_in_major
    def get_all_major(self):
        """
        get all majors in the system
        :return a list of majors
        """
        majors = []
        for student in self.students:
            if student["major"] not in majors:
                majors.append(student["major"])
        return majors
    def get_most_popular_class_in_major(self, major):
        """
        get the class with the highest enrollment in the major.
        :return  a string of the most popular class in this major
        """
        # Create a dictionary to store the count of each class
        class_count = {}
    
        # Iterate over each student
        for student in self.students:
            # Check if the student's major matches the input major
            if student["major"] == major:
                # If it does, iterate over the classes they're registered for
                for class_name in self.students_registration_classes[student["name"]]:
                    # If the class is already in the dictionary, increment its count
                    if class_name in class_count:
                        class_count[class_name] += 1
                    # If the class is not in the dictionary, add it with a count of 1
                    else:
                        class_count[class_name] = 1
    
        # Find the class with the highest count
        most_popular_class = max(class_count, key=class_count.get)
    
        return most_popular_class