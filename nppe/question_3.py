# Position of a Point Relative to a Line
# Note: This question will be evaluated using an evaluation script and not based on the provided test cases. The test cases shown are only for illustration. Your solution should work correctly for all valid inputs according to the problem specification.
# Write a function point_position_relative_to_line(a, b, c, x, y) -> int that determines the position of a point (x, y) with respect to a line described by the equation ax + by + c = 0.

# The function should return:

# +1 if the point is above the line
# -1 if the point is below the line
# 0 if the point is on the line


def point_position_relative_to_line(a, b, c, x, y) -> int:
    value = a * x + b * y + c

    if value > 0:
        return 1
    elif value < 0:
        return -1
    else:
        return 0