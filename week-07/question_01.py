# Find the index of the row with maximum number of zeros in a matrix
# Given a m x n matrix, find the index of the row with the maximum number of zeros. Assume there will be only one row with the maximum number of zeros.

# Example

# [
#     [1,0,1,4,1],
#     [1,5,1,1,2],
#     [2,0,2,0,3],
#     [3,0,0,0,4],
# ]
# The 4th row(index 3) has the maximum number of zeros, so the answer is 3.



def row_index_with_most_number_of_zeros(matrix:list)->int:
    '''
    Given a matrix, find the index of the row with the 
    maximum number of zeros in it.

    Arguments: matrix: list[list] 
    Rertun: int - index of the row with the maximum number of zeros.
    '''
    max_zeros = -1
    row_zeros = -1
    
    for i in range(len(matrix)):
        zeros = matrix[i].count(0)
        
        if zeros > max_zeros:
            max_zeros = zeros
            row_index = i
            
    return row_index        
    

