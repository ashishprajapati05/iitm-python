# Accept a positive integer 
# n as input and print a "number arrow" of size 
# n. For example, 
# n=5 should produce the following output:

# 1
# 1,2
# 1,2,3
# 1,2,3,4
# 1,2,3,4,5
# 1,2,3,4
# 1,2,3
# 1,2
# 1

# You can assume that 
# n≥2 for all test cases.

n = int(input())

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == i:
            print(j, end="")
        else:
            print(j, end=",")
    print()
for i in range(n - 1, 0, -1):
    for j in range(1, i + 1):
        if j == i:
            print(j, end="")
        else:
            print(j, end=",")
    print()        