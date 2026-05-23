
class SQLQueryBuilder: 

    def select(self, table, columns='*', where=None):
        """
        Generate the SELECT SQL statement from the given parameters.
        :param table: str, the query table in database.
        :param columns: list of str, ['col1', 'col2'].
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        return query: str, the SQL query statement.
        """
        # Start building the query
        query = "SELECT "
    
        # Add the columns to the query
        if columns == '*':
            query += "* "
        else:
            query += ', '.join(columns) + " "
    
        # Add the table to the query
        query += "FROM " + table
    
        # Add the WHERE clause if it exists
        if where is not None:
            query += " WHERE " + ' AND '.join([f"{k}='{v}'" for k, v in where.items()])
    
        return query
    def insert(self, table, data):
        """
        Generate the INSERT SQL statement from the given parameters.
        :param table: str, the table to be inserted in database.
        :param data: dict, the key and value in SQL insert statement
        :return query: str, the SQL insert statement.
        """
        # Start building the query
        query = "INSERT INTO " + table
    
        # Add the columns and values to the query
        columns = ', '.join(data.keys())
        values = ', '.join([f"'{v}'" for v in data.values()])
        query += f" ({columns}) VALUES ({values})"
    
        return query
    @staticmethod
    def delete(table, where=None):
        """
        Generate the DELETE SQL statement from the given parameters.
        :param table: str, the table that will be excuted with DELETE operation in database
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        :return query: str, the SQL delete statement.
        >>> SQLQueryBuilder.delete('table1', {'name': 'Test', 'age': 14})
        "DELETE FROM table1 WHERE name='Test' AND age='14'"
        """
        # Start building the query
        query = "DELETE FROM " + table

        # Add the WHERE clause if it exists
        if where is not None:
            query += " WHERE " + ' AND '.join([f"{k}='{v}'" for k, v in where.items()])

        return query
    @staticmethod
    def update(table, data, where=None):
        """
        Generate the UPDATE SQL statement from the given parameters.
        :param table: str, the table that will be excuted with UPDATE operation in database
        :param data: dict, the key and value in SQL update statement
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        >>> SQLQueryBuilder.update('table1', {'name': 'Test2', 'age': 15}, where = {'name':'Test'})
        "UPDATE table1 SET name='Test2', age='15' WHERE name='Test'"
        """
        # Start building the query
        query = "UPDATE " + table

        # Add the columns and values to the query
        set_clause = ', '.join([f"{k}='{v}'" for k, v in data.items()])
        query += f" SET {set_clause}"

        # Add the WHERE clause if it exists
        if where is not None:
            query += " WHERE " + ' AND '.join([f"{k}='{v}'" for k, v in where.items()])

        return query
