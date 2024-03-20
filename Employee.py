from Role import Role


class Employee:
    def __init__(self, first_name, last_name, id, age, gender, monthly_salary, role: Role):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__id = id
        self.__age = age
        self.__gender = gender
        self.__monthly_salary = monthly_salary
        self.__role = role

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        self.__gender = gender

    @property
    def monthly_salary(self):
        return self.__monthly_salary

    @monthly_salary.setter
    def monthly_salary(self, monthly_salary):
        self.__monthly_salary = monthly_salary

    def _calculate_bonus(self):
        return self.__role.monthly_salary_factor * self.__monthly_salary

    def get_bonus(self):
        bonus = self._calculate_bonus()
        print(f'{self.first_name} {self.last_name} you got {bonus} as the annual bonus')

    def promote(self, role):
        self.__role = role
        self.get_bonus()

    def print_employee(self):
        print(
            f'first name: {self.first_name}, last name: {self.last_name}, id: {self.id}, age: {self.age}, gender: {self.gender}, monthly salary: {self.monthly_salary}, name: {self.__role.name}, description: {self.__role.description}')
