from datetime import datetime
class Classroom:  
    """
    This is a class representing a classroom, capable of adding and removing courses, checking availability at a given time, and detecting conflicts when scheduling new courses.
    """

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
        if course in self.courses:
            self.courses.remove(course)
        else:
            print("Course not found in the list.")

    def is_free_at(self, check_time):
        check_time_str = check_time.strftime("%H:%M")
        for course in self.courses:
            course_start_time = course['start_time'].strftime("%H:%M")
            course_end_time = course['end_time'].strftime("%H:%M")
            if check_time_str == course_start_time or check_time_str == course_end_time:
                return False
        return True

    def check_course_conflict(self, new_course):
        if self.is_free_at(new_course['start_time']):
            return True
        for course in self.courses:
            if self.is_free_at(course['start_time']):
                return True
        return False