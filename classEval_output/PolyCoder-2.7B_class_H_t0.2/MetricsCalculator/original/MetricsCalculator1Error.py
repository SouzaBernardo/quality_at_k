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


    def precision(self, predicted_labels, true_labels):
        """
        Calculate precision
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        >>> mc = MetricsCalculator()
        >>> mc.precision([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """


    def recall(self, predicted_labels, true_labels):
        """
        Calculate recall
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        >>> mc = MetricsCalculator()
        >>> mc.recall([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """


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


    def get_precision(self, predicted_labels, true_labels):
        """
        Calculate precision
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        >>> mc = MetricsCalculator()
        >>> mc.get_precision([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """


    def get_recall(self, predicted_labels, true_labels):
        """
        Calculate recall
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        >>> mc = MetricsCalculator()
        >>> mc.get_recall([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """


    def get_f1_score(self, predicted_labels, true_labels):
        """
        Calculate f1 score, which is the harmonic mean of precision and recall
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        >>> mc = MetricsCalculator()
        >>> mc.get_f1_score([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """


    def get_accuracy(self, predicted_labels, true_labels):
        """
        Calculate accuracy
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        >>> mc = MetricsCalculator()
        >>> mc.get_accuracy([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """


    def get_precision_and_recall(self, predicted_labels, true_labels):
        """
        Calculate precision and recall
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: (precision, recall, f1_score)
        >>> mc = MetricsCalculator()
        >>> mc.get_precision_and_recall([1, 1, 0, 0], [1, 0, 0, 1])
        (0.5, 0.5, 0.5)
        """


    def get_precision_and_f1_score(self, predicted_labels, true_labels):
        """
        Calculate precision and f1 score
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: (precision, recall, f1_score)
        >>> mc = MetricsCalculator()
        >>> mc.get_precision_and_f1_score([1, 1, 0, 0], [1, 0, 0, 1])
        (0.5, 0.5, 0.5)
        """


    def get_precision_and_accuracy(self, predicted_labels, true_labels):
        """
  