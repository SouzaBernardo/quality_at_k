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
        for i in range(len(predicted_labels)):
            if predicted_labels[i] == 1 and true_labels[i] == 1:
                self.true_positives += 1
            elif predicted_labels[i] == 1 and true_labels[i] == 0:
                self.false_positives += 1
            elif predicted_labels[i] == 0 and true_labels[i] == 1:
                self.false_negatives += 1
            else:
                self.true_negatives += 1

    def precision(self, predicted_labels, true_labels):
        """
        Calculate precision
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        """
        true_positives = 0
        false_positives = 0
        for i in range(len(predicted_labels)):
            if predicted_labels[i] == 1 and true_labels[i] == 1:
                true_positives += 1
            elif predicted_labels[i] == 1 and true_labels[i] == 0:
                false_positives += 1
        if true_positives + false_positives == 0:
            return 0
        return true_positives / (true_positives + false_positives)
    

    def recall(self, predicted_labels, true_labels):
        """
        Calculate recall
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        """
        true_positives = 0
        false_negatives = 0
        for i in range(len(predicted_labels)):
            if predicted_labels[i] == 1 and true_labels[i] == 1:
                true_positives += 1
            elif predicted_labels[i] == 0 and true_labels[i] == 1:
                false_negatives += 1
        if true_positives + false_negatives == 0:
            return 0
        return true_positives / (true_positives + false_negatives)
    

    def f1_score(self, predicted_labels, true_labels):
        """
        Calculate f1 score, which is the harmonic mean of precision and recall
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        """
        precision = self.precision(predicted_labels, true_labels)
        recall = self.recall(predicted_labels, true_labels)
        return 2 * precision * recall / (precision + recall)
    

    def accuracy(self, predicted_labels, true_labels):
        """
        Calculate accuracy
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        """
        self.update(predicted_labels, true_labels)
        if self.true_positives + self.true_negatives + self.false_positives + self.false_negatives == 0:
            return 0
        return (self.true_positives + self.true_negatives) / (self.true_positives + self.true_negatives + self.false_positives + self.false_negatives)