import json

readed_field = ['name', "surname", "age", "gender", "studentNumber", "gpa"]
sended_field = []


class Ogrenci:
    def addingStudent(self, name, surname, age, gender, studentNumber, gpa):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        self.studentNumber = studentNumber
        self.gpa = gpa
        with open("noOneKnowsWhatItsLikeToBeTheBadMan.json", "wr") as file:
            file.write()

    def editingStudent(self):
        pass


class UserMenu(Ogrenci):
    def __init__(self):
        ogrenci = Ogrenci()
        print("Welcome!")
        while True:
            choice = int(
                input("1 for Add a Student\n 2 for Edit a Student\n 3 for Exit. "))
            if choice == 1:
                for i in readed_field:
                    value = input(f"Please Enter the {i} data: ")
                    sended_field.append(value)
                ogrenci.addingStudent(sended_field)
            elif choice == 2:
                ogrenci.editingStudent()
            elif choice == 3:
                break
            else:
                continue


UserMenu()
