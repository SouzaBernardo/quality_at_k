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
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name':'math','start_time': '8:00', 'end_time': '9:40'})
        """

    def remove_course(self, course):
        """
        Remove course from self.courses list if the course was in it.
        :param course: dict, information of the course, including'start_time', 'end_time' and 'name'
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name':'math','start_time': '8:00', 'end_time': '9:40'})
        >>> classroom.add_course({'name':'math','start_time': '8:00', 'end_time': '9:40'})
        """

    def is_free_at(self, check_time):
        """
        change the time format as '%H:%M' and check the time is free or not in the classroom.
        :param check_time: str, the time need to be checked
        :return: True if the check_time does not conflict with every course time, or False otherwise.
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name':'math','start_time': '8:00', 'end_time': '9:40'})
        >>> classroom.is_free_at('10:00')
        True
        >>> classroom.is_free_at('9:00')
        False
        """

    def check_course_conflict(self, new_course):
        """
        Before adding a new course, check if the new course time conflicts with any other course.
        :param new_course: dict, information of the course, including'start_time', 'end_time' and 'name'
        :return: False if the new course time conflicts(including two courses have the same boundary time) with other courses, or True otherwise.
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name':'math','start_time': '8:00', 'end_time': '9:40'})
        >>> classroom.check_course_conflict({'name': 'SE','start_time': '9:40', 'end_time': '10:40'})
        False
        """

    def check_course_conflict_for_time(self, new_course, check_time):
        """
        Before adding a new course, check if the new course time conflicts with any other course.
        :param new_course: dict, information of the course, including'start_time', 'end_time' and 'name'
        :param check_time: str, the time need to be checked
        :return: False if the new course time conflicts(including two courses have the same boundary time) with other courses, or True otherwise.
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name':'math','start_time': '8:00', 'end_time': '9:40'})
        >>> classroom.check_course_conflict_for_time({'name':'math','start_time': '9:40', 'end_time': '10:40'})
        False
        """

    def get_course_list(self):
        """
        Get a list of all courses in the classroom.
        :return: list, the list of courses in the classroom
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name':'math','start_time': '8:00', 'end_time': '9:40'})
        >>> classroom.get_course_list()
        [Course(name='math', start_time='8:00', end_time='9:40')]
        """

    def get_course_list_for_time(self, check_time):
        """
        Get a list of all courses in the classroom.
        :param check_time: str, the time need to be checked
        :return: list, the list of courses in the classroom
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name':'math','start_time': '8:00', 'end_time': '9:40'})
        >>> classroom.get_course_list_for_time('9:40')
        [Course(name='math', start_time='8:00', end_time='9:40')]
        """

    def get_course_list_for_time_for_name(self, check_time):
        """
        Get a list of all courses in the classroom.
        :param check_time: str, the time need to be checked
        :return: list, the list of courses in the classroom
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name':'math','start_time': '8:00', 'end_time': '9:40'})
        >>> classroom.get_course_list_for_time_for_name('9:40')
        [Course(name='math', start_time='8:00', end_time='9:40')]
        """

    def get_course_list_for_time_for_name_and_start_time(self, check_time):
        """
        Get a list of all courses in the classroom.
        :param check_time: str, the time need to be checked
        :return: list, the list of courses in the classroom
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name':'math','start_time': '8:00', 'end_time