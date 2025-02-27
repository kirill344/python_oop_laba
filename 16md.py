class Employee:
    def __init__(self, name, salary, age):
        self.__name = name         
        self.__salary = salary      
        self.__age = age           

    def getName(self):
        return self.__name        

    def getSalary(self):
        return self.__salary      

    def getAge(self):
        return self.__age     

employee = Employee('John', 50000, 30)

print(employee.getName())   
print(employee.getSalary()) 
print(employee.getAge())   
