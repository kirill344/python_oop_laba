
class Employee:
    def __init__(self, name, surname):
        self.name = name     
        self.surname = surname  
        print('+++')  

employee = Employee('John', 'Doe')

print(employee.name)    
print(employee.surname)
