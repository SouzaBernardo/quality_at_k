
class SQLGenerator: 
    def __init__(self, table_name):
        """
        Initialize the table name.
        :param table_name: str
        """
        self.table_name = table_name









    def delete(self, condition):
        """
        Generates a DELETE SQL statement based on the given condition.
        :param condition: str. The condition expression for the delete.
        :return: str. The generated SQL statement.
        >>> sql.delete("field1 = value1")
        'DELETE FROM table1 WHERE field1 = value1;'
        """
        sql = f"DELETE FROM {self.table_name}"
        if condition is not None:
            sql += f" WHERE {condition}"
        sql += ";"
        return sql



