#RPS.py
#Name:
#Date:
#Assignment:
import random

def main():
  wins = 0
  ties = 0
  losses = 0

  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.
  play = "Y"
  while (play == "Y"):
    #Randomly choose the computer between 'R', 'P', or 'S'
    CPUchoice = random.choice(["R", "P", "S"])

    #Prompt the user for their RPS selection

    userChoice = input("Choose Rock, Paper, or Scissors (R, P, S): ")

    #Determine winner and state what happened to the user

    if userChoice == "R":
      print("You chose Rock")
      if CPUchoice == "R":
        print("The computer chose Rock")
        print("Tie")
        ties = ties + 1
      if CPUchoice == "P":
        print("The computer chose Paper")
        print("LOSER!")
        losses = losses + 1
      if CPUchoice == "S":
        print("The computer chose Scissors")
        print("You Win!")
        wins = wins + 1

    if userChoice == "P":
      print("You chose Paper")
      if CPUchoice == "P":
        print("The computer chose Paper")
        print("TIE")
        ties = ties + 1
      if CPUchoice == "S":
        print("The computer chose Scissors")
        print("LOSER!")
        losses = losses + 1
      if CPUchoice == "R":
        print("The computer chose Rock")
        print("You Win!")
        wins = wins + 1

    if userChoice == "S":
      print("You chose Scissors")
      if CPUchoice == "S":
        print("The computer chose Scissors")
        print("TIE")
        ties = ties + 1
      if CPUchoice == "R":
        print("The computer chose Rock")
        print("LOSER!")
        losses = losses + 1
      if CPUchoice == "P":
        print("The computer chose Paper")
        print("You Win!")
        wins = wins + 1

    #Ask the user if they would like to play again.
    play = input("Play again (Y/N)? ")
    
  print("Game over")
      


  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
