
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
            if 'courses' in self.students[name]:
                self.students[name]['courses'][course] = score
            else:
                self.students[name]['courses'] = {course: score}
        else:
            self.students[name] = {'name': name, 'courses': {course: score}}
    

    def get_gpa(self, name):
        if name in self.students and self.students[name]:
            total_score = sum(self.students[name].values())
            num_courses = len(self.students[name])
            return total_score / num_courses
        else:
            return None
    

    def get_all_students_with_fail_course(self):
        """
        Get all students who have any score below 60
        :return: list of str, student names
        """
        failed_students = []
        for student in self.students:
            for course_scores in self.students[student].values():
                if course_scores < 60:
                    failed_students.append(student)
                    break
        return failed_students
    

    def get_course_average(self, course):
        """
        Get the average score of a specific course.
        :param course: str, course name
        :return: float, average scores of this course if anyone has a score for this course, or None if nobody has records.
        """
        if course in self.students:
            scores = [self.students[name]['courses'][course] for name in self.students]
            average_score = sum(scores) / len(scores)
            return average_score
        else:
            return None
    

    def get_top_student(self):
        top_student = None
        highest_gpa = 0
    
        for student in self.students:
            gpa = self.get_gpa(student)
            if gpa > highest_gpa:
                highest_gpa = gpa
                top_student = student
    
        return top_student
    