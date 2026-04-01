 Sudoku as a Constraint Satisfaction Problem (CSP)

Problem

A Sudoku consists of a 9×9 grid with some cells already filled (digits 1–9). The task is to fill the remaining cells such that:

No digit repeats in any row
No digit repeats in any column
No digit repeats in any 3×3 box

Each row, column, and box is called a unit.

CSP Formulation
Variables

Each cell in the grid is a variable (total 81 variables)

Example:
A1, A2, ..., I9

Domains

Each variable can take values from:
{1, 2, 3, 4, 5, 6, 7, 8, 9}

For already filled cells, the domain has only one value.

Constraints
Row constraint
No two cells in the same row can have the same number

Column constraint
No two cells in the same column can have the same number

Box constraint
No two cells in the same 3×3 subgrid can have the same number
Approach Used

Backtracking search:

Select an empty cell
Assign a number from domain
Check all constraints (row, column, box)
If valid, continue
If not, try next value
If no value works, backtrack