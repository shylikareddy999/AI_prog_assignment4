Australia Map Coloring using CSP
Aim

To solve the map coloring problem for Australian states using Constraint Satisfaction Problem (CSP) techniques, ensuring no two adjacent states have the same color.

Method / Approach

The solution uses backtracking:

Start with no assignments
Pick an unassigned state
Assign a color from the given list
Check if it conflicts with neighboring states
If valid, continue
If not, try another color
If no color works, backtrack
Data Used

States: WA, NT, SA, Q, NSW, V, T

Adjacency:

WA → NT, SA
NT → WA, SA, Q
SA → WA, NT, Q, NSW, V
Q → NT, SA, NSW
NSW → Q, SA, V
V → SA, NSW
T → none

Colors used: Red, Green, Blue

Output

The program prints a valid coloring of all states. Example:

Australia Map Coloring:
WA : Red
NT : Green
SA : Blue
Q : Red
NSW : Green
V : Red
T : Red

The output may vary since multiple valid solutions exist.

