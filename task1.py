def caching_fibonacci ():
    cache = {0: 'invalid value', 1: 0, 2: 1}
    def inner (n):
        if n not in cache:
            prev, curr = 0, 1
            for _ in range(3, n + 1):
                prev, curr = curr, prev + curr
            cache[n] = curr
            return cache[n]
        else:
            print('cache used')
            return cache[n]
    return inner

fib = caching_fibonacci()
print(fib(10))