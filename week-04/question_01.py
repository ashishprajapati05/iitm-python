# List Comprehension Exercises
# These exercises will help you build the basics of list comprehensions.

# sum_of_squares – Find the sum of the squares of all numbers in a list.
# Concept: Mapping and aggregation.
# total_cost – Given the quantity and price of each item as a list of tuples, find the total cost using list comprehensions.
# abbreviation – Given a string containing multiple words separated by spaces, form an abbreviation by taking the first letter of each word and converting it to uppercase.
# Concept: Mapping and aggregation.
# palindromes – Given a list of strings, create a new list containing only the palindrome strings.
# Concept: Filtering.
# all_chars_from_big_words – Find all unique characters (case-insensitive, convert all to lowercase) from words whose length is greater than 5 in a sentence.
# Input: A sentence with words separated by spaces.
# Concept: Filtering.
# flatten – Flatten a nested list into a single list using list comprehension.
# unflatten – Given a flat list and the required number of rows, create a matrix (2D list) with that number of rows.
# Concept: Nested aggregation.
# make_identity_matrix – Create an identity matrix (ones on the main diagonal and zeros elsewhere) of the given size.
# make_lower_triangular_matrix – Given the number of rows m, create a lower triangular matrix as shown below.
# Example: For m = 5

# [
#   [1,0,0,0,0],
#   [1,2,0,0,0],
#   [1,2,3,0,0],
#   [1,2,3,4,0],
#   [1,2,3,4,5]
# ]



def sum_of_squares(numbers):
    return sum(x*x for x in numbers)

def total_cost(cart):
    return sum(price * qty for price, qty in cart) 

def abbreviation(sentence):
    return ".".join(word[0].upper() for word in sentence.split()) + "."

def palindromes(words):
    return[word for word in words if word == word [::-1]]

def all_chars_from_big_words(sentence):
    return {ch for word in sentence.split() if len(word) > 3 for ch in word.lower()}

def flatten(lol):
    return[item for sublist in lol for item in sublist]

def unflatten(items, n_rows):
    return [items[i:i + len(item)//n_rows] for i in range(0, len(items), len(items)//n_rows)]

def make_identity_matrix(m):
    return [[1 if i == j else 0 for j in range(m)] for i in range(m)]

def make_lower_triangular_matrix(m):
    return [[j + 1 if j <= i else 0 for j in range (m)] for i in range(m)] 
