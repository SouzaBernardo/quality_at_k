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
        try:
            conn = sqlite3.connect(self.database_name)
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, gender TEXT, grade INTEGER)''')
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)

    def insert_student(self, student_data):
        try:
            conn = sqlite3.connect(self.database_name)
            c = conn.cursor()
            c.execute("INSERT INTO students (name, age, gender, grade) VALUES (?, ?, ?, ?)", (student_data['name'], student_data['age'], student_data['gender'], student_data['grade']))
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)

    def search_student_by_name(self, name):
        try:
            conn = sqlite3.connect(self.database_name)
            c = conn.cursor()
            c.execute("SELECT * FROM students WHERE name = ?", (name,))
            rows = c.fetchall()
            conn.close()
            return [row[0] for row in rows]
        except Exception as e:
            print(e)

    def delete_student_by_name(self, name):
        try:
            conn = sqlite3.connect(self.database_name)
            c = conn.cursor()
            c.execute("DELETE FROM students WHERE name = ?", (name,))
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)