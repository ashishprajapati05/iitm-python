# Consider a grid-world of size 
# n
# ×
# n
# n×n. You are at the bottom-left corner, at the cell 
# (
# 1
# ,
# 1
# )
# (1,1), to start with. A sample grid-world for the case of 
# n
# =
# 5
# n=5 is given below for your reference:



# You can move one step at a time in any one of the four directions: "North", "East", "West", "South". At every cell of the grid, all four moves are possible. The only catch is that if you make a move that will take you out of the grid at a border cell, you will stay put at the same cell. Concretely, if you are at the cell 
# (
# 1
# ,
# 4
# )
# (1,4) and try to move west, you will remain at the same cell. Or if you are at 
# (
# 3
# ,
# 1
# )
# (3,1) and try to move south, you will remain there.

# Write a function named final that accepts a positive integer 
# n
# n and a sequence of moves (string) as arguments and returns the final position where you would end up in an 
# n
# ×
# n
# n×n grid-world if you start at 
# (
# 1
# ,
# 1
# )
# (1,1). You must return a tuple of size 2, where the first element is the x-coordinate and the second is the y-coordinate.

# You do not have to accept input from the user or print output to the console. You just have to write the function definition.

def final(n, moves):
    x = 1
    y = 1

    for m in moves:
        if m == "N" and y < n:
            y += 1
        elif m == "S" and y > 1:
            y -= 1
        elif m == "E" and x < n:
            x += 1
        elif m == "W" and x > 1:
            x -= 1

    return (x, y)