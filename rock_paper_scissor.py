import random  # Importing the random module to generate random choices for the computer

# Define the available options for the game
options = ['Rock', 'Paper', 'Scissor']

# Display the title of the game
print("\t\t\tROCK PAPER SCISSOR GAME")

# Ask the user if they are ready to play the game
state = input("Are you Ready Yes|No:")

# Loop to continue the game as long as the user inputs "Yes" (in any case variation)
while state.capitalize() == "Yes" or state.lower() == "yes" or state.upper() == "YES":
    # Prompt the user to select their choice
    User_action = input("Select one choice:\nRock\nPaper\nScissor\n")
    
    # Randomly select the computer's choice
    Computer_action = random.choice(options)
    
    # Display the user's and computer's choices
    print("You choosen:", User_action)
    print("Computer choosen:", Computer_action)
    
    # Compare the user's and computer's choices to determine the outcome
    if User_action.capitalize() == Computer_action:
        print("\nWell done, Match is Tie")  # Case when it's a tie
    elif User_action.capitalize() == "Rock" and Computer_action == "Scissor":
        print("\nCongratulations, you won the match\n")  # Rock beats Scissor
    elif User_action.capitalize() == "Rock" and Computer_action == "Paper":
        print("\nYou lost the match, Better luck next time\n")  # Paper beats Rock
    elif User_action.capitalize() == "Paper" and Computer_action == "Rock":
        print("\nCongratulations, you won the match")  # Paper beats Rock
    elif User_action.capitalize() == "Paper" and Computer_action == "Scissor":
        print("\nYou lost the match, Better luck next time\n")  # Scissor beats Paper
    elif User_action.capitalize() == "Scissor" and Computer_action == "Rock":
        print("\nYou lost the match, Better luck next time\n")  # Rock beats Scissor
    elif User_action.capitalize() == "Scissor" and Computer_action == "Paper":
        print("\nCongratulations, you won the match")  # Scissor beats Paper

    # Ask the user if they want to play again
    state = input("Are you ready Yes|No:")
    
    # If the user says "No" (in any case variation), exit the game
    if state.capitalize() == "No" or state.lower() == "no" or state.upper() == "NO":
        print("Ok Bye")  # Farewell message

#India will win today
#This newly added second line
# Hi, I learned how to use git