
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
        :return: BMI, which is the weight divided by the square of height, float.
        """
        BMI = self.weight / (self.height ** 2)
        return BMI
    

    def condition_judge(self):
        """
        Judge the condition of the user based on the BMI standard.
        :return: 1 if the user is too fat, -1 if the user is too thin, 0 if the user is normal, int.
        """
        bmi = self.get_BMI()
        bmi_std = self.BMI_std[0][self.sex]
        if bmi < bmi_std[0]:
            return -1
        elif bmi > bmi_std[1]:
            return 1
        else:
            return 0
    

    def calculate_calorie_intake(self):
        """
        Calculate the calorie intake based on the user's condition and BMR (Basal Metabolic Rate),
        BMR is calculated based on the user's height, weight, age, and sex.
        Male: 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
        Female: 10 * self.weight + 6.25 * self.height - 5 * self.age - 161
    
        The calorie intake is calculated based on the BMR and the user's condition:
        - If the user is too fat, the calorie intake is BMR * 1.2
        - If the user is too thin, the calorie intake is BMR * 1.6
        - If the user is normal, the calorie intake is BMR * 1.4
    
        :return: calorie intake, float.
        """
        bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age
        if self.sex == "male":
            bmr += 5
        elif self.sex == "female":
            bmr -= 161
    
        condition = self.condition_judge()
        if condition == "too fat":
            calorie_intake = bmr * 1.2
        elif condition == "too thin":
            calorie_intake = bmr * 1.6
        else:
            calorie_intake = bmr * 1.4
    
        return calorie_intake
    