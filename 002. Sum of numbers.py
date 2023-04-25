def get_sum(a,b):
    """
    Given two integers a and b, which can be positive or negative, find the sum of all the
    integers between and including them and return it. If the two numbers are equal return a or b.
    """
    summ = 0
    if a <= b:
        for number in range(a, b+1):
            summ += number
    else:
        for number in range(b, a+1):
            summ += number
    print(summ)


get_sum(0, -1)
