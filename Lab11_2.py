def fib(n):
    a, b = 1, 1
    with open('fib.txt', 'w') as txt:
        for i in range(n):
            yield a
            a, b = b, a + b
            txt.write(str(a) + '\n')
for num in fib(200):
    print(num)