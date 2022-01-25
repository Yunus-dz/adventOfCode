def classify(number):
    """ A perfect number equals the sum of its positive divisors.
 
    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    sum = 0
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    for value in range(1, (number // 2) + 1):
        if number % value == 0:
            sum += value
    if number == sum:
        return "perfect"
    elif number > sum:
        return "deficient"
    return "abundant"