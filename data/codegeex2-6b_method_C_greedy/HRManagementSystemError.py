class HRManagementSystem: 
    def __init__(self):
        """
        Initialize the HRManagementSystem withan attribute employees, which is an empty dictionary.
        """
        self.employees = {}



    def add_employee(self, employee_id, name, position, department, salary):


    def remove_employee(self, employee_id):


    def update_employee(self, employee_id: int, employee_info: dict):


    def get_employee(self, employee_id):


    def list_employees(self):
        “”“
        :return: A list of all employees' information,dict.
        >>> hrManagementSystem = HRManagementSystem()
        >>> hrManagementSystem.employees = {1: {'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}}
        >>> hrManagementSystem.list_employees()
        {1: {'employee_ID': 1, 'name': 'John', 'position': 'Manager', 'department': 'Sales', 'salary': 100000}}