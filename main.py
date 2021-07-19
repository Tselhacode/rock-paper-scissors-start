rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
Pick = [rock,paper,scissors]
user_pick = int(input("What do you pick? 0 for Rock, 1 for Paper or 2 for Scissors?\n"))
if user_pick >= 3 or user_pick < 0:
  print("Invalid input. You lose!")
else:
  print(f"{Pick[user_pick]}\nYou Chose:")
  computer_pick = random.randint(0,2)
  print(f"{Pick[computer_pick]}\nComputer Chose:")
  if user_pick == 0 and computer_pick == 2:
    print("You Won")
  elif user_pick == 2 and computer_pick == 0:
    print("Computer Won")
  elif user_pick == computer_pick:
    print("Play Again!") 
  elif user_pick > computer_pick:
    print("You Won")  
  else:
    print("You Lost")
