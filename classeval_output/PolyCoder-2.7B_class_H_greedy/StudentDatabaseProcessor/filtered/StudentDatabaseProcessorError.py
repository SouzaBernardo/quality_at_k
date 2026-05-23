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
        :param name: str, the name of the student to search for.
        :return: tuple, the row from the "students" table that matches the search criteria.
        >>> processor = StudentDatabaseProcessor("students.db")
        >>> processor.create_student_table()
        >>> result = processor.get_student_by_name("John")
        """

    def get_student_by_id(self, id):
        """
        Gets a student from the "students" table by its ID.
        :param id: int, the ID of the student to search for.
        :return: tuple, the row from the "students" table that matches the search criteria.
        >>> processor = StudentDatabaseProcessor("students.db")
        >>> processor.create_student_table()
        >>> result = processor.get_student_by_id(1)
        """

    def get_student_by_id_and_name(self, id, name):
        """
        Gets a student from the "students" table by its ID and its name.
        :param id: int, the ID of the student to search for.
        :param name: str, the name of the student to search for.
        :return: tuple, the row from the "students" table that matches the search criteria.
        >>> processor = StudentDatabaseProcessor("students.db")
        >>> processor.create_student_table()
        >>> result = processor.get_student_by_id_and_name(1, "John")
        """

    def get_student_by_id_and_name_and_age(self, id, name, age):
        """
        Gets a student from the "students" table by its ID and its name and age.
        :param id: int, the ID of the student to search for.
        :param name: str, the name of the student to search for.
        :param age: int, the age of the student to search for.
        :return: tuple, the row from the "students" table that matches the search criteria.
        >>> processor = StudentDatabaseProcessor("students.db")
        >>> processor.create_student_table()
        >>> result = processor.get_student_by_id_and_name_and_age(1, "John", 18)
        """

    def get_student_by_id_and_name_and_age_and_gender(self, id, name, age, gender):
        """
        Gets a student from the "students" table by its ID and its name and age and gender.
        :param id: int, the ID of the student to search for.
        :param name: str, the name of the student to search for.
        :param age: int, the age of the student to search for.
        :param gender: str, the gender of the student to search for.
        :return: tuple, the row from the "students" table that matches the search criteria.
        >>> processor = StudentDatabaseProcessor("students.db")
        >>> processor.create_student_table()
        >>> result = processor.get_student_by_id_and_name_and_age_and_gender(1, "John", 18, "Male")
        """

    def get_student_by_id_and_name_and_age_and_gender_and_grade(self, id, name, age, gender, grade):
        """
        Gets a student from the "students" table by its ID and its name and age and gender and grade.
        :param id: int, the ID of the student to search for.