
class SQLQueryBuilder: 


    @staticmethod
    def select(table, columns='*', where=None):
        """
        Generate the SELECT SQL statement from the given parameters.
        :param table: str, the query table in database.
        :param columns: list of str, ['col1', 'col2'].
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        return query: str, the SQL query statement.
        >>> SQLQueryBuilder.select('table1', columns = ["col1","col2"], where = {"age": 15})
        "SELECT col1, col2 FROM table1 WHERE age='15'"
        """
        query = "SELECT "
        if isinstance(columns, list):
            query += ", ".join(columns)
        else:
            query += columns
        query += " FROM " + table
        if where:
            query += " WHERE "
            conditions = []
            for key, value in where.items():
                conditions.append(f"{key}='{value}'")
            query += " AND ".join(conditions)
        return query
    

    @staticmethod
    def insert(table, data):
        """
        Generate the INSERT SQL statement from the given parameters.
        :param table: str, the table to be inserted in database.
        :param data: dict, the key and value in SQL insert statement
        :return query: str, the SQL insert statement.
        """
        columns = ', '.join(data.keys())
        values = ', '.join([f"'{value}'" for value in data.values()])
        query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
        return query
    

    @staticmethod
    def delete(table, where=None):
        """
        Generate the DELETE SQL statement from the given parameters.
        :param table: str, the table that will be executed with DELETE operation in the database
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        :return query: str, the SQL delete statement.
        >>> SQLQueryBuilder.delete('table1', {'name': 'Test', 'age': 14})
        "DELETE FROM table1 WHERE name='Test' AND age='14'"
        """
        query = "DELETE FROM " + table
        if where:
            conditions = []
            for key, value in where.items():
                conditions.append(key + "='" + str(value) + "'")
            query += " WHERE " + " AND ".join(conditions)
        return query
    

    @staticmethod
    def update(table, data, where=None):
        """
        Generate the UPDATE SQL statement from the given parameters.
        :param table: str, the table that will be executed with UPDATE operation in the database
        :param data: dict, the key and value in SQL update statement
        :param where: dict, {key1: value1, key2: value2 ...}. The query condition.
        :return: str, the generated UPDATE SQL statement
        """
        update_query = "UPDATE {} SET ".format(table)
        update_values = []
        for key, value in data.items():
            update_values.append("{}='{}'".format(key, value))
        update_query += ", ".join(update_values)
        if where:
            where_values = []
            for key, value in where.items():
                where_values.append("{}='{}'".format(key, value))
            update_query += " WHERE " + " AND ".join(where_values)
        return update_query
    