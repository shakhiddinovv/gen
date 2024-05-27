def fibonacci(n: int):
    index = 0
    a, b = 0, 1
    while index < n:
        yield a
        index += 1
        a, b = b, a + b
fibo = fibonacci(25)
for i in fibo:
    print(i)

def square(n: int):
    