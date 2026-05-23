class SQLQueryBuilder: 






    def delete(table, where=None):
        """
        Generate the DELETE SQL statement from the given parameters.
        :param table: str, the table that will be excuted with DELETE operation in database
        :param where: dict, {key1: value1, key2: value2...}. The query condition.
        :return query: str, the SQL delete statement.
        """
        query = f"DELETE FROM {table}"
        if where:
            conditions = []
            for key, value in where.items():
                conditions.append(f"{key}='{value}'")
            query += f" WHERE {' AND '.join(conditions)}"
        return query