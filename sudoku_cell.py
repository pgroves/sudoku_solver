
NINE = 9

class SudokuCell():
  """
  A single cell in a sudoku puzzle. Keeps track of possible values
  it can take on, as well as whether it has been 'fixed' (only 
  one possible value left).
  """

  def __init__(self, row_index, column_index):
    """
    row_index, column_index: int indices of where in the board
      this cell is located
    """
    self.possibilities = set([x + 1 for x in range(NINE)])
    self.row_index = row_index
    self.column_index = column_index
    return

  def fix_value(self, number_value):
    """
    Force the number of possibilities to exactly only the number_value
    """
    self.possibilities = set()
    self.possibilities.add(number_value)
    return
  
  def is_fixed(self):
    """
    True if only one possible value.
    """
    fixed = (len(self.possibilities) == 1)
    return fixed

  def get_possibilities(self):
    return self.possibilities

  def get_fixed_value(self):
    if self.is_fixed():
      #there is no peek() on sets in python?
      for x in self.possibilities:
        return x
    return None

  def remove_possibility(self, number_value):
    """
    Instruct the cell to not consider number_value as a potential value.
    Can safely be called with a number_value that is already not
    a possibility.
    """
    if number_value in self.possibilities:
      self.possibilities.remove(number_value)
      if len(self.possibilities) == 0:
        print('WARN: removed last possibility: ' + str(self) + ' value: ' + str(number_value))
      return True
    return False

  def is_same_location(self, other_cell):
    """
    equality based on board position only
    """
    same_row = (self.row_index == other_cell.row_index)
    same_col = (self.column_index == other_cell.column_index)
    same_location = (same_row and same_col)
    return same_location


  def copy(self):
    """
    deep copy
    """
    cell_copy = SudokuCell(self.row_index, self.column_index)
    cell_copy.possibilities = self.possibilities.copy()
    return cell_copy

  def location_str(self):
    s = str((self.row_index, self.column_index))
    return s

  def __str__(self):
    return self.location_str()
  
  def __repr__(self):
    return self.location_str()
