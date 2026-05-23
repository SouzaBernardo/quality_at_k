
class SQLQueryBuilder:  
    """
    This class provides to build SQL queries, including SELECT, INSERT, UPDATE, and DELETE statements. 
    """



    def select(table, columns='*', where=None):
        """
        Generate the SELECT SQL statement from the given parameters.
        :param table: str, the query table in database.
        :param columns: list of str, ['col1', 'col2'].
        :param where: dict, {key1: value1, key2: value2...}. The query condition.
        return query: str, the SQL query statement.
        """
        query = f"SELECT {', '.join(columns)} FROM {table}"
        if where:
            conditions = []
            for key, value in where.items():
                conditions.append(f"{key}='{value}'")
            query += f" WHERE {' AND '.join(conditions)}"
        return query





