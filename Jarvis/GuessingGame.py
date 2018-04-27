import random
from checks import exitCheck, numCheck, symCheck
#This is a game for guessing a number between 1-10
def guessingGame():
    random_number = random.randint(1,11)
    user_guess = input("Guess a random number between 1-10. ")
    exitCheck(user_guess)
    if user_guess.isdigit():
        if random_number == int(user_guess):
            print ("Correct!")
        else:
            print ("Sorry the correct answer was ",random_number, " , try again.")
    else:
        print ("Please enter an integer.")
        guessingGame()

def ageGuess():
    movie = {"Cars":5, "The Dark Knight":13, "Shawshank Redemption":30, "Gone with the Wind":70}
    TV = {"Dora the Explorer":5, "Adventure Time":13, "Game of Thrones":30, "Golden Girls":70}
    food = {"Apple Sauce":5, "Pizza":13, "Steak":30, "Tapioca Pudding":70}
    choices = {"movie":0, "tv":0, "food":0}

    while True:
        print("What is your favorate Movie?")
        print("1. Cars")
        print("2. The Dark Knight")
        print("3. Shawshank Redemption")
        print("4. Gone with the Wind")
        print("5. Exit Game")

        user_input = input()
        exitCheck(user_input)
        while not(user_input == "1" or user_input == "2" or user_input == "3" or user_input == "4" or user_input == "5"):
            print(user_input)
            print("Invalid input, please try again.")
            user_input = input()
            print(user_input)
            exitCheck(user_input)
        if user_input == "1":
            choices["movie"] = movie["Cars"]
        elif user_input == "2":
            choices["movie"] = movie["The Dark Knight"]
        elif user_input == "3":
            choices["movie"] = movie["Shawshank Redemption"]
        elif user_input == "4":
            choices["movie"] = movie["Gone with the Wind"]
        elif user_input == "5":
            break

        print("What is your favorate TV show?")
        print("1. Dora the Explorer")
        print("2. Adventure Time")
        print("3. Game of Thrones")
        print("4. Golden Girls")
        print("5. Exit Game")

        user_input = input()
        exitCheck(user_input)
        while not(user_input == "1" or user_input == "2" or user_input == "3" or user_input == "4" or user_input == "5"):
            print("Invalid input, please try again.")
            user_input = input()
            exitCheck(user_input)
        if user_input == "1":
            choices["tv"] = TV["Dora the Explorer"]
        elif user_input == "2":
            choices["tv"] = TV["Adventure Time"]
        elif user_input == "3":
            choices["tv"] = TV["Game of Thrones"]
        elif user_input == "4":
            choices["tv"] = TV["Golden Girls"]
        elif user_input == "5":
            break

        print("What is your favorate food?")
        print("1. Apple Sauce")
        print("2. Pizza")
        print("3. Steak")
        print("4. Tapioca Pudding")
        print("5. Exit Game")

        user_input = input()
        exitCheck(user_input)
        while not(user_input == "1" or user_input == "2" or user_input == "3" or user_input == "4" or user_input == "5"):
            print("Invalid input, please try again.")
            user_input = input()
            exitCheck(user_input)
        if user_input == "1":
            choices["food"] = food["Apple Sauce"]
        elif user_input == "2":
            choices["food"] = food["Pizza"]
        elif user_input == "3":
            choices["food"] = food["Steak"]
        elif user_input == "4":
            choices["food"] = food["Tapioca Pudding"]
        elif user_input == "5":
            break

        print("You are between the ages of ", min(choices.values()), " and ", max (choices.values()))
        print("Your estimated average age is ", sum(choices.values())/len(choices.values()))
