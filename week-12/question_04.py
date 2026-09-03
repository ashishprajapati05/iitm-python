# Write a function named std_dev that accepts a list of real numbers 
# X
# X as argument. It should return the standard deviation of the points given by the following formula:

# σ
# =
# ∑
# i
# =
# 0
# n
# −
# 1
# (
# X
# i
# −
# X
# ˉ
# )
# 2
# n
# −
# 1
# X. Try to use list-comprehension wherever possible. However, we won't be evaluating you on this.

# You do not have to accept the input from the user or print output to the console. You just have to write the function definition.

def std_dev(X):
    m = sum(X) / len(X)
    return (sum((x - m) ** 2 for x in X) / (len(X) - 1)) ** 0.5