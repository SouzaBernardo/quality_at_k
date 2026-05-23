class SQLGenerator:  
    """
    This class generates SQL statements for common operations on a table, such as SELECT, INSERT, UPDATE, and DELETE.
    """

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
        # Start building the SQL statement
        sql = "SELECT "
    
        # Add the fields to be queried
        if fields is not None:
            sql += ", ".join(fields)
        else:
            sql += "*"
    
        # Add the table name
        sql += " FROM " + self.table_name
    
        # Add the condition if provided
        if condition is not None:
            sql += " WHERE " + condition
    
        # Add the semicolon at the end
        sql += ";"
    
        return sql
    

    def insert(self, data):
        """
        Generates an INSERT SQL statement based on the given data.
        :param data: dict. The data to be inserted, in dictionary form where keys are field names and values are field values.
        :return: str. The generated SQL statement.
        """
        # Start building the SQL statement
        sql = "INSERT INTO " + self.table_name + " ("
    
        # Add the field names
        sql += ", ".join(data.keys())
    
        # Add the field values
        sql += ") VALUES ("
        sql += ", ".join("'" + str(value) + "'" for value in data.values())
        sql += ");"
    
        return sql
    

    def update(self, data, condition):
        """
        Generates an UPDATE SQL statement based on the given data and condition.
        :param data: dict. The data to be updated, in dictionary form where keys are field names and values are new field values.
        :param condition: str. The condition expression for the update.
        :return: str. The generated SQL statement.
        """
        # Start building the SQL statement
        sql = "UPDATE " + self.table_name + " SET "
        
        # Add the field names and new values
        sql += ", ".join(field + " = '" + str(value) + "'" for field, value in data.items())
        
        # Add the condition
        sql += " WHERE " + condition
        
        # Add the semicolon at the end
        sql += ";"
        
        return sql
    

    def delete(self, condition):
        """
        Generates a DELETE SQL statement based on the given condition.
        :param condition: str. The condition expression for the delete.
        :return: str. The generated SQL statement.
        """
        # Start building the SQL statement
        sql = "DELETE FROM " + self.table_name
        
        # Add the condition
        sql += " WHERE " + condition
        
        # Add the semicolon at the end
        sql += ";"
        
        return sql
    

    def select_female_under_age(self, age):
        """
        Generates a SQL statement to select females under a specified age.
        :param age: int. The specified age.
        :return: str. The generated SQL statement.
        """
        # Build the condition for selecting females under the specified age
        condition = "age < " + str(age) + " AND gender = 'female'"
        
        # Use the select method to generate the SQL statement
        sql = self.select(condition=condition)
        
        return sql
    

    def select_by_age_range(self, min_age, max_age):
        """
        Generates a SQL statement to select records within a specified age range.
        :param min_age: int. The minimum age.
        :param max_age: int. The maximum age.
        :return: str. The generated SQL statement.
        """
        # Build the condition for selecting records within the specified age range
        condition = "age BETWEEN " + str(min_age) + " AND " + str(max_age)
        
        # Use the select method to generate the SQL statement
        sql = self.select(condition=condition)
        
        return sql