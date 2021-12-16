import json

studentDict = {
    {
        "identity": "001",
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

newFieldList = []


studentListDictionary = {}


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

    def addingStudent():
        fieldInClass = [identity, name, surname,
                        age, gender, claass, studentNumber, gpa]
        for i in fieldInClass:
            for j in fieldList:
                studentListDictionary.update({j: i})
            studentDict.update({identity: studentListDictionary})
            with open("noOneKnowsWhatItsLiketoBeTheBadMan.json", "wr") as file:
                json.dumps(studentDict, file)

    def editStudent():
        while True:
            with open("noOneKnowsWhatItsLiketoBeTheBadMan.json", "wr") as file:
                print(file)
            while True:
                choice1 = input("Whose Value Going to Changed?")
                if choice1 in studentDict.keys():
                    break
                else:
                    print("You Passed Wrong Value, Please Try Again")
                while True:
                    choice2 = input("Which Value You Want to Change? ")
                    if choice2 in fieldList:
                        break
                    else:
                        print("You Passed Wrong Value, Please Try Again")
                choice3 = input("What Will be Replaced With Value? ")
                studentDict.update({choice2: choice3})


whatever = StudentList()

def mainTab():
    while True:
        Thoughts = int(input(
            "What Would You to Do?\n 1 For Add New Students,\n 2 for Edit Students,\n 3 For Exit"))
        if Thoughts == 1:
            for i in fieldList:
                value = input(f'please enter {i} value')
                newFieldList.append(value)
            StudentList(newFieldList)
        elif Thoughts == 2:
            whatever.editStudents()
        else:
            break


# mainTab()
