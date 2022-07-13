# Random Module
import math
import random

# Banker Roulette
# You are going to write a program which will select a random name from a list of names.
# The person selected will have to pay for everybody's food bill.

#  Important: You are not allowed to use the choice() function.
# The choice() method returns a randomly selected element from the specified sequence.
# The sequence can be a string, a range, a list, a tuple or any other kind of sequence.

# Line 8 splits the string names_string into individual names and
# puts them inside a List called names. For this to work, you must
# enter all the names as name followed by comma then space. e.g. name, name, name

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")  # This creates a list people available

total_guys = len(names)

unlucky_guy = random.randint(0, total_guys-1)
print(names[unlucky_guy], " This unlucky guys has to pay for everyone")

exit()
# covert a string into list
sample = "DAATA"
print(list(sample))

exit()
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]
# List index Starts with Zero
print(states_of_america[::-1])

exit()
toss = random.randint(0, 1)
if toss == 1:
    print("Heads")
else:
    print("Tails")
