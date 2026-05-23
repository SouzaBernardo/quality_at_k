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
        :param course: dict, information of the course, including 'start_time', 'end_time' and 'name'
        """
        if course['name'] not in self.courses:
            self.courses.append(course)
        else:
            print("Course already exists.")


    def remove_course(self, course):
        for course_info in self.courses:
            if course_info['start_time'] == course['start_time'] and course_info['end_time'] == course['end_time']:
                self.courses.remove(course_info)
                return

    def is_free_at(self, check_time):
        check_time = check_time.strftime("%H:%M")
        for course in self.courses:
            start_time = course['start_time'].strftime("%H:%M")
            end_time = course['end_time'].strftime("%H:%M")
            if check_time in (start_time, end_time):
                return False
        return True

    def check_course_conflict(self, new_course):
        start_time = new_course['start_time']
        end_time = new_course['end_time']
        for course in self.courses:
            if start_time < course['start_time']:
                continue
            if end_time < course['start_time']:
                return False
            if start_time > course['end_time']:
                return False
            if end_time > course['end_time']:
                return False
        return True