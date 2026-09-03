# Note: This question will be evaluated using an evaluation script .

# Write a function named primes_galore that accepts a list L of non-negative integers as argument and returns the number of primes that are located at prime indices in L.

# For example:

# L = [1, 3, 11, 18, 17, 23, 6, 8, 10]

# The prime indices in the list are 

# 2,3,5,7. Of these, there are prime numbers at the indices and 
# Therefore, the function should return the value  in this case.

# You do not have to accept input from the user or print the output to the console. You just have to write the function definition.

# To view a worked out version of this problem, play the below video:



# ans
def primes_galore(L):
    def prime(n):
        return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

    return sum(prime(i) and prime(x) for i, x in enumerate(L))
