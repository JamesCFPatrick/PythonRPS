from sys import *
import random

# Use hash to comment out code for testing/debugging or just to add comments on parts of code!
# All inputs are case sensitive so make sure to enter correctly.
# Feel free to add more activites and maybe even randomise which ones get chosen.

"""
3 double quotations and you can have multiline comments!
Make sure you remember to close your comment otherwise it will comment all your code out.
"""

# Defining all main variables needed below.
win = str("\nWell done! You won!\n") 
tie = str("\nYou tied! Try again.\n")
loss = str("\nUh oh, you lost! Prepare yourself!\n")

#Lists work like this -> rpsList[0] = Rock rpsList[1] = Paper, so on.
#Inputs pulled from this list below are case sensitive!

rpsList = ["Rock", "Paper", "Scissors"]
actInputList = ["1", "2", "3", "4", "5", "6", "7"]
ynList = ["Y", "N"]

#7 win activities.

actw1 = str("\nDo 15 star jumps!")
actw2 = str("\nDo 10 second plank!")
actw3 = str("\nDo 10 lunges!")
actw4 = str("\nDo 10 pushups!")
actw5 = str("\nDo 10 crunches!")
actw6 = str("\nDo a 15 second wall sit!")
actw7 = str("\nDo 10 mountain climbers!")

#7 loss activities.

actl1 = str("\nDo 15 star jumps!")
actl2 = str("\nDo 10 second plank!")
actl3 = str("\nDo 10 lunges!")
actl4 = str("\nDo 15 burpees!")
actl5 = str("\nDo 10 pushups!")
actl6 = str("\nDo a thing.")
actl7 = str("\nDo 10 mountain climbers!")

#Activity functions are called depending on win or loss.

def actWin():
	global actWinList, actChoose
	actWinList = [actw1, actw2, actw3, actw4, actw5, actw6, actw7]
	actInputCheck()
	if actChoose == "1":
		print(actWinList[0])
	if actChoose == "2":
		print(actWinList[1])
	if actChoose == "3":
		print(actWinList[2])
	if actChoose == "4":
		print(actWinList[3])
	if actChoose == "5":
		print(actWinList[4])

def actLoss():
	global actLossList, actChoose
	actLossList = [actl1, actl2, actl3, actl4, actl5, actl6, actl7]
	actInputCheck()
	if actChoose == "1":
		print(actLossList[0])
	if actChoose == "2":
		print(actLossList[1])
	if actChoose == "3":
		print(actLossList[2])
	if actChoose == "4":
		print(actLossList[3])
	if actChoose == "5":
		print(actLossList[4])
	if actChoose == "5":
		print(actLossList[5])
	if actChoose == "6":
		print(actLossList[6])

def actInputCheck():
	global actChoose, actInputList
	actChoices = actInputList
	while True:
		actChoose = input(str("\nPick an activity - 1, 2, 3, 4, 5, 6 or 7: "))
		if actChoose in actChoices:
			break
		else:
			print("\nInvalid input. Numbers only!")
			continue

def inputCheck():
	global yourChoice
	choices = rpsList
	while True:
		yourChoice = input("\nRock, Paper or Scissors?: ")
		if yourChoice in choices:
			break
		else:
			print("\nInvalid input. Try again.")
			continue

def playAgain():
	global inputPlayAgain
	inputPlayAgain = input("\nDo you want to play again? Y/N: ")
	try:
		if inputPlayAgain[0] == "Y":
			return True
		elif inputPlayAgain[0] == "N":
			return False
		else:
			print("Invalid input.")
			return playAgain()
	except:
		print("Please enter valid input.")
		return playAgain()

#This will be the main loop of the game below.

while True:
	global yourChoice, inputPlayAgain
	inputCheck()
	rpsComp = random.choice(rpsList)
	print(f"\nYou chose {yourChoice}, the computer chose {rpsComp}.\n")
	if yourChoice == rpsComp:
		print(tie)
		continue
	elif yourChoice == "Rock":
		if rpsComp == "Scissors":
			print(win)
			actWin()
		else: 
			print(loss)
			actLoss()
	elif yourChoice == "Paper":
		if rpsComp == "Rock":
			print(win)
			actWin()
		else:
			print(loss)
			actLoss()
	elif yourChoice == "Scissors":
		if rpsComp == "Paper":
			print(win)
			actWin()			
		else:
			print(loss)
			actLoss()

	playAgain()

	"""
	playAgain = input("\nDo you want to play again? Y/N: ")				
	#This if statement checks if N is entered. Then it prints a goodbye message and uses the break statement to end the loop.
	if playAgain == "N":
		print("\nThanks for playing!\n")
		break
	"""
