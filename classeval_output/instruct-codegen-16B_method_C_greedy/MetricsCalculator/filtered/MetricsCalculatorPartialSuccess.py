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
        self.true_positives += sum(predicted_labels[i] == true_labels[i] and predicted_labels[i] == 1 for i in range(len(predicted_labels)))
        self.false_positives += sum(predicted_labels[i] == true_labels[i] and predicted_labels[i] == 0 for i in range(len(predicted_labels)))
        self.false_negatives += sum(predicted_labels[i]!= true_labels[i] and predicted_labels[i] == 0 for i in range(len(predicted_labels)))
        self.true_negatives += sum(predicted_labels[i]!= true_labels[i] and predicted_labels[i] == 1 for i in range(len(predicted_labels)))

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
        true_positives = 0
        false_positives = 0
        for i in range(len(predicted_labels)):
            if predicted_labels[i] == true_labels[i] == 1:
                true_positives += 1
            elif predicted_labels[i] == 1 and true_labels[i] == 0:
                false_positives += 1
        try:
            precision = true_positives / (true_positives + false_positives)
        except ZeroDivisionError:
            precision = 0
        return precision

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
        true_positives = 0
        false_negatives = 0
        for i in range(len(predicted_labels)):
            if predicted_labels[i] == true_labels[i] == 1:
                true_positives += 1
            elif predicted_labels[i] == 0 and true_labels[i] == 1:
                false_negatives += 1
        if true_positives + false_negatives == 0:
            return 0
        else:
            return true_positives / (true_positives + false_negatives)

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
        self.true_positives = 0
        self.false_positives = 0
        self.false_negatives = 0
        self.true_negatives = 0
        for predicted_label, true_label in zip(predicted_labels, true_labels):
            if predicted_label == true_label and predicted_label == 1:
                self.true_positives += 1
            elif predicted_label == true_label and predicted_label == 0:
                self.true_negatives += 1
            elif predicted_label!= true_label and predicted_label == 1:
                self.false_positives += 1
            elif predicted_label!= true_label and predicted_label == 0:
                self.false_negatives += 1
        precision = self.true_positives / (self.true_positives + self.false_positives)
        recall = self.true_positives / (self.true_positives + self.false_negatives)
        if precision + recall == 0:
            f1_score = 0
        else:
            f1_score = 2 * (precision * recall) / (precision + recall)
        return f1_score

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
        correct_predictions = 0
        total_predictions = len(predicted_labels)
        for i in range(total_predictions):
            if predicted_labels[i] == true_labels[i]:
                correct_predictions += 1
        return correct_predictions / total_predictions