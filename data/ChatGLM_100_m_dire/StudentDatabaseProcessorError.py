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
        conn = sqlite3.connect("students.db")
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS students (ID INTEGER PRIMARY KEY, name TEXT, age INTEGER, gender TEXT, grade INTEGER)")
        conn.commit()
        conn.close()

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
        self.student_table.insert_row(student_data)



    def delete_student_by_name(self, name):
        """
        Deletes a student from the "students" table by their name.
        :param name: str, the name of the student to delete.
        :return: None
        >>> processor = StudentDatabaseProcessor("students.db")
        >>> processor.create_student_table()
        >>> student_data = {'name': 'John', 'age': 15, 'gender': 'Male', 'grade': 9}
        >>> processor.insert_student(student_data)
        >>> processor.search_student_by_name("John")
        >>> processor.search_student_by_name("Jane")
        >>> processor.search_student_by_name("Bob")
        >>> processor.delete_student_by_name("John")
        >>> processor.delete_student_by_name("Jane")
        >>> processor.delete_student_by_name("Bob")
        """
        # Delete the student from the database
        self.delete_student(name)