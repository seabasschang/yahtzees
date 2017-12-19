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
		self.chance = 0

	def check(self, dicestate, choice):
		#dicestate will be the list of dice values.
		#choice will be the combo to check for.
		#Checks if the current list of dice values satisfies a special combination.
		choice_is_valid = False
		while not choice_is_valid:
			choice_is_valid = True
			valid = False
			value = None
			if choice.lower() == 'aces' and self.aces == 0:
				if dicestate.count(1) >= 1:
					valid = False
					value = dicestate.count(1)
			elif choice.lower() == 'twos' and self.twos == 0:
				if dicestate.count(2) >= 1:
					valid = False
					value = dicestate.count(2)*2
			elif choice.lower() == 'threes' and self.twos == 0:
				if dicestate.count(3) >= 1:
					valid = False
					value = dicestate.count(3)*3
			elif choice.lower() == 'fours' and self.twos == 0:
				if dicestate.count(4) >= 1:
					valid = False
					value = dicestate.count(4)*4
			elif choice.lower() == 'fives' and self.twos == 0:
				if dicestate.count(5) >= 1:
					valid = False
					value = dicestate.count(5)*5
			elif choice.lower() == 'sixes' and self.twos == 0:
				if dicestate.count(6) >= 1:
					valid = False
					value = dicestate.count(6)*6							
			elif choice.lower() == str('three of a kind') or choice.lower() == str('3 of a kind') and self.threekind == 0:
				for n in range(1,7):
					if dicestate.count(n) >= 3:
						valid = True
						value = sum(dicestate)
						break
			elif choice.lower() == str('four of a kind') or choice.lower() == str('4 of a kind') and self.fourkind == 0:
				for n in range(1,7):
					if dicestate.count(n) >= 4:
						valid = True
						value = sum(dicestate)
						break
			elif choice.lower() == str('full house') and self.fullhouse == 0:
				for n in range(1,7):
					if dicestate.count(n) == 3:
						for d in range(1,7):
							if dicestate.count(d) == 2:						
								valid = True
								value = 25
								break
			elif choice.lower() == str('small straight') and self.smstraight == 0:
				sequence = ''.join(sorted(dicestate))
				if '1234' in sequence or '2345' in sequence or '3456' in sequence:
					valid = True
					value = 30
			elif choice.lower() == str('large straight') and self.lgstraight == 0:
				sequence = sorted(dicestate)
				if '12345' in sequence or '23456' in sequence:
					valid = True
					value = 40
			elif choice.lower() == str('yahtzee') and self.yahtzee == 0:
				for n in range(1,7):
					if dicestate.count(n) == 6:
						valid = True
						value = 50
						break
			elif choice.lower() == str('chance') and self.chance == 0:
				valid = True
				value = sum(dicestate)
			else:
				input("\nThat's not a valid Combo! Try again... (Press Enter)")
				choice_is_valid = False
				os.system('clear')

		return (valid, value)
		#Returns whether the combo itself is valid, whether the dice is valid as a combo, and the produced value.

	def stats(self):
		self.score = self.aces + self.twos + self.threes + self.fours + self.fives + self.sixes + self.threekind 
		+ self.fourkind + self.fullhouse + self.smstraight + self.lgstraight + self.yahtzee
		print('Yahtzee The Very Good Game')
		print('-------------------------')
		print('Aces: '+str(self.aces))
		print('Twos: ' +str(self.twos))
		print('Threes: ' +str(self.threes))
		print('Fours: ' +str(self.fours))
		print('Fives: '+str(self.fives))
		print('Sixes: ' +str(self.sixes))
		print('3 of a Kind: ' +str(self.threekind))
		print('4 of a Kind: ' +str(self.fourkind))
		print('Full House: ' +str(self.fullhouse))
		print('Small Straight: ' +str(self.smstraight))
		print('Large Straight: ' +str(self.lgstraight))
		print('YAHTZEE: ' +str(self.yahtzee))
		print('Chance: ' +str(self.chance))
		print('-------------------------')
		print('Total = '+str(self.score)+'')
		print('-------------------------')
