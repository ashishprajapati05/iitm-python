# Accept a string of lowercase letters from the user and encrypt it using the following image:



# Each letter in the string that appears in the the upper half should be replaced with the corresponding letter in the lower half and vice versa. Print the encrypted string as output.

s = input()
a = "abcdefghijklmnopqrstuvwxyz"

for x in s:
    print(a[25 - a.index(x)], end="")