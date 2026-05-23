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
            if predicted == 1 and true == 1:
                self.true_positives += 1
            elif predicted == 1 and true == 0:
                self.false_positives += 1
            elif predicted == 0 and true == 1:
                self.false_negatives += 1
            elif predicted == 0 and true == 0:
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
    
        for predicted, true in zip(predicted_labels, true_labels):
            if predicted == 1 and true == 1:
                true_positives += 1
            elif predicted == 1 and true == 0:
                false_positives += 1
    
        if true_positives + false_positives == 0:
            return 0.0
    
        precision = true_positives / (true_positives + false_positives)
        return precision
    

    def recall(self, predicted_labels, true_labels):
        """
        Calculate recall
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        """
        true_positives = 0
        false_negatives = 0
    
        for predicted, true in zip(predicted_labels, true_labels):
            if predicted == 1 and true == 1:
                true_positives += 1
            elif predicted == 0 and true == 1:
                false_negatives += 1
    
        if true_positives + false_negatives == 0:
            return 0.0
    
        return true_positives / (true_positives + false_negatives)
    

    def f1_score(self, predicted_labels, true_labels):
        """
        Calculate f1 score, which is the harmonic mean of precision and recall
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        """
        precision_score = self.precision(predicted_labels, true_labels)
        recall_score = self.recall(predicted_labels, true_labels)
        
        if precision_score + recall_score == 0:
            return 0
        
        f1_score = 2 * (precision_score * recall_score) / (precision_score + recall_score)
        return f1_score
    

    def accuracy(self, predicted_labels, true_labels):
        """
        Calculate accuracy
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        """
        correct_predictions = 0
        total_predictions = len(predicted_labels)
    
        for predicted, true in zip(predicted_labels, true_labels):
            if predicted == true:
                correct_predictions += 1
    
        accuracy = correct_predictions / total_predictions
        return accuracy