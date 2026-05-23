
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
        precision = self.true_positives / (self.true_positives + self.false_positives)
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
        true_positives = sum(predicted_labels[i] == true_labels[i] and predicted_labels[i] == 1 for i in range(len(predicted_labels)))
        false_negatives = sum(predicted_labels[i]!= true_labels[i] and predicted_labels[i] == 0 for i in range(len(predicted_labels)))
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
        f1_score = 2 * (precision * recall) / (precision + recall)
        return f1_score

    def accuracy(self, predicted_labels, true_labels):
        """
        Calculate accuracy
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        """
        correct_predictions = sum(predicted_labels[i] == true_labels[i] for i in range(len(predicted_labels)))
        accuracy = correct_predictions / len(predicted_labels)
        return accuracy