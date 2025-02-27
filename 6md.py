
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_info(self, name, salary):
        return f"Employee Name: {name}, Salary: {salary}"

employee1 = Employee('Alice', 50000)
employee2 = Employee('Bob', 60000)

print(employee1.show_info(employee1.name, employee1.salary))
print(employee2.show_info(employee2.name, employee2.salary)) 
