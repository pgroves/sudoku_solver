from sudoku_cell import SudokuCell

NINE = 9
THREE = 3

class SudokuPuzzle():
  """
  A sudoku puzzle board, made up of a 9X9 grid of SudokuCells.
  Provides access to information on the board and the cells.

  Also tracks 'cohorts', which are lists of 9 cells that must contain
  each number from [1,9]. Cohorts can be rows, column, or nonants (3x3 square
  representing 1/9 of the board).
  """

  def __init__(self):
    self.cell_ary = list()
    for i in range(NINE):
      row = list()
      for j in range(NINE):
        cell = SudokuCell(i, j)
        row.append(cell)
      self.cell_ary.append(row)
    return

  def get_cell(self, row_index, column_index):
    cell = self.cell_ary[row_index][column_index]
    return cell

  def get_cohort_row(self, row_index):
    cohort = list()
    for j in range(NINE):
      cohort.append(self.get_cell(row_index, j))
    return cohort

  def get_cohort_column(self, column_index):
    cohort = list()
    for i in range(NINE):
      cohort.append(self.get_cell(i, column_index))
    return cohort

  def get_cohort_nonant(self, row_index, column_index):
    """
    row_index, column_index can define any position on the board
    and this method will return the cohort it belongs to (this method
    will deduce the upper left corner of the nonant).
    """
    (origin_i, origin_j) = self._find_nonant_origin(row_index, column_index)
    cohort = list()
    for i in range(THREE):
      neighbor_i = origin_i + i
      for j in range(THREE):
        neighbor_j = origin_j + j
        cohort.append(self.get_cell(neighbor_i, neighbor_j))
    return cohort

  def is_complete(self):
    """
    True if every cell has exactly one possible value.
    """
    for row_index in range(NINE):
      cohort = self.get_cohort_row(row_index)
      if not (self._is_complete_cohort(cohort)):
        return False
    return True

  def has_contradiction(self):
    """
    True if any cohort has more than one value twice, or if
    any cell has zero possible values.
    """
    all_cohorts = list()
    for i in range(NINE):
      cohort = self.get_cohort_row(i)
      all_cohorts.append(cohort)
    for j in range(NINE):
      cohort = self.get_cohort_column(j)
      all_cohorts.append(cohort)
    for i in range(THREE):
      for j in range(THREE):
        cohort = self.get_cohort_nonant(i * 3, j * 3)
        all_cohorts.append(cohort)

    for cohort in all_cohorts:
      if self._cohort_has_contradiction(cohort):
        return True
    return False

  def copy(self):
    """
    deep copy
    """
    puzzle_copy = SudokuPuzzle()
    for i in range(NINE):
      for j in range(NINE):
        puzzle_copy.cell_ary[i][j] = self.cell_ary[i][j].copy()
    return puzzle_copy

  def _is_complete_cohort(self, cohort):
    """
    for a single cohort (list of cell), does every cell have a single
    possible value.
    """
    for cell in cohort:
      if not cell.is_fixed():
        return False
    return True

  def _cohort_has_contradiction(self, cohort):
    """
    for a single cohort (list of cell), is any value fixed to more
    than one cell, or does any cell have no possible valid values.
    """
    seen_values = set()
    for cell in cohort:
      if cell.is_fixed():
        value = cell.get_fixed_value()
        if value in seen_values:
          return True
        else:
          seen_values.add(value)
      else:
        if len(cell.get_possibilities()) == 0:
          return True
    return False

  def _find_nonant_origin(self, row_index, column_index):
    """
    given coordinates of any cell in the board, find the coordinates 
    of the upper left corner of it's nonant.

    returns a pair of ints: (nonant_origin_row, nonant_origin_col)
    """
    nonant_i = int(row_index / 3)
    nonant_j = int(column_index / 3)
    origin_i = THREE * nonant_i
    origin_j = THREE * nonant_j
    origin = (origin_i, origin_j)
    return origin
    
  def to_verbose_string(self):
    """
    string of all possible values of all cells, one cell per line
    """
    s = ''
    for i in range(NINE):
      for j in range(NINE):
        cell = self.get_cell(i, j)
        s += cell.location_str()
        s += ' possibilities = ' + str(cell.get_possibilities())
        s += '\n'
    return s

 
  
