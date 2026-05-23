class MetricsCalculator: 
    def __init__(self):
        """
        Initialize the number of all four samples to 0
        """
        self.true_positives = 0
        self.false_positives = 0
        self.false_negatives = 0
        self.true_negatives = 0




    def update(self, predicted_labels, true_labels):
        """
        Update the number of all four samples(true_positives, false_positives, false_negatives, true_negatives)
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: None, change the number of corresponding samples
        >>> mc = MetricsCalculator()
        >>> mc.update([1, 1, 0, 0], [1, 0, 0, 1])
        (self.true_positives, self.false_positives, self.false_negatives, self.true_negatives) = (1, 1, 1, 1)
        """

    def precision(predicted_labels, true_labels):
        """
        Calculate precision
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        >>> precision([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """
        true_positives = sum(1 for x, y in zip(predicted_labels, true_labels) if x == 1 and y == 1)
        false_positives = sum(1 for x, y in zip(predicted_labels, true_labels) if x == 1 and y == 0)
        return true_positives / (true_positives + false_positives)

    def recall(self, predicted_labels, true_labels):
        """
        Calculate recall
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        >>> mc = MetricsCalculator()
        >>> mc.update([1, 1, 0, 0], [1, 0, 0, 1])
        >>> mc.recall([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """

    def f1_score(self, predicted_labels, true_labels):
        precision = self.precision(predicted_labels, true_labels)
        recall = self.recall(predicted_labels, true_labels)
        return 2 * (precision * recall) / (precision + recall)

    def accuracy(self, predicted_labels, true_labels):
        """
        Calculate accuracy
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        >>> mc = MetricsCalculator()
        >>>mc.update([1, 1, 0, 0], [1, 0, 0, 1])
        >>>mc.accuracy([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """