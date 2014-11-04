sudoku_solver
=============
For algorithm description, see sudoku_solver.py.

__Usage__

  > python solve_sudoku.py input_sudoku_puzzle output_solved_puzzle
 
  where input_sudoku_puzzle is an existing file and output_solved_puzzle                                                                                                                                      
  will be overwritten by the final solution               

__Example 1 (From Problem Definition)__

___Input File___:

0,3,5,2,9,0,8,6,4
0,8,2,4,1,0,7,0,3
7,6,4,3,8,0,0,9,0
2,1,8,7,3,9,0,4,0
0,0,0,8,0,4,2,3,0
0,4,3,0,5,2,9,7,0
4,0,6,5,7,1,0,0,9
3,5,9,0,2,8,4,1,7
8,0,0,9,0,0,5,2,6

___Output File___

1,3,5,2,9,7,8,6,4
9,8,2,4,1,6,7,5,3
7,6,4,3,8,5,1,9,2
2,1,8,7,3,9,6,4,5
5,9,7,8,6,4,2,3,1
6,4,3,1,5,2,9,7,8
4,2,6,5,7,1,3,8,9
3,5,9,6,2,8,4,1,7
8,7,1,9,4,3,5,2,6

__Example 2 (All Zeros)__

___Input File___:

0,0,0,0,0,0,0,0,0
0,0,0,0,0,0,0,0,0
0,0,0,0,0,0,0,0,0
0,0,0,0,0,0,0,0,0
0,0,0,0,0,0,0,0,0
0,0,0,0,0,0,0,0,0
0,0,0,0,0,0,0,0,0
0,0,0,0,0,0,0,0,0
0,0,0,0,0,0,0,0,0

___Output File___

1,2,3,4,5,6,7,8,9
4,5,6,7,8,9,1,2,3
7,8,9,1,2,3,4,5,6
2,1,4,3,6,5,8,9,7
3,6,5,8,9,7,2,1,4
8,9,7,2,1,4,3,6,5
5,3,1,6,4,2,9,7,8
6,4,2,9,7,8,5,3,1
9,7,8,5,3,1,6,4,2

