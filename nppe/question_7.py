# Visualize Pattern Lock
# Given a sequence of numbers representing the order in which dots are connected in a 3×3 pattern lock, generate a text-based visualization of the pattern. Dots should be marked in the order they were visited, with all others left blank ([ ]).

# Dot layout and numbering

# The 3×3 grid is numbered as follows:

# [1]---[2]---[3]
#  |     |     |
# [4]---[5]---[6]
#  |     |     |
# [7]---[8]---[9]
# Input Format

# A single line containing a space-separated sequence of integers (1–9), representing the order of dots visited.
# The input will be a valid pattern lock.
# Output Format

# A visual 3×3 grid (text format) with visited positions replaced by [n] where n is the order in which that dot was visited (starting from 1).
# Unvisited positions should be shown as [ ].
# The layout and spacing must match the dot layout shown above.
# There is no space at the end of each line while displaying the pattern.
# Sample Input

# 2 5 7 4 1
# Sample Output

# [5]---[1]---[ ]
#  |     |     |
# [4]---[2]---[ ]
#  |     |     |
# [3]---[ ]---[ ]






p = [' ']*9

for i, cell in enumerate(input().split(),1):
    p[int(cell) - 1] = i 

break_line = " |     |     |"
def dot_line(vals):
    return "---".join(f"[{val}]" for val in vals)

print(dot_line(p[:3]))
print(break_line)
print(dot_line(p[3:6]))
print(break_line)
print(dot_line(p[6:]))

