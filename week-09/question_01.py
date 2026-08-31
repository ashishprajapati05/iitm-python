# Write a recursive function named reverse that accepts a list L as argument and returns the reversed list.

# You do not have to accept input from the user or print output to the console. You just have to write the function definition.

def reverse(L):
    """
    A recursive function to reverse a list L

    Arguments:
        L: list, type of elements could be anything
    Return:
        result: list
    """
    if len(L) == 0:
        return []
        
    return reverse(L[1:]) + [L[0]]    