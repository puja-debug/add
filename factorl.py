def factorial_iterative(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Get user input
num = int(input("Enter a number to find its factorial: "))
print(f"Factorial of {num} (iterative): {factorial_iterative(num)}")
