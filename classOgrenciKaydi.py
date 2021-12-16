

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
#?ic ice bir dictionary`de nasil keys() kullanirim?

fieldList = ["identity", "name", "surname", 'age',
             "gender", "claass", "studentNumber", 'gpa']


class StudentList:
    def __init__(self, identity, name, surname, age, gender, claass, studentNumber, gpa):
        self.identity = identity
        self.name = name
        self.surname = surname
        self.age = age 
        self.gender = gender
        self.claass = claass
        self.studentNumber = studentNumber
        self.gpa = gpa

    def editStudent():
        while True:
            choice = input("Which Value You Want to Change?")
            for j in fieldList:
                if j == choice:


newFieldList = []


studentListDictionary = []


def mainTab():
    while True:
        Thoughts = int(input(
            "What Would You to Do?\n 1 For Add New Students,\n 2 for Edit Students,\n 3 For Exit"))
        if Thoughts == 1:
            for i in fieldList:
                value = input(f'please enter {i} value')
                studentListDictionary.append(value)
            StudentList(studentListDictionary)
        elif Thoughts == 2:
            editStudents()
        else:
            break


# mainTab()
