A More Strategic Version of Tic-Tac-Toe.

Imagine a 3x3 grid of tictactoe boards:

0.0 0.1 0.2 | 1.0 1.1 1.2 | 2.0 2.1 2.2
0.3 0.4 0.5 | 1.3 1.4 1.5 | 2.3 2.4 2.5
0.6 0.7 0.8 | 1.6 1.7 1.8 | 2.6 2.7 2.8
---------------------------------------
3.0 3.1 3.2 | 4.0 4.1 4.2 | 5.0 5.1 5.2
3.3 3.4 3.5 | 4.3 4.4 4.5 | 5.3 5.4 5.5
3.6 3.7 3.8 | 4.6 4.7 4.8 | 5.6 5.7 5.8
---------------------------------------
6.0 6.1 6.2 | 7.0 7.1 7.2 | 8.0 8.1 8.2
6.3 6.4 6.5 | 7.3 7.4 7.5 | 8.3 8.4 8.5
6.6 6.7 6.8 | 7.6 7.7 7.8 | 8.6 8.7 8.8


START - Player X chooses any spot on the board.
1. Switch players 
    2a. could use boolean player: True='X', False='O' using player = -player to toggle
2. Player chooses a spot in the corresponding section
    ex. if X went in 3.2, then O goes in 2.x
3. If there's a win on any board, then disable it and change its color to identify (X=blue, O=red)
    3a. Check if there's a win across all the boards (ex. boards 0, 3, 6 would be game over)

IDEA: Make a Board class and have objects of these as the 9 sections of the game.
- When you press a button, you are calling the method of the Board class changing its symbol.
- It would have methods like win() which would disable the buttons and change colors
- It would have accessor methods for the win state so we can check if it's game over

Extensions:
1. Add a menu bar to reset the game board
2. Somehow use pictures as the buttons to make it look nicer
3. **AMBITIOUS** make a 1-player mode with some kind of AI that you play against



NOTES:
Try to make a way to highlight the buttons that are available to click. FRAME BORDERS
Make the button text bigger too.