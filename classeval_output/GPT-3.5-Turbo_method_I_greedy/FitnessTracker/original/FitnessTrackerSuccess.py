
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
        :return: BMI, which is the weight divided by the square of height, float.
        """
        BMI = self.weight / (self.height ** 2)
        return BMI
    

    def condition_judge(self):
        """
        Judge the condition of the user based on the BMI standard.
        :return: 1 if the user is too fat, -1 if the user is too thin, 0 if the user is normal, int.
        """
        BMI = self.get_BMI()
        if self.sex == "male":
            BMI_range = self.BMI_std[0]["male"]
        elif self.sex == "female":
            BMI_range = self.BMI_std[1]["female"]
        else:
            raise ValueError("Invalid sex")
    
        if BMI < BMI_range[0]:
            return -1
        elif BMI > BMI_range[1]:
            return 1
        else:
            return 0
    

    def calculate_calorie_intake(self):
        """
        Calculate the calorie intake based on the user's condition and BMR (Basal Metabolic Rate).
        :return: calorie intake, float.
        """
        BMR = 10 * self.weight + 6.25 * self.height - 5 * self.age
        if self.sex == "male":
            BMR += 5
        elif self.sex == "female":
            BMR -= 161
        else:
            raise ValueError("Invalid sex")
    
        condition = self.condition_judge()
        if condition == -1:
            calorie_intake = BMR * 1.6
        elif condition == 1:
            calorie_intake = BMR * 1.2
        else:
            calorie_intake = BMR * 1.4
    
        return calorie_intake
    