
class Student:
    def __init__(self, name, surname):
        self.name = name     
        self.surname = surname 

    def capitalize_first_letter(self, string):
        return string.capitalize()

    def get_initials(self):
        initial_name = self.capitalize_first_letter(self.name)
        initial_surname = self.capitalize_first_letter(self.surname) 
        return f"{initial_name[0]}. {initial_surname[0]}."

student = Student('john', 'doe')

print(student.get_initials())  # Выведет: J. D.
