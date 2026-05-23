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
        :param course: dict, information of the course, including 'start_time', 'end_time' and 'name'
        """
        if course not in self.courses:
            self.courses.append(course)

    def remove_course(self, course):
        """
        Remove course from self.courses list if the course was in it.
        :param course: dict, information of the course, including 'start_time', 'end_time' and 'name'
        """
        if course in self.courses:
            self.courses.remove(course)

    def is_free_at(self, check_time):
        """
        change the time format as '%H:%M' and check the time is free or not in the classroom.
        :param check_time: str, the time need to be checked
        :return: True if the check_time does not conflict with every course time, or False otherwise.
        """
        if check_time not in self.courses:
            return True
        else:
            for course in self.courses:
                if check_time in course['start_time'], course['end_time']:
                    return False
            return True

    def check_course_conflict(self, new_course):
        """
        Before adding a new course, check if the new course time conflicts with any other course.
        :param new_course: dict, information of the course, including 'start_time', 'end_time' and 'name'
        :return: False if the new course time conflicts(including two courses have the same boundary time) with other courses, or True otherwise.
        """
        if new_course not in self.courses:
            return False
        else:
            for course in self.courses:
                if new_course['start_time'] == course['start_time'] and new_course['end_time'] == course['end_time']:
                    return True
            return False

# Example usage
classroom = Classroom(1)
classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
classroom.add_course({'name': 'english', 'start_time': '9:00', 'end_time': '10:20'})
classroom.add_course({'name': 'science', 'start_time': '10:30', 'end_time': '12:00'})
classroom.is_free_at('10:00')
classroom.check_course_conflict({'name': 'SE', 'start_time': '9:40', 'end_time': '10:40'})