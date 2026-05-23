import itertools

class ArrangementCalculator:
    """
    The Arrangement class provides permutation calculations and selection operations for a given set of data elements.
    """

    def __init__(self, datas):
        """
        Initializes the ArrangementCalculator object with a list of datas.
        :param datas: List, the data elements to be used for arrangements.
        """
        self.datas = datas

    @staticmethod
    def count(n, m=None):
        """
        Counts the number of arrangements by choosing m items from n items (permutations).
        If m is not provided or n equals m, returns factorial(n).
        :param n: int, the total number of items.
        :param m: int, the number of items to be chosen (default=None).
        :return: int, the count of arrangements.
        >>> ArrangementCalculator.count(5, 3)
        60

        """

    @staticmethod
    def count_all(n):
        """
        Counts the total number of all possible arrangements by choosing at least 1 item and at most n items from n items.
        :param n: int, the total number of items.
        :return: int, the count of all arrangements.
        >>> ArrangementCalculator.count_all(4)
        64

        """


    def select(self, m=None):
        """
        Generates a list of arrangements by selecting m items from the internal datas.
        If m is not provided, selects all items.
        :param m: int, the number of items to be chosen (default=None).
        :return: List, a list of arrangements.
        >>> ac = ArrangementCalculator([1, 2, 3, 4])
        >>> ac.select(2)
        [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]]

        """


    def select_all(self):
        """
        Generates a list of all arrangements by selecting at least 1 item and at most the number of internal datas.
        :return: List, a list of all arrangements.
        >>> ac = ArrangementCalculator([1, 2, 3])
        >>> ac.select_all()
        [[1], [2], [3], [1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2], [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

        """


    @staticmethod
    def factorial(n):
        """
        Calculates the factorial of a given number.
        :param n: int, the number to calculate the factorial.
        :return: int, the factorial of the given number.
        >>> ArrangementCalculator.factorial(4)
        24

        """


    @staticmethod
    def permutations(n):
        """
        Calculates the number of permutations of a given number.
        :param n: int, the number to calculate the permutations.
        :return: int, the number of permutations of the given number.
        >>> ArrangementCalculator.permutations(4)
        240

        """


    @staticmethod
    def combinations(n, m):
        """
        Calculates the number of combinations of a given number and a given number of items.
        :param n: int, the number to calculate the combinations.
        :param m: int, the number of items to calculate the combinations.
        :return: int, the number of combinations of the given number and the given number of items.
        >>> ArrangementCalculator.combinations(4, 2)
        120

        """


    @staticmethod
    def combinations_all(n, m):
        """
        Calculates the number of all combinations of a given number and a given number of items.
        :param n: int, the number to calculate the combinations.
        :param m: int, the number of items to calculate the combinations.
        :return: int, the number of all combinations of the given number and the given number of items.
        >>> ArrangementCalculator.combinations_all(4, 2)
        1200

        """


    @staticmethod
    def combinations_all_with_replacement(n, m):
        """
        Calculates the number of all combinations of a given number and a given number of items with replacement.
        :param n: int, the number to calculate the combinations.
        :param m: int, the number of items to calculate the combinations.
        :return: int, the number of all combinations of the given number and the given number of items with replacement.
        >>> ArrangementCalculator.combinations_all_with_replacement(4, 2)
        1200

        """


    @staticmethod
    def combinations_with_replacement(n, m):
        """
        Calculates the number of combinations of a given number and a given number of items with replacement.
        :param n: int, the number to calculate the combinations.
        :param m: int, the number of items to calculate the combinations.
        :return: int, the number of combinations of the given number and the given number of items with replacement.
        >>> ArrangementCalculator.combinations_with_replacement(4, 2)
        1200

        """


    @staticmethod
    def combinations_with_replacement_all(n, m):
        """
        Calculates the number of all combinations of a given number and a given number of items with replacement.
        :param n: int, the number to calculate the combinations.
        :param m: int, the number of items to calculate the combinations.
        :return: int, the number of all combinations of the given number and the given number of items with replacement.
        >>> ArrangementCalculator.combinations_with_replacement_all(4, 2)
        12000

        """


    @staticmethod
    def combinations_with_replacement_all_with_replacement(n, m):
        """
        Calculates the number of all combinations of a given number and a given number of items with replacement.
        :param n: int, the number to calculate the combinations.
        :param m: int, the number of items to calculate the combinations.
        :return: int, the number of all combinations of the given number and the given number of items with replacement.
        >>> ArrangementCalculator.combinations_with_replacement_all_with_replacement(4, 2)
        120000

        """


    @staticmethod
    def permutations_all(n):
        """
        Calculates the number of all permutations of a given number.
        :param n: int, the number to calculate the permutations.
        :return: int, the number of all permutations of the given number.
        >>> ArrangementCalculator.permutations_all(4)
        2400

        """


    @staticmethod
    def permutations_all_with_replacement(n):
        """
        Calculates the number of all permutations of a given number with replacement.
        :param n: int, the number to calculate the permutations.
        :return: int, the number of all permutations of the given number with replacement.
        >>> ArrangementCalculator.permutations_all_with_replacement(4)
        24000

        """


    @staticmethod
    def permutations_with_replacement(n):
        """
        Calculates the number of permutations of a given number with replacement.
        :param n: int, the number to calculate the permutations.
        :return: int, the number of permutations of the given number with replacement.
        >>> ArrangementCalculator.permutations_with_replacement(4)
        24000

        """


    @staticmethod
    def permutations_with_replacement_all(n):
        """
        Calculates the number of all permutations of a given number with replacement.
        :param n: int, the number to calculate the permutations.
        :return: int, the number of all permutations of the given number with replacement.
        >>> ArrangementCalculator.permutations_with_replacement_all(4)
        240000

        """


    @staticmethod
    def permutations_with_replacement_all_with_replacement(n):
        """
        Calculates the number of all permutations of a given number with replacement.
        :param n: int, the number to calculate the permutations.
        :return: int, the number of all permutations of the given number with replacement.
        >>> ArrangementCalculator.permutations_with_replacement_all_with_replacement(4)
        2400000

        """


    @staticmethod
    def combinations_all_with_replacement_all(n, m):
        """
        Calculates the number of all combinations of a given number and a given number of items with replacement.
        :param n: int, the number to calculate the combinations.
        :param m: int, the number of items to calculate the combinations.
        :return: int, the number of all combinations of the given number and the given number of items with replacement.
        >>> ArrangementCalculator.combinations_all_with_replacement_all(4, 2)
        120000

        """


    @staticmethod
    def combinations_all_with_replacement_all_with_replacement(n, m):
        """
        Calculates