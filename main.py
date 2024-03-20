from Employee import Employee
from Role import Role

if __name__ == '__main__':
    emp_role = Role('student', 'study stuff', 30)
    new_role = Role('designer', 'design stuff', 50)

    emp = Employee('Yarin', 'Peretz', 322262817, 23, 'male', 400000, emp_role)
    emp.get_bonus()
    emp.print_employee()
    emp.promote(new_role)
    emp.print_employee()
