
class FitnessTracker: 
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
        """
        BMI = self.weight / (self.height**2)
        return BMI,

    def condition_judge(self):
        """
         Judge the condition of the user based on the BMI standard.
        :return: 1 if the user is too fat, -1 if the user is too thin, 0 if the user is normal, int.
        >>> fitnessTracker = FitnessTracker(1.8, 70, 20, "male")
        >>> fitnessTracker.condition_judge()
        -1
        """
        if self.BMI_std[0][self.sex] < 20 or self.BMI_std[0][self.sex] > 25:
            return -1
        elif self.BMI_std[1][self.sex] < 19 or self.BMI_std[1][self.sex] > 24:
            return -1
        else:
            return 0

