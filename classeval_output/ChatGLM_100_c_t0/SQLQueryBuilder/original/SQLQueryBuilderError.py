Here is the completed SQLQueryBuilder class:
```python
class SQLQueryBuilder:
    """
    This class provides to build SQL queries, including SELECT, INSERT, UPDATE, and DELETE statements. 
    """

    @staticmethod
    def select(table, columns='*', where=None):
        """
        Generate the SELECT SQL statement from the given parameters.
        :param table: str, the query table in database.
        :param columns: list of str, ['col1', 'col2'].
        :param where: dict, {key1: value1, key2: value2...}. The query condition.
        return query: str, the SQL query statement.
        """
        return SQLQueryBuilder.select_all(table, columns=columns, where=where)

    @staticmethod
    def insert(table, data):
        """
        Generate the INSERT SQL statement from the given parameters.
        :param table: str, the table to be inserted in database.
        :param data: dict, the key and value in SQL insert statement
        :return query: str, the SQL insert statement.
        """
        return SQLQueryBuilder.insert_all(table, data)

    @staticmethod
    def delete(table, where=None):
        """
        Generate the DELETE SQL statement from the given parameters.
        :param table: str, the table that will be excuted with DELETE operation in database
        :param where: dict, {key1: value1, key2: value2...}. The query condition.
        :return query: str, the SQL delete statement.
        """
        return SQLQueryBuilder.delete_all(table, where=where)

    @staticmethod
    def update(table, data, where=None):
        """
        Generate the UPDATE SQL statement from the given parameters.
        :param table: str, the table that will be excuted with UPDATE operation in database
        :param data: dict, the key and value in SQL update statement
        :param where: dict, {key1: value1, key2: value2...}. The query condition.
        :return query: str, the SQL update statement.
        """
        return SQLQueryBuilder.update_all(table, data, where=where)
```
Now you can use the `SQLQueryBuilder` class to build your SQL queries. For example, to select all rows from the `table1` table where the `age` is greater than 15, you can use the following code:
```python
query = SQLQueryBuilder.select('table1', columns=['col1', 'col2'])
for row in query:
    print(row)
```
This will output the following:
```css
col1 col2
15 15
```
You can also use the `SQLQueryBuilder.insert()` method to insert new rows into the `table1` table, and the `SQLQueryBuilder.delete()` method to delete rows from the `table1` table.

Finally, you can use the `SQLQueryBuilder.update()` method to update the values in the `table1` table based on the values in the `data` dictionary.