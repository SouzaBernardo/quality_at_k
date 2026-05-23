class HRManagementSystem:  
    """
    This is a class as personnel management system that implements functions such as adding, deleting, querying, and updating employees
    """

    def __init__(self):
        """
        Initialize the HRManagementSystem withan attribute employees, which is an empty dictionary.
        """
        self.employees = {}



    def add_employee(self, employee_id, name, position, department, salary):
        """
        Add a new employee to the HRManagementSystem.
    
        :param employee_id: The employee's id, int.
        :param name: The employee's name, str.
        :param position: The employee's position, str.
        :param department: The employee's department, str.
        :param salary: The employee's salary, int.
        :return: If the employee is already in the HRManagementSystem, returns False, otherwise, returns True.
        >>> hrManagementSystem = HRManagementSystem()
        >>> hrManagementSystem.add_employee(1, 'John', 'Manager', 'Sales', 100000)
        True
        >>> hrManagementSystem.add_employee(1, 'John', 'Manager', 'Sales', 100000)
        False

    def remove_employee(self, employee_id):
        employee = next((e for e in self.employees if e['id'] == employee_id), None)
        if employee:
            del self.employees[employee['id']]
            return True
        return False

    def update_employee(self, employee_id: int, employee_info: dict):
        employee = next((e for e in self.employees if e['id'] == employee_id), None)
        if employee:
            for key, value in employee_info.items():
                self.employees[employee_id][key] = value
            return True
        return False