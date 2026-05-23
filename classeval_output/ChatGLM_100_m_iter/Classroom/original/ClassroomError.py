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
        if course['start_time'] not in self.courses:
            self.courses.append(course)
        if course['end_time'] not in self.courses:
            self.courses.append(course)
        if course['name'] not in self.courses:
            self.courses.append(course)

    def remove_course(self, course):
        """
        Remove course from self.courses list if the course was in it.
        :param course: dict, information of the course, including'start_time', 'end_time' and 'name'
        """
        if course['start_time'] in self.courses and course['end_time'] in self.courses and course['name'] in self.courses:
            self.courses.remove(course)

    def is_free_at(self, check_time):
        """
        change the time format as '%H:%M' and check the time is free or not in the classroom.
        :param check_time: str, the time need to be checked
        :return: True if the check_time does not conflict with every course time, or False otherwise.
        """
        check_time = check_time.replace('8:00', '10:00')
        check_time = check_time.replace('9:40', '11:00')
        check_time = check_time.replace('10:00', '12:00')
        
        for course in self.courses:
            if course['start_time'] == check_time and course['end_time'] == check_time and course['name'] == check_time:
                return True
        return False

    def check_course_conflict(self, new_course):
        """
        Before adding a new course, check if the new course time conflicts with any other course.
        :param new_course: dict, information of the course, including'start_time', 'end_time' and 'name'
        :return: False if the new course time conflicts(including two courses have the same boundary time) with other courses, or True otherwise.
        """
        # Check if the new course conflicts with other courses
         conflicts = self.check_course_conflict_with_other_courses(new_course)
        if conflicts:
            return True
        # Check if the new course conflicts with self.courses
         conflicts = self.check_course_conflict_with_courses(new_course)
        if conflicts:
            return True
        return False
