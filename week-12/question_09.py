# Task
# Write a function named pearson that accepts two vectors, 
# X
# X and 
# Y
# Y, as arguments and returns their Pearson correlation coefficient.

# Implementation Details
# Helper Functions: Several helper functions are already defined in the prefix code. You can complete this task by using only these pre-defined functions. This exercise will help you learn how to work with external libraries in future projects.
# Input and Output: You do not need to handle user input or print results to the console. Write only the function definition.

def f(P):
    mean = sum(P) / len(P)
    return [p - mean for p in P]

def g(P, Q):
    return sum(P[i] * Q[i] for i in range(len(P)))

def h(x):
    return x ** 0.5

def pearson(X, Y):
    A = f(X)
    B = f(Y)
    return g(A, B) / (h(g(A, A)) * h(g(B, B)))