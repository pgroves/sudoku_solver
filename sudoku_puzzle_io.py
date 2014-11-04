from sudoku_puzzle import SudokuPuzzle
import csv

NINE = 9

def load_puzzle(filename):
  """
  utility method for loading a SudokuPuzzle from a csv file.
  zeros should be used to denote an 'unset' cell.
  """
  puzzle = SudokuPuzzle()
  with open(filename, 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    row_idx = 0
    for row in reader:
      col_idx = 0
      for col_str in row:
        col = int(col_str)
        if col > 0:
          puzzle.get_cell(row_idx, col_idx).fix_value(col)
        col_idx += 1
      row_idx += 1
  return puzzle

def dump_puzzle(puzzle, filename):
  """
  writes a (possibly solved) SudokuPuzzle to a csv file.
  If a cell has more than one possible value at the time
  this method is called, will write a '?' in that cell's 
  position.
  """
  with open(filename, 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for i in range(NINE):
      row_values = list()
      for j in range(NINE):
        cell = puzzle.get_cell(i, j)
        if cell.is_fixed():
          cell_token = str(cell.get_fixed_value())
        else:
          cell_token = '?'
        row_values.append(cell_token)
      writer.writerow(row_values)
  return
