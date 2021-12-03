studentList = {
    "001":{
    "Name":"Musa",
    "Surname":"Karaaslan",
    "Class":305,
    "Gender":"helicopter",
    "student Number":921,
    "Students Grade-Point average":74
}}

def studentInformations():
    name = input(print('Please Enter Students Name'))
    
    surname = input(print('Please Enter Students Surname'))
    
    clas = input(print('Please Enter Students Class'))
    
    gender = input(print('Please Enter Students Gender'))
    
    studentNumber = input(print('Please Enter Students studentNumber'))
    
    gpa = input(print('Please Enter Students Grade-Point average')) 

    c = 0
    c += 1

    studentList.update({"Name": name, "Surname": surname, "Class": clas, "Gender": gender, "Student Number": studentNumber, "Students Grade-Point average":gpa})
   
fieldChoice = ["name", "name", "class", "gender", "student number", "grade-point average"]

def editStudents():
    while True:
        print(studentList)
        editChoice = str(input('Please Enter the ID of student that you want to change: '))
        student = studentList[editChoice]
        if editChoice in studentList:
            while True:
                editParams = str(input('Please Write which Property You Want to Change'))
                if editParams.lower in fieldChoice:
                    break
                else:
                    print('You Write a Property That Does not Exist, Please Write Again')
            newValue = input(f'Enter The New Value of {editParams.lower}: ')
            student.update({editParams:newValue})
            studentList.update({editChoice:student})
        else:
            print('You Picked a Number That Does not Exist')

newStudent = {}
def addStudents():
    newID = input('Please Specify New Students ID: ')
    if newID in studentList:
        print('This ID is Already Taken, Please Enter Some Other ID')
    for i in fieldChoice:
        value = input(f"Please Enter the {i} of New Student")
        newStudent.update({i:value})
        studentList.update({newID:newStudent})
    



def mainTab():
    while True:
        print(studentList)
        choice = str(input('Choice Your Action;\n1 For Edit Students,\n2 For Add Students\n For Exit please Write "exit" \n Please Enter an Action: '))
        if choice == "1":
            editStudents()
        elif choice == "2":
            addStudents()
        elif choice == "exit":
            break
        else:
            pass


mainTab() 