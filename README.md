# Explorer-Maze-Escape in python 3
Given a map of the area (as a square grid), can you help the Explorer find the way from position [0,0] to the goal? The explorer can go right or down within in the grid, and cannot go through walls.

## Format
### Input
- n*n square consisting of 0's, 1's and one 9.
- 0's mark empty space.
- 1's are walls.
- 9 is the goal.

### Output
Return the (shortest) path to the goal. Return an array with each position  [x, y] in the path to the goal.