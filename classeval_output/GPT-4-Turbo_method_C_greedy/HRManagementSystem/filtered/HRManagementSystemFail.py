class HRManagementSystem: 
    def __init__(self):
        """
        Initialize the HRManagementSystem withan attribute employees, which is an empty dictionary.
        """
        self.employees = {}


    def add_employee(self, employee_id, name, position, department, salary):
        if employee_id in self.employees:
            return False
        else:
            self.employees[employee_id] = {
                'name': name,
                'position': position,
                'department': department,
                'salary': salary
            }
            return True
    def remove_employee(self, employee_id):
        """
        Remove an employee from the HRManagementSystem.
        :param employee_id: The employee's id, int.
        :return: If the employee is already in the HRManagementSystem, returns True, otherwise, returns False.
        """
        if employee_id in self.employees:
            del self.employees[employee_id]
            return True
        else:
            return False
    def update_employee(self, employee_id: int, employee_info: dict) -> bool:
        """
        Update an employee's information in the HRManagementSystem.
        :param employee_id: The employee's id, int.
        :param employee_info: The employee's information, dict.
        :return: If the employee is already in the HRManagementSystem, returns True, otherwise, returns False.
        """
        if employee_id in self.employees:
            self.employees[employee_id] = employee_info
            return True
        else:
            return False
    def get_employee(self, employee_id):
        """
        Get an employee's information from the HRManagementSystem.
        :param employee_id: The employee's id, int.
        :return: If the employee is already in the HRManagementSystem, returns the employee's information, otherwise, returns False.
        """
        if employee_id in self.employees:
            return self.employees[employee_id]
        else:
            return False
    def list_employees(self):
        """
        List all employees' information in the HRManagementSystem.
        :return: A dictionary of all employees' information.
        """
        return self.employees