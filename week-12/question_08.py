# Nesting Depth of Balanced Expressions
# Consider the problem about balanced expressions discussed in PPA-5. We have a balanced expression (string) that contains only the brackets (). We can recursively define a concept called nesting depth for each pair of opening and closing brackets.

# The nesting depth is defined as follows:

# For a pair of brackets that is not surrounded by any other pair, the nesting depth is 
# 1
# 1.
# The nesting depth of a pair that lies within another pair is one more than the nesting depth of the pair that immediately encloses it.
# Diagram illustrating the nesting depth of brackets

# Programming Task
# Write a function named depth that accepts a balanced expression (string) as an argument. It should return the maximum nesting depth in this expression.

# You do not need to accept input from the user or print output to the console. You only need to write the function definition.


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