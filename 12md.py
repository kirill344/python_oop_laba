class Employee:
    def __init__(self, name, salary):
        self.name = name         
        self.salary = salary    

    def show_name(self):
        return self.name         

    def show_salary(self):
        return self.salary      

    def increase_salary(self):
        self.salary *= 1.10      
        return self.salary        

employee = Employee('John', 50000)

print(employee.show_name())   

print(employee.show_salary())   

new_salary = employee.increase_salary()
print(f"New Salary: {new_salary}")  
