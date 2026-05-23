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
        """
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    gender TEXT,
    grade INTEGER
);""")
        conn.close()
    def insert_student(self, student_data):
        """
        Inserts a new student into the "students" table.
        :param student_data: dict, a dictionary containing the student's information (name, age, gender, grade).
        :return: None
        """
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        c.execute("""INSERT INTO students (name, age, gender, grade) VALUES (?,?,?,?)""", (student_data['name'], student_data['age'], student_data['gender'], student_data['grade']))
        conn.commit()
        conn.close()
    def search_student_by_name(self, name):
        """
        Searches for a student in the "students" table by their name.
        :param name: str, the name of the student to search for.
        :return: list of tuples, the rows from the "students" table that match the search criteria.
        """
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        c.execute("""SELECT * FROM students WHERE name =?""", (name,))
        rows = c.fetchall()
        conn.close()
        return rows
    def delete_student_by_name(self, name):
        """
        Deletes a student from the "students" table by their name.
        :param name: str, the name of the student to delete.
        :return: None
        """
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        c.execute("""DELETE FROM students WHERE name =?""", (name,))
        conn.commit()
        conn.close()