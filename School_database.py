
#Klasa stworzona do zapisu i odczytu uczniow.
class Student:
    def __init__(self, student_name, student_lastname, student_class, students_lessons):
        self.student_name = student_name
        self.student_lastname = student_lastname
        self.student_class = student_class
        self.students_lessons = students_lessons
    def __repr__(self):
        return f'Student: {self.student_name} {self.student_lastname} {self.student_class} {self.students_lessons} \n'

#Klasa stworzona do zapisu i odczytu nauczycieli.
class Teacher:
    def __init__(self, teacher_name, teacher_lastname, teacher_lesson):
        self.teacher_name = teacher_name
        self.teacher_lastname = teacher_lastname
        self.teacher_lesson = teacher_lesson
    def __repr__(self):
        return  f'Teacher: {self.teacher_name} {self.teacher_lastname} {self.teacher_lesson} \n'

#Klasa stworzona do zapisu i odczytu wychowawcow.
class Educator:
    def __init__(self, educator_name, educator_lastname, educator_class):
        self.educator_name = educator_name
        self.educator_lastname = educator_lastname
        self.educator_class = educator_class
    def __repr__(self):
        return f'Educator: {educator_name} {educator_lastname} {educator_class} \n'

#Listy komend do wykorzystania w zadaniu.
command_list = ['Create', 'Manage', 'End']
create_command_list = ['Student', 'Teacher', 'Educator', 'End']
manage_command_list = ['Class', 'Student', 'Teacher', 'Educator', 'End']

#Listy uczniow, nauczycieli, wychowawcow.
students_lessons = ['j.polski', 'matematyka', 'historia']
students_list = [Student('Aleksander', 'Kasprzyk', '3a', f'\n {students_lessons}'),
                 Student('Anna', 'Kowalska', '1a', f'\n {students_lessons}')]
teacher_list = [Teacher('Adam', 'Nowak', 'historia')]
educator_list = [Educator('Piotr', 'Kowalski', '3a')]

#Glowna petla wykonujaca zadanie.
while True:
    print(f'Command list: \n {command_list}')
    command = input('What command do you want to use?: \n')
    #Wewnetrzna petla obslugujaca zadanie.
    while True:
        #Polecenie "utwórz" - Przechodzi do procesu tworzenia użytkowników.
        if command == 'Create' or command == 'create':
            print(f'Create commands list: \n {create_command_list} \n')
            command_create = input('Which user do You want to add?: \n')

            #Warunki zapisu dla poszczegolnych osob w programie.
            if command_create == 'Student' or command_create == 'student':
                student_name = input('Enter the student name: ')
                student_lastname = input('Enter the student last name: ')
                student_class = input('Enter the student class: ')
                #Dodanie studentow do listy.
                student = Student(student_name, student_lastname, student_class)
                students_list.append(student)
                print(students_list)
                #Dodawanie lekcji do uczniow.
                lesson = input('Do You want add some lessons? (Yes/No): ')
                if lesson == 'Yes' or lesson == 'yes':
                    while True:
                        student_lesson = input('Enter the lessons to student: ')
                        students_lessons.append(student_lesson)
                        students_list.append(students_lessons)
                        print(students_lessons)
                        back = input('Do You want back? (Yes or No): ')
                        if back == 'Yes' or back == 'yes':
                            break
                        elif back == 'No' or back == 'no':
                            continue
                elif lesson == 'No' or lesson == 'no':
                    break

            elif command_create == 'Teacher' or command_create == 'teacher':
                teacher_name = input('Enter the teacher name: ')
                teacher_lastname = input('Enter the teacher last name: ')
                teacher_lesson = input('what kind of lesson She/He is teaching: ')
                #Dodanie nauczycieli do listy.
                teacher = teacher_list(teacher_name, teacher_lastname, teacher_lesson)
                teacher_list.append(teacher)
                print(teacher_list)

            elif command_create == 'Educator' or command_create == 'educator':
                educator_name = input('Enter the educator name: ')
                educator_lastname = input('Enter the educator lastname: ')
                educator_class = input('What class She/He is the teacher of: ')
                # Dodanie wychowawcow do listy.
                educator = educator_list(educator_name, educator_lastname, educator_class)
                educator_list.append(educator)
                print(educator_list)

            #Przerwanie wewnetrznej petli.
            elif command_create == 'End' or command_create == 'end':
                print('Back to start.')
                break

        #Polecenie "zarządzaj" - Przechodzi do procesu zarządzania użytkownikami.
        elif command == 'Manage' or command == 'manage':
            print(f'Manage commands: \n {manage_command_list} \n')
            command_manage = input('What do You want to manage?: \n')
            #Polecenie Class zwraca uczniow znajdujacych sie w danej klasie.
            if command_manage == "class" or command_manage == 'Class':
                class_checking = input("Which class do You want to check?: ")
                for student in students_list:
                    if student.student_class == class_checking:
                        print(student)
                        continue
                    else:
                        print('There is no such class, try again. \n')
            #Polecenie Student sprawdza w liscie podanego ucznia.
            elif command_manage == 'student' or command_manage == 'Student':
                student_name_checking = input('Write name student: ')
                student_lastname_checking = input('Write surname student: ')
                for student in students_list:
                    if student.student_name == student_name_checking:
                        print(student)
                    elif student.student_lastname == student_lastname_checking:
                        print(student)
                    else:
                        print('There is no such person, try again. \n')
            #Polecenie Teacher sprawdza w liscie podanego nauczyciela.
            elif command_manage == 'teacher' or command_manage == 'Teacher':
                teacher_name_checking = input('Write teacher name: ')
                teacher_lastname_checking = input('Write teacher surname: ')
                teacher_lesson_checking = input('Write teacher lesson which He/She teaching: ')
                for teacher in teacher_list:
                    if teacher.teacher_name == teacher_name_checking:
                        print(teacher)
                    elif teacher.teacher_lastname == teacher_lastname_checking:
                        print(teacher)
                    elif teacher.teacher_lesson == teacher_lesson_checking:
                        print(teacher)
                    else:
                        print('There is no such teacher, try again. \n')
            # Polecenie Educator sprawdza w liscie podanego wychowawce.
            elif command_manage == 'educator' or command_manage == 'Educator':
                educator_name_checking = input('Write educator name: ')
                educator_lastname_checking = input('Write educator surname: ')
                educator_class_checking = input('Write educator class: ')
                for educator in educator_list:
                    if educator.educator_name == educator_name_checking:
                        print(educator)
                    elif educator.educator_lastname == educator_lastname_checking:
                        print(educator)
                    elif educator.educator_class == educator_class_checking:
                        print(educator)
                    else:
                        print('There is no such educator, try again. \n')

            elif command_manage == 'end' or command_manage == 'End':
                break
