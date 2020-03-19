# Puzzles_LightOutPuzzle
It also Include N_Queen Puzzle and Linear Disk Puzzle. But GUI not included for N_Queen and Linear Disk.

# Instruction
use cmd in the location of the py files, enter:\
# python homework2_lights_out_gui.py rows cols\
Light Out Puzzle Game good to play!

# Rules
1. Light Out Puzzle\
The Lights Out puzzle consists of an m x n grid of lights, each of which has two
states: on and off. The goal of the puzzle is to turn all the lights off, with the
caveat that whenever a light is toggled, its neighbors above, below, to the left,
and to the right will be toggled as well. If a light along the edge of the board is
toggled, then fewer than four other lights will be affected, as the missing
neighbors will be ignored.

2. N_Queens\
N queens are to be placed on an n x n chessboard so that no pair of queens can
attack each other. Recall that in chess, a queen can attack any piece that lies in
the same row, column, or diagonal as itself.

3. Linear Disk\
The starting configuration of this puzzle is a row of L cells, with disks located on
cells 0 through n - 1. The goal is to move the disks to the end of the row using a
constrained set of actions. At each step, a disk can only be moved to an adjacent
empty cell, or to an empty cell two spaces away, provided another disk is located
on the intervening cell. Given these restrictions, it can be seen that in many
cases, no movements will be possible for the majority of the disks. For example,
from the starting position, the only two options are to move the last disk from
cell n - 1 to cell n, or to move the second-to-last disk from cell n - 2 to cell n.
