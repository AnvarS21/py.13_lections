# class University:

#     def __init__(self, university_name):
#         self.name = university_name
#         self.departaments = {}


#     def add_departament(self, departament):
#         self.departaments[departament] = []
        
# class Student:
#     def __init__(self, first_name, last_name):
#         self.name = first_name + ' ' + last_name

#     def add_student(self, departament, uni):
#         if isinstance(uni, University):
#             uni.departaments[departament].append(self.name)


# codify = University('Codify')
# codify.add_departament('Bootcamp-python')
# codify.add_departament('Bootcamp-js')
# codify.add_departament('Java')
# codify.add_departament('Testing')
# codify.add_departament('Design')



# anvar = Student('Anvar', 'Shamsutdinov')
# anvar.add_student('Bootcamp-python', codify)

# print(codify.departaments)

##--------------------------##--------------------------##--------------------------##--------------------------


                        
                        # РАБОЧИЙ МЕТОД
class University:

    def __init__(self, university_name):
        self.name = university_name
        self.departaments = {}


    def add_departament(self, departament):
        if departament not in self.departaments:
            self.departaments[departament] = []

    def add_student(self, departament, student):
        if isinstance(student, Student):
            if departament in self.departaments:
                if student.name not in self.departaments[departament]:
                    self.departaments[departament].append(student.name)
            else:
                raise KeyError('Такого факультета не существует!')
        else:
            raise Exception('Это не студент!')

class Student:
    def __init__(self, first_name, last_name):
        self.name = first_name + ' ' + last_name

anvar = Student('Anvar', 'Shamsutdinov')
codify = University('Codify')
codify.add_departament('Python')
codify.add_departament('Python')

codify.add_student('Python', anvar)
codify.add_student('Python', anvar)
codify.add_departament('Python')

print(codify.departaments)


