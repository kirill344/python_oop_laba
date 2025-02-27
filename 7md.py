
class Employee:
    def __init__(self, name, salary):
        self.name = name  
        self.salary = salary  

    def show_name(self):
        print(self.name)

    def show_salary(self):
        print(self.salary)

employee = Employee('Alice', 50000)

employee.show_name()   # Выведет: Alice
employee.show_salary() # Выведет: 50000
