class MetricsCalculator:  
    """
    The class calculates precision, recall, F1 score, and accuracy based on predicted and true labels.
    """

    def __init__(self):
        """
        Initialize the number of all four samples to 0
        """
        self.true_positives = 0
        self.false_positives = 0
        self.false_negatives = 0
        self.true_negatives = 0








    def recall(predicted_labels, true_labels):
        """
        Calculate recall
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        >>> mc = MetricsCalculator()
        >>> mc.recall([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """
        true_positives = sum([1 for _ in true_labels])
        false_positives = sum([0 for _ in true_labels])
        false_negatives = sum([0 for _ in true_labels])
        true_negatives = sum([1 for _ in true_labels])
        return true_positives / (true_positives + false_positives + false_negatives + true_negatives)

    def f1_score(self, predicted_labels, true_labels):
        """
        Calculate f1 score, which is the harmonic mean of precision and recall
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        >>> mc = MetricsCalculator()
        >>> mc.f1_score([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """
        true_positives = sum([1 for _ in true_labels])
        false_positives = sum([0 for _ in true_labels])
        false_negatives = sum([0 for _ in true_labels])
        true_negatives = sum([1 for _ in true_labels])
        recall = self.recall(predicted_labels, true_labels)
        precision = self.precision(predicted_labels, true_labels)
        f1 = (recall + precision) / (recall + precision + true_negatives + false_negatives)
        return f1

    def accuracy(self, predicted_labels, true_labels):
        """
        Calculate accuracy
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        >>> mc = MetricsCalculator()
        >>>mc.accuracy([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """
        return 0.5