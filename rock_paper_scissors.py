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
game_gestures = [rock, paper, scissors]
player_choice = int(input('What do you want to choose? Type 0 for "Rock"'
                    '1 for  "Paper" 2 for "Scissors"\n'))
if player_choice >= 0 and player_choice <= 2:
    print(game_gestures[player_choice])

comp_choice = random.randint(0,2)
print("Computer chose:")
print(game_gestures[comp_choice])

if player_choice >= 3 or player_choice < 0:
    print("Sorry! Your Gesture you chose is invalid ")
elif player_choice == 0 and comp_choice == 2:
    print("You Win!")
elif player_choice > comp_choice:
    print("You Win!")
elif player_choice < comp_choice:
    print("You lose")
elif player_choice == 2 and comp_choice == 0:
    print("You lose")
elif player_choice ==  comp_choice:
    print("It's Draw!")

else:
    print("Game Over")

