
class Employee:
    pass
employee1 = Employee()
employee2 = Employee()
employee3 = Employee()
employee1.name = 'Alice'
employee1.salary = 50000
employee2.name = 'Bob'
employee2.salary = 60000
employee3.name = 'Charlie'
employee3.salary = 55000

print(f"{employee1.name} earns {employee1.salary}")
print(f"{employee2.name} earns {employee2.salary}")
print(f"{employee3.name} earns {employee3.salary}")

total_salary = employee1.salary + employee2.salary + employee3.salary

print(f"Total salary of all employees: {total_salary}")
