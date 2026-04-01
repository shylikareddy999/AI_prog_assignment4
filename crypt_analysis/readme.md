 Cryptarithmetic Puzzle using CSP

Problem

Solve the puzzle:

  T W O
+ T W O
--------
F O U R

Each letter represents a unique digit (0–9).

Conditions:

No two letters have the same digit
Leading letters (T, F) cannot be zero
The arithmetic equation must be correct
CSP Formulation
Variables

T, W, O, F, U, R

Domains

Each variable can take values from 0–9

Constraints
All letters must have different digits
T ≠ 0, F ≠ 0
2 × (TWO) = FOUR
Approach Used

Backtracking:

Assign digits to letters
Ensure all digits are unique
Check arithmetic condition
If valid, print solution
Otherwise, try next combination