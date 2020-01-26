def fibonacci(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a+b


print(list(fibonacci(10)))