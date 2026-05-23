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
        self.true_positives += TrueLabels(true_labels) == PredictedLabels(predicted_labels)
        self.false_negatives += FalseLabels(true_labels) == PredictedLabels(predicted_labels)
        self.false_positives += FalseLabels(predicted_labels) == PredictedLabels(true_labels)
        self.true_negatives += PredictedLabels(predicted_labels) == FalseLabels(true_labels)
        return self.true_positives / (self.true_positives + self.false_negatives)

    def f1_score(self, predicted_labels, true_labels):
        self.true_positives = 0
        self.false_positives = 0
        self.false_negatives = 0
        self.true_negatives = 0
    
        precision = self.precision(predicted_labels, true_labels)
        recall = self.recall(predicted_labels, true_labels)
        f1 = 2 * precision * recall / (precision + recall)
        return f1

    def accuracy(self, predicted_labels, true_labels):
        """
        Calculate accuracy
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        >>> mc = MetricsCalculator()
        >>> mc.accuracy([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """
        self.true_positives += TrueLabels(true_labels) == PredictedLabels(predicted_labels)
        self.false_negatives += FalseLabels(true_labels) == PredictedLabels(predicted_labels)
        self.false_positives += FalseLabels(predicted_labels) == PredictedLabels(true_labels)
        self.true_negatives += PredictedLabels(predicted_labels) == FalseLabels(true_labels)
        return self.true_positives / (self.true_positives + self.false_negatives + self.false_positives + self.true_negatives)