import sys
import sudoku_puzzle_io
import sudoku_solver

"""
  commandline executable to run the sudoku solver.

  usage:
   > python solve_sudoku.py <input_sudoku_puzzle> <output_solved_puzzle>

   where input_sudoku_puzzle is an existing file and output_solved_puzzle
   will be overwritten by the final solution
"""

def main(args):
  puzzle_input_fn = args[0]
  solution_output_fn = args[1]
  puzzle_def = sudoku_puzzle_io.load_puzzle(puzzle_input_fn)
  solution = sudoku_solver.solve_puzzle(puzzle_def)
  sudoku_puzzle_io.dump_puzzle(solution, solution_output_fn)
  return

if __name__ == '__main__':
  main(sys.argv[1:])
