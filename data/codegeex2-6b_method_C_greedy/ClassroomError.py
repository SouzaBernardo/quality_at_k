from datetime import datetime
class Classroom: 
    def __init__(self, id):
        """
        Initialize the classroom management system.
        :param id: int, the id of classroom
        """
        self.id = id
        self.courses = []



    def add_course(self, course):
        
        if course not in self.courses:
            self.courses.append(course)


    def remove_course(self, course):


    def is_free_at(self, check_time):


    def check_course_conflict(self, new_course):