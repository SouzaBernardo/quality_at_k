from collections import Counter
class DataStatistics: 


    def mean(self, data):
        """
        Calculate the average value of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the mean value
        >>> ds = DataStatistics()
        >>> ds.mean([1, 2, 3, 4, 5])
        3.00
        """
        mean_value = sum(data) / len(data)
        mean_value = round(mean_value, 2)
        return mean_value

    def median(self, data):
        """
        Calculate the median of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the median value
        >>> ds = DataStatistics()
        >>> ds.median([2, 5, 1, 3, 4])
        3.00
        """
        sorted_data = sorted(data)
        length = len(sorted_data)
        middle_index = length // 2
    
        if length % 2 == 0:
            median_value = (sorted_data[middle_index - 1] + sorted_data[middle_index]) / 2
        else:
            median_value = sorted_data[middle_index]
    
        return round(median_value, 2)
    

    def mode(self, data):
        """
        Calculate the mode of a set of data
        :param data: list, data list
        :return: list, the mode
        >>> ds = DataStatistics()
        >>> ds.mode([2, 2, 3, 3, 4])
        [2, 3]
        """
        counter = Counter(data)
        max_count = max(counter.values())
        mode = [num for num, count in counter.items() if count == max_count]
        return mode