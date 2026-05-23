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
        >>> system = AssessmentSystem()
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
        >>> system = AssessmentSystem()
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
        if name not in self.students:
            return None
        total_score = sum(self.students[name]['courses'].values())
        total_course = len(self.students[name]['courses'])
        return total_score / total_course if total_course!= 0 else None

    def get_all_students_with_fail_course(self):
        """
        Get all students who have any score blow 60
        :return: list of str,student name
        >>> system.add_course_score('student 1', 'Society', 59)
        >>> system.get_all_students_with_fail_course()
        ['student 1']
        """
        result = []
        for name, student in self.students.items():
            for course, score in student['courses'].items():
                if score < 60:
                    result.append(name)
        return result

    def get_course_average(self, course):
        """
        Get the average score of a specific course.
        :param course: str, course name
        :return: float, average scores of this course if anyone have score of this course, or None if nobody have records.
        """
        total_score = 0
        total_student = 0
        for name, student in self.students.items():
            if course in student['courses']:
                total_score += student['courses'][course]
                total_student += 1
        return total_score / total_student if total_student!= 0 else None

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
        gpa_dict = {}
        for name, student in self.students.items():
            gpa = self.get_gpa(name)
            gpa_dict[name] = gpa
        return max(gpa_dict, key=gpa_dict.get)