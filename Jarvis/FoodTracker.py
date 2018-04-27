from checks import exitCheck, numCheck, symCheck
from ReadWrite import foodFile

def foodTracker():
    foodDB = foodFile()
    foodChoice = ["Select Breakfast", ""],["Select Lunch",""],["Select Dinner", ""],["Select First Snack",""],["Select Second Snack",""]
    for j in range(0,len(foodChoice)):
        print(foodChoice[j][0])
        for i in range(0,len(foodDB)):
            print(i+1, " ", foodDB[i][0])
        while True:
            user_input = input()
            #exitCheck(user_input)
            if numCheck(user_input):
                if int(user_input) > 0 and int(user_input) <= len(foodDB):
                    foodChoice[j][1] = foodDB[int(user_input)-1]
                    break
                else:
                    print("Invalid input, please try again.")
            else:
                print("Invalid input, please try again.")

    healthy = foodCalculator(foodChoice)
    if healthy:
        print("You did a good job!")
    else:
        healthyChoice(foodDB)

def foodCalculator(foodChoice):
    healthyItem = 0
    unhealthyItem = 0
    caloryCount = 0
    for i in range(0,len(foodChoice)):
        if foodChoice[i][1][2] == "Y" or foodChoice[i][1][2] == "Y\n":
            healthyItem +=1
            caloryCount += int(foodChoice[i][1][1])
        else:
            unhealthyItem +=1
            caloryCount += int(foodChoice[i][1][1])
    print("You condsumed ", caloryCount, "calories.")
    print("You made", healthyItem, "healthy choice(s) and", unhealthyItem, "unhealthy choice(s)")
    if healthyItem >= unhealthyItem:
        return True
    else:
        return False

def healthyChoice(foodDB):
    print("I would recommend choosing one of the following. ")
    for i in range(0,len(foodDB)):
        if foodDB[i][2] == "Y" or foodDB[i][2] == "Y\n":
            print(foodDB[i][0])
