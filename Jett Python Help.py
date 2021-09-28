from sys import *
import random

# Use hash to comment out code for testing/debugging or just to add comments on parts of code!
# All inputs are case sensitive so make sure to enter correctly.
# Feel free to add more activites and maybe even randomise which ones get chosen.

"""
3 double quotations and you can have multiline comments!
Make sure you remember to close your comment otherwise it will comment all your code out.
:)
"""

# Defining all main variables needed below.
win = str("\nWell done! You won!\n") 
tie = str("\nYou tied! Try again.\n")
loss = str("\nUh oh, you lost! Prepare yourself!\n")

#Lists work like this -> rpsList[0] = Rock rpsList[1] = Paper, so on.
#Inputs pulled from this list below are case sensitive!
rpsList = ["Rock", "Paper", "Scissors"]

#Only 5 activity variables for the time being.

act1 = str("\nDo 10 starjumps!")
act2 = str("\nDo a 30 second plank!")
act3 = str("\nDo a 180kg deadlift! HA!!")
act4 = str("\nDo 15 burpees!")
act5 = str("\nDo 10 pushups!")

#Activity function is called when the game is lost.

def actFunction():
	actList = [act1, act2, act3, act4, act5]
	actChoose = input("\nPick an activity - 1, 2, 3 or 5: ")
	if actChoose == "1":
		print(actList[0])
	if actChoose == "2":
		print(actList[1])
	if actChoose == "3":
		print(actList[2])
	if actChoose == "4":
		print(actList[3])
	if actChoose == "5":
		print(actList[4])

#This will be the main loop of the game below.

while True:
	yourChoice = input("\nRock, Paper or Scissors?: ")
	rpsComp = random.choice(rpsList)
	print(f"\nYou chose {yourChoice}, the computer chose {rpsComp}.\n")


	if yourChoice == rpsComp:
		print(tie)
		continue
	elif yourChoice == "Rock":
		if rpsComp == "Scissors":
			print(win)
			continue
		else: 
			print(loss)
			actFunction()
	elif yourChoice == "Paper":
		if rpsComp == "Rock":
			print(win)
			continue
		else:
			print(loss)
			actFunction()
	elif yourChoice == "Scissors":
		if rpsComp == "Paper":
			print(win)
			continue
		else:
			print(loss)
			actFunction()

	playAgain = input("\nDo you want to play again? Y/N: ")				
	#This if statement checks if N is entered. Then it prints a goodbye message and uses the break statement to end the loop.
	if playAgain == "N":
		print("\nThanks for playing!\n")
		break
