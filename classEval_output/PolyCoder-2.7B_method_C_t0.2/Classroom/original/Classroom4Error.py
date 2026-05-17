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
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name':'math','start_time': '8:00', 'end_time': '9:40'})
        """
        course_id = course['id']
        course_name = course['name']
        course_start_time = course['start_time']
        course_end_time = course['end_time']
        course_id = course_id
        course_name = course_name
        course_start_time = course_start_time
        course_end_time = course_end_time
        course_id = course_id
        course_name = course_name
        course_start_time = course_start_time
        course_end_time = course_end_time
        course_id = course_id
        course_name = course_name
        course_start_time = course_start_time
        course_end_time = course_end_time
        course_id = course_id
        course_name = course_name
        course_start_time = course_start_time
        course_end_time = course_end_time
        course_id = course_id
        course_name = course_name
        course_start_time = course_start_time
        course_end_time = course_end_time
        course_id = course_id
        course_name = course_name
        course_start_time = course_start_time
        course_end_time = course_end_time
        course_id = course_id
        course_name = course_name
        course_start_time = course_start_time
        course_end_time = course_end_time
        course_id = course_id
        course_name = course_name
        course_start_time = course_start_time
        course_end_time = course_end_time
        course_id = course_id
        course_name = course_name
        course_start_time = course_start_time
        course_end_time = course_end_time
        course_id = course_id
        course_name = course_name
        course_start_time = course_start_time
        course_end_time = course_end_time
        course_id = course_id
        course_name = course_name
        course_start_time = course_start_time
        course_end_time = course_end_time
        course_id = course_id
        course_name = course_name
        course_start_time = course_start_time
        course_end_time = course_end_time
        course_id = course_id
        course_name = course_name
        course_start_time = course_start_time
        course_end_time = course_end_time
        course_id = course_id
        course_name = course_name
        course_start_time = course_start_time
        course_end_time = course_end_time
        course_id = course_id
        course_name = course_name
        course_start_time = course_start_time
        course_end_time = course_end_time
        course_id = course_id
        course_name = course_name
        course_start_time = course_start_time
        course_end_time = course_end_time
        course_id = course_id
        course_name = course_name
        course_start_time = course_start_time
        course_end_time = course_end_time
        course_id = course_id
        course_name = course_name
        course_start_time = course_start_time
        course_end_time = course_end_time
        course_id = course_id
        course_name = course_name
        course_start_time = course_start_time
        course_end_time = course_end_time
        course_id = course_id
        course_name = course_name
        course_start_time = course_start_time
        course_end_time = course_end_time
        course_id = course_id
        course_name = course_name
        course_start_time = course_start_time
        course_end_time = course_end_time
        course_id = course_id
        course_name = course_name
        course_start_time = course_start_time
        course_end_time = course_end_time
        course_id = course_id
        course_name = course_name
        course_start_time = course_start_time
        course_end_time = course_end_time
        course_id = course_id
        course_name = course_name

    def remove_course(self, course):
        """
        Remove course from self.courses list if the course was in it.
        :param course: dict, information of the course, including'start_time', 'end_time' and 'name'
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name':'math','start_time': '8:00', 'end_time': '9:40'})
        >>> classroom.add_course({'name':'math','start_time': '8:00', 'end_time': '9:40'})
        """
        course_name = course['name']
        course_start_time = course['start_time']
        course_end_time = course['end_time']
        course_id = course['id']
        course_id_str = str(course_id)
        course_id_int = int(course_id)
        course_id_float = float(course_id)
        course_id_bool = bool(course_id)
        course_id_list = [course_id_str, course_id_int, course_id_float, course_id_bool]
        course_id_list_str = ', '.join(course_id_list)
        course_id_list_int = ', '.join(course_id_list)
        course_id_list_float = ', '.join(course_id_list)
        course_id_list_bool = ', '.join(course_id_list)
        course_id_list_list = [course_id_list_str, course_id_list_int, course_id_list_float, course_id_list_bool]
        course_id_list_list_str = ', '.join(course_id_list_list)
        course_id_list_list_int = ', '.join(course_id_list_list)
        course_id_list_list_float = ', '.join(course_id_list_list)
        course_id_list_list_bool = ', '.join(course_id_list_list)
        course_id_list_list_list = [course_id_list_list_str, course_id_list_list_int, course_id_list_list_float, course_id_list_list_bool]
        course_id_list_list_list_str = ', '.join(course_id_list_list_list)
        course_id_list_list_list_int = ', '.join(course_id_list_list_list)
        course_id_list_list_list_float = ', '.join(course_id_list_list_list)
        course_id_list_list_list_bool = ', '.join(course_id_list_list_list)
        course_id_list_list_list_list = [course_id_list_list_list_str, course_id_list_list_list_int, course_id_list_list_list_float, course_id_list_list_list_bool]
        course_id_list_list_list_list_str = ', '.join(course_id_list_list_list_list)
        course_id_list_list_list_list_int = ', '.join(course_id_list_list_list_list)
        course_id_list_list_list_list_float = ', '.join(course_id_list_list_list_list)
        course_id_list_list_list_list_bool = ', '.join(course_id_list_list_list_list)
        course_id_list_list_list_list_list = [course_id_list_list_list_list_str, course_id_list_list_list_list_int, course_id_list_list_list_list_float, course_id_list_list_list_list_bool]
        course_id_list_list_list_list_list_str = ', '.join(course_id_list_list_list_list_list)
        course_id_list_list_list_list_list_int = ', '.join(course_id_list_list_list_list_list)
        course_id_list_list_list_list_list_float = ', '.join(course_id_list_list_list_list_list)
        course_id_list_list_list_list_list_bool = ', '.join(course_id_list_list_list_list_list)
        course_id_list_list_list_list_list_list = [course_id_list_list_list_list_list_str, course_id_list_list_list_list_list_int, course_id_list_list_list_list_list_float, course_id_list_list_list_list_list_bool]
        course_id_list_list_list_list_list_list_str = ', '.join(course_id_list_list_list_list_list_list)
        course_id_list_list_list_list_list_list_int = ', '.join(course_id_list_list_list_list_list_list)
        course_id_list_list_list_list_list_list_float = ', '.join(course_id_list_list_list_list_list_list)
        course_id_list_list_list_list_list_list_bool = ', '.join(course_id_list_list_list_list_list_list)
        course_id_list_list_list_list_list_list_list = [course_id_list_list_list_list_list_list_str, course_id_list_list_list_list_list_list_int, course_id_list_list_list_list_list_list_float, course_id_list_list_list_list_list_list_bool]
        course_id_list_list_list_list_list_list_list_str = ', '.join(course_id_list_list_list_list_list_list_list)
        course_id_list_list_list_list_list_list_list_int = ', '.join(course_id_list_list_list_list_list_list_list)
        course_id_list_list_list_list_list_list_list_float = ', '.

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
        if check_time.find(' ')!= -1:
            return False
        if check_time.find(':')!= -1:
            return False
        if check_time.find(' ')!= -1:
            return False
        if check_time.find(':')!= -1:
            return False
        if check_time.find(' ')!= -1:
            return False
        if check_time.find(':')!= -1:
            return False
        if check_time.find(' ')!= -1:
            return False
        if check_time.find(':')!= -1:
            return False
        if check_time.find(' ')!= -1:
            return False
        if check_time.find(':')!= -1:
            return False
        if check_time.find(' ')!= -1:
            return False
        if check_time.find(':')!= -1:
            return False
        if check_time.find(' ')!= -1:
            return False
        if check_time.find(':')!= -1:
            return False
        if check_time.find(' ')!= -1:
            return False
        if check_time.find(':')!= -1:
            return False
        if check_time.find(' ')!= -1:
            return False
        if check_time.find(':')!= -1:
            return False
        if check_time.find(' ')!= -1:
            return False
        if check_time.find(':')!= -1:
            return False
        if check_time.find(' ')!= -1:
            return False
        if check_time.find(':')!= -1:
            return False
        if check_time.find(' ')!= -1:
            return False
        if check_time.find(':')!= -1:
            return False
        if check_time.find(' ')!= -1:
            return False
        if check_time.find(':')!= -1:
            return False
        if check_time.find(' ')!= -1:
            return False
        if check_time.find(':')!= -1:
            return False
        if check_time.find(' ')!= -1:
            return False
        if check_time.find(':')!= -1:
            return False
        if check_time.find(' ')!= -1:
            return False
        if check_time.find(':')!= -1:
            return False
        if check_time.find(' ')!= -1:
            return False
        if check_time.find(':')!= -1:
            return False
        if check_time.find(' ')!= -1:
            return False
        if check_time.find(':')!= -1:
            return False
        if check_time.find(' ')!= -1:
            return False
        if check_time.find(':')!= -1:
            return False
        if check_time.find(' ')!= -1:
            return False
        if check_time.find(':')!= -1:
            return False
        if check_time.find(' ')!= -1:
            return False
        if check_time.find(':')!= -1:
            return False
        if check_time.find(' ')!= -1:
            return False
        if check_time.find(':')!= -1:
            return False
        if check_time.find(' ')!= -1:
            return False
        if check_time.find(':')!= -1:
            return False
        if check_time.find(' ')!= -1

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
        return True
