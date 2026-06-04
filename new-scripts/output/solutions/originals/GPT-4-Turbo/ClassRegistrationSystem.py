```python
class ClassRegistrationSystem:
    def __init__(self):
        self.students = []
        self.students_registration_classes = {}

    def register_student(self, student):
        if student not in self.students:
            self.students.append(student)
            return 1
        else:
            return 0

    def register_class(self, student_name, class_name):
        if student_name in self.students_registration_classes:
            self.students_registration_classes[student_name].append(class_name)
        else:
            self.students_registration_classes[student_name] = [class_name]
        return self.students_registration_classes[student_name]

    def get_students_by_major(self, major):
        return [student['name'] for student in self.students if student['major'] == major]

    def get_all_major(self):
        return list(set([student['major'] for student in self.students]))

    def get_most_popular_class_in_major(self, major):
        classes = []
        for student in self.students:
            if student['major'] == major:
                classes.extend(self.students_registration_classes.get(student['name'], []))
        return max(set(classes), key=classes.count)
```