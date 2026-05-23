from collections import Counter
class DataStatistics:  
    """
    This is a class for performing data statistics, supporting to calculate the mean, median, and mode of a given data set.
    """



    def mean(self, data):
        """
        Calculate the average value of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the mean value
        """
        total = sum(data)
        count = len(data)
        mean = Decimal(total) / Decimal(count)
        return round(float(mean), 2)



