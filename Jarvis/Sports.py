from checks import exitCheck, numCheck, symCheck
#This function will recommend a sport depending on the number of players
def sport():
    number_of_players = input("How many players do you have? 1, 2, 10, 12, 18, or 22? ")
    exitCheck(number_of_players)
    print (number_of_players)
    if number_of_players == "1":
        print("You should play... ")
        print("Golf")
    elif number_of_players == "2":
        print("You should play... ")
        print("Tennis")
    elif number_of_players == "10":
        print("You should play... ")
        print("Basketball")
    elif number_of_players == "12":
        print("You should play... ")
        print("Hockey")
    elif number_of_players == "18":
        print("You should play... ")
        print("Baseball")
    elif number_of_players == "22":
        print("You should play... ")
        print("Football")
    else:
        print("Invalid value, please try again.")
        sport()
