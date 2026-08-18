# Solve all the below tasks related to string concatenation, repeatition and substring check in strings.

# Problem Type: Input variable - Output Variable, Hidden suffix for evaluation

# Instructions on how to solve (Click to expand)
# NOTE: In this type of questions you should not take input or print anything unless your are explicitly asked to. Assign the result of the required computation to the correct variable name as it will be evaluated for type and value by the evaluator.

# The input variables will be assigned by the evaluator based on the test cases.

# The grey part before the white part (if any) in the code is the prefix code. The grey part after the white part (if any) is the suffix code which are not editable. Usually they will be the part of code but in this type of questions it will be removed by the evaluator.

# The Three dots (...) called as Ellipsis in python are like placeholders, replace them with your answer.

# The inputs on the code blocks are just sample inputs they won't be evaluated in the actual testcases.

# Each testcase will have its own set of testcases defined as variables. The check function in the testcases is in the hidden evaluation code that checks the value and type of the variable.

# ans
# Sample inputs (# note: The values given in the prefix code(grey) will be changed by the autograder according to the testcase while running them.
word1 = "Wingardium" # str
word2 = "Leviyosa" # str
word3 = "Silver" # str
sentence = "Learning python is fun"
n1 = 6 # int
n2 = 4 # int
# <eoi>

output1 = word1 + " " + word2 # str: join word1 and word2 with space in between

output2 = word1[:4] + "-" + word2[-4:]  # str: join first four letters of word1 and last four letters of word 2 with a hyphen "-" in between

output3 =  word3 + " " + str(n1) # str: join the word3 and n1 with a space in between

output4 = "-" * 50 # str: just the hypen "-" repeated 50 times

output5 = "-" * n2 # str: just the hypen "-" repeated n2 times

output6 =str(n1) * n2 # str: repeat the number n1, n2 times

are_all_words_equal = word1 == word2 and word2 == word3 # bool: True if all three words are equal

is_word1_comes_before_other_two = word1 < word2 and word1 < word3  # bool: True if word1 comes before word2 and word3 assume all words are different

has_h = "h" in word1.lower()  # bool: True if word1 has the letter h

ends_with_a =word1.endswith(("a", "A"))   # bool: True if word1 ends with letter a or A

has_the_word_python = "python" in sentence.lower().split()  # bool: True if the sentence has the word python
