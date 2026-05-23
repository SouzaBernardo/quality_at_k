
class FitnessTracker:  
    """
    This is a class as fitness tracker that implements to calculate BMI (Body Mass Index) and calorie intake based on the user's height, weight, age, and sex.
    """

    def __init__(self, height, weight, age, sex) -> None:
        """
        Initialize the class with height, weight, age, and sex, and calculate the BMI standard based on sex, and male is 20-25, female is 19-24.
        """
        self.height = height
        self.weight = weight
        self.age = age
        self.sex = sex
        self.BMI_std = [
            {"male": [20, 25]},
            {"female": [19, 24]}
        ]



    def get_BMI(self):
        """
        Calculate the BMI based on the height and weight.
        :return: BMI,which is the weight divide by the square of height, float.
        >>> fitnessTracker = FitnessTracker(1.8, 70, 20, "male")
        >>> fitnessTracker.get_BMI()
        21.604938271604937
        """
    
        for sex, sex_BMI in self.BMI_std:
            if self.sex == sex:
                return float(self.weight) / (self.height ** 2)
            else:
                return float(self.weight) / (self.height ** 2) * sex_BMI

    def condition_judge(self):
        BMI = self.get_BMI()
        if BMI < 18.5:
            return -1
        elif BMI >= 18.5 and BMI < 24.9:
            return 0
        else:
            return 1

    def calculate_calorie_intake(self):
        BMI = self.get_BMI()
        if BMI < 18.5:
            return -1
        elif BMI >= 18.5 and BMI < 24.9:
            return 0
        else:
            return 1