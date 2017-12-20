# Yahtzee The Very Good Game:
Will G. and Sebastian

## Description
A class-oriented game inspired by Yahtzee, featuring an updating scoreboard which checks the validity and value of certain dice combinations and an interactive Tkinter dice roller. 

![](http://famfonts.com/wp-content/uploads/yahtzee-wide.png)
## Classes
#### D = Dice():   W.G.
Dice class that holds its value.

- d.roll():
Rolls dice by generating "randint(1, 6)". 

- returnState():
Iterates through all 5 dice and returns their values as a list

#### B = Board():  S.C.
Class that holds current scoreboard values, essentially the current state of the game.

- B.check(dicestate):
Checks the current dice in list "dicestate" to see if it satisfies a specified combo, as well as calculating the resulting score and other features like the Yahtzee bonuses. (ex. Does (5, 5, 3, 2, 5) satisfy "Three of a Kind"?)

- B.stats():
Displays all the stats of the board and calculates the current score by adding all the attributes together.

#### S = Button1(): W.G.
Class that stores a button and values relating to Tkinter button, allowing the user to select and click the buttons, which represent the dice.

- S.select():
Selects and unselects buttons, changing its appearance to reflect its state. This will later designate which dice will be re-rolled.

#### R = Button2(): W.G.
Class for the button which allows the player to re-roll the selected dice.

- R.active():
Sends the re-roll command and updates the display.









 
