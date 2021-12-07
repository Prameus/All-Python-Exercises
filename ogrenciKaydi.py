import json

studentList = {
    "001": {
        "Name": "Musa",
        "Surname": "Karaaslan",
        "Class": 305,
        "Gender": "helicopter",
        "student Number": 921,
        "Students Grade-Point average": 74
    }}


def writeToFile(a):
    with open("studentInformations.json", "w") as file:
        file.write(json.dumps(a))


def readFromFile():
    try:
        with open("studentInformations.json", "r") as file:
            file.read("studentInformations.json")
            json.loads(file.read("studentInformations.json"))
    except:
        pass


fieldChoice = ["name", "surname", "class", "gender",
               "student number", "grade-point average"]


def editStudents():
    while True:
        print(studentList)
        editChoice = input(
            'Please Enter the ID of student that you want to change: ')
        student = studentList[editChoice]
        if editChoice in studentList:
            while True:
                editParams = str(
                    input('Please Write which Property You Want to Change: '))
                if editParams in fieldChoice:
                    break
                else:
                    print(
                        'You Write a Property That Does not Exist, Please Write Again')
            newValue = input(f'Enter The New Value of {editParams}: ')
            student.update({editParams: newValue})
            studentList.update({editChoice: student})
            isExit = str(
                input('Is There Any Other Changes You Want to Do? If There is not Write `exit`'))
            if isExit.lower == "exit":
                break
        else:
            print('You Picked a Number That Does not Exist')
            writeToFile(studentList)


newStudent = {}


def addStudents():
    newID = input('Please Specify New Students ID: ')
    if newID in studentList:
        print('This ID is Already Taken, Please Enter Some Other ID')
    for i in fieldChoice:
        value = input(f"Please Enter the {i} of New Student")
        newStudent.update({i: value})
        studentList.update({newID: newStudent})
    writeToFile(studentList)


def mainTab():
    while True:
        print(studentList)
        choice = str(input(
            'Choice Your Action;\n1 For Edit Students,\n2 For Add Students\n For Exit please Write "exit" \n Please Enter an Action: '))
        if choice == "1":
            editStudents()
        elif choice == "2":
            addStudents()
        elif choice == "exit":
            break
        else:
            pass


mainTab()
