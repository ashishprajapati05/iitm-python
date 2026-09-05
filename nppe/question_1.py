# Compare Last Digits
# Write a function compare_last_digits(num1, num2) that takes two integers as input and checks whether they have the same last digit. Return "same" if the last digits match, otherwise return "different".


def compare_last_digits(num1:int, num2:int) -> str:
    '''
    Given two integers, check whether their last digits are the same.

    Args:
        num1 (int): First number
        num2 (int): Second number

    Returns:
        str: "same" if last digits match else "different"
    '''
    return "same" if num1 % 10 == num2 % 10 else "different"
   