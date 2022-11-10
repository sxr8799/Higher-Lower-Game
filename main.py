import random
from art import logo, vs
from game_data import data
import os

def get_random_account():
  """Get data from random account"""
  return random.choice(data) # returns a dict

def format_data(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"

end_game = False

def game():
    score = 0
    account_a = get_random_account()
    account_b = get_random_account()
    while not end_game:
      print(logo)
      print(f"Compare A: {format_data(account_a)}.")
      print(vs)
      print(f"Against B: {format_data(account_b)}.")
      user_input = input("\nWho has more followers? Type 'A' or 'B': ")
      if user_input == "A":
        if account_a["follower_count"] > account_b["follower_count"]:
          account_a = account_a
          account_b = get_random_account()
          os.system('clear')
          score += 1
          print(f"You're right! Current score: {score}.")
        elif account_b["follower_count"] > account_a["follower_count"]:
          print("You were wrong")
          break
      elif user_input == "B":
        if account_b["follower_count"] > account_a["follower_count"]:
          print("You are correct")
          account_a = account_b
          account_b = get_random_account()
          os.system('clear')
          score += 1
          print(f"You're right! Current score: {score}.")
        elif account_a["follower_count"] > account_b["follower_count"]:
          print("You were wrong")
          break

game()
