from checks import exitCheck, numCheck, symCheck
from ReadWrite import writeFile, readFile

def studentsGrades():
    grades = {"English":0, "Math":0, "Science":0, "History":0, "Gym":0}
    gradefile = readFile()
    grades = convertToDic(grades,gradefile)
    while True:
        print("\nSelect the subject you would like to change the grade for. (Enter Number)")
        print("1. English")
        print("2. Math")
        print("3. Science")
        print("4. History")
        print("5. Gym")
        print("6. Show average")
        print("7. Back to Jarvis")
        user_input = input()
        exitCheck(user_input)
        if user_input == "1":
            grade_input = input("Input your grade for English. ")
            exitCheck(grade_input)
            if numCheck(grade_input):
                grades["English"] = int(grade_input)
            else:
                print("Invalid input, please try again.")
        elif user_input == "2":
            grade_input = input("Input your grade for Math. ")
            exitCheck(grade_input)
            if numCheck(grade_input):
                grades["Math"] = int(grade_input)
            else:
                print("Invalid input, please try again.")
        elif user_input == "3":
            grade_input = input("Input your grade for Science. ")
            exitCheck(grade_input)
            if numCheck(grade_input):
                grades["Science"] = int(grade_input)
            else:
                print("Invalid input, please try again.")
        elif user_input =="4":
            grade_input = input("Input your grade for History. ")
            exitCheck(grade_input)
            if numCheck(grade_input):
                grades["History"] = int(grade_input)
            else:
                print("Invalid input, please try again.")
        elif user_input =="5":
            grade_input = input("Input your grade for Gym. ")
            exitCheck(grade_input)
            if numCheck(grade_input):
                grades["Gym"] = int(grade_input)
            else:
                print("Invalid input, please try again.")
        elif user_input =="6":
            average = sum(grades.values())/len(grades.values())
            print("Your average is ", average)
        elif user_input =="7":
            break
        else:
            print("I do not understand your command. Please try again")
            studentsGrades()
        print("Your new grades are ", grades)
        writeFile(grades)

def convertToDic(grades, gradeFile):
    classCounter = 0
    txtValue = ""
    value = 0
    for i in range (0, len(gradeFile)):
        if gradeFile[i] == ":":
            j = i + 2
            while gradeFile[j].isdigit():
                txtValue += gradeFile[j]
                j += 1
            value = int(txtValue)
            txtValue = ""
            if classCounter == 0:
                grades["English"] = value
            if classCounter == 1:
                grades["Math"] = value
            if classCounter == 2:
                grades["Science"] = value
            if classCounter == 3:
                grades["History"] = value
            if classCounter == 4:
                grades["Gym"] = value
            classCounter += 1
    return grades
