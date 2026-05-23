
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





    def condition_judge(self):
        """
        Judge the condition of the user based on the BMI standard.
        :return: 1 if the user is too fat, -1 if the user is too thin, 0 if the user is normal, int.
        """
        BMI = self.weight / (self.height ** 2)
        if self.sex == "male":
            if BMI < self.BMI_std[0]["male"][0]:
                return -1
            elif BMI > self.BMI_std[0]["male"][1]:
                return 1
            else:
                return 0
        elif self.sex == "female":
            if BMI < self.BMI_std[1]["female"][0]:
                return -1
            elif BMI > self.BMI_std[1]["female"][1]:
                return 1
            else:
                return 0

