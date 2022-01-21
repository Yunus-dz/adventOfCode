def steps(number):
    if number <= 0:
        raise ValueError("Only positive numbers are allowed")
    count_steps = 0
    while number != 1:
        # Proceso de numero par
        if number % 2 == 0:
            number = number / 2
            count_steps += 1
        else:
            number = (3*number) + 1
            count_steps += 1
    return count_steps
