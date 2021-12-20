import json


readed_field = ['name', "surname", "age", "gender", "studentNumber", "gpa"]
sended_field = []
dictionary = {}
new_student = {}


class Ogrenci:
    def addingStudent(self):
        id = input("Please Enter ID of New Student: ")

        for i in readed_field:
            value = input(f"Please Enter the {i} data: ")
            dictionary.update({i: value})
        new_student.update({id: dictionary})
        with open("noOneKnowsWhatItsLikeToBeTheBadMan.json", "a") as file:
            a = json.dumps(new_student)
            file.write(a)

    def editingStudent(self):
        choice = input(
            "Please Enter the Students Data That You Want to Change?: ")
        while True:
            with open("noOneKnowsWhatItsLikeToBeTheBadMan.json") as file:
                str_file = str(file)
                data = json.loads(str_file)
            if choice in file:
                break
            else:
                print("Please Enter Valid Value")
        the_student = new_student[choice]
        propertty = input(
            "Please Enter The Data of Choosen Student You Want to Change?: ")
        choosen = data[f"{propertty}"]
        while True:
            if propertty in readed_field:
                break
            else:
                print("Please Enter Valid Value")
        new_propertty = input("Please Enter The New Data: ")
        the_student.update({propertty: new_propertty})
        new_student.update({choice: new_propertty})

    def all_students(self):
        with open("noOneKnowsWhatItsLikeToBeTheBadMan.json", "r") as file:
            b = json.loads(file)
            print(b)


class UserMenu(Ogrenci):
    def __init__(self):
        ogrenci = Ogrenci()
        print("Welcome!")
        while True:
            choice = int(
                input("1 for Add a Student\n 2 for Edit a Student\n 3 See The Students.\n 4 for Exit.\n Your Turn?:  "))
            if choice == 1:
                #!Sended_fielda gonderdigim bilgiler, adding studenta tek arguman olarak gidiyor?
                for i in readed_field:
                    ogrenci.addingStudent()
                break
            elif choice == 2:
                ogrenci.editingStudent()
            elif choice == 3:
                ogrenci.all_students()
                print("Is There Any Thing You Want To Do?")
            elif choice == 4:
                break
            else:
                continue


UserMenu()
