class Employee:
    def __init__(self, name, salary, age):
        self.__name = name        
        self.__salary = salary     
        self.setAge(age)           

    def getName(self):
        return self.__name         

    def getSalary(self):
        return f"${self.__salary}" 

    def getAge(self):
        return self.__age         

    def setName(self, name):
        self.__name = name       

    def setSalary(self, salary):
        self.__salary = salary    

    def setAge(self, age):
        if 0 <= age <= 120:      
            self.__age = age     
        else:
            raise ValueError("Age must be between 0 and 120.")

employee = Employee('John', 50000, 30)

employee.setName('Jane')
employee.setSalary(60000)

try:
    employee.setAge(150)  
except ValueError as e:
    print(e)  

employee.setAge(28)

print(employee.getName())   
print(employee.getSalary())  
print(employee.getAge())     
