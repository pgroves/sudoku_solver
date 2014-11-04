import unittest
from sudoku_cell import SudokuCell
from sudoku_puzzle import SudokuPuzzle

class TestSudoku(unittest.TestCase):
  """
  Tests to spot check a few functions throughout this sudoku solver package.
  """

  def test_cell_fixing_value(self):
    cell = SudokuCell(5, 5)

    #init
    init_possibilities = cell.get_possibilities()
    self.assertEqual(9, len(init_possibilities))
    for x in [1,2,3,4,5,6,7,8,9]:
      self.assertTrue(x in init_possibilities)
    self.assertFalse(cell.is_fixed())
    self.assertTrue(cell.get_fixed_value() is None)


    #reducing possibilities
    for x in [1,2,3,4,5,6,7]:
      cell.remove_possibility(x)
    reduced_possibilities = cell.get_possibilities()
    self.assertEqual(2, len(reduced_possibilities))
    self.assertFalse(cell.is_fixed())
    self.assertTrue(cell.get_fixed_value() is None)
    for x in [8, 9]:
      self.assertTrue(x in reduced_possibilities)
      
    #fixed value via reduction
    cell.remove_possibility(8)
    fixed_possibilities = cell.get_possibilities()
    self.assertEqual(1, len(fixed_possibilities))
    self.assertTrue(cell.is_fixed())
    self.assertEquals(9, cell.get_fixed_value());

    #forced fixed value
    cell.fix_value(3)
    fixed_possibilities = cell.get_possibilities()
    self.assertEqual(1, len(fixed_possibilities))
    self.assertTrue(cell.is_fixed())
    self.assertEquals(3, cell.get_fixed_value());

    return

  def test_puzzle_get_nonant(self):
    puzzle = SudokuPuzzle()
    cohort00 = puzzle.get_cohort_nonant(0,0)
    obs_locations = list()
    for cell in cohort00:
      obs_locations.append(cell.location_str())
    exp_locations = [
      '(0, 0)', '(0, 1)', '(0, 2)', 
      '(1, 0)', '(1, 1)', '(1, 2)', 
      '(2, 0)', '(2, 1)', '(2, 2)'
      ]
    self.assertEqual(exp_locations, obs_locations)

    cohort88 = puzzle.get_cohort_nonant(8,8)
    print(str(cohort88))
    return
    obs_locations = list()
    for cell in cohort88:
      obs_locations.append(cell.location_str())
    exp_locations = [
      '(6, 6)', '(6, 7)', '(6, 8)', 
      '(7, 6)', '(7, 7)', '(7, 8)', 
      '(8, 6)', '(8, 7)', '(8, 8)'
      ]
    self.assertEqual(exp_locations, obs_locations)

    return



if __name__ == '__main__':
  unittest.main()
