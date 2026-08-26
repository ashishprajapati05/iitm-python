# Find largest sub sequence with the antakshari property
# The input is in multiple lines. The first line contains a positive integer n. This is followed by n lines, each containing sequences of words. Each line thus consists of multiple words, separated by commas, with no spaces in between words.

# You have to output, for each line, the length of the longest subsequence of words following the antakshari property.

# Assume all words are lowercase.

# A sub-sequence is a subset of consecutive words in this sequence.

# A sub-sequence is said to have the antakshari property if the last letter of every word is equal to the first letter in the next word in the sequence.

# Input Format

# The first line contains an integer n denoting the number of sequences.
# The following n lines each contain a sequence of comma-separated words.
# Output Format For each sequence, output the length of the largest sub-sequence that follows the antakshari property over multiple lines.

# Example

# Input:

# 2
# one,two,order,real,long,tight,tree,cool,lot,trouble
# ant,tree,ear,rat,tower,retail
# Output:

# 4
# 6
# Explanation

# For the first sequence one,two,order,real,long,tight,tree,cool,lot,trouble, the longest sub-sequence with the antakshari property is two,order,real,long, which has a length of 4.

# For the second sequence ant,tree,ear,rat,tower,retail, the longest sub-sequence with the antakshari property is ant,tree,ear,rat,tower,retail, which has a length of 6.


# Take the input from standard input using input()
# and print the output according to the problem .

# Write your code here

n = int(input())
for _ in range(n):
    words = input().split(",")
     
    current = 1
    maximum = 1
     
    for i in range(len(words) - 1):
        if words[i][-1] == words[i + 1][0]:
             current += 1
             maximum = max(maximum, current)
        else:
            current = 1
    print(maximum)        