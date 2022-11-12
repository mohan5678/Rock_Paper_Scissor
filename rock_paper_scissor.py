import random
options=['Rock','Paper','Scissor']
print("\t\t\tROCK PAPER SCISSOR GAME")
state=input("Are you Ready Yes|No:")
while(state.capitalize()=="Yes" or state.lower()=="yes" or state.upper()=="YES"):
    User_action=input(("Select one choice:\nRock\nPaper\nScissor\n"))
    Computer_action=random.choice(options)
    print("You choosen:",User_action)
    print("Computer choosen:",Computer_action)
    if  User_action.capitalize()==Computer_action:
        print("\nWell done, Match is Tie")
    elif  User_action.capitalize()=="Rock" and Computer_action=="Scissor":
        print("\nCongratulations, you won the match\n")
    elif  User_action.capitalize()=="Rock" and Computer_action=="Paper":
        print("\nYou lost the match, Better luck next time\n")
    elif  User_action.capitalize()=="Paper" and Computer_action=="Rock":
        print("\nCongratulations, you won the match")
    elif  User_action.capitalize()=="Paper" and Computer_action=="Scissor":
        print("\nYou lost the match, Better luck next time\n")
    elif  User_action.capitalize()=="Scissor" and Computer_action=="Rock":
        print("\nYou lost the match, Better luck next time\n")
    elif  User_action.capitalize()=="Scissor" and Computer_action=="Paper":
        print("\nCongratulations, you won the match")
    state=input("Are you ready Yes|No:")
    if state.capitalize()=="No" or state.lower()=="no" or state.upper()=="NO":
        print("Ok Bye")
      
    
