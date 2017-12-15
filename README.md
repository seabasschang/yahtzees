# Yahtzee


## Yahtzee Group:
Will G. and Sebastian

#### D = Dice():   S.C.
Dice class that holds all five dice as values, essentially the current state of all dice.

##### d.value:
Returns the values of the di as a tuple: (Dice A, Dice B, Dice C...)

##### d.roll(rollnum):
Rolls dice by generating "randint(1, 6)". This is based on a list "rollnum", that designates which dice are to be rolled (ex. for a list (a, b, d), Dice A, B, and D will be rolled.)


#### B = Board():  S.C.
Class that holds current scoreboard values, essentially the current state of the game.

##### B.check(dicestate):
Checks the current dice in list "dicestate" to see if it satisfies a specified combo. (ex. Does (5, 5, 5, 2, 3) satisfy "Three of a Kind"?)

#####B.stats():
Displays the stats of the board and calculates the current score by adding all the attributes together.


#### S = Button1(): W.G.
Class that stores a button and values relating to Tkinter button, allowing the user to select and click the buttons, which represent the dice.

##### S.select():
Selects and unselects buttons, changing its appearance to reflect its state. This will later designate which dice will be re-rolled.

#### R = Button2(): W.G.
Class for the button which allows the player to re-roll the selected dice.

##### R.active():
Sends the re-roll command and updates the display.









 