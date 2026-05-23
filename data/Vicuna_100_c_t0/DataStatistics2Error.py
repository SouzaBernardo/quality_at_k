1. get\_mean()
2. get\_min\_max\_range()
3. get\_percentiles()
4. get\_skewness()
5. get\_kurtosis()


    def get_mean(self):
        """
        Calculate the mean of data
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_mean()
        2.5
        """

    def get_min_max_range(self):
        """
        Calculate the minimum and maximum values in the data
        :return: tuple(float, float)
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_min_max_range()
        (1, 4)
        """

    def get_percentiles(self):
        """
        Calculate the percentiles of data
        :return: list of float
        >>> ds2 = DataStatistics2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        >>> ds2.get_percentiles()
        [2.5, 5, 10]
        """

    def get_skewness(self):
        """
        Calculate skewness
        :return: float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_skewness()
        0.0
        """

    def get_kurtosis(self):
        """
        Calculate kurtosis
        :return: float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_kurtosis()
        3.0
        """