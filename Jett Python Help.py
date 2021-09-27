from sys import *
import random

# Use hash to comment out code for testing/debugging or just to add comments on parts of code!

"""
3 double quotations and you can have multiline comments!
Make sure you remember to close your comment otherwise it will comment all your code out.
:)
"""

# Defining all main variables needed below. asdjajsdbjasdaj

win = str("Well done! You won!") 
tie = str("\nYou tied! Try again.\n")
loss = str("\nUh oh, you lost! Prepare yourself!\n")

#Lists work like this -> rpsList[0] = Rock rpsList[1] = Paper, so on.
#Inputs pulled from this list below are case sensitive!
rpsList = ["Rock", "Paper", "Scissors"]

#Only 5 activity variables for the time being.

act1 = str("\nDo 10 starjumps!")
act2 = str("Do a 30 second plank!")
act3 = str("Do a 180kg deadlift! HA!!")
act4 = str("Do 15 burpees!")
act5 = str("Do 10 pushups!")

#Activity function is called when the game is lost.

def actFunction():
	actList = [act1, act2, act3, act4, act5]
	actChoose = input("\nPick an activity - 0, 1: ")
	if actChoose == "0":
		print(actList[0])
	if actChoose == "1"
		print(actList[1])


#This will be the main loop of the game below.

while True:
	yourChoice = input("\nRock, Paper or Scissors?: ")
	rpsComp = random.choice(rpsList)
	print(f"\nYou chose {yourChoice}, the computer chose {rpsComp}.\n")

	if yourChoice == rpsComp:
		print(tie)
	elif yourChoice == "Rock":
		if rpsComp == "Scissors":
			print(win)
		else: 
			print(loss)
			actFunction()
					
	#elif
