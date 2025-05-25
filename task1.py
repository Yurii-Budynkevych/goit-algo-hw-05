def caching_fibonacci():
    cache = {0: 0, 1: 1, 2: 1}

    def inner(n):
        if n in cache:
            print("cache used")
            return cache[n]
        # Recursion
        cache[n] = inner(n - 1) + inner(n - 2)
        return cache[n]

    return inner

fib = caching_fibonacci()
print(fib(4))