class Employee(object):
        """This is a constructor to initialize what an Employee has"""
    def __init__(self, firstname, lastname, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
class Permanent__Employee(Employee):
    """Permanent__Employee(child class) inherits from Employee class which is the parent class"""
    __salary = 0

    def pay_salary(self):
        return annual_salary
    def set_salary(self, annual_salary):
        self.__salary = annual_salary
    def get_salary(self):
        return self.__salary

class Contract_Employee(Employee):
"""Contract_Employee(child class) also inherits from class Employee which is the parent class"""

    __salary = 0

    def wage(hourly, hours):
        salary = hourly * hours
       if hours > 40:
           overtime = 40 - hours
           salary += 0.5 * overtime
       return salary
    def pay_salary(self):
        return wage()

    def set_hourly_salary(self, hourlypay):
        self.__salary = hourlypay
    def get_hourly_salary(self):
        return self.__salary
   

def pay_salary(any_employee):
"""polymorphism in action which is done through a function"""
	return any_employee.pay_salary()
