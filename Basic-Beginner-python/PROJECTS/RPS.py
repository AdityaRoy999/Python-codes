import random
while True:
    choices = ["Rock","Paper","Scissors"]
    player = input("enter your choice:").lower()
    #print(player.lower())

    computer = random.choice(choices).lower()
    

    #print(computer.lower())
    
    if computer == player:
       print("Computer choice: "+ computer)
       print("Your choice: "+ player)
       print("it is a tie")
    elif computer == "rock":
        if player == "paper":
          print("Computer choice: "+ computer)
          print("Your choice: "+ player)
          print("You Won!!")
        if player == "scissors":
          print("Computer choice:"+ computer)
          print("Your choice: "+ player)
          print("You Lost")
    elif computer == "paper":
        if player == "scissors":
         print("Computer choice:"+ computer)
         print("Your choice: "+ player)
         print("You Won!!")
        if player == "rock":
         print("Computer choice: "+ computer)
         print("Your choice"+ player)
         print("You Lost")
    elif computer == "scissors":
        if player == "rock":
         print("Computer choice: "+ computer)
         print("Your choice: "+ player)
         print("You Won!!")
        if player == "paper":
         print("Computer choice: "+ computer)
         print("Your choice: "+ player)
         print("You Lost")
    else:
       print("pls try again")
    play_again = input("do you want to play again(yes/No):").lower()
    if play_again != "yes":
       break    
print("bye")




        
