def writeFile(dicGrades):
    gradefile = open("grades.txt", "w")
    gradefile.write(str(dicGrades))
    gradefile.close()

def readFile():
    gradeFile = open("grades.txt", "r")
    strFile = gradeFile.read()
    return strFile

def foodFile():
    foodDB = []
    with open("food.txt") as f:
        for line in f:
            fields = line.split(",")
            foodDB.append([fields[0],fields[1],fields[2]])
    return foodDB

foodFile()
