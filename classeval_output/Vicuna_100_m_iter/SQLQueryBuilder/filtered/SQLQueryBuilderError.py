class SQLQueryBuilder:  
    """
    This class provides to build SQL queries, including SELECT, INSERT, UPDATE, and DELETE statements. 
    """





    def insert(table, data):
        """
        Generate the INSERT SQL statement from the given parameters.
        :param table: str, the table to be inserted in database.
        :param data: dict, the key and value in SQL insert statement
        :return query: str, the SQL insert statement.
        >>> SQLQueryBuilder.insert('table1', {'name': 'Test', 'age': 14})
        "INSERT INTO table1 (name, age) VALUES ('Test', '14')"
        """
        query = f"INSERT INTO {table} ({', '.join(['%s'] * len(data))}) VALUES (%s)"
        values = [data[key] for key in data]
        return query % tuple(values)

    def delete(table, where=None):

    def update(table, data, where=None):
        """
        Generate the UPDATE SQL statement from the given parameters.
    
        :param table: str, the table that will be excuted with UPDATE operation in database
        :param data: dict, the key and value in SQL update statement
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        :return: str, the SQL update statement.
        >>> SQLQueryBuilder.update('table1', {'name': 'Test2', 'age': 15}, where = {'name':'Test'})
        "UPDATE table1 SET name='Test2', age='15' WHERE name='Test'"
        """
        query = "UPDATE " + table + " SET "
        for key, value in data.items():
            query += key + "=" + str(value) + ", "
        query = query[:-2] + " WHERE " + where
        return query