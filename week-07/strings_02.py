# Given an even-length string s, check if the second half contains the character "a" or "A". Return True if it does, otherwise return False.

# Example

# s = "abcDef"



def has_a_in_second_half(s: str) -> bool:
    '''
    Given an even-length string, check if the second half contains 
    the character "a" or "A".

    Arguments:
    s: str - an even-length string.

    Return: bool - True if "a" or "A" is found in the second half, else False.
    '''
    
    second_half = s[len(s) // 2:]
    return 'a' in second_half or 'A' in second_half

