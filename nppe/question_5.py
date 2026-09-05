# Reverse Vowel Order in a String
# Write a python program that reads a multiline string and reverses only the vowels in the string while keeping all other characters in their original positions.

# Input Format

# First line will have the number of lines (n) in the input
# Next n lines will have the multiline string
# Output Format The modified multiline string.



n = int(input())
s = "\n".join(input() for i in range(n))

vowels = "aeiou"
vowel_indices = [i for i in range(len(s)) if s[i].lower() in vowels]
s_list = list(s)
n = len(vowel_indices)//2
for i,j in zip(vowel_indices[:n] , vowel_indices[n:][::-1]):
    s_list[i],s_list[j] = s_list[j],s_list[i]

print("".join(s_list))

