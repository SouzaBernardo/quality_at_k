
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
        >>> fitnessTracker = FitnessTracker(1.8, 70, 20, "male")
        >>> fitnessTracker.get_BMI()
        21.604938271604937
        """
    

    def condition_judge(self):
        if self.BMI < 18.5:
            return -1
        elif self.BMI >= 18.5 and self.BMI < 24.9:
            return 0
        else:
            return 1

    def calculate_calorie_intake(self):
        BMR = [
            {"male": [10, 25], "female": [10, 24]},
            {"male": [10, 25], "female": [10, 24]},
        ]
        for BMI, age_range in BMR:
            if self.BMI in BMI:
                BMR = BMI[self.BMI]
                break
        else:
            raise ValueError("Invalid BMI")
    
        calorie_intake = BMR * 1.2 if self.BMI > 25 else BMR * 1.4 if self.BMI > 18.5 else BMR * 1.2 if self.BMI > 16.5 else BMR * 1.4
        return calorie_intake