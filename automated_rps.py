# Name: Francis Oludhe
# Homework on coding Rock, Paper, Scissors

import random

print "Welcome to a game of Rock, Paper, Scissors\nMake your choice?\n"

""" Placing suitable inputs for both players """
right = ["rock", "paper", "scissors"]


one = raw_input("Your choice? \n")
comp = random.choice(right)

""" Making a condition for the input """
while one not in right:
    print "Please pick between rock, paper and scissors"
    one = raw_input("Your choice? \n")

"""" The actual rules to the game """
if (one == "rock" and
comp == "rock"):
    print "\n\nYou both tied.\n\nBoth of you chose", one+"."

if (one == "rock" and
comp == "scissors"):
    print "\n\nYou win.\n\nYou chose", one, "and the computer chose", comp+"."

if (one == "rock" and
comp == "paper"):
    print "\n\nThe computer wins.\n\nYou chose", one, "and the computer chose", comp+"."

if (one == "scissors" and
comp == "rock"):
    print "\n\nThe computer wins.\n\nYou chose", one, "and the computer chose", comp+"."

if (one == "scissors" and
comp == "scissors"):
    print "\n\nYou both tied.\n\nBoth of you chose", one+"."

if (one == "scissors" and
comp == "paper"):
    print "\n\nYou win.\n\nYou chose", one, "and the computer chose", comp+"."

if (one == "paper" and
comp == "rock"):
    print "\n\nYou win.\n\nYou chose", one, "and the computer chose", comp+"."

if (one == "paper" and
comp == "scissors"):
    print "\n\nThe computer wins.\n\nYou chose", one, "and the computer chose", comp+"."

if (one == "paper" and
comp == "paper"):
    print "\n\nYou both tied.\n\nBoth of you chose", one+"."
