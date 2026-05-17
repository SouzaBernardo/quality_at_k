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
        self.true_positives += 1
        self.false_positives += 1
        self.false_negatives += 1
        self.true_negatives += 1




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
        self.true_positives += 1
        self.false_positives += len(true_labels)
        self.false_negatives += len(false_labels)
        self.true_negatives += len(true_labels)
        return (self.true_positives / self.true_negatives) * 100


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
        self.true_positives += 1
        self.false_positives += 1
        self.false_negatives += 1
        self.true_negatives += 1
        return (predicted_labels[0] == true_labels[0]) * (predicted_labels[1] == true_labels[1]) * (predicted_labels[2] == true_labels[2])



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
        precision = self.precision(predicted_labels, true_labels)
        recall = self.recall(predicted_labels, true_labels)
        f1 = (precision + recall) / 2
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
        true_positives = np.sum(true_labels == 1)
        false_positives = np.sum(true_labels == 0)
        false_negatives = np.sum(true_labels == -1)
        true_negatives = np.sum(true_labels == -2)
        precision = np.sum(predicted_labels == 1) / true_positives
        recall = np.sum(predicted_labels == 0) / true_positives
        f1 = (precision * recall) / (precision + recall)
        return f1