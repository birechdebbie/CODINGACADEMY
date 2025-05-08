def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.
    
    :param n: Non-negative integer
    :return: Factorial of n
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
#number = 5

number = 7
print(f"The factorial of {number} is {factorial(number)}")

