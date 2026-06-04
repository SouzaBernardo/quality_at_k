class AssessmentSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade, major):
        self.students[name] = {'name': name, 'grade': grade, 'major': major, 'courses': {}}

    def add_course_score(self, name, course, score):
        if name in self.students:
            self.students[name]['courses'][course] = score

    def get_gpa(self, name):
        if name in self.students and self.students[name]['courses']:
            return sum(self.students[name]['courses'].values()) / len(self.students[name]['courses'])
        return None

    def get_all_students_with_fail_course(self):
        return [name for name, info in self.students.items() if any(score < 60 for score in info['courses'].values())]

    def get_course_average(self, course):
        scores = [info['courses'][course] for name, info in self.students.items() if course in info['courses']]
        return sum(scores) / len(scores) if scores else None

    def get_top_student(self):
        return max(self.students, key=self.get_gpa, default=None)