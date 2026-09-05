# Divide Number Into Almost Equal Parts
# Write a function divide_into_almost_equal_parts(n: int, k: int) -> list that takes two integers, n and k, and creates a list of size k where the elements are approximately equal and sum up to n. The list should contain larger numbers towards the beginning.

# The larger numbers should be prioritized for the earlier parts of the list, and you should ensure that the sum of the list matches n.

# Constraints

# The integers n (total) and k (parts) are both positive integers.
# The output list will always be of length k.



def divide_into_almost_equal_parts(n: int, k: int) -> list:
    '''
    Given two integers n and k, return a list of size k 
    such that the values are almost equal and their sum is n. 
    Larger numbers should appear earlier in the list.

    Examples:
    >>> divide_into_almost_equal_parts(5, 3)
    [2, 2, 1]
    >>> divide_into_almost_equal_parts(16, 3)
    [6, 5, 5]
    >>> divide_into_almost_equal_parts(12, 4)
    [3, 3, 3, 3]
    >>> divide_into_almost_equal_parts(10, 3)
    [4, 3, 3]

    Args:
        n (int): Total number to be divided
        k (int): Number of parts

    Returns:
        list: A list of size k with values summing to n
    '''
    
    
    q, r = divmod(n, k)
    return [q+1] * r + [q] * (k-r)
    
