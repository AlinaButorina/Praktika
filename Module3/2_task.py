fibonacci = lambda n: None if n < 2 else [0, 1] if n == 2 else fibonacci(n - 1) + [fibonacci(n - 1)[-1] + fibonacci(n - 1)[-2]]
n = 1
result = fibonacci(n)
print(result)
