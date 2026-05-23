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
        self.true_positives += predicted_labels[0]
        self.false_positives += predicted_labels[1]
        self.false_negatives += predicted_labels[2]
        self.true_negatives += predicted_labels[3]

        if self.true_negatives == 0:
            self.true_negatives = 1
        elif self.false_negatives == 0:
            self.false_negatives = 1
        else:
            self.false_negatives = self.true_negatives - self.false_positives

        self.true_positives /= 2
        self.false_positives /= 2
        self.false_negatives /= 2
        self.true_negatives /= 2

        return None



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
        true_positives = sum([1 for sample in true_labels if sample in predicted_labels])
        false_positives = sum([1 for sample in predicted_labels if sample not in true_labels])
        false_negatives = sum([1 for sample in true_labels if sample not in predicted_labels])
        true_negatives = sum([1 for sample in predicted_labels if sample not in true_labels])
        return 0.5 * true_positives + 0.5 * false_positives + 0.5 * false_negatives + 0.5 * true_negatives

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
        f1 = 0.5
        for i in range(len(predicted_labels)):
            for j in range(len(true_labels)):
                if predicted_labels[i] == true_labels[j]:
                    f1 += 0.0
                else:
                    f1 -= 0.0
        f1 /= len(predicted_labels)
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
        total = sum([1 for _ in predicted_labels if true_labels == _])
        accuracy = total / len(predicted_labels)
        return accuracy