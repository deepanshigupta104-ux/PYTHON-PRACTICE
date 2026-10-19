import random
computer = random.choice([-1, 0,1])

youstr = input("Enter your choice")
youDict = {"s": 1, "w":-1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}
you  =youDict[youstr]

print(f"you choose{reverseDict[you]}\nCOMPUTER  CHOOSE {reverseDict[computer]}")

if computer == you:
    print("Draw!")

else:
  '''
  if computer == -1 and you == 1:
    print("You win!")

  elif computer == -1 and you == 0:
    print("You lose!")
  elif computer == 1 and you == -1:
      print("loose")
  elif computer == 1 and you == 0:
      print("loose!")
  elif computer == 0 and you == 1:
      print("loose")
  elif computer == 0 and you == -1:
      print("You win")
      
      '''
  if((computer - you) == -1 or (computer - you) == 2):
      print("you loose")
  else:
      print("YOU WIN")
      
      
  