# Implement all the given functions that are used to solve the below problems.

# Follow the path

# You are given a matrix of size m x n consisting of ones (1) and zeros (0). There is a single continuous path formed with ones that starts from the rightmost cell in the last row (m-th row) with one and ends at leftmost cell in the first row with one in it. The path does not branch, and there is only one such path. Your task is to traverse along the path and print the coordinates of the path from start to end as tuples over multiple lines. The path can move vertically and horizontally.

# Input

# matrix = [
#     [0, 0, 1, 1],
#     [0, 0, 0, 1],
#     [1, 1, 1, 1],
#     [1, 0, 0, 0],
#     [1, 1, 0, 0]
# ]
# Output

# (4,1)
# (4,0)
# (3,0)
# (2,0)
# (2,1)
# (2,2)
# (2,3)
# (1,3)
# (0,3)
# (0,2)
# Alternate the path Same setup, but while going in that path, flip every ones in the even position in the path to 2. Modify the matrix inplace.

# Output

# [
#     [0, 0, 2, 1],
#     [0, 0, 0, 2],
#     [2, 1, 2, 1],
#     [1, 0, 0, 0],
#     [2, 1, 0, 0]
# ]
# Count the path Same setup, but instead of flipping put the count of the step in the path. Modify the matrix inplace.

# Output

# [
#     [0, 0, 10, 9],
#     [0, 0, 0, 8],
#     [4, 5, 6, 7],
#     [3, 0, 0, 0],
#     [2, 1, 0, 0]
# ]
# Mirror the path horizontally Same setup, but also add a path that is the horizontal mirror of the original path in the same matrix.

# Input

# [
#   [0,1,0,0,0],
#   [0,1,1,1,0],
#   [0,0,0,1,0],
#   [0,0,0,1,1]
# ]
# Output

# [
#   [0,1,0,1,0],
#   [0,1,1,1,0],
#   [0,1,0,1,0],
#   [1,1,0,1,1]
# ]
# Mirror the path vertically Same setup, but also add a path that is the vertical mirror of the original path in the same matrix.

# Input

# [
#   [0,1,0,0,0],
#   [0,1,1,1,0],
#   [0,0,0,1,0],
#   [0,0,0,1,1]
# ]
# Output

# [
#   [0,1,0,1,1],
#   [0,1,1,1,0],
#   [0,1,1,1,0],
#   [0,1,0,1,1]
# ]



def index_of_first_occurance(row:list,elem):
    '''
    Given a list find the index of first occurance of 1 in it
    '''
    return row.index(elem) 

def index_of_last_occurance(row:list,elem):
    '''
    Given a list find the index of last occurance of 1 in it.
    Hint: use index_of_first_one with reversal.
    '''
    return len(row) - 1 - row[::-1].index(elem)

def is_valid_coordinate(x:int,y:int, M):
    '''
    Checks if the x,y is a valid corrdinate(indices) in th matrix M(list of list). Assume coordinates are non-negative
    '''
    return 0 <= x < len(M) and 0 <= y < len(M[0])

def valid_adjacent_coordinates(x:int, y:int, M):
    '''
    Create a set of valid adjacent coordinates(indices) given x,y and a matrix M
    '''
    return {
      (x1, y1)
      for x1, y1 in [
          (x - 1, y),
          (x + 1, y),
          (x, y - 1),
          (x, y + 1)
     ] # all the possible adjacent coordinates
      if is_valid_coordinate(x1, y1, M)
    }

def next_coordinate_with_value(curr_coords, value, M, prev_coords=None):
    '''
    Find the coordinate(indices) of the next coordinate that has the `value` in it. For the starting coordinate the prev_coords would be None
    '''
    for coord in valid_adjacent_coordinates(curr_coords[0], curr_coords[1], M):
        if coord != prev_coords and M[coord[0]][coord[1]] == value:
            return coord
    return None        

def get_path_coordinates(M):
    '''
    Given the matrix m, find the path formed by 1 from the last row to the first row.
    '''
    x_start, x_end = len(M)-1,0
    y_start, y_end = index_of_last_occurance(M[-1],1), index_of_first_occurance(M[0],1)
    
    curr = (x_start, y_start)
    prev = None
    
    path = []
    
    while curr is not None:
        path.append(curr)
        
        if curr == (x_end, y_end):
            break
        
        nxt = next_coordinate_with_value(curr, 1, M, prev)
        prev = curr
        curr = nxt
        
    return path    

def print_path(M):
    path = get_path_coordinates(M)
    for coord in path:
        print(coord)

def alternate_path(M):
    path = get_path_coordinates(M)
    
    for i, (x, y) in enumerate(path):
        if i % 2 == 1:
            M[x][y] = 2

def count_path(M):
    path = get_path_coordinates(M)
    
    for i, (x, y) in enumerate(path, start=1):
        M[x][y] = i

def mirror_horizontally(M):
    path = get_path_coordinates(M)
    cols = len(M[0])
    for x, y in path:
        M[x][cols - 1 - y] = 1

def mirror_vertically(M):
    path = get_path_coordinates(M)
    row = len(M)
    
    for x, y in path:
        M[row - 1 - x][y] = 1
