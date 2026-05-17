class HRManagementSystem:
    """
    This is a class as personnel management system that implements functions such as adding, deleting, querying, and updating employees
    """

    def __init__(self):
        """
        Initialize the HRManagementSystem with an attribute employees, which is an empty dictionary.
        """
        self.employees = {}

    def add_employee(self, employee_id, name, position, department, salary):
        if employee_id in self.employees:
            return False
        else:
            self.employees[employee_id] = {'name': name, 'position': position, 'department': department, 'salary': salary}
            return True

    def remove_employee(self, employee_id):
        if employee_id in self.employees:
            del self.employees[employee_id]
            return True
        else:
            return False

    def update_employee(self, employee_id: int, employee_info: dict):
        if employee_id in self.employees:
            self.employees[employee_id] = employee_info
            return True
        else:
            return False

    def get_employee(self, employee_id):
        if employee_id in self.employees:
            return self.employees[employee_id]
        else:
            return False

    def list_employees(self):
        return self.employees