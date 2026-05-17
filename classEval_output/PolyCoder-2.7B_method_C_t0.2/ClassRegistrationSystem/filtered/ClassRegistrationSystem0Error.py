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
        if student.major in self.students_registration_classes:
            return 0
        self.students_registration_classes[student.major] = [student.name]
        self.students.append(student)
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
        >>> registration_system.get_students_by_major(major=1)
        [["John", "CS101"], ["John", "CS102"]]
        >>> registration_system.get_students_by_major(major=2)
        [["John", "CS101"], ["John", "CS102"], ["John", "CS103"]]
        >>> registration_system.get_students_by_major(major=3)
        []
        >>> registration_system.get_students_by_major(major=4)
        []
        >>> registration_system.get_students_by_major(major=5)
        []
        >>> registration_system.get_students_by_major(major=6)
        []
        >>> registration_system.get_students_by_major(major=7)
        []
        >>> registration_system.get_students_by_major(major=8)
        []
        >>> registration_system.get_students_by_major(major=9)
        []
        >>> registration_system.get_students_by_major(major=10)
        []
        >>> registration_system.get_students_by_major(major=11)
        []
        >>> registration_system.get_students_by_major(major=12)
        []
        >>> registration_system.get_students_by_major(major=13)
        []
        >>> registration_system.get_students_by_major(major=14)
        []
        >>> registration_system.get_students_by_major(major=15)
        []
        >>> registration_system.get_students_by_major(major=16)
        []
        >>> registration_system.get_students_by_major(major=17)
        []
        >>> registration_system.get_students_by_major(major=18)
        []
        >>> registration_system.get_students_by_major(major=19)
        []
        >>> registration_system.get_students_by_major(major=20)
        []
        >>> registration_system.get_students_by_major(major=21)
        []
        >>> registration_system.get_students_by_major(major=22)
        []
        >>> registration_system.get_students_by_major(major=23)
        []
        >>> registration_system.get_students_by_major(major=24)
        []
        >>> registration_system.get_students_by_major(major=25)
        []
        >>> registration_system.get_students_by_major(major=26)
        []
        >>> registration_system.get_students_by_major(major=27)
        []
        >>> registration_system.get_students_by_major(major=28)
        []
        >>> registration_system.get_students_by_major(major=29)
        []
        >>> registration_system.get_students_by_major(major=30)
        []
        >>> registration_system.get_students_by_major(major=31)
        []
        >>> registration_system.get_students_by_major(major=32)
        []
        >>> registration_system.get_students_by_major(major=33)
        []
        >>> registration_system.get_students_by_major(major=34)
        []
        >>> registration_system.get_students_by_major(major=35)
        []
        >>> registration_system.get_students_by_major(major=36)
        []
        >>> registration_system.get_students_by_major(major=37)
        []
        >>> registration_system.get_students_by_major(major=38)
        []
        >>> registration_system.get_students_by_major(major=39)
        []
        >>> registration_system.get_students_by_major(major=40)
        []
        >>> registration_system.get_students_by_major(major=41)
        []
        >>> registration_system.get_students_by_major(major=42)
        []
        >>> registration_system.get_students_by_major(major=43)
        """

    def get_students_by_major(self, major):
        """
        get all students in the major
        :param major: str
        :return a list of student name
        >>> registration_system = ClassRegistrationSystem()
        >>> student1 = {"name": "John", "major": "Computer Science"}
        >>> registration_system.register_student(student1)
        >>> registration_system.get_students_by_major("Computer Science")
        ["John"]
        """
        return self.students


    def get_all_major(self):
        """
        get all majors in the system
        :return a list of majors
        >>> registration_system = ClassRegistrationSystem()
        >>> registration_system.students = [{"name": "John", "major": "Computer Science"}],
        >>> registration_system.get_all_major(student1)
        ["Computer Science"]
        """
        return self.students


    def get_most_popular_class_in_major(self, major):
        """
        get the class with the highest enrollment in the major.
        :return  a string of the most popular class in this major
        >>> registration_system = ClassRegistrationSystem()
        >>> registration_system.students = [{"name": "John", "major": "Computer Science"},
                                             {"name": "Bob", "major": "Computer Science"},
                                             {"name": "Alice", "major": "Computer Science"}]
        >>> registration_system.students_registration_classes = {"John": ["Algorithms", "Data Structures"],
                                            "Bob": ["Operating Systems", "Data Structures", "Algorithms"]}
        >>> registration_system.get_most_popular_class_in_major("Computer Science")
        "Data Structures"
        """
        return self.students_registration_classes[major][0]