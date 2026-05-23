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
        Creates a "students" table in the database if it does not exist already. Fields include ID of type int, name of type str, age of type int, gender of type str, and grade of type int
        :return: None
        """
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
    
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                ID INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER,
                gender TEXT,
                grade INTEGER
            )
        """)
    
        conn.commit()
        conn.close()
    def insert_student(self, student_data):
        """
        Inserts a new student into the "students" table.
        :param student_data: dict, a dictionary containing the student's information (name, age, gender, grade).
        :return: None
        """
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
    
        cursor.execute("""
            INSERT INTO students (name, age, gender, grade)
            VALUES (:name, :age, :gender, :grade)
        """, student_data)
    
        conn.commit()
        conn.close()
    def search_student_by_name(self, name):
        """
        Searches for a student in the "students" table by their name.
        :param name: str, the name of the student to search for.
        :return: list of tuples, the rows from the "students" table that match the search criteria.
        """
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
    
        cursor.execute("""
            SELECT * FROM students WHERE name = ?
        """, (name,))
    
        rows = cursor.fetchall()
    
        conn.close()
    
        return rows
    def delete_student_by_name(self, name):
        """
        Deletes a student from the "students" table by their name.
        :param name: str, the name of the student to delete.
        :return: None
        """
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
    
        cursor.execute("""
            DELETE FROM students WHERE name = ?
        """, (name,))
    
        conn.commit()
        conn.close()
