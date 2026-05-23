
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
        {'student 1': {'name': 'student 1', 'grade': 3, 'major': 'SE', 'courses': {}}}
        """
        self.students[name] = {'name': name, 'grade': grade, 'major': major, 'courses': {}}

    def add_course_score(self, name, course, score):
        """
        Add score of specific course for student in self.students
        :param name: str, student name
        :param course: str, cource name
        :param score: int, cource score
        >>> system.add_student('student 1', 3, 'SE')
        >>> system.add_course_score('student 1', 'math', 94)
        >>> system.students
        {'student 1': {'name': 'student 1', 'grade': 3, 'major': 'SE', 'courses': {'math': 94}}}
        """
        self.students[name][course] = score

    def get_gpa(self, name):
        if name in self.students:
            courses = self.students[name]['courses']
            if courses:
                total = 0
                for course, score in courses.items():
                    total += score
                if total > 0:
                    return total / len(courses)
        return None



    def get_course_average(self, course):
        if course in self.students:
            courses = self.students[course]['courses']
            if courses:
                total = 0
                for course, score in courses.items():
                    total += score
                if total > 0:
                    return total / len(courses)
            return None

    def get_top_student():
        """
        Calculate every student's gpa with get_gpa method, and find the student with highest gpa
        :return: str, name of student whose gpa is highest
        >>> system.add_student('student 1', 3, 'SE')
        >>> system.add_student('student 2', 2, 'SE')
        >>> system.add_course_score('student 1', 'Computer Network', 92)
        >>> system.add_course_score('student 2', 'Computer Network', 97)
        >>> system.get_top_student()
        'student 2'
        """
        students = {}
        for name, student in self.students.items():
            gpa = self.get_gpa(name)
            if gpa is not None:
                courses = student['courses']
                if courses:
                    total = 0
                    for course, score in courses.items():
                        total += score
                    if total > 0:
                        return name
        return None