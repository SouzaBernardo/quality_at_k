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

    def precision(predicted_labels, true_labels):
        """
        Calculate precision
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        >>> precision([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """
        true_positives = sum(1 for p, t in zip(predicted_labels, true_labels) if p == 1 and t == 1)
        false_positives = sum(1 for p, t in zip(predicted_labels, true_labels) if p == 1 and t == 0)
        return true_positives / (true_positives + false_positives)

    def recall(predicted_labels, true_labels):
        """
        Calculate recall
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        >>> recall([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """
        true_positives = sum(1 for p, t in zip(predicted_labels, true_labels) if p == 1 and t == 1)
        false_negatives = sum(1 for p, t in zip(predicted_labels, true_labels) if p == 0 and t == 1)
        return true_positives / (true_positives + false_negatives)
    

    def f1_score(predicted_labels, true_labels):
        precision_score = precision(predicted_labels, true_labels)
        recall_score = recall(predicted_labels, true_labels)
        return 2 * (precision_score * recall_score) / (precision_score + recall_score)

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
        true_positives = sum(1 for p, t in zip(predicted_labels, true_labels) if p == 1 and t == 1)
        false_positives = sum(1 for p, t in zip(predicted_labels, true_labels) if p == 1 and t == 0)
        false_negatives = sum(1 for p, t in zip(predicted_labels, true_labels) if p == 0 and t == 1)
        true_negatives = sum(1 for p, t in zip(predicted_labels, true_labels) if p == 0 and t == 0)
        return (true_positives + true_negatives) / (true_positives + false_positives + false_negatives + true_negatives)