```python
class SQLGenerator:
    def __init__(self, table_name):
        self.table_name = table_name

    def select(self, fields=None, condition=None):
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
        keys = ', '.join(data.keys())
        values = ', '.join(f"'{v}'" for v in data.values())
        sql = f"INSERT INTO {self.table_name} ({keys}) VALUES ({values});"
        return sql

    def update(self, data, condition):
        updates = ', '.join(f"{k} = '{v}'" for k, v in data.items())
        sql = f"UPDATE {self.table_name} SET {updates} WHERE {condition};"
        return sql

    def delete(self, condition):
        sql = f"DELETE FROM {self.table_name} WHERE {condition};"
        return sql

    def select_female_under_age(self, age):
        sql = f"SELECT * FROM {self.table_name} WHERE age < {age} AND gender = 'female';"
        return sql

    def select_by_age_range(self, min_age, max_age):
        sql = f"SELECT * FROM {self.table_name} WHERE age BETWEEN {min_age} AND {max_age};"
        return sql
```
This code completes the SQLGenerator class by implementing the methods to generate SQL statements for SELECT, INSERT, UPDATE, DELETE, and two specific SELECT operations. The methods take in parameters as described in the docstrings and return the corresponding SQL statements as strings.