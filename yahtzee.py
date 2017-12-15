from random import randint

class Dice:
	def __init__(self,):
		#Holds all five dice as values
		self.a = randint(1,6)
		self.b = randint(1,6)
		self.c = randint(1,6)
		self.d = randint(1,6)
		self.e = randint(1,6)

	def value(self):
		return (self.a, self.b, self.c, self.d, self.e)

	def roll(self, rollnum):
		#rollnum is the specific positions of dice being rolled
		#Doesn't need to return an array, but the updated values will need to be called
		if rollnum.count('a') == 1:
			self.a = randint(1,6)
		if rollnum.count('b') == 1:
			self.b = randint(1,6)
		if rollnum.count('c') == 1:
			self.c = randint(1,6)
		if rollnum.count('d') == 1:
			self.d = randint(1,6)
		if rollnum.count('e') == 1:
			self.e = randint(1,6)


class Board:
	def __init__(self,):
		self.score = 0
		self.aces = 0
		self.twos = 0
		self.threes = 0
		self.fours = 0
		self.fives = 0
		self.sixes = 0
		self.threekind = 0
		self.fourkind = 0
		self.fullhouse = 0
		self.smstraight = 0
		self.lgstraight = 0
		self.yahtzee = 0

	def check(self, dicestate):
		#dicestate will be the list of dice values.
		#Checks if the current list of dice values satisfies a special combination.
		choice_is_valid = False
		while not choice_is_valid:
			choice = input('Input Combo: ')
			choice_is_valid = True
			if choice.lower() == str('three of a kind') or choice.lower() == str('3 of a kind'):
				valid = False
				for n in range(1,7):
					if dicestate.count(n) >= 3:
						valid = True
						break
			elif choice.lower() == str('four of a kind') or choice.lower() == str('4 of a kind'):
				valid = False
				for n in range(1,7):
					if dicestate.count(n) >= 4:
						valid = True
						break
			elif choice.lower() == str('full house'):
				valid = False
				for n in range(1,7):
					if dicestate.count(n) == 3:
						for d in range(1,7):
							if dicestate.count(d) == 2:						
							valid = True
							break
			elif choice.lower() == str('small straight'):
				sequence = sorted(dicestate)
				if [1, 2, 3, 4] in sequence or [2, 3, 4, 5] in sequence or [3, 4, 5, 6] in sequence
					
			elif choice.lower() == str('large straight'):
			elif choice.lower() == str('chance'):
			else:
				input("\nThat's not a valid Combo! Try again... (Press Enter)")
				choice_is_valid = False
				os.system('clear')

		return (valid, value)

	def stats(self):
		self.score = self.aces + self.twos + self.threes + self.fours + self.fives + self.sixes + self.threekind 
		+ self.fourkind + self.fullhouse + self.smstraight + self.lgstraight + self.yahtzee
		print('Yahtzee: ')
		print('-------------------------')
		print('Aces: '+str(self.nice)+)
		print('Twos: ' +str(self.humor)+)
		print('Threes: ' +str(self.salty)+)
		print('Fours: ' +str(self.mad)+)
		print('Fives: '+str(self.nice)+)
		print('Sixes: ' +str(self.humor)+)
		print('3 of a Kind: ' +str(self.salty)+)
		print('4 of a Kind: ' +str(self.mad)+)
		print('Full House: ' +str(self.salty)+)
		print('Small Straight: ' +str(self.mad)+)
		print('Large Straight: ' +str(self.salty)+)
		print('YAHTZEE: ' +str(self.mad)+)
		print('Chance: ' +str(self.salty)+)
		print('-------------------------')
		print('Total: '+self.score+'')
		print('Quote: Ask Ventre for a quote on how he feels.')
		print('Conduct: Play for Maestro Ventre to improve (or worsen) his mood!')
		print('Nothing: Or play for him another day...')
		print('-------------------------')


input('Roll which dice?: ')


print('A:'+a+'')