
import random
import tkinter as tk

from Yahtzee import *


root = tk.Tk()
frame = tk.Frame(root)	




class Dice:
	def __init__(self, sides):
		self.sides = sides
		self.value = 0

	def roll(self):
		self.value = random.randint(1,self.sides)

def returnState():
	y = []
	for i in x:
		y.append(i.dice.value)
	return(y)

class square:

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

class reroll:
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


class Score:
	def __init__(self):
		self.box = tk.Button(frame, text = 'Score', width = 4, command = self.active)
		self.box.grid(row = 1, column = 3)

	def active(self):
		z = input('How would you like this scored? ')
		info = B.check(returnState(), z)
		print(info)
		if info[0]:	
			for i in x:
				i.roll()
			y.rolls = 2
		B.stats()




x = [square(i) for i in range(5)]

for i in x:
	i.roll()

y = reroll()

z = Score()

B = Board()

B.stats()
frame.pack()



root.mainloop()

