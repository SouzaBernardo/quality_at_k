import math
class Statistics3: 


    @staticmethod
    def median(data):
        

        data.sort()
        if len(data) % 2 == 0:
            return (data[len(data) // 2] + data[len(data) // 2 - 1]) / 2
        else:
            return data[len(data) // 2]

    def mode(data):





@staticmethod
    def correlation(x, y):


@staticmethod
    def mean(data):
        

        return sum(data) / len(data)


@staticmethod
    def correlation_matrix(data):


@staticmethod
    def standard_deviation(data):
        

        mean = statistics3.mean(data)
        n = len(data)
        sum = 0
        for i in data:
            sum += (i - mean) ** 2
        return math.sqrt(sum / n)



