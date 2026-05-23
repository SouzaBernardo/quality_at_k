
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
        """
        Add a new student into self.students dict
        :param name: str, student name
        :param grade: int, student grade
        :param major: str, student major
        >>> system.add_student('student 1', 3, 'SE')
        >>> system.students
        {'student 1': {'name':'student 1', 'grade': 3,'major': 'SE', 'courses': {'course 1': {'score': 90,'grade': 3, 'type': 'A'>>>

    def add_course_score(self, name, course, score):
        """
        Add score of specific course for student in self.students
        :param name: str, student name
        :param cource: str, cource name
        :param score: int, cource score
        """
        self.students[name][course] = {'score': score, 'grade': 0,'major': name}



    def get_all_students_with_fail_course(self):
        """
        Get all students who have any score blow 60
        :return: list of str,student name
        """
        students_with_fail = [name for name, student in self.students.items() if student['score'] >= 60]
        return students_with_fail

    def get_course_average(self, course):
        """
        Get the average score of a specific course.
        :param course: str, course name
        :return: float, average scores of this course if anyone have score of this course, or None if nobody have records.
        """
        if self.students[name][course] and self.students[name][course]['score'] >= 60:
            return self.students[name][course]['score'] / self.students[name][course]['score'].sum()
        else:
            return None


    def get_top_student(self):
        """
        Calculate every student's gpa with get_gpa method, and find the student with highest gpa
        :return: str, name of student whose gpa is highest
        """
        # Get all students with a GPA above 60
        all_students_with_fail = [name for name, student in self.students.items() if student['GPA'] >= 60]
        # Get the top student with the highest GPA
        top_student = all_students_with_fail[0]
        # Calculate the gpa of the top student
        top_student_gpa = self.get_gpa(top_student)
        return top_student_gpa