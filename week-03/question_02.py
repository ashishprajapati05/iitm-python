# Accept a positive integer 
# n, with 
# n>1, as input from the user and print all the prime factors of 
# n in ascending order.


n = int(input())

i = 2

while i <= n:
    if n % i == 0:
        print(i)
        while n % i == 0:
            n = n // i
    i += 1        