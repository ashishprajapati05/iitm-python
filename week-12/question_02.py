# Accept two positive integers 

# a and b as arguments and print a rectangular pattern that has 
# a lines. The first and last line should have 
# b stars, all other lines should have exactly two stars that are aligned with either end of the rectangle. You can assume that 

# a,b≥2 for all test cases.

# Test cases (1) and (3) are misleading. Due to a formatting issue, the spaces are not represented properly. This is how you have to print it.

# Test-Case-1

# oooo
# o  o
# oooo

# Test-Case-3

# ooooooo
# o     o
# o     o
# ooooooo

# ans

a = int(input())
b = int(input())

print("o" * b)

for i in range(a - 2):
    print("o" + " " * (b - 2) + "o")

print("o" * b)

