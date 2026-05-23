import sqlite3
class StudentDatabaseProcessor: 
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
        """
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            insert_query = f"INSERT INTO students (name, age, gender, grade) VALUES ('{student_data['name']}', {student_data['age']}, '{student_data['gender']}', {student_data['grade']})"
            cursor.execute(insert_query)


    def search_student_by_name(self, name):
        """
        Searches for a student in the "students" table by their name.
        :param name: str, the name of the student to search for.
        :return: list of tuples, the rows from the "students" table that match the search criteria.
        >>> processor = StudentDatabaseProcessor("students.db")
        >>> processor.create_student_table()
        >>> result = processor.search_student_by_name("John")
        >>> print(result)
        [(1, 'John', 25, 'Engineering')]
        """

    def delete_student_by_name(self, name):
        """
        Deletes a student from the "students" table by their name.
        :param name: str, the name of the student to delete.
        :return: None
        """
        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()
        query = '''DELETE FROM students WHERE name =?'''
        cursor.execute(query, (name,))
        connection.commit()
        connection.close()