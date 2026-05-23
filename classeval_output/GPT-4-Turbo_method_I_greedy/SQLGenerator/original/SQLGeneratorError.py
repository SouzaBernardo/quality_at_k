
class SQLGenerator: 
    def __init__(self, table_name):
        """
        Initialize the table name.
        :param table_name: str
        """
        self.table_name = table_name


    def select(self, fields=None, condition=None):
        """
        Generates a SELECT SQL statement based on the specified fields and conditions.
        :param fields: list, optional. Default is None. The list of fields to be queried.
        :param condition: str, optional. Default is None. The condition expression for the query.
        :return: str. The generated SQL statement.
        """
        if fields:
            fields_str = ', '.join(fields)
        else:
            fields_str = '*'
    
        sql = f'SELECT {fields_str} FROM {self.table_name}'
    
        if condition:
            sql += f' WHERE {condition}'
    
        sql += ';'
    
        return sql
    def insert(self, data):
        """
        Generates an INSERT SQL statement based on the given data.
        :param data: dict. The data to be inserted, in dictionary form where keys are field names and values are field values.
        :return: str. The generated SQL statement.
        """
        keys = ', '.join(data.keys())
        values = ', '.join(f"'{value}'" for value in data.values())
        sql = f"INSERT INTO {self.table_name} ({keys}) VALUES ({values});"
        return sql
    def update(self, data, condition):
        """
        Generates an UPDATE SQL statement based on the given data and condition.
        :param data: dict. The data to be updated, in dictionary form where keys are field names and values are new field values.
        :param condition: str. The condition expression for the update.
        :return: str. The generated SQL statement.
        """
        set_clause = ', '.join(f"{key} = '{value}'" for key, value in data.items())
        sql = f"UPDATE {self.table_name} SET {set_clause} WHERE {condition};"
        return sql
    def delete(self, condition):
        """
        Generates a DELETE SQL statement based on the given condition.
        :param condition: str. The condition expression for the delete.
        :return: str. The generated SQL statement.
        """
        sql = f"DELETE FROM {self.table_name} WHERE {condition};"
        return sql
    
    def select_female_under_age(self, age):
        condition = f"age < {age} AND gender = 'female'"
        return self.select(condition=condition)
    def select_by_age_range(self, min_age, max_age):
        condition = f"age BETWEEN {min_age} AND {max_age}"
        return self.select(condition=condition)
