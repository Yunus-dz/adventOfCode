def largest_product(series, size):
            # span of numbers is longer than number series
    if size > len(str(series)):
        raise ValueError("span must be smaller than string length")
    if int(size) < 0:
        # span of number is zero or negative
        raise ValueError("span must be greater than zero")
    # series includes non-number input
    for item in series:
        if item.isdigit():
            continue
        else:
            raise ValueError("digits input must only contain digits")

    largest = 0
    for i in range(len(series) - size + 1):
        elements = series[i:i + size]
        product = 1
        for element in elements:
            product = product * int(element)
        if product > largest:
            largest = product
    return largest
