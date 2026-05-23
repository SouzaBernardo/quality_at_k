
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
        """
        self.students[name] = {'name': name, 'grade': grade,'major': major, 'courses': {}}

    def add_course_score(self, name, course, score):
        """
        Add score of specific course for student in self.students
        :param name: str, student name
        :param course: str, cource name
        :param score: int, cource score
        >>> system.add_student('student 1', 3, 'SE')
        >>> system.add_course_score('student 1','math', 94)
        >>> system.students
        {'student 1': {'name':'student 1', 'grade': 3,'major': 'SE', 'courses': {'math': 94}}}
        """
        self.students[name]['courses'][course] = score

    def get_gpa(self, name):
        """
        Get average grade of one student.
        :param name: str, student name
        :return: if name is in students and this students have courses grade, return average grade(float)
                    or None otherwise
        """
        if name in self.students and self.students[name]['courses']:
            total_score = 0
            total_course_num = 0
            for course in self.students[name]['courses']:
                total_score += self.students[name]['courses'][course]
                total_course_num += 1
            return total_score/total_course_num
            # return round(total_score/total_course_num, 2)
        else:
            return None

    def get_all_students_with_fail_course(self):
        """
        Get all students who have any score blow 60
        :return: list of str,student name
        >>> system.add_course_score('student 1', 'Society', 59)
        >>> system.get_all_students_with_fail_course()
        ['student 1']
        """
        result = []
        for student in self.students:
            if self.get_gpa(student) < 60:
                result.append(student)
        return result

    def get_course_average(self, course):
        """
        Get the average score of a specific course.
        :param course: str, course name
        :return: float, average scores of this course if anyone have score of this course, or None if nobody have records.
        """
        total_score = 0
        total_student_num = 0
        for student in self.students:
            if course in self.students[student]['courses']:
                total_score += self.students[student]['courses'][course]
                total_student_num += 1
        return total_score/total_student_num if total_student_num else None

    def get_top_student(self):
        """
        Calculate every student's gpa with get_gpa method, and find the student with highest gpa
        :return: str, name of student whose gpa is highest
        """
        highest_gpa = 0
        top_student = None
        for student in self.students:
            student_gpa = self.get_gpa(student)
            if student_gpa > highest_gpa:
                highest_gpa = student_gpa
                top_student = student
        return top_student