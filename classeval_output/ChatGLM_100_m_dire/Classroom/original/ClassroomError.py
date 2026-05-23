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
        if course in self.courses:
            self.courses.append(course)
        else:
            self.courses.insert(0, course)

    def remove_course(self, course):
        """
        Remove course from self.courses list if the course was in it.
        :param course: dict, information of the course, including'start_time', 'end_time' and 'name'
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name':'math','start_time': '8:00', 'end_time': '9:40'})
        >>> classroom.add_course({'name':'math','start_time': '8:00', 'end_time': '9:40'})
        """
        if course['start_time'] == self.is_free_at(self.check_time) and course['end_time'] == self.is_free_at(self.check_time):
            self.courses.remove(course)
            print(f"Successfully removed course {course['name']} at {course['start_time']} to {course['end_time']}")
        else:
            print(f"Could not remove course {course['name']} because it is already in use at {course['start_time']} to {course['end_time']}")



    def check_course_conflict(self, new_course):
        """
        Before adding a new course, check if the new course time conflicts with any other course.
        :param new_course: dict, information of the course, including'start_time', 'end_time' and 'name'
        :return: False if the new course time conflicts(including two courses have the same boundary time) with other courses, or True otherwise.
        """
         conflicts = self.check_course_conflict_for_new_course(new_course)
        return conflicts or not conflicts
