# Functions to Implement
# find_min: Find the minimum value in a list of integers.
# Input: A list of integers.
# Output: An integer representing the minimum value in the list.
# odd_increment_even_decrement_no_modify: Increment all odd numbers by 1 and decrement all even numbers by 1, without modifying the original list.
# Input: A list of integers.
# Output: A new list containing the modified values.
# odd_square_even_double_modify: Square all odd numbers and double all even numbers, modifying the input list in place.
# Input: A list of integers.
# Output: None (the input list is modified in place).
# more_than_two_unique_vowels: Given a string of comma-separated words, return a set containing words that have more than two unique vowels.
# Input: A string of comma-separated words.
# Output: A set of words with more than two unique vowels.
# sum_of_list_of_lists: Find the sum of all integers in a list of lists.
# Input: A list of lists of integers.
# Output: An integer representing the total sum.
# flatten: Flatten a list of lists into a single list.
# Input: A list of lists.
# Output: A single flattened list.
# all_common: Find the characters that are common to all strings in a list and return them as a string in ascending order.
# Input: A list of strings.
# Output: A string containing the common characters sorted in ascending order.
# vocabulary: Given a list of sentences (containing only alphabets and spaces), find the vocabulary (unique words). Convert all words to lowercase before adding them to the vocabulary.
# Input: A list of sentences.
# Output: A set of unique words in lowercase.  

# ans


min =  None

def find_min(items:list):
    smallest = items[0]
    for x in items:
        if x < smallest:
            smallest = x
    return smallest        

def odd_increment_even_decrement_no_modify(items) -> list:
    new = []
    for i in items:
        if i % 2 == 0:
            new.append(i - 1)
        else:
            new.append(i + 1)
    return new    

def odd_square_even_double_modify(items:list):
    for i in range(len(items)):
        if items[i] % 2 == 0:
            items[i] = items[i] * 2
        else:
            items[i] = items[i] * items[i]
    

def more_than_two_unique_vowels(sentence):
    ans = set()
    vowels = "aeiou"
    for word in sentence.split(","):
        s = set()
        for ch in word.lower():
            if ch in vowels:
                s.add(ch)
        if len(s) > 2:
            ans.add(word)
    return ans        

def sum_of_list_of_lists(lol):
    total = 0
    for row in lol:
        total += sum(row)
    return total    

def flatten(lol):
    ans = []
    for row in lol:
        ans.extend(row)
    return ans    

def all_common(strings):
    common = set(strings[0])
    for s in strings[1:]:
        common = common & set(s)
    return "".join(sorted(common))
    

def vocabulary(sentences):
    words = set()
    for sentence in sentences:
        for word in sentence.lower().split():
            words.add(word)
    return words        
