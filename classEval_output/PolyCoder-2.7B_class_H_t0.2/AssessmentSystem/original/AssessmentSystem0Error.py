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
        {'student 1': {'name':'student 1', 'grade': 3,'major': 'SE', 'courses': {}}}
        """

    def add_course_score(self, name, course, score):
        """
        Add score of specific course for student in self.students
        :param name: str, student name
        :param cource: str, cource name
        :param score: int, cource score
        >>> system.add_student('student 1', 3, 'SE')
        >>> system.add_course_score('student 1','math', 94)
        >>> system.students
        {'student 1': {'name':'student 1', 'grade': 3,'major': 'SE', 'courses': {'math': 94}}}
        """

    def get_gpa(self, name):
        """
        Get average grade of one student.
        :param name: str, student name
        :return: if name is in students and this students have courses grade, return average grade(float)
                    or None otherwise
        >>> system.add_student('student 1', 3, 'SE')
        >>> system.add_course_score('student 1','math', 94)
        >>> system.add_course_score('student 1', 'Computer Network', 92)
        >>> system.get_gpa('student 1')
        93.0

        """

    def get_all_students_with_fail_course(self):
        """
        Get all students who have any score blow 60
        :return: list of str,student name
        >>> system.add_course_score('student 1', 'Society', 59)
        >>> system.get_all_students_with_fail_course()
        ['student 1']
        """

    def get_course_average(self, course):
        """
        Get the average score of a specific course.
        :param course: str, course name
        :return: float, average scores of this course if anyone have score of this course, or None if nobody have records.
        """

    def get_top_student(self):
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

    def get_student_by_gpa(self, gpa):
        """
        Get student with gpa
        :param gpa: int, gpa
        :return: str, student name
        >>> system.add_student('student 1', 3, 'SE')
        >>> system.add_student('student 2', 2, 'SE')
        >>> system.get_student_by_gpa(3)
       'student 1'
        """

    def get_student_by_gpa_and_grade(self, gpa, grade):
        """
        Get student with gpa and grade
        :param gpa: int, gpa
        :param grade: int, grade
        :return: str, student name
        >>> system.add_student('student 1', 3, 'SE')
        >>> system.add_student('student 2', 2, 'SE')
        >>> system.add_course_score('student 1','math', 94)
        >>> system.add_course_score('student 2','math', 94)
        >>> system.get_student_by_gpa_and_grade(3, 94)
       'student 1'
        """

    def get_student_by_gpa_and_grade_and_major(self, gpa, grade, major):
        """
        Get student with gpa and grade and major
        :param gpa: int, gpa
        :param grade: int, grade
        :param major: str, major
        :return: str, student name
        >>> system.add_student('student 1', 3, 'SE')
        >>> system.add_student('student 2', 2, 'SE')
        >>> system.add_course_score('student 1','math', 94)
        >>> system.add_course_score('student 2','math', 94)
        >>> system.add_course_score('student 3','math', 94)
        >>> system.get_student_by_gpa_and_grade_and_major(3, 94,'math')
       'student 1'
        """

    def get_student_by_gpa_and_grade_and_major_and_grade(self, gpa, grade, major, grade_grade):
        """
        Get student with gpa, grade and major
        :param gpa: int, gpa
        :param grade: int, grade
        :param major: str, major
        :param grade_grade: int, grade_grade
        :return: str, student name
        >>> system.add_student('student 1', 3, 'SE')
        >>> system.add_