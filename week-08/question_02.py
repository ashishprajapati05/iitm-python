# You are given two non-empty text files file1 and file2 that have 
# f
# 1
# f 
# 1
# ​
#   and 
# f
# 2
# f 
# 2
# ​
#   lines respectively. Each file is a collection of ten-digit phone numbers, one number per line. It is also known that 
# 0
# <
# f
# 1
# ≤
# f
# 2
# 0<f 
# 1
# ​
#  ≤f 
# 2
# ​
#  .

# The following relations are defined on these two files:

# Subset: file1 is a subset of file2 if the phone number in the 
# i
# t
# h
# i 
# th
#   line of file1 is equal to the number in the 
# i
# t
# h
# i 
# th
#   line of file2, for 
# 1
# ≤
# i
# ≤
# f
# 1
# 1≤i≤f 
# 1
# ​
#  , and 
# f
# 1
# <
# f
# 2
# f 
# 1
# ​
#  <f 
# 2
# ​
#  .
# Equal: file1 is equal to file2 if the phone number in the 
# i
# t
# h
# i 
# th
#   line of file1 is equal to the number in the 
# i
# t
# h
# i 
# th
#   line of file2 for 
# 1
# ≤
# i
# ≤
# f
# 1
# 1≤i≤f 
# 1
# ​
#  , and 
# f
# 1
# =
# f
# 2
# f 
# 1
# ​
#  =f 
# 2
# ​
#  .
# Write a function named relation that accepts these two text files as arguments. It should return the string Subset if file1 is a subset of file2. It should return Equal if file1 is equal to file2. If both these conditions are not satisfied, it should return the string No Relation.

# (1) file1 and file2 are string variables that hold the names of the two files. For example, in the first test case, it is file1 = 'public_1_1.txt' and file2 = 'public_1_2.txt'.

# (2) You do not have to accept input from the console or print the output to the console. You just have to write the function definition.

# (3) The strings '9876543210' and '9876543210\n' are not the same, though the phone numbers are the same. So, strip the strings of all new lines using the strip method before checking for equality of two lines across the files.



def relation(file1, file2):
    """
    Determine the relationship between two files

    Arguments:
        file1, file2: strings, paths to two files
    Return:
        string: 'Equal', 'Subset' or 'No Relation'
    """
    
    with open (file1, "r") as f1:
        lines1 = [line.strip() for line in f1]
        
    with open(file2, "r") as f2:
        lines2 = [line.strip() for line in f2]
        
    if lines1 == lines2[:len(lines1)]:
        if len(lines1) == len(lines2):
            return "Equal"
        else:
            return "Subset"
    return "No Relation"        
    