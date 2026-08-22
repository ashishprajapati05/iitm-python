# Accept a positive integer 
# n
# n as input and print the sum of the first 
# n
# n terms of the series given below:

# 1+(1+2)+(1+2+3)+(1+2+3+4)+ ⋯
# 1+(1+2)+(1+2+3)+(1+2+3+4)+⋯
# Just to be clear, the first term in the series is 
# 1
# 1, the second term is (1+2)
# (1+2) and so on.

n = int(input())

total = 0
s = 0

for i in range(1, n + 1):
    s = s + i
    total = total + s
    
print(total)    
