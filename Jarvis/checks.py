def exitCheck(user_input):
    if user_input.lower() == "exit":
        lastCheck = input("Are you sure? ")
        if lastCheck.lower() == "yes" or lastCheck.lower() == "y":
            print("Thanks for stopping by!")
            exit()
        elif lastCheck.lower() == "no" or lastCheck.lower() == "n":
            return False
        else:
            print("I do not understand your command. Please try again")
            exitCheck(user_input)

def numCheck(function):
    exit = ""
    for i in range(0,len(function)):
        if function[i].isdigit():
            return True
        elif function[i] == "e" or function[i] == "x" or function[i] == "i" or function[i] == "t":
            exit += function[i]
            if exit.lower() == "exit":
                return exitCheck(exit)
        else:
            False

def symCheck(function):
    exit = ""
    for i in range(0,len(function)):
        if function[i] == "+" or function[i] == "-" or function[i] == "/" or function[i] == "*" or function[i] == " ":
            return True
        elif function[i] == "e" or function[i] == "x" or function[i] == "i" or function[i] == "t":
            exit += function[i]
            if exit.lower() == "exit":
                exitCheck(exit)
        else:
            False
