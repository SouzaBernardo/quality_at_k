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
        """
        Add course to self.courses list if the course wasn't in it.
        :param course: dict, information of the course, including'start_time', 'end_time' and 'name'
        """
        course_name = course['name']
        course_start_time = datetime.strptime(course['start_time'], '%H:%M').time()
        course_end_time = datetime.strptime(course['end_time'], '%H:%M').time()
        for existing_course in self.courses:
            if existing_course['name'] == course_name:
                return
        self.courses.append({
            'name': course_name,
           'start_time': course_start_time,
            'end_time': course_end_time
        })