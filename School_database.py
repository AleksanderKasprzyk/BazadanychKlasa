#Klasa stworzona do zapisu i odczytu uczniow.
class student:
    def __init__(self, student_name, student_lastname, student_class):
        self.student_name = student_name
        self.student_lastname = student_lastname
        self.student_class = student_class
    def __repr__(self):
        return f'Student: {self.student_name} {self.student_lastname} {self.student_class} \n'

#Klasa stworzona do zapisu i odczytu nauczycieli.
class teacher:
    def __init__(self, teacher_name, teacher_lastname):
        self.teacher_name = teacher_name
        self.teacher_lastname = teacher_lastname
    def __repr__(self):
        return  f'Teacher: {self.teacher_name} {teacher_lastname} \n'

#Klasa stworzona do zapisu i odczytu wychowawcow.
class educator:
    def __init__(self, educator_name, educator_lastname):
        self.educator_name = educator_name
        self.educator_lastname = educator_lastname
    def __repr__(self):
        return f'Educator: {educator_name} {educator_lastname} \n'

#Listy komend do wykorzystania w zadaniu.
command_list = ['Create', 'Manage', 'End']
create_command_list = ['Student', 'Teacher', 'Educator', 'End']
manage_command_list = []

#Glowna petla wykonujaca zadanie.
while True:
    print(f'Command list: \n {command_list}')
    command = input('What command do you want to use?: \n')
    #Wewnetrzna petla obslugujaca zadanie.
    while True:
        if command == 'Create' or command == 'create':
            print(f'Create commands list: \n {create_command_list} \n')
            command_create = input('Which user do You want to add?: \n')
            #Warunki zapisu dla poszczegolnych osob w programie.
            if command_create == 'Student' or command_create == 'student':
                student_name = input('Enter the student name: ')
                student_lastname = input('Enter the student last name: ')
                student_class = input('Enter the student class: ')
                # TODO klasa dla ucznia

            elif command_create == 'Teacher' or command_create == 'teacher':
                teacher_name = input('Enter the teacher name: ')
                teacher_lastname = input('Enter the teacher last name: ')
                # TODO klasa dla nauczyciela

            elif command_create == 'Educator' or command_create == 'educator':
                educator_name = input('Enter the educator name: ')
                educator_lastname = input('Enter the educator lastname: ')
                # TODO klasa dla wychowacy

        elif command_create == 'Manage' or command_create == 'manage':
            print(f'Manage commands: \n {manage_command_list} \n')
        elif command_create == 'End' or command_create == 'end':
            print('End of program')
            break
