import sqlite3

class StudentDatabaseProcessor:
    """
    This is a class with database operation, including inserting student information, searching for student information by name, and deleting student information by name.
    """

    def __init__(self, database_name):
        """
        Initializes the StudentDatabaseProcessor object with the specified database name.
        :param database_name: str, the name of the SQLite database.
        """
        self.database_name = database_name

    def create_student_table(self):
        """
        Creates a "students" table in the database if it does not exist already.Fields include ID of type int, name of type str, age of type int, gender of type str, and grade of type int
        :return: None
        >>> processor = StudentDatabaseProcessor("students.db")
        >>> processor.create_student_table()
        """

    def insert_student(self, student_data):
        """
        Inserts a new student into the "students" table.
        :param student_data: dict, a dictionary containing the student's information (name, age, gender, grade).
        :return: None
        >>> processor = StudentDatabaseProcessor("students.db")
        >>> processor.create_student_table()
        >>> student_data = {'name': 'John', 'age': 15, 'gender': 'Male', 'grade': 9}
        >>> processor.insert_student(student_data)
        """

    def search_student_by_name(self, name):
        """
        Searches for a student in the "students" table by their name.
        :param name: str, the name of the student to search for.
        :return: list of tuples, the rows from the "students" table that match the search criteria.
        >>> processor = StudentDatabaseProcessor("students.db")
        >>> processor.create_student_table()
        >>> result = processor.search_student_by_name("John")
        """

    def delete_student_by_name(self, name):
        """
        Deletes a student from the "students" table by their name.
        :param name: str, the name of the student to delete.
        :return: None
        >>> processor = StudentDatabaseProcessor("students.db")
        >>> processor.create_student_table()
        >>> student_data = {'name': 'John', 'age': 15, 'gender': 'Male', 'grade': 9}
        >>> processor.insert_student(student_data)
        >>> processor.delete_student_by_name("John")
        """

    def get_student_by_name(self, name):
        """
        Gets a student from the "students" table by their name.
        :param name: str, the name of the student to get.
        :return: dict, the student information.
        >>> processor = StudentDatabaseProcessor("students.db")
        >>> processor.create_student_table()
        >>> student_data = {'name': 'John', 'age': 15, 'gender': 'Male', 'grade': 9}
        >>> processor.insert_student(student_data)
        >>> result = processor.get_student_by_name("John")
        >>> result['name']
        'John'
        """

    def get_student_by_id(self, student_id):
        """
        Gets a student from the "students" table by its ID.
        :param student_id: int, the ID of the student to get.
        :return: dict, the student information.
        >>> processor = StudentDatabaseProcessor("students.db")
        >>> processor.create_student_table()
        >>> student_data = {'name': 'John', 'age': 15, 'gender': 'Male', 'grade': 9}
        >>> processor.insert_student(student_data)
        >>> result = processor.get_student_by_id(student_id)
        >>> result['name']
        'John'
        """

    def get_student_by_id_and_name(self, student_id, name):
        """
        Gets a student from the "students" table by its ID and name.
        :param student_id: int, the ID of the student to get.
        :param name: str, the name of the student to get.
        :return: dict, the student information.
        >>> processor = StudentDatabaseProcessor("students.db")
        >>> processor.create_student_table()
        >>> student_data = {'name': 'John', 'age': 15, 'gender': 'Male', 'grade': 9}
        >>> processor.insert_student(student_data)
        >>> result = processor.get_student_by_id_and_name(student_id, "John")
        >>> result['name']
        'John'
        """

    def get_student_by_id_and_name_and_age(self, student_id, name, age):
        """
        Gets a student from the "students" table by its ID and name and age.
        :param student_id: int, the ID of the student to get.
        :param name: str, the name of the student to get.
        :param age: int, the age of the student to get.
        :return: dict, the student information.
        >>> processor = StudentDatabaseProcessor("students.db")
        >>> processor.create_student_table()
        >>> student_data = {'name': 'John', 'age': 15, 'gender': 'Male', 'grade': 9}
        >>> processor.insert_student(student_data)
        >>> result = processor.get_student_by_id_and_name_and_age(student_id, "John", 18)
        >>> result['name']
        'John'
        """

    def get_student_by_id_and_name_and_age_and_gender(self, student_id, name, age, gender):
        """
        Gets a student from the "students" table by its ID and name and age and gender.
        :param student_id: int, the ID of the student to get.
        :param name: str, the name