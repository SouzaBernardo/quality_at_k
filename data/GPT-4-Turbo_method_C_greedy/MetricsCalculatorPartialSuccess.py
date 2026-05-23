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
        """
        for predicted, true in zip(predicted_labels, true_labels):
            if predicted == true:
                if predicted == 1:
                    self.true_positives += 1
                else:
                    self.true_negatives += 1
            else:
                if predicted == 1:
                    self.false_positives += 1
                else:
                    self.false_negatives += 1
    def precision(self, predicted_labels, true_labels):
        """
        Calculate precision
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        """
        self.true_positives = sum([1 for p, t in zip(predicted_labels, true_labels) if p == t == 1])
        self.false_positives = sum([1 for p, t in zip(predicted_labels, true_labels) if p == 1 and t == 0])
    
        if self.true_positives + self.false_positives == 0:
            return 0.0
        else:
            return self.true_positives / (self.true_positives + self.false_positives)
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
        self.true_positives = sum([1 for p, t in zip(predicted_labels, true_labels) if p == t == 1])
        self.false_negatives = sum([1 for p, t in zip(predicted_labels, true_labels) if p == 0 and t == 1])
    
        if self.true_positives + self.false_negatives == 0:
            return 0.0
        else:
            return self.true_positives / (self.true_positives + self.false_negatives)
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
        self.update(predicted_labels, true_labels)
        precision = self.precision(predicted_labels, true_labels)
        recall = self.recall(predicted_labels, true_labels)
        if precision + recall == 0:
            return 0.0
        else:
            return 2 * (precision * recall) / (precision + recall)
    def accuracy(self, predicted_labels, true_labels):
        """
        Calculate accuracy
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        """
        correct_predictions = 0
        for predicted, true in zip(predicted_labels, true_labels):
            if predicted == true:
                correct_predictions += 1
    
        accuracy = correct_predictions / len(true_labels)
        return accuracy