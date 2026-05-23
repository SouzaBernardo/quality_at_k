class ClassRegistrationSystem:
    """
    This is a class as a class registration system, allowing to register students, register them for classes, retrieve students by major, get a list of all majors, and determine the most popular class within a specific major.
    """

    def __init__(self):
        """
        Initialize the registration system with the attribute students and students\_registration\_class.
        students is a list of student dictionaries, each student dictionary has the key of name and major.
        students\_registration\_class is a dictionaries, key is the student name, value is a list of class names
        """
        self.students = []
        self.students\_registration\_classes = {}

    def register\_student(self, student):
        """
        register a student to the system, add the student to the students list, if the student is already registered, return 0, else return 1
        """
        if student not in self.students:
            self.students.append(student)
            return 1
        else:
            return 0

    def register\_class(self, student\_name, class\_name):
        """
        register a class to the student.
        :param student\_name: str
        :param class\_name: str
        :return a list of class names that the student has registered
        >>> registration\_system = ClassRegistrationSystem()
        >>> registration\_system.register\_class(student\_name="John", class\_name="CS101")
        >>> registration\_system.register\_class(student\_name="John", class\_name="CS102")
        ["CS101", "CS102"]

    def get\_students\_by\_major(self, major):
        """
        get all students in the major
        :param major: str
        :return a list of student name
        >>> registration\_system = ClassRegistrationSystem()
        >>> student1 = {"name": "John", "major": "Computer Science"}
        >>> registration\_system.register\_student(student1)
        >>> registration\_system.get\_students\_by\_major("Computer Science")
        ["John"]
        """
        if major not in self.students:
            return []
        else:
            return [student["name"] for student in self.students if student["major"] == major]

    def get\_all\_majors(self):
        """
        get all majors in the system
        :return a list of majors
        >>> registration\_system = ClassRegistrationSystem()
        >>> registration\_system.students = [{"name": "John", "major": "Computer Science"}],
        >>> registration\_system.get\_all\_majors(student1)
        ["Computer Science"]
        """
        return [student["major"] for student in self.students]

    def get\_most\_popular\_class\_in\_major(self, major):
        """
        get the class with the highest enrollment in the major.
        :param major: str
        :return a string of the most popular class in this major
        >>> registration\_system = ClassRegistrationSystem()
        >>> registration\_system.students = [{"name": "John", "major": "Computer Science"},
        ...                                   {"name": "Bob", "major": "Computer Science"},
        ...                                   {"name": "Alice", "major": "Computer Science"}]
        >>> registration\_system.students\_registration\_classes = {"John": ["Algorithms", "Data Structures"],
        ...                                            "Bob": ["Operating Systems", "Data Structures", "Algorithms"]}
        >>> registration\_system.get\_most\_popular\_class\_in\_major("Computer Science")
        "Data Structures"
        """
        if major not in self.students\_registration\_classes:
            return ""
        else:
            most\_enrolled\_class = max(self.students\_registration\_classes[major], key=lambda x: len(x))
            return most\_enrolled\_class[0]

if __name__ == "__main__":
    registration\_system = ClassRegistrationSystem()
    print(registration\_system.get\_most\_popular\_class\_in\_major("Computer Science"))
```

This is a class as a class registration system, allowing to register students,