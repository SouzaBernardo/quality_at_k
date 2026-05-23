
class SQLGenerator: 
    def __init__(self, table_name):
        """
        Initialize the table name.
        :param table_name: str
        """
        self.table_name = table_name



    def select(self, fields=None, condition=None):
        """
        Generates a SELECT SQL statement based on the specified fields and conditions.
        :param fields: list, optional. Default is None. The list of fields to be queried.
        :param condition: str, optional. Default is None. The condition expression for the query.
        :return: str. The generated SQL statement.
        """
        if fields is None:
            fields = '*'
        else:
            fields = ', '.join(fields)
    
        sql = f"SELECT {fields} FROM {self.table_name}"
    
        if condition is not None:
            sql += f" WHERE {condition}"
    
        sql += ";"
    
        return sql
    

    def insert(self, data):
        """
        Generates an INSERT SQL statement based on the given data.
        :param data: dict. The data to be inserted, in dictionary form where keys are field names and values are field values.
        :return: str. The generated SQL statement.
        """
        fields = ', '.join(data.keys())
        values = "', '".join(data.values())
        sql_statement = f"INSERT INTO {self.table_name} ({fields}) VALUES ('{values}');"
        return sql_statement
    

    def update(self, data, condition):
        """
        Generates an UPDATE SQL statement based on the given data and condition.
        :param data: dict. The data to be updated, in dictionary form where keys are field names and values are new field values.
        :param condition: str. The condition expression for the update.
        :return: str. The generated SQL statement.
        """
        set_clause = ", ".join([f"{field} = '{value}'" for field, value in data.items()])
        sql_statement = f"UPDATE {self.table_name} SET {set_clause} WHERE {condition};"
        return sql_statement
    

    def delete(self, condition):
        """
        Generates a DELETE SQL statement based on the given condition.
        :param condition: str. The condition expression for the delete.
        :return: str. The generated SQL statement.
        """
        sql_statement = f"DELETE FROM {self.table_name} WHERE {condition};"
        return sql_statement
    

    def select_female_under_age(self, age):
        """
        Generates a SQL statement to select females under a specified age.
        :param age: int. The specified age.
        :return: str. The generated SQL statement.
        """
        sql_statement = f"SELECT * FROM {self.table_name} WHERE age < {age} AND gender = 'female';"
        return sql_statement
    

    def select_by_age_range(self, min_age, max_age):
        """
        Generates a SQL statement to select records within a specified age range.
        :param min_age: int. The minimum age.
        :param max_age: int. The maximum age.
        :return: str. The generated SQL statement.
        """
        sql_statement = f"SELECT * FROM {self.table_name} WHERE age BETWEEN {min_age} AND {max_age};"
        return sql_statement
    