
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
        {'student 1': {'name':'student 1', 'grade': 3,'major': 'SE', 'courses': {}}}
        """
        self.students[name] = {'name': name, 'grade': grade,'major': major, 'courses': {}}

    def add_course_score(self, name, course, score):
        """
        Add score of specific course for student in self.students
        :param name: str, student name
        :param cource: str, cource name
        :param score: int, cource score
        """
        if name not in self.students:
            self.students[name] = {'name': name, 'grade': None,'major': None, 'courses': {}}
        self.students[name]['courses'][course] = score

    def get_gpa(self, name):
        """
        Get average grade of one student.
        :param name: str, student name
        :return: if name is in students and this students have courses grade, return average grade(float)
                    or None otherwise
        """
        if name in self.students and self.students[name]['courses']:
            total_grade = sum(self.students[name]['courses'].values())
            return total_grade / len(self.students[name]['courses'])
        else:
            return None

    def get_all_students_with_fail_course(self):
        """
        Get all students who have any score blow 60
        :return: list of str,student name
        """
        fail_students = []
        for student in self.students:
            for course in self.students[student]:
                if self.students[student][course] < 60:
                    fail_students.append(student)
                    break
        return fail_students

    def get_course_average(self, course):
        """
        Get the average score of a specific course.
        :param course: str, course name
        :return: float, average scores of this course if anyone have score of this course, or None if nobody have records.
        """
        scores = []
        for student in self.students.values():
            if course in student.scores:
                scores.append(student.scores[course])
        if scores:
            return sum(scores) / len(scores)
        else:
            return None

    def get_top_student(self):
        """
        Calculate every student's gpa with get_gpa method, and find the student with highest gpa
        :return: str, name of student whose gpa is highest
        """
        max_gpa = 0
        max_gpa_student = None
        for name, student in self.students.items():
            gpa = self.get_gpa(name)
            if gpa > max_gpa:
                max_gpa = gpa
                max_gpa_student = name
        return max_gpa_student