#import random function
import random
import time
from collections import OrderedDict
import os
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


#Define function to play against computer
def playComputer():
    """Play the computer"""
    #Declare a variable called computerChoices as an empty list
    computerChoices = []
    #Declare a variable called computerChoice as an empty string
    #Declare a variable called userChoice as an empty string
    #Declare a variable called playAgain as an empty string
    computerChoice = userChoice = playAgain = ""
    
    #Declare a variable called computerScore as an int
    #Declare a variable called userScore as an int
    computerScore = userScore = 0

    #Set computerChoices with the list of weapons
    computerChoices = ["Rock", "Paper", "Scissors", "Lizzard", "Spock"]

    #While playAgain is not the string n, play the game
    while playAgain != "n":
        clear()
        #Set computerChoice as a random choice from the computerChoices list
        computerChoice = random.choice(computerChoices)

        #Display choices to user
        #Prompt user for their choice
        #Store input in userChoice
        userChoice = input("> ").strip().title()
        #if computerChoice equals Rock
        if computerChoice == "Rock":
            #if userChoice equals Paper
            if userChoice == "Paper":
                #win
                print("You win! Now adding 1 to your score")
                #Add 1 to userScore
                userScore +=1
            #else if userChoice equals scissors
            elif userChoice == "Scissors":
                #loss
                print("You Lose! Now adding 1 to the compuer's score")
                # Add 1 to computerScore
                computerScore += 1
            #else if userChoice equals rock
            elif userChoice == "Rock":
                #tie
                print("You tied! No Score for anyone")
            #else if userChoice equals Lizzard
            elif userChoice == "Lizzard":
                #Lose
                print("You Lose! Now adding 1 to the compuer's score")
                # Add 1 to computerScore
                computerScore += 1
            elif userChoice == "Spock":
                #Win
                print("You win! Now adding 1 to your score")
                # Add 1 to computerScore
                userScore +=1
        #if computerChoice equals Paper
        elif computerChoice == "Paper":
            #if userChoice equals Scissors
            if userChoice == "Scissors":
                #win
                print("You win! Now adding 1 to your score")
                #Add 1 to userScore
                userScore +=1
            #else if userChoice equals Rock
            elif userChoice == "Rock":
               #loss
                print("You Lose! Now adding 1 to the compuer's score")
                # Add 1 to computerScore
                computerScore += 1
            #else if userChoice equals Paper
            elif userChoice == "Paper":
                #tie
                print("You tied! No Score for anyone")
            #else if userChoice equals Lizzard
            elif userChoice == "Lizzard":
                #win
                print("You win! Now adding 1 to your score")
                #Add 1 to userScore
                userScore +=1
            #else if userChoice equals Spock
            elif userChoice == "Spock":
                #loss
                print("You Lose! Now adding 1 to the compuer's score")
                # Add 1 to computerScore
                computerScore += 1
        elif computerChoice == "Scissors":
            #if userChoice equals Rock
            if userChoice == "Rock":
                #win
                print("You win! Now adding 1 to your score")
                #Add 1 to userScore
                userScore +=1
            #else if userChoice equals Paper
            elif userChoice == "Paper":
                #loss
                print("You Lose! Now adding 1 to the compuer's score")
                # Add 1 to computerScore
                computerScore += 1
            #else if userChoice equals Scissors
            elif userChoice == "Scissors":
                #tie
                print("You tied! No Score for anyone")
            #else if userChoice equals Lizzard
            elif userChoice == "Lizzard":
                #loss
                print("You Lose! Now adding 1 to the compuer's score")
                # Add 1 to computerScore
                computerScore += 1
            elif userChoice == "Spock":
                #win
                print("You win! Now adding 1 to your score")
                #Add 1 to userScore
                userScore +=1
        elif computerChoice == "Lizzard":
            #if userChoice equals Rock
            if userChoice == "Paper":
                #loss
                print("You Lose! Now adding 1 to the compuer's score")
                # Add 1 to computerScore
                computerScore += 1
            #else if userChoice equals Paper
            elif userChoice == "Rock":
                #win
                print("You win! Now adding 1 to your score")
                #Add 1 to userScore
                userScore +=1
            #else if userChoice equals Scissors
            elif userChoice == "Lizzard":
                #tie
                print("You tied! No Score for anyone")
            #else if userChoice equals Scissors
            elif userChoice == "Spock":
                #loss
                print("You Lose! Now adding 1 to the compuer's score")
                # Add 1 to computerScore
                computerScore += 1
            elif userChoice == "Scissors":
                #win
                print("You win! Now adding 1 to your score")
                #Add 1 to userScore
                userScore +=1
        elif computerChoice == "Spock":
            #if userChoice equals Rock
            if userChoice == "Rock":
                #loss
                print("You Lose! Now adding 1 to the compuer's score")
                # Add 1 to computerScore
                computerScore += 1
            #else if userChoice equals Paper
            elif userChoice == "Paper":
                #win
                print("You win! Now adding 1 to your score")
                #Add 1 to userScore
                userScore +=1
            #else if userChoice equals Scissors
            elif userChoice == "Spock":
                #tie
                print("You tied! No Score for anyone")
            #else if userChoice equals Scissors
            elif userChoice == "Scissors":
                #loss
                print("You Lose! Now adding 1 to the compuer's score")
                # Add 1 to computerScore
                computerScore += 1
            elif userChoice == "Lizzard":
                #win
                print("You win! Now adding 1 to your score")
                #Add 1 to userScore
                userScore +=1
        print("Do you want to play again?")
        playAgain = input("> ").strip().lower()
    if userScore > computerScore:
        print("You win the game")
        print("The final score is {}-{}".format(computerScore, userScore))
    else:
        print("Looks like the computer won this game")
        print("The final score is {}-{}".format(userScore, computerScore))
def showRules():
    """Display the rules of the game"""
    clear()
    print("These are the rules of RPSLS")
    print("Scissors cuts paper")
    print("Paper covers rock")
    print("Rock crushes lizard")
    print("Lizard poisons Spock")
    print("Spock smashes scissors")
    print("Scissors decapitates lizard")
    print("Lizard eats paper")
    print("paper disproves Spock,")
    print("Spock vaporizes rock")
    print("And as it always has, Rock crushes scissors")
    time.sleep(5)
    return main()
def main():
    userSelection = None
    while userSelection != "q":
        print("Enter q to quit")
        
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input('Action: ').lower().strip()
        
        if choice in menu:
            menu[choice]()
menu = OrderedDict ([
    ("c", playComputer),
    ("r", showRules),
])

main()