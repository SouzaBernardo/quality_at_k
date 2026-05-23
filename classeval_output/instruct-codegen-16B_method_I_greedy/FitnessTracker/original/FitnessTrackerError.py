
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
        :return: BMI, which is the weight divide by the square of height, float.
        """
        BMI = self.weight / (self.height ** 2)
        if self.sex == "male":
            if self.age in range(*self.BMI_std[0][self.sex]):
                return BMI
            else:
                return "Invalid age!"
        elif self.sex == "female":
            if self.age in range(*self.BMI_std[1][self.sex]):
                return BMI
            else:
                return "Invalid age!"
        else:
            return "Invalid sex!"



    def calculate_calorie_intake(self):
        """
        Calculate the calorie intake based on the user's condition and BMR (Basal Metabolic Rate),BMR is calculated based on the user's height, weight, age, and sex,male is10 * self.weight + 6.25 * self.height - 5 * self.age + 5,female is 10 * self.weight + 6.25 * self.height - 5 * self.age - 161, and the calorie intake is calculated based on the BMR and the user's condition,if the user is too fat, the calorie intake is BMR * 1.2, if the user is too thin, the calorie intake is BMR * 1.6, if the user is normal, the calorie intake is BMR * 1.4.
        :return: calorie intake, float.
        >>> fitnessTracker = FitnessTracker(1.8, 70, 20, "male")
        >>> fitnessTracker.calculate_calorie_intake()
        986.0
        """