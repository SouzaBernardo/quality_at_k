class SQLGenerator:
    """
    This class generates SQL statements for common operations on a table, such as SELECT, INSERT, UPDATE, and DELETE.
    """

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
        >>> sql = SQLGenerator('table1')
        >>> sql.select(['field1', 'field2'], 'filed3 = value1')
        'SELECT field1, field2 FROM table1 WHERE filed3 = value1;'
        """

    def insert(self, data):
        """
        Generates an INSERT SQL statement based on the given data.
        :param data: dict. The data to be inserted, in dictionary form where keys are field names and values are field values.
        :return: str. The generated SQL statement.
        >>> sql.insert({'key1': 'value1', 'key2': 'value2'})
        "INSERT INTO table1 (key1, key2) VALUES ('value1', 'value2');"
        """


    def update(self, data, condition):
        """
        Generates an UPDATE SQL statement based on the given data and condition.
        :param data: dict. The data to be updated, in dictionary form where keys are field names and values are new field values.
        :param condition: str. The condition expression for the update.
        :return: str. The generated SQL statement.
        >>> sql.update({'field1': 'new_value1', 'field2': 'new_value2'}, "field3 = value1")
        "UPDATE table1 SET field1 = 'new_value1', field2 = 'new_value2' WHERE field3 = value1;"
        """

    def delete(self, condition):
        """
        Generates a DELETE SQL statement based on the given condition.
        :param condition: str. The condition expression for the delete.
        :return: str. The generated SQL statement.
        >>> sql.delete("field1 = value1")
        'DELETE FROM table1 WHERE field1 = value1;'
        """

    def select_female_under_age(self, age):
        """
        Generates a SQL statement to select females under a specified age.
        :param age: int. The specified age.
        :return: str. The generated SQL statement.
        >>> sql.select_female_under_age(30)
        "SELECT * FROM table1 WHERE age < 30 AND gender = 'female';"
        """

    def select_by_age_range(self, min_age, max_age):
        """
        Generates a SQL statement to select records within a specified age range.
        :param min_age: int. The minimum age.
        :param max_age: int. The maximum age.
        :return: str. The generated SQL statement.
        >>> sql.select_by_age_range(20, 30)
        'SELECT * FROM table1 WHERE age BETWEEN 20 AND 30;'
        """

    def select_by_gender(self, gender):
        """
        Generates a SQL statement to select records with a specified gender.
        :param gender: str. The specified gender.
        :return: str. The generated SQL statement.
        >>> sql.select_by_gender('male')
        'SELECT * FROM table1 WHERE gender = \'male\';'
        """

    def select_by_name(self, name):
        """
        Generates a SQL statement to select records with a specified name.
        :param name: str. The specified name.
        :return: str. The generated SQL statement.
        >>> sql.select_by_name('John Doe')
        'SELECT * FROM table1 WHERE name = \'John Doe\';'
        """

    def select_by_id(self, id):
        """
        Generates a SQL statement to select records with a specified ID.
        :param id: int. The specified ID.
        :return: str. The generated SQL statement.
        >>> sql.select_by_id(1)
        'SELECT * FROM table1 WHERE id = 1;'
        """

    def select_by_id_range(self, min_id, max_id):
        """
        Generates a SQL statement to select records with a specified ID range.
        :param min_id: int. The minimum ID.
        :param max_id: int. The maximum ID.
        :return: str. The generated SQL statement.
        >>> sql.select_by_id_range(1, 2)
        'SELECT * FROM table1 WHERE id BETWEEN 1 AND 2;'
        """

    def select_by_id_list(self, id_list):
        """
        Generates a SQL statement to select records with a specified ID list.
        :param id_list: list. The specified ID list.
        :return: str. The generated SQL statement.
        >>> sql.select_by_id_list([1, 2, 3])
        'SELECT * FROM table1 WHERE id IN (1, 2, 3);'
        """

    def select_by_id_list_range(self, min_id, max_id):
        """
        Generates a SQL statement to select records with a specified ID list range.
        :param min_id: int. The minimum ID.
        :param max_id: int. The maximum ID.
        :return: str. The generated SQL statement.
        >>> sql.select_by_id_list_range(1, 2)
        'SELECT * FROM table1 WHERE id BETWEEN 1 AND 2;'
        """

    def select_by_id_list_and_name(self, id_list, name):
        """
        Generates a SQL statement to select records with a specified ID list and name.
        :param id_list: list. The specified ID list.
        :param name: str. The specified name.
        :return: str. The generated SQL statement.
        >>> sql.select_by_id_list_and_name([1, 2, 3], 'John Doe')
        'SELECT * FROM table1 WHERE id IN (1, 2, 3) AND name = \'John Doe\';'
        """

    def select_by_id_list_and_name_range(self, min_id, max_id, name):
        """
        Generates a SQL statement to select records with a specified ID list and name range.
        :param min_id: int. The minimum ID.
        :param max_id: int. The maximum ID.
        :param name: str. The specified name.
        :return: str. The generated SQL statement.
        >>> sql.select_by_id_list_and_name_range(1, 2, 'John Doe')
        'SELECT * FROM table1 WHERE id BETWEEN 1 AND 2 AND name = \'John Doe\';'
        """

    def select_by_id_list_and_name_list(self, id_list, name_list):
        """
        Generates a SQL statement to select records with a specified ID list and name list.
        :param id_list: list. The specified ID list.
        :param name_list: list. The specified name list.
        :return: str. The generated SQL statement.
        >>> sql.select_by_id_list_and_name_list([1, 2, 3], ['John Doe', 'Jane Doe'])
        'SELECT * FROM table1 WHERE id IN (1, 2, 3) AND name IN (\'John Doe\', \'Jane Doe\');'
        """

    def select_by_id_list_and_name_list_range(self, min_id, max_id, name_list):
        """
        Generates a SQL statement to select records with a specified ID list and name list range.
        :param min_id: int. The minimum ID.
        :param max_id: int. The maximum ID.
        :param name_list: list. The specified name list.
        :return: str. The generated SQL statement.
        >>> sql.select_by_id_list_and_name_list_range(1, 2, ['John Doe', 'Jane Doe'])
        'SELECT * FROM table1 WHERE id BETWEEN 1 AND 2 AND name IN (\'John Doe\', \'Jane Doe\');'
        """

    def select_by_id_list_and_name_list_and_gender(self, id_list, name_list, gender):
        """
        Generates a SQL statement to select records with a specified ID list, name list, and gender.
        :param id_list: list. The specified ID list.
        :param name_list: list. The specified name list.
        :param gender: str. The specified gender.
        :return: str. The generated SQL statement.
        >>> sql.select_by_id_list_and_name_list_and_gender([1, 2, 3], ['John Doe', 'Jane Doe'],'male')
        'SELECT * FROM table