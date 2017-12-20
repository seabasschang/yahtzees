import random, sys
import tkinter as tk

from Yahtzee import *


root = tk.Tk()
frame = tk.Frame(root)	

counter = 13


class Dice: #This class is simply a dice with the ability to be rolled, and which holds its current value.
	def __init__(self, sides):
		self.sides = sides
		self.value = 0

	def roll(self):
		self.value = random.randint(1,self.sides)

def returnState(): #This function iterates through all of the dice and returns the values of all 5.
	y = []
	for i in x:
		y.append(i.dice.value)
	return(y)

class square: #This class is a button which can be selected or unselected, and which stores
#a dice. 

	def __init__(self, x):
		self.dice = Dice(6)
		self.yes = False
		self.box = tk.Button(frame, text = self.dice.value, width = 4, command = self.select)
		self.box.grid(row = 0, column = x)

	def select(self):
		self.yes = not self.yes
		if not self.yes:
			self.box['text'] = self.dice.value
		else:
			self.box['text'] = '[' + str(self.dice.value) + ']'
		frame.pack()
	def roll(self):
		self.dice.roll()
		self.box['text'] = self.dice.value
		frame.pack()

class reroll: #this class is the button which rerolls the selected dice.
	def __init__(self): 
		self.box = tk.Button(frame, text = 'Reroll', width = 4, command = self.active)
		self.box.grid(row = 1, column = 6)
		self.rolls = 2

	def active(self):
		if self.rolls > 0:
			for i in x:
				if i.yes:
					i.roll()
					i.yes = False
			self.rolls -= 1
		else:
			print('You are out of rolls')


class Score: #This class is the button which allows you to score your current dice. 
	#When clicked it prompts the user to input, in test, how they would like their dice to be scored.
	#It then calls B.check, which checks if that score method is allowed, and returns the value if it is.
	def __init__(self):
		self.box = tk.Button(frame, text = 'Score', width = 4, command = self.active)
		self.box.grid(row = 1, column = 3)

	def active(self):
		global counter
		z = input('How would you like this scored? ')
		info = B.check(returnState(), z)
		print(info)
		if info[0]:	
			counter -= 1
			for i in x:
				i.roll()
			y.rolls = 2
		B.stats()
		if counter <= 0:
			sys.exit('Thanks for playing!')



#Initializes all 5 dice buttons and stores them in an array.
x = [square(i) for i in range(5)]
#Rolls the dice the first time
for i in x:
	i.roll()
#Initializes the reroll button
y = reroll()
#Initializes the score button
z = Score()
#Initializes the Board, which holds score information and processess score attempts
B = Board()
#calls B.Stats, which shows all relevent score information and tells the user how many rounds are left.
B.stats()
#Runs the program
frame.pack()
root.mainloop()
