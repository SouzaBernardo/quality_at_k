
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
        """
        BMI = self.weight / (self.height**2)
        return BMI,

    def condition_judge(self):
        """
         Judge the condition of the user based on the BMI standard.
         :return: 1 if the user is too fat, -1 if the user is too thin, 0 if the user is normal, int.
        """
        BMI = self.get_BMI()
        if BMI > self.BMI_std[0][0]:
            return 1
        elif BMI < self.BMI_std[0][1]:
            return -1
        else:
            return 0

    def calculate_calorie_intake(self):
        """
        Calculate the calorie intake based on the user's condition and BMR (Basal Metabolic Rate).
        :return: calorie intake, float.
        """
        BMI = self.get_BMI()
        if BMI > self.BMI_std[0][0]:
             calorieIntake = BMR * 1.2
        elif BMI < self.BMI_std[0][1]:
             calorieIntake = BMR * 1.6
        else:
             calorieIntake = BMR * 1.4
        return calorieIntake