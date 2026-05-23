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
        """
        Add course to self.courses list if the course wasn't in it.
        :param course: dict, information of the course, including'start_time', 'end_time' and 'name'
        """
        if course not in self.courses:
            self.courses.append(course)

    def remove_course(self, course):
        """
        Remove course from self.courses list if the course was in it.
        :param course: dict, information of the course, including'start_time', 'end_time' and 'name'
        """
        if course in self.courses:
            self.courses.remove(course)



    def check_course_conflict(self, new_course):
        """
        Before adding a new course, check if the new course time conflicts with any other course.
        :param new_course: dict, information of the course, including'start_time', 'end_time' and 'name'
        :return: False if the new course time conflicts(including two courses have the same boundary time) with other courses, or True otherwise.
        """
        start_time = datetime.strptime(new_course['start_time'], '%H:%M')
        end_time = datetime.strptime(new_course['end_time'], '%H:%M')
        for course in self.courses:
            if start_time == datetime.strptime(course['start_time'], '%H:%M') or end_time == datetime.strptime(course['end_time'], '%H:%M'):
                return False
        return True