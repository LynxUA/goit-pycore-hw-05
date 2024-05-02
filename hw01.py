'''
Caching fibonacci module
'''
def caching_fibonacci() -> callable:
    '''
    Recursive function that calculates Nth fibonacci number (with caching)
    '''
    cache = {}

    def fibonacci(n: int):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if cache.get(n) is not None:
            print(f"We already have a cache for the fibonacci number {n}")
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

def main():
    '''
    Main function
    '''
    fib = caching_fibonacci()
    print(fib(5))
    print(fib(7))
    print(fib(10))

if __name__ == "__main__":
    main()
