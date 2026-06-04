Please find the completed code for the ClassRegistrationSystem class below:

```python
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
        """
        register a student to the system, add the student to the students list, if the student is already registered, return 0, else return 1
        """
        if student in self.students:
            return 0
        else:
            self.students.append(student)
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
            if student["major"] not in majors:
                majors.append(student["major"])
        return majors

    def get_most_popular_class_in_major(self, major):
        """
        get the class with the highest enrollment in the major.
        :return  a string of the most popular class in this major
        """
        class_enrollment = {}
        for student, classes in self.students_registration_classes.items():
            if student in self.students:
                if self.students[student]["major"] == major:
                    for class_name in classes:
                        if class_name in class_enrollment:
                            class_enrollment[class_name] += 1
                        else:
                            class_enrollment[class_name] = 1
        most_popular_class = max(class_enrollment, key=class_enrollment.get)
        return most_popular_class
```

Please let me know if you need any further assistance!