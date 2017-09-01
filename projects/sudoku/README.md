# Diagonal Sudoku Solver

![](https://i.imgur.com/SJVEeg8.png)

![](https://i.imgur.com/PnCj7Pu.png)

The function (naked_twins) first looks for all boxes with only two values inside. The function then iterates over these boxes, finds all units the current box is a member of. Now having a box and a unit, the function looks for identical boxes. I a match is found, the boxes are called naked twins, and the values of this naked twins can be removed from all other boxes in the current unit.

One important note to make is that it is tempting to detect pairs in all boxes, and flag them as candidates, and process through them one at the time. It is important to chech if the box previously flagged as pair, can have been pruned down to a single value in an earlier naked twin detection. A last check if the box is still a pair is important.

