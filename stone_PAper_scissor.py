import random
while True:
    choices = ["rock","paper","scissor"]

    computer= random.choice(choices)
    player=None

    while player not in choices:  
        player = input("rock,paper,scissor: ").lower()

    if player == computer:
          print("Computer: ",computer)
          print("PLayer: ",player)
          print("Tie!!")

    elif player=="rock":
        if computer == "paper":
             print("Computer: ",computer)
             print("PLayer: ",player)
             print("You loss")
        if computer == "scissor" :
             print("Computer: ",computer)
             print("PLayer: ",player)
             print("YOu win")

    elif player=="paper":
        if computer == "scissor":
              print("Computer: ",computer)
              print("PLayer: ",player)
              print("You lost")
        if computer == "scissor" :
              print("Computer: ",computer)
              print("PLayer: ",player)
              print("You won!")

    elif player=="paper":
        if computer == "rock":
              print("Computer: ",computer)
              print("PLayer: ",player)
              print("You won")
        if computer == "scissor" :
             print("Computer: ",computer)
             print("PLayer: ",player)
             print("you loss")

    play_again = input("Do you want to play again? (Yes/no): ").lower()
    if play_again != "yes":
           break
        
print("Goodbye")