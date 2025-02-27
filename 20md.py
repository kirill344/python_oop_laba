1. Результат сравнения:
emp1 = Employee('john') 
emp2 = Employee('eric') 

print(emp1 == emp2) 
Результат: False

2. Результат сравнения:
emp1 = Employee('john') 
emp2 = Employee('eric') 

print(emp1 == emp1) 
Результат: True

3. Результат сравнения:
emp1 = Employee('john') 
emp2 = Employee('john') 

print(emp1 == emp2) 
Результат: False

4. Результат сравнения:
emp1 = Employee('john') 
emp2 = Employee('eric') 

print(emp1 != emp1) 
Результат: False

5. Результат сравнения:
emp1 = Employee('john') 
emp2 = emp1 

print(emp1 == emp2) 
Результат: True

6. Результат сравнения:
emp1 = Employee('john') 
emp2 = Employee('eric') 

print(emp1 !== emp2) 
Результат: Это вызовет ошибку SyntaxError.

7. Результат сравнения:
emp1 = Employee('john') 
emp2 = emp1 
emp2.name = 'eric' 

print(emp1 == emp2) 
Результат: False