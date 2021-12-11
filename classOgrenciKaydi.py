

studentDict = {
    "001": {
        "name": 'musa',
        "surname": 'karaaslan',
        "age": 21,
        "Gender": 'male',
        "claass": 'C305',
        "studentNumber": 921,
        "GPA": 74.5
    },
}

class StudentList:
    def __init__(self, name, surname, age, gender, claass, studentNumber, gpa):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        self.claass = claass
        self.studentNumber = studentNumber
        self.GPA = gpa


fieldList = ["name", "surname", "age",
             "gender", "claass", "studentNumber", "gpa"]

newFieldList = []

whatever = StudentList()


def editStudents():
    while True:
        choice2 = input('Write Which Property You Want to Change?')
        if choice2.lower in fieldList:
            choice3 = input(
                'Write Which Property You Want to Change Instead of Old One?')
            whatever.choice2 = choice3
            print(whatever)
        else:
            break


def newStudent():
    while True:
        for i in fieldList:
            i = input(f"Please Enter The {i}: ")
            newFieldList.append(i)
        whatever.addStudent(newFieldList)
        choice = str(
            input('Is There Any Other Thing You Want to Change? Write Yes/No'))
        if choice == "Yes":
            continue
        else:
            break


def mainTab():
    while True:
        Thoughts = input(
            "What Would You to Do?\n 1 For Add New Students,\n 2 for Edit Students,\n 3 For Exit")
        if Thoughts == 1:
            newStudent()
        elif Thoughts == 2:
            editStudents()
        else:
            break
