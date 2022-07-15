# Day 14: Higher Lower Game
import random
from pprint import pprint

from art import HigherLower_logo, vs_logo
from Day14_game_data import data

count = 0


def higherLower():
    global count
    a = random.randint(0, len(data) - 1)
    b = random.randint(0, len(data) - 1)
    while a == b or data[b]['follower_count'] == data[a]['follower_count']:
        b = random.randint(0, len(data) - 1)
    print(HigherLower_logo)
    print(f"Compare A:{data[a]['name']},{data[a]['country']},{data[a]['description']},{data[a]['follower_count']}")
    print(vs_logo)
    print(f"Against B:{data[b]['name']},{data[b]['country']},{data[b]['description']},{data[b]['follower_count']}")

    guess = input("Who has more followers? Type A or B::").lower()

    if guess == 'a' and data[a]['follower_count'] > data[b]['follower_count']:
        count += 1
        higherLower()
    elif guess == 'b' and data[a]['follower_count'] < data[b]['follower_count']:
        count += 1
        higherLower()
    else:
        print(f"Yo lose Final Score:{count}")


higherLower()

print(count)
if count == len(data):
    print("You have achieved the Highest Possible Score")
# pprint(data)
