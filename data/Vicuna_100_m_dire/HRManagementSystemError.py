class HRManagementSystem: 
    def __init__(self):
        """
        Initialize the HRManagementSystem withan attribute employees, which is an empty dictionary.
        """
        self.employees = {}





    def remove_employee(self, employee_id):
        employee = self.employees.get(employee_id)
        if employee:
            del self.employees[employee_id]
            return True
        else:
            return False

    def update_employee(self, employee_id: int, employee_info: dict):
        employee_id = self.get_employee_id(employee_id)
        if employee_id is None:
            raise ValueError("Employee not found.")

        employee = {**self.employees[employee_id], **employee_info}
        self.employees[employee_id] = employee
        return True

    def get_employee(self, employee_id):
        """
        Get an employee's information from the HRManagementSystem.
        :param employee_id: The employee's id, int.
        :return: If the employee is already in the HRManagementSystem, returns the employee's information, otherwise, returns False.
        """
        return self.employees.get(employee_id, False)