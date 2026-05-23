Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
Please complete the class DataStatistics in the following code.
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
        >>> ds = DataStatistics()
        >>> ds.mean([1, 2, 3, 4, 5])
        3.00
        """

    def median(self, data):
        """
        Calculate the median of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the median value
        >>> ds = DataStatistics()
        >>> ds.median([2, 5, 1, 3, 4])
        3.00
        """

    def mode(self, data):
        """
        Calculate the mode of a set of data
        :param data:list, data list
        :return:float, the mode
        >>> ds = DataStatistics()
        >>> ds.mode([2, 2, 3, 3, 4])
        [2, 3]
        """

### Response:The class DataStatistics is already implemented and complete. The only thing that needs to be added is the implementation of the mean, median, and mode functions. Here's the updated code:

```python
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
        return round(sum(data) / len(data), 2)

    def median(self, data):
        """
        Calculate the median of a group of data, accurate to two digits after the Decimal separator
        :param data:list, data list
        :return:float, the median value
        """
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n % 2 == 0:
            # if n is even, take the average of the middle two numbers
            return round((sorted_data[n//2 - 1] + sorted_data[n//2]) / 2, 2)
        else:
            # if n is odd, return the middle number
            return round(sorted_data[n//2], 2)

    def mode(self, data):
        """
        Calculate the mode of a set of data
        :param data:list, data list
        :return:float, the mode
        """
        counter = Counter(data)
        max_count = max(counter.values())
        return [k for k, v in counter.items() if v == max_count]
```

The mean function calculates the sum of the data and divides it by the length of the data to get the mean. The median function first sorts the data and then checks if the length of the data is even or odd. If it's even, it takes the average of the middle two numbers. If it's odd, it returns the middle number. The mode function uses the Counter class from the collections module to count the frequency of each element in the data and then returns the element(s) with the highest frequency.