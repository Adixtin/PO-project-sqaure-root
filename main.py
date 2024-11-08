def get_input():
    n = float(input("Enter the number to find the square root of: "))
    accuracy = int(input("Enter the desired decimal accuracy: "))
    return n, accuracy

def calculate_square_root(n, accuracy):
    if n < 0:
        raise ValueError("Cannot calculate the square root of a negative number")
    if n == 0:
        return 0.0

    epsilon = 10 ** (-accuracy)
    b = n / 2
    a = n / b

    while abs(b - a) > epsilon:
        b = (b + a) / 2
        a = n / b

    return round(b, accuracy)

def display_output(result):
    print(f"The square root is approximately: {result}")

if __name__ == "__main__":
    n, accuracy = get_input()
    result = calculate_square_root(n, accuracy)
    display_output(result)