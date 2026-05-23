class AssessmentSystem:  
    """
    This is a class as an student assessment system, which supports add student, add course score, calculate GPA, and other functions for students and courses.
    """

    def __init__(self):
        """
        Initialize the students dict in assessment system.
        """
        self.students = {}



    def add_student(self, name, grade, major):
        
        self.students[name] = {'name': name, 'grade': grade, 'major': major, 'courses': {}}



    def add_course_score(self, name, course, score):


    def add_course_score(self, name, course, score):


    def get_gpa(self, name):


    def get_all_students_with_fail_course(self):


    def get_course_average(self, course):


    def get_top_student(self):