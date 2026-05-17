import sqlite3
import pandas as pd

class DatabaseProcessor:
    """
    This is a class for processing a database, supporting to create tables, insert data into the database, search for data based on name, and delete data from the database.
    """


    def __init__(self, database_name):
        """
        Initialize database name of database processor
        """
        self.database_name = database_name


    def create_table(self, table_name, key1, key2):
        """
        Create a new table in the database if it doesn't exist.
        And make id (INTEGER) as PRIMARY KEY, make key1 as TEXT, key2 as INTEGER
        :param table_name: str, the name of the table to create.
        :param key1: str, the name of the first column in the table.
        :param key2: str, the name of the second column in the table.
        >>> db.create_table('user', 'name', 'age')
        """


    def insert_into_database(self, table_name, data):
        """
        Insert data into the specified table in the database.
        :param table_name: str, the name of the table to insert data into.
        :param data: list, a list of dictionaries where each dictionary represents a row of data.
        >>> db.insert_into_database('user', [
                {'name': 'John', 'age': 25},
                {'name': 'Alice', 'age': 30}
            ])
        """


    def search_database(self, table_name, name):
        """
        Search the specified table in the database for rows with a matching name.
        :param table_name: str, the name of the table to search.
        :param name: str, the name to search for.
        :return: list, a list of tuples representing the rows with matching name, if any;
                    otherwise, returns None.
        >>> db.search_database('user', 'John')
        [(1, 'John', 25)]
        """


    def delete_from_database(self, table_name, name):
        """
        Delete rows from the specified table in the database with a matching name.
        :param table_name: str, the name of the table to delete rows from.
        :param name: str, the name to match for deletion.
        >>> db.delete_from_database('user', 'John')
        """


    def get_table_names(self):
        """
        Return a list of the names of all tables in the database.
        :return: list, a list of strings representing the names of all tables in the database.
        >>> db.get_table_names()
        ['user', 'user_name', 'user_name_2', 'user_name_3', 'user_name_4', 'user_name_5', 'user_name_6', 'user_name_7', 'user_name_8', 'user_name_9', 'user_name_10', 'user_name_11', 'user_name_12', 'user_name_13', 'user_name_14', 'user_name_15', 'user_name_16', 'user_name_17', 'user_name_18', 'user_name_19', 'user_name_20', 'user_name_21', 'user_name_22', 'user_name_23', 'user_name_24', 'user_name_25', 'user_name_26', 'user_name_27', 'user_name_28', 'user_name_29', 'user_name_30', 'user_name_31', 'user_name_32', 'user_name_33', 'user_name_34', 'user_name_35', 'user_name_36', 'user_name_37', 'user_name_38', 'user_name_39', 'user_name_40', 'user_name_41', 'user_name_42', 'user_name_43', 'user_name_44', 'user_name_45', 'user_name_46', 'user_name_47', 'user_name_48', 'user_name_49', 'user_name_50', 'user_name_51', 'user_name_52', 'user_name_53', 'user_name_54', 'user_name_55', 'user_name_56', 'user_name_57', 'user_name_58', 'user_name_59', 'user_name_60', 'user_name_61', 'user_name_62', 'user_name_63', 'user_name_64', 'user_name_65', 'user_name_66', 'user_name_67', 'user_name_68', 'user_name_69', 'user_name_70', 'user_name_71', 'user_name_72', 'user_name_73', 'user_name_74', 'user_name_75', 'user_name_76', 'user_name_77', 'user_name_78', 'user_name_79', 'user_name_80', 'user_name_81', 'user_name_82', 'user_name_83', 'user_name_84', 'user_name_85', 'user_name_86', 'user_name_87', 'user_name_88', 'user_name_89', 'user_name_90', 'user_name_91', 'user_name_92', 'user_name_93', 'user_name_94', 'user_name_95', 'user_name_96', 'user_name_97', 'user_name_98', 'user_name_99', 'user_name_100', 'user_name_101', 'user_name_102', 'user_name_103', 'user_name_104', 'user_name_105', 'user_name_106', 'user_name_107', 'user_name_108', 'user_name_109', 'user_name_110', 'user_name_111', 'user_name_112', 'user_name_113', 'user_name_114', 'user_name_115', 'user_name_116', 'user_name_117', 'user_name_118', 'user_name_119', 'user_name_120', 'user_name_121', 'user_name_122', 'user_name_123', 'user_name_124', 'user_name_125', 'user_name_126', 'user_name_127', 'user_name_128', 'user_name_129', 'user_name_130', 'user_name_131', 'user_name_132', 'user_name_133', 'user_name_134', 'user_name_135', 'user_name_136', 'user_name_137', 'user_name_138', 'user_name_139', 'user_name_140', 'user_name_141', 'user_name_142', 'user_name_143', 'user_name_144', 'user_name_145', 'user_name_146', 'user_name_147', 'user_name_148', 'user_name_149', 'user_name_150', 'user_name_151', 'user_name_152', 'user_name_153', 'user_name_154', 'user_name_155', 'user_name_156', 'user_name_157', 'user_name_158', 'user_name_159', 'user_