def square_root(n, accuracy):
    if n < 0:
        raise ValueError("Cannot calculate the square root of a negative number")

    if n == 0:
        return 0.0  # Special case for sqrt(0)

    epsilon = 10 ** (-accuracy)

    b = n / 2  # Start with an initial guess for the square root
    a = n / b

    while abs(b - a) > epsilon:
        b = (b + a) / 2
        a = n / b

    return round(b, accuracy)
