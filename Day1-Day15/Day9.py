# Day 9
from art import Bid

print(Bid)

bidder_dict = {}


def bidders(bidder_name, bidder_bid):
    bidder_dict[name] = bid


auction = "yes"

while auction == "yes":
    name = input("What is you name")
    bid = int(input("What is your bid"))
    bidders(bidder_name=name, bidder_bid=bid)
    auction = (input("Do you want to continue the auction? yes or no"))

print(bidder_dict)


def winner(participant):
    win = 0
    winner_guy = ""
    for a in participant:
        if participant[a] > win:
            win = participant[a]
            winner_guy = a
        else:
            pass
    print(win, winner_guy)


winner(bidder_dict)

exit()

# Dictionary in List Exercise
# You are going to write a program that adds to a travel_log.
# You can see a travel_log which is a List that contains 2 Dictionaries.
# Write a function that will work with the following line of code on line 21
# to add the entry for Russia to the travel_log.
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(country, visits, cities):
    K = len(travel_log)
    travel_log.append("")
    travel_log[K] = {
        "country": country,
        "visits": visits,
        "cities": cities
    }
    print(travel_log)


add_new_country("India", 12, ["Jabalpur", "Jalandhar", "Bangalore"])

# 🚨 Do NOT change the code above

# : Write the function that will allow new countries
# to be added to the travel_log. 👇


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
exit()
# Student Grades Exercise

# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"


student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆
student_grades = {}
for key in student_scores:

    if 91 <= student_scores[key] <= 100:
        student_grades[key] = "Outstanding"
    elif 81 <= student_scores[key] <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif 71 <= student_scores[key] <= 80:
        student_grades[key] = "Acceptable"
    elif student_scores[key] <= 70:
        student_grades[key] = "Fail"
    else:
        pass

print(student_grades)
