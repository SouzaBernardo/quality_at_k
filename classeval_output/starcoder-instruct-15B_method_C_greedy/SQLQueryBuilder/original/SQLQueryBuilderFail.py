
class SQLQueryBuilder: 






    def delete(table, where=None):
        """
        Generate the DELETE SQL statement from the given parameters.
        :param table: str, the table that will be excuted with DELETE operation in database
        :param where: dict, {key1: value1, key2: value2...}. The query condition.
        :return query: str, the SQL delete statement.
        >>> SQLQueryBuilder.delete('table1', {'name': 'Test', 'age': 14})
        "DELETE FROM table1 WHERE name='Test' AND age='14'"
        """
        where_clause = ''
        if where:
            where_clause = 'WHERE '
            where_clause +='AND '.join([f'{key}="{value}"' for key, value in where.items()])

        query = f'DELETE FROM {table} {where_clause}'
        return query

