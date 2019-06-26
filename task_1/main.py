def fibonacci(n):
    if n < 3:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

for n in range(1, 16 + 1):
    print('%i,' %fibonacci(n), end=' ')
    ui = fibonacci(n)

print('new line')

def fibonacci_2(fn):
    if fn < 3:
        return 1
    else:
        return fibonacci_2(fn - 1) + fibonacci_2(fn - 2) + fibonacci_2(fn - 2)
for fn in range(1, 16 + 1):
    print('%i,' %fibonacci_2(fn), end=' ')
