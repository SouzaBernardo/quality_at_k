
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
        {'student 1': {'name': 'student 1', 'grade': 3, 'major': 'SE', 'courses': {}}}
        """
        self.students[name] = {'name': name, 'grade': grade, 'major': major, 'courses': {}}

    def add_course_score(self, name, course, score):
        self.students[name][course] = score

    def get_gpa(self, name):
        if name in self.students and len(self.students[name]) > 0:
            return sum(self.students[name]) / len(self.students[name])
        else:
            return None

    def get_all_students_with_fail_course(self):
        students = []
        for student in self.students.values():
            if student['score'] < 60:
                students.append(student['name'])
        return students

    def get_course_average(self, course):
        average_score = 0.0
        for student_name, student_grade in self.students.items():
            if student_name in self.get_all_students_with_fail_course():
                scores = self.get_all_scores_of_student(student_name, course)
                if scores:
                    average_score += scores[0]
                else:
                    average_score += 0.0
            else:
                average_score += 0.0
        return average_score / len(self.students) if len(self.students) > 0 else None

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
    
        # Calculate every student's gpa with get_gpa method
        student_gpas = {}
        for name, grade, major in self.students.items():
            gpa = self.get_gpa(name)
            student_gpas[name] = gpa
    
        # Find the student with highest gpa
        highest_gpa = max(student_gpas, key=student_gpas.get)
        return highest_gpa