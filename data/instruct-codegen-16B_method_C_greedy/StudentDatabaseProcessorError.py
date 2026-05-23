import sqlite3
class StudentDatabaseProcessor: 
    def __init__(self, database_name):
        """
        Initializes the StudentDatabaseProcessor object with the specified database name.
        :param database_name: str, the name of the SQLite database.
        """
        self.database_name = database_name







    def search_student_by_name(self, name):
        """
        Searches for a student in the "students" table by their name.
        :param name: str, the name of the student to search for.
        :return: list of tuples, the rows from the "students" table that match the search criteria.
        """
        query = f"SELECT * FROM students WHERE name='{name}'"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def delete_student_by_name(self, name):
        """
        Deletes a student from the "students" table in the database by their name.
        :param name: str, the name of the student to delete.
        :return: None
        """
        conn = sqlite3.connect(self.database_name)
        c = conn.cursor()
        c.execute("DELETE FROM students WHERE name=:name", {'name': name})
        conn.commit()
        conn.close()