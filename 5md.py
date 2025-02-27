
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_info(self):
        return f"Employee Name: {self.name}, Salary: {self.salary}"

employee1 = Employee('Alice', 50000)
employee2 = Employee('Bob', 60000)

print(employee1.show_info())  
print(employee2.show_info()) 
