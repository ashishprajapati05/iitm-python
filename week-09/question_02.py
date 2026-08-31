# Write a recursive function named linear that accepts the following arguments:

# P: a non-empty list of positive integers
# Q: a non-empty list of positive integers
# k: a positive integer
# It should return True only if both the conditions given below are satisfied:

# P
# P and 
# Q
# Q are of same length.
# P
# [
# i
# ]
# =
# k
# ⋅
# Q
# [
# i
# ]
# P[i]=k⋅Q[i], for every integer 
# i
# i in the range 
# [
# 0
# ,
# len
# (
# P
# )
# −
# 1
# ]
# [0,len(P)−1], endpoints inclusive.
# You do not have to accept input from the user or print output to the console. You just have to write the function definition.



def linear(P, Q, k):
    """
    A recursive function to determine if a list is scalar multiple of the other

    Arguments:
        P: list of integers
        Q: list of integers
        k: integer
    Return:
        result: bool
    """
    if not P:
        return True
    return len(P) == len(Q) and P[0] == k * Q[0] and linear(P[1:], Q[1:],k)    