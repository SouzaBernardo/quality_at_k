class SQLQueryBuilder:
    """
    This class provides to build SQL queries, including SELECT, INSERT, UPDATE, and DELETE statements. 
    """

    @staticmethod
    def select(table, columns='*', where=None):
        query = f"SELECT {', '.join(columns)} FROM {table}"
        if where:
            query += " WHERE " + " AND ".join([f"{k}='{v}'" for k, v in where.items()])
        return query

    @staticmethod
    def insert(table, data):
        keys = ', '.join(data.keys())
        values = ', '.join([f"'{v}'" for v in data.values()])
        query = f"INSERT INTO {table} ({keys}) VALUES ({values})"
        return query

    @staticmethod
    def delete(table, where=None):
        query = f"DELETE FROM {table}"
        if where:
            query += " WHERE " + " AND ".join([f"{k}='{v}'" for k, v in where.items()])
        return query

    @staticmethod
    def update(table, data, where=None):
        set_clause = ', '.join([f"{k}='{v}'" for k, v in data.items()])
        query = f"UPDATE {table} SET {set_clause}"
        if where:
            query += " WHERE " + " AND ".join([f"{k}='{v}'" for k, v in where.items()])
        return query