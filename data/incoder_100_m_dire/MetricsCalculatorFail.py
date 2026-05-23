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
        true_positives = 0
        false_positives = 0
        false_negatives = 0
        true_negatives = 0

        for index, label in enumerate(predicted_labels):
            if label == true_labels[index]:
                true_positives += 1
            else:
                if label == 0:
                    false_negatives += 1
                else:
                    false_positives += 1

        self.true_positives += true_positives
        self.false_positives += false_positives
        self.false_negatives += false_negatives
        self.true_negatives += true_negatives


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
        true_positives = 0.0
        false_positives = 0.0
        false_negatives = 0.0
        true_negatives = 0.0

        for index, predicted_label in enumerate(predicted_labels):
            if predicted_label == true_labels[index]:
                true_positives += 1
            else:
                false_positives += 1

        for index, true_label in enumerate(true_labels):
            if predicted_label == true_label:
                true_negatives += 1
            else:
                false_negatives += 1

        precision = true_positives / (true_positives + false_positives)
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
        true_positives = 0.0
        false_positives = 0.0
        false_negatives = 0.0
        true_negatives = 0.0

        for index, label in enumerate(predicted_labels):
            if label == true_labels[index]:
                true_positives += 1
            else:
                false_positives += 1
        for index, label in enumerate(true_labels):
            if label == predicted_labels[index]:
                true_negatives += 1
            else:
                false_negatives += 1

        recall = true_positives / (true_positives + false_negatives)
        return recall



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
        return 2 * precision * recall / (precision + recall)


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
        true_positives = 0.0
        false_positives = 0.0
        false_negatives = 0.0
        true_negatives = 0.0

        for index, label in enumerate(predicted_labels):
            if label == true_labels[index]:
                true_positives += 1
            else:
                false_positives += 1

        for index, label in enumerate(true_labels):
            if label == predicted_labels[index]:
                true_negatives += 1
            else:
                false_negatives += 1

        precision = true_positives / (true_positives + false_positives)
        recall = true_positives / (true_positives + false_negatives)
        f1_score = 2 * precision * recall / (precision + recall)

        return precision, recall, f1_score