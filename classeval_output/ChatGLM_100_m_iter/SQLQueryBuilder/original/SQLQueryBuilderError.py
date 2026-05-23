
class SQLQueryBuilder:  
    """
    This class provides to build SQL queries, including SELECT, INSERT, UPDATE, and DELETE statements. 
    """



    def select(table: str, columns: list = ['*'], where: dict = None):
        """
        Generate the SELECT SQL statement from the given parameters.
        :param table: str, the query table in database.
        :param columns: list of str, ['col1', 'col2'].
        :param where: dict, {key1: value1, key2: value2...}. The query condition.
        return query: str, the SQL query statement.
        """
        return f"SELECT {table}, {columns} FROM {table} WHERE {where}"

    def insert(table: str, data: dict):
        """
        Generate the INSERT SQL statement from the given parameters.
        :param table: str, the table to be inserted in database.
        :param data: dict, the key and value in SQL insert statement
        :return query: str, the SQL insert statement.
        """
        query = f"INSERT INTO {table} ({data.keys())} VALUES ({data.values())}"
        return query

    def delete(table: str, where=None):
        """
        Generate the DELETE SQL statement from the given parameters.
        :param table: str, the table that will be deleted from the database
        :param where: dict, {key1: value1, key2: value2...}. The query condition.
        :return query: str, the SQL delete statement.
        """
        if where is None:
            where = {}
        query = f"DELETE FROM {table}"
        for key, value in where.items():
            query = query.replace(f"{key}={value}", value)
        return query


    def update(table: str, data: dict, where=None):
        """
        Generate the UPDATE SQL statement from the given parameters.
        :param table: str, the table that will be excuted with UPDATE operation in database
        :param data: dict, the key and value in SQL update statement
        :param where: dict, {key1: value1, key2: value2...}. The query condition.
        >>> SQLQueryBuilder.update('table1', {'name': 'Test2', 'age': 15}, where = {'name':'Test'})
        "UPDATE table1 SET name='Test2', age='15' WHERE name='Test'"
        """
        return SQLQueryBuilder.update(table, data, where)