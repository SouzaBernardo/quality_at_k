class SQLQueryBuilder:  
    """
    This class provides to build SQL queries, including SELECT, INSERT, UPDATE, and DELETE statements. 
    """







    def delete(table, where=None):
        query = "DELETE FROM {}".format(table)
        if where:
            query += " WHERE "
            for key, value in where.items():
                query += key + "='" + str(value) + "' AND "
        query = query[:-4]
        return query