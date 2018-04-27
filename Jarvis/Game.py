from checks import exitCheck, numCheck, symCheck
from Sports import sport
from GuessingGame import guessingGame, ageGuess
from calculator import math
from StudentGrades import studentsGrades
from FoodTracker import foodTracker
import datetime

#This will check to see if the user wants to play
def switchBoard():
    sport_counter = 0
    guess_counter = 0
    calculator_counter = 0
    grades_counter = 0
    age_guess_counter = 0
    food_counter = 0
    while True:
        print("\nWhat you you like to do? (Enter Number)")
        print("1. Play sports")
        print("2. Play guessing game")
        print("3. Use Calculator")
        print("4. Grades")
        print("5. Play guess age game")
        print("6. Food tracker")
        print("7. Display stats")
        user_input = input()
        exitCheck(user_input)
        numCheck(user_input)
        if user_input == "1":
            sport()
            sport_counter += 1
        elif user_input == "2":
            guessingGame()
            guess_counter += 1
        elif user_input == "3":
            math()
            calculator_counter += 1
        elif user_input == "4":
            studentsGrades()
            grades_counter += 1
        elif user_input == "5":
            ageGuess()
            age_guess_counter += 1
        elif user_input == "6":
            foodTracker()
            food_counter += 1
        elif user_input =="7":
            print("\nYou have selected sports " , sport_counter, "time(s)")
            print("You have selected the guessing game " , guess_counter, "time(s)")
            print("You have selected the calculator " , calculator_counter, "time(s)")
            print("You have selected the grades " , grades_counter, "time(s)")
            print("You have selected the grades " , age_guess_counter, "time(s)")
            print("You have selected the food tracker " , food_counter, "time(s)")
        else:
            print("I do not understand your command. Please try again")


"""
    if user_input.lower() == "yes" or user_input.lower() == "y":
        print ("Fantastic!")
        #guessingGame()
        sport()
    elif user_input.lower() == "no" or user_input.lower() == "n":
        print("Ok maybe next time.")
    else:
        print("I do not understand your command. Please try again")
        startGame()
"""

#This will ask for the users name
def userName():
    user_name = input("What is your name? ")
    exitCheck(user_name)
    print ("Hello " + user_name)
    now = datetime.datetime.now()
    print ("Current date and time : ")
    print (now.strftime("%Y-%m-%d %H:%M:%S"))

def main():
    print("Type 'exit' to exit the program at anytime.")
    userName()
    switchBoard()

main()
