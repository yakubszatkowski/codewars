def digital_root(n):
    """
    Given n, take the sum of the digits of n. If that value has more than one digit,
    continue reducing in this way until a single-digit number is produced. The input will be a
    non-negative integer.

    Example: 942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
    """
    numbers = str(n)
    while len(numbers) > 1:
        summ = 0
        for number in numbers:
            summ += int(number)
        numbers = str(summ)
    print(numbers)

digital_root(493193)

"""
Different interesting solution that I've found on codewars:

n = str(n)
while len(n) != 1:
    res = sum(int(digit) for digit in n)
    n = str(res)
return int(res)
"""