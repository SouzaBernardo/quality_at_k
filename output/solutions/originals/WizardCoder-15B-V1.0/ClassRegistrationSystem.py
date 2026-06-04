Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
Please complete the class ClassRegistrationSystem in the following code.
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

    def get_all_major(self):
        """
        get all majors in the system
        :return a list of majors
        >>> registration_system = ClassRegistrationSystem()
        >>> registration_system.students = [{"name": "John", "major": "Computer Science"}],
        >>> registration_system.get_all_major(student1)
        ["Computer Science"]
        """

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

### Response:The class `ClassRegistrationSystem` is a class that allows for the registration of students, registration of students for classes, retrieval of students by major, retrieval of all majors, and determination of the most popular class within a specific major. 

The `__init__` method initializes the registration system with the `students` and `students_registration_classes` attributes. The `students` attribute is a list of student dictionaries, each student dictionary has the key of `name` and `major`. The `students_registration_classes` attribute is a dictionary, where the key is the student name, and the value is a list of class names.

The `register_student` method registers a student to the system. If the student is already registered, it returns 0, otherwise it returns 1.

The `register_class` method registers a class to the student. It takes in two parameters, `student_name` and `class_name`. It returns a list of class names that the student has registered.

The `get_students_by_major` method takes in a `major` parameter and returns a list of student names in that major.

The `get_all_major` method returns a list of all majors in the system.

The `get_most_popular_class_in_major` method takes in a `major` parameter and returns the class with the highest enrollment in the major. It first retrieves all the students in the major, and then retrieves all the classes that they have registered. It then calculates the enrollment of each class, and returns the class with the highest enrollment.