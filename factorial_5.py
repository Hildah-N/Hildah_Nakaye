factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)
result = factorial(5)
print(f"Factorial of 5 is {result}")