from sys import *
import random

# Use hash to comment out code for testing/debugging or just to add comments on parts of code!

"""
3 double quotations and you can have multiline comments!
Make sure you remember to close your comment otherwise it will comment all your code out.
:)
"""

# Defining all main variables needed below.

win = str("You won!") 
loss = str("You lost! Pick your punishment. 1, 2, 3, 4, or 5? ")

#Lists work like this -> rpsList[0] = Rock rpsList[1] = Paper, so on.
rpsList = ["Rock", "Paper", "Scissors"]

#Only 5 activity variables for the time being.

act1 = str("Do 10 starjumps!")
act2 = str("Do a 30 second plank!")
act3 = str("Do a 180kg deadlift! HA!!")
act4 = str("Do 15 burpees!")
act5 = str("Do 10 pushups!")

def rpsMain():
	rnum = str(random.randint(1,3))
	try:
		guess["r", "p", "s"] = input("Rock, Paper or Scissors? ")
		if(rnum == guess):
			print(win)
		else:
			print(loss)
	except:
		print("Invalid input! Try again!")
#coreRPS()


		

#def computerRPS():
#	rnum = str(random.randint(1,3))
#	if(rnum == 1):
#		print(r)
#	elif(rnum == 2):
#		print(p)
#	elif(rnum == 3):
#		print(s)

#computerRPS()


