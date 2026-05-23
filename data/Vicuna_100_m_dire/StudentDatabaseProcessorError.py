import sqlite3
class StudentDatabaseProcessor: 
    def __init__(self, database_name):
        """
        Initializes the StudentDatabaseProcessor object with the specified database name.
        :param database_name: str, the name of the SQLite database.
        """
        self.database_name = database_name



    def create_student_table(self):
        try:
            conn = sqlite3.connect(self.database_name)
            c = conn.cursor()
            c.execute("""CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER, gender TEXT, grade INTEGER)""")
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)

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
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        c.execute("INSERT INTO students (name, age, gender, grade) VALUES (?, ?, ?, ?)", [student_data['name'], student_data['age'], student_data['gender'], student_data['grade']])
        conn.commit()
        conn.close()

    def search_student_by_name(self, name):
        """
        Searches for a student in the "students" table by their name.
        :param name: str, the name of the student to search for.
        :return: list of tuples, the rows from the "students" table that match the search criteria.
        >>> processor = StudentDatabaseProcessor("students.db")
        >>> processor.create_student_table()
        >>> result = processor.search_student_by_name("John")
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
        return cursor.fetchall()

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
        >>> processor.create_student_table()
        >>> student_data = {'name': 'Jane', 'age': 16, 'gender': 'Female', 'grade': 10}
        >>> processor.insert_student(student_data)
        >>> processor.delete_student_by_name("Jane")