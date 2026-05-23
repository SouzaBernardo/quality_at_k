
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
        self.students[name] = {'name': name, 'grade': grade, 'major': major, 'courses': {}}
    

    def add_course_score(self, name, course, score):
        """
        Add score of specific course for student in self.students
        :param name: str, student name
        :param course: str, course name
        :param score: int, course score
        """
        if name in self.students:
            self.students[name]['courses'][course] = score
        else:
            print("Student not found.")
    

    def get_gpa(self, name):
        """
        Get average grade of one student.
        :param name: str, student name
        :return: if name is in students and this students have courses grade, return average grade(float)
                    or None otherwise
        """
        if name in self.students and self.students[name]['courses']:
            total_score = sum(self.students[name]['courses'].values())
            num_courses = len(self.students[name]['courses'])
            return total_score / num_courses
        else:
            return None
    

    def get_all_students_with_fail_course(self):
        """
        Get all students who have any score below 60
        :return: list of str, student names
        """
        failed_students = []
        for student in self.students.values():
            for score in student['courses'].values():
                if score < 60:
                    failed_students.append(student['name'])
                    break
        return failed_students
    

    def get_course_average(self, course):
        """
        Get the average score of a specific course.
        :param course: str, course name
        :return: float, average scores of this course if anyone has a score for this course, or None if nobody has records.
        """
        scores = []
        for student in self.students.values():
            if course in student['courses']:
                scores.append(student['courses'][course])
        if scores:
            return sum(scores) / len(scores)
        else:
            return None
    

    def get_top_student(self):
        """
        Calculate every student's gpa with get_gpa method, and find the student with highest gpa
        :return: str, name of student whose gpa is highest
        """
        top_student = None
        highest_gpa = 0
    
        for student in self.students.values():
            gpa = self.get_gpa(student['name'])
            if gpa is not None and gpa > highest_gpa:
                highest_gpa = gpa
                top_student = student['name']
    
        return top_student
    