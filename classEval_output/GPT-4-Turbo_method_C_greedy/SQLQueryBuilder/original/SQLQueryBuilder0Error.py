
class SQLQueryBuilder: 

    @staticmethod
    def select(table, columns='*', where=None):
        # Start the query
        query = "SELECT "
    
        # Add the columns or default to *
        if columns != '*':
            query += ', '.join(columns)
        else:
            query += '*'
    
        # Add the table
        query += " FROM " + table
    
        # Add the WHERE clause if it exists
        if where is not None:
            query += " WHERE " + ' AND '.join([f"{k}='{v}'" for k, v in where.items()])
    
        return query
    @staticmethod
    def insert(table, data):
        keys = ', '.join(data.keys())
        values = ', '.join(f"'{value}'" if isinstance(value, str) else str(value) for value in data.values())
        query = f"INSERT INTO {table} ({keys}) VALUES ({values})"
        return query
    @staticmethod
    def delete(table, where=None):
        query = "DELETE FROM " + table
        if where:
            conditions = []
            for key, value in where.items():
                conditions.append(f"{key}='{value}'")
            query += " WHERE " + " AND ".join(conditions)
        return query
    @staticmethod
    def update(table, data, where=None):
        # Start the query
        query = f"UPDATE {table} SET "
    
        # Add each data item to the query
        for key, value in data.items():
            query += f"{key}='{value}', "
    
        # Remove the last comma and space
        query = query[:-2]
    
        # If a WHERE clause was provided
        if where is not None:
            query += " WHERE "
    
            # Add each condition to the query
            for key, value in where.items():
                query += f"{key}='{value}' AND "
    
            # Remove the last AND and space
            query = query[:-5]
    
        # Return the final query
        return query
