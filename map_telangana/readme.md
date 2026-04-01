 Telangana Map Coloring using CSP
Problem

The task is to color all 33 districts of Telangana such that no two neighboring districts have the same color.

Idea
Each district is treated as a variable
Each variable can take one of three colors: Red, Green, Blue
Adjacent districts must have different colors
Approach Used

Backtracking is used.

Steps:

Select an uncolored district
Assign a color
Check if it conflicts with neighbors
If valid, continue
If not, try another color
If no color works, backtrack
Graph Representation

The districts and their neighbors are stored in a dictionary.

Each district is mapped to a list of adjacent districts.