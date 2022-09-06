'''
Multiples of 3 or 5
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''


def number_multiples(number_1, number_2, number_range):
    """Takes two integers finds their multiples
       Takes an upper bound and returns the sum of the 
       multiples below the upper bound 

    Args:
        number_1 (interer): Whole number
        number_2 (integer): Whole number
        number_range (integer): Whole number

    Returns:
        : Whole number
    """
    divisor = []
    subtractor = []
    for n in range(number_range):
        x = n % number_1
        if x == 0:
            divisor.append(n)

    for n1 in range(number_range):
        y = n1 % number_2
        if y == 0:
            divisor.append(n1)
    for n3 in range(number_range):
        z = n3 % (number_1*number_2)
        if z == 0:
            subtractor.append(n3)

    return sum(divisor) - sum(subtractor)


# Test on established problem
print('The sum of all the multiples of 3 or 5 below 10 is:',
      number_multiples(5, 3, 10))

# Challenge question:
print('The sum of all the multiples of 3 or 5 below 1000 is:',
      number_multiples(5, 3, 1000))
