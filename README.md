# NQueens-Puzzle-using-MiniSAT
Solving NQueens Puzzle using MiniSAT

Description:
===================
This program takes an integer 'n' as input(where 'n' signifies nXn chess board) and finds a solution to the n-queens problem by encoding it into SAT.

Instructions:
====================

Run the following command (assuming minisat is installed on the machine, put all files in the core folder of minisat):

"python nqueens.py"

Contents:
====================

The submission includes the following file:

nqueens.py
----------

This file will take 'n' as input from the user and then generate the required constraints for the SAT solver in a file (qin.cnf) which will be fed as input to the MiniSAT.

files generated by the program:
-------------------------------
qin.cnf: Contains all generated constraints

qout.txt: MiniSAT generated output

ans.txt: A Solution to N-Queens problem

Methodology:
====================
The program begins by taking 'n' as input from the user. It will generate the required constraints for the SAT solver in a file (qin.cnf) which will be fed as input to the MiniSAT. The SAT output gets outputted to the text file "qout.txt". The program will then parse the SAT generated output and then finally produce the solution to the problem, by outputting to the "ans.txt" file.
