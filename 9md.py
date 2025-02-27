
class Student:
    name = 'Alice'       
    surname = 'Smith'   

    def show(self):
        return f"{self.name} {self.surname}"  

student = Student()

print(student.name)    
print(student.surname) 
print(student.show())  
