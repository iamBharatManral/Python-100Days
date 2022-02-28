import random

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

choices = ["rock", "scissors" , "paper"]

user_choice = int(
    input("\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

computer_choice=random.randint(0, 2)

user_choice = choices[user_choice]
computer_choice = choices[computer_choice]

if user_choice == "rock" and computer_choice == "scissors":
  print("\nYou WON! Hail to rock!")
  print(f"{rock}")
elif user_choice == "scissors" and computer_choice == "paper":
  print("\nYou WON! Hail to scissors!")
  print(f"{scissors}")
elif user_choice == "paper" and computer_choice == "rock":
  print("\nYou WON! Hail to paper!")
  print(f"{paper}")
else:
  print(f"\nYou LOST to {computer_choice}!")
  print(f"{locals() [computer_choice]}")




