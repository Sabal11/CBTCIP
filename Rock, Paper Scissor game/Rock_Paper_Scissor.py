import random

i = 1
while i <= 3:
    In = input("Enter Rock, Paper or scissor: ")
    In = In.capitalize()
    
    User_actions = ["Rock", "Paper", "Scissor"]
    Computer_actions = random.choice(User_actions)

    print (f"The Computer have selected {Computer_actions}")

    if In == "Rock":
     print(f"You have selected {In}")
    elif In == "Paper":
     print(f"You have selected {In}")
    elif In == "Scissor":
     print(f"You have selected {In}")
    else:
     print("Invalid")
     print("Please enter a valid input....")
     break

    if In == "Rock" and Computer_actions == "Paper":
        print("You lost, Try again !!!")
    elif In == "Paper" and Computer_actions == "Scissor":
        print("You lost, Try again !!!")
    elif In == "Scissor" and Computer_actions == "Rock":
        print("You lost, Try again !!!")
    elif In == "Rock" and Computer_actions == "Scissor":
        print("You win Congratulation !!!")
    elif In == "Paper" and Computer_actions == "Rock":
        print("You win Congratulation !!!")
    elif In == "Scissor" and Computer_actions == "Paper":
        print("You win Congratulation !!!")
    else:
        print("It's a Tie")
    i = i + 1