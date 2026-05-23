class AssessmentSystem: 
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
        {'student 1': {'name':'student 1', 'grade': 3,'major': 'SE', 'courses': {'course 1': {'score': 90, 'name': 'course 1','major': 'SE'}, 'course 2': {'score': 80, 'name': 'course 2','major': 'SE'}, 'course 3': {'score': 70, 'name': 'course 3','major': 'SE'}, 'course 4': {'score': 60, 'name': 'course 4','major': 'SE'}, 'course 5': {'score': 75, 'name': 'course 5','major': 'SE'}, 'course 6': {'score': 85, 'name': 'course 6','major': 'SE'}, 'course 7': {'score': 95, 'name': 'course 7','major': 'SE'}, 'course 8': {'score': 90, 'name': 'course 8','major': 'SE'}, 'course 9': {'score': 85, 'name': 'course 9','major': 'SE'}, 'course 10': {'score': 95, 'name': 'course 10','major': 'SE'}, 'course 11': {'score': 80, 'name': 'course 11','major': 'SE'}, 'course 12': {'score': 70, 'name': 'course 12','major': 'SE'}, 'course 13': {'score': 60, 'name': 'course 13','major': 'SE'}, 'course 14': {'score': 75, 'name': 'course 14','major': 'SE'}, 'course 15': {'score': 85, 'name': 'course 15','major': 'SE'}, 'course 16': {'score': 95, 'name': 'course 16','major': 'SE'}, 'course 17': {'score': 80, 'name': 'course 17','major': 'SE'}, 'course 18': {'score': 70, 'name': 'course 18','major': 'SE'}, 'course 19': {'score': 60, 'name': 'course 19','major': 'SE'}, 'course 20': {'score': 75, 'name': 'course 20','major': 'SE'}, 'course 21': {'score': 85, 'name': 'course 21','major': 'SE'}, 'course 22': {'score': 95, 'name': 'course 22','major': 'SE'}, 'course 23': {'score': 80, 'name': 'course 23','major': 'SE'}, 'course 24': {'score': 70, 'name': 'course 24','major': 'SE'}, 'course 25': {'score': 60, 'name': 'course 25','major': 'SE'}, 'course 26': {'score': 75, 'name': 'course 26','major': 'SE'}, 'course 27': {'score': 85, 'name': 'course 27','major': 'SE'}, 'course 28': {'score': 95, 'name': 'course 28','major': 'SE'}, 'course 29': {'score': 80, 'name': 'course 29','major': 'SE'}, 'course 30': {'score'

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
        # Add the student's information to the dictionary
        student = {'name': name, 'grade': grade,'major': major}
        student['courses'][course] = {'score': score}
        # Return the updated dictionary
        return student

    def get_gpa(self, name):
        """
        :param name: str, student name
        :return: if name is in students and this students have courses grade, return average grade(float)
                        or None otherwise
        """
        if name in self.students:
            return self.students[name].average_grade
        else:
            return None

    def get_all_students_with_fail_course(self):
        """
        Get all students who have any score blow 60
        :return: list of str,student name
        >>> system.add_course_score('student 1','Society', 59)
        >>> system.get_all_students_with_fail_course()
        ['student 1', 59]
        """
        scores = [
            self.students.get(name, None)
            for name in self.students.keys()
            if self.students.get(name, None) == 60
        ]
        return [(name, score) for name, score in scores]

    def get_course_average(self, course):
        """
        :param course: str, course name
        :return: float, average scores of this course if anyone have score of this course, or None if nobody have records.
        """
        if self.has_course_score(course):
            return self.get_course_score(course)
        else:
            return None

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
        students = self.students.values()
         GPA = sum([self.get_gpa(name, i) for name, i in students]) / len(students)
        return f"{students[0]} {GPA:.2f}"