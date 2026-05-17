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
        course['start_time'] = datetime.strptime(course['start_time'], '%Y-%m-%d %H:%M:%S')
        course['end_time'] = datetime.strptime(course['end_time'], '%Y-%m-%d %H:%M:%S')
        course['name'] = course['name'].lower()
        if course['name'] in self.courses:
            self.courses.remove(course['name'])
        self.courses.append(course)


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
        if course_id in self.courses:
            course_id = self.courses[course_id]['id']
            if course_start_time < course_end_time:
                if course_id in self.courses[course_id]['courses']:
                    self.courses[course_id]['courses'].remove(course_id)
                    self.courses[course_id]['courses'].append(course)
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


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
        return False


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
        return False