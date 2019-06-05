This is a Sudoku Puzzle solver. Written in Python using the Tkinter library for the GUI. 

Rules for the puzzle, from http://www.counton.org/sudoku/rules-of-sudoku.php...

"The classic Sudoku game involves a grid of 81 squares. The grid is divided into nine blocks, each containing nine squares.

The rules of the game are simple: each of the nine blocks has to contain all the numbers 1-9 within its squares. Each number can only appear once in a row, column or box.

The difficulty lies in that each vertical nine-square column, or horizontal nine-square line across, within the larger square, must also contain the numbers 1-9, without repetition or omission.

Every puzzle has just one correct solution."

This program uses a backtracking algorithm to solve the puzzle. More info about the algorithm can be found at https://en.wikipedia.org/wiki/Sudoku_solving_algorithms#Backtracking

I can guarantee there are more bugs in here to count, but I will try to find most of them as I add more functionality to the program.


To launch the program, run the Main.py file. This will launch the GUI which lays out the puzzle board. By clicking each box, it increases the value which wraps around to an empty box after 9. There are 2 button, "start solving" and "clear puzzle". These are pretty self-explanatory.
