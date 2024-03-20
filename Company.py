class Company:
    def __init__(self, employees):
        self.__employees = employees

    @property
    def employees(self):
        return self.__employees

    @employees.setter
    def employees(self, employees):
        self.__employees = employees

    def add_employee(self, employee):
        self.__employees.append(employee)

    def annual_expense(self):
        expense_sum = 0
        for emp in self.__employees:
            expense_sum += emp.monthly_salary + emp.get_bonus()
        return expense_sum

    def print_company(self):
        print(f'employees: {self.employees}')
