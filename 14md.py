class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getSalary(self):
        return self.__addSign(self.salary)

    def __addSign(self, num):
        return f"${num}" 

employee = Employee('John', 50000)

print(employee.getSalary())  
