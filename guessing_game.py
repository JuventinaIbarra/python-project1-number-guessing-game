"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
by juventina ibarra
--------------------------------
"""
import random

def start_game():
  print("Welcome to the Number Guessing Game") #prints welcome message

  x_number = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) #variable that stores a random number from an array
  attemps = 0 #variable that stores number of atemps

  while True:
    attemps += 1
    try:
      chosen_number = int(input("Choose a number from 1 to 10: "))
      if chosen_number > 10 or chosen_number < 1:
        raise ValueError("choose a number from 1 to 10")
      if chosen_number == x_number:
        print("you won")
        print("You got it!!! Your number of attemps was {}".format(attemps))
        print("Game is over")
        break
      elif chosen_number > x_number:
        print("Its lower")
        continue
      elif chosen_number < x_number:
        print("Its higher")
        continue
    except ValueError:
      print("oops it wasnt a valid number TRY AGAIN")
    
      
    



# Kick off the program by calling the start_game function.
start_game()