# Name: Francis Oludhe
# Homework on coding Rock, Paper, Scissors

print "Welcome to a game of Rock, Paper, Scissors\nMake your choice?\n"

""" Placing suitable inputs for both players """
right = ["rock", "paper", "scissors"]


one = raw_input("Player 1 choice? \n")
two = raw_input("Player 2 choice? \n")

""" Making a condition for the input """
while one not in right:
    print "Player 1 please pick between rock, paper and scissors"
    one = raw_input("Player 1 choice? \n")

while two not in right:
    print "Player 2 please pick between rock, paper and scissors"
    two = raw_input("Player 2 choice? \n")


"""" The actual rules to the game """
if (one == "rock" and
two == "rock"):
    print "\n\nYou both tied.\n\nBoth of you chose", one+"."

if (one == "rock" and
two == "scissors"):
    print "\n\nPlayer 1 wins.\n\nPlayer 1 chose", one, "and Player 2 chose", two+"."

if (one == "rock" and
two == "paper"):
    print "\n\nPlayer 2 wins.\n\nPlayer 1 chose", one, "and Player 2 chose", two+"."

if (one == "scissors" and
two == "rock"):
    print "\n\nPlayer 2 wins.\n\nPlayer 1 chose", one, "and Player 2 chose", two+"."

if (one == "scissors" and
two == "scissors"):
    print "\n\nYou both tied.\n\nBoth of you chose", one+"."

if (one == "scissors" and
two == "paper"):
    print "\n\nPlayer 1 wins.\n\nPlayer 1 chose", one, "and Player 2 chose", two+"."

if (one == "paper" and
two == "rock"):
    print "\n\nPlayer 1 wins.\n\nPlayer 1 chose", one, "and Player 2 chose", two+"."

if (one == "paper" and
two == "scissors"):
    print "\n\nPlayer 2 wins.\n\nPlayer 1 chose", one, "and Player 2 chose", two+"."

if (one == "paper" and
two == "paper"):
    print "\n\nYou both tied.\n\nBoth of you chose", one+"."
