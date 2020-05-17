def fibo(start, stop=None, step=1):
    def generate_fibo():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    fibo_generator = generate_fibo()
    for _ in range(start):
        next(fibo_generator)
    if stop is None:
        return next(fibo_generator)

    res = []
    for i in range(stop-start):
        n = next(fibo_generator)
        if i % step == 0:
            res.append(n)
    return res


print(fibo(10))
print(fibo(5, 16, 5))
print(fibo(10000))
