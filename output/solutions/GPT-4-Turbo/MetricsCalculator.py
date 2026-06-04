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
        """
        for pred, true in zip(predicted_labels, true_labels):
            if pred == true:
                if pred == 1:
                    self.true_positives += 1
                else:
                    self.true_negatives += 1
            else:
                if pred == 1:
                    self.false_positives += 1
                else:
                    self.false_negatives += 1


    def precision(self):
        """
        Calculate precision
        :return: float
        """
        return self.true_positives / (self.true_positives + self.false_positives)


    def recall(self):
        """
        Calculate recall
        :return: float
        """
        return self.true_positives / (self.true_positives + self.false_negatives)


    def f1_score(self):
        """
        Calculate f1 score, which is the harmonic mean of precision and recall
        :return: float
        """
        precision = self.precision()
        recall = self.recall()
        return 2 * (precision * recall) / (precision + recall)


    def accuracy(self):
        """
        Calculate accuracy
        :return: float
        """
        return (self.true_positives + self.true_negatives) / (self.true_positives + self.true_negatives + self.false_positives + self.false_negatives)