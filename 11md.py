
class Employee:
    def __init__(self, name, salary):
        self.name = name          
        self.salary = salary     
        print(f"Employee created: {self.name} with salary {self.salary}")  

employee = Employee('John', 50000)

print(f"Name: {employee.name}")    
print(f"Salary: {employee.salary}") 
