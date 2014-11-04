
NINE = 9

def solve_puzzle(puzzle):
  """
  Solves a sudoko_puzzle. Any cells that have more than one possible
  value will have a fixed value when done.

  Uses a fairly brute force algorithm with 2 parts:
   1) removes all possibilities that are impossible given the cells' 
      cohorts (vertical, horizontal, nonant). see remove_all_impossibilities()
   2) if there are ambiguities after removing all impossibilities, will 
      recursively 'guess' a value for a cell from it's possible values, and
      try to solve again. 

  Returns a puzzle that is either complete and has no contradictions or None
  if no such puzzle exists given the state of the input puzzle.
  """
  puzzle = puzzle.copy()
  remove_all_impossibilities(puzzle)
  if puzzle.has_contradiction():
    return None
  elif puzzle.is_complete():
    return puzzle
  else:
    for row in range(NINE):
      for col in range(NINE):
        cell = puzzle.get_cell(row, col)
        if not cell.is_fixed():
          local_possibilities = cell.get_possibilities()
          for n in sorted(local_possibilities):
            candidate_puzzle = puzzle.copy()
            candidate_cell = candidate_puzzle.get_cell(row, col)
            candidate_cell.fix_value(n)
            solved_candidate = solve_puzzle(candidate_puzzle)
            if solved_candidate is not None:
              return solved_candidate
          return None #no valid solutions given our cell's possible values

def remove_all_impossibilities(puzzle):
  """
  iterates over all cells and removes all number values that already 
  exist in it's cohorts (row, column, or nonant) from the cell's 
  internal list of possibile values.
  continues until it passes over the entire puzzle without finding
  any possibilities to remove.

  operates on the input puzzle in place.
  """
  puzzle_was_modified = True
  while puzzle_was_modified:
    puzzle_was_modified = False
    for row in range(NINE):
      for col in range(NINE):
        cell = puzzle.get_cell(row, col)
        if not cell.is_fixed():
          cohorts = [
            puzzle.get_cohort_row(row),
            puzzle.get_cohort_column(col),
            puzzle.get_cohort_nonant(row, col)
          ]
          for cohort in cohorts:
            for cohort_cell in cohort:
              if(cohort_cell.is_fixed() and not (cohort_cell.is_same_location(cell))):
                impossible_value = cohort_cell.get_fixed_value()
                cell_was_modified = cell.remove_possibility(impossible_value)
                puzzle_was_modified = puzzle_was_modified or cell_was_modified
  return

