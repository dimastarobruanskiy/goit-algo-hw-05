def caching_fibonacci():
    cache = {}
    
    def fibonacci(n):
         # базові випадки рекурсії
        if n <= 0:
            return 0
        if n == 1:
            return 1
         # перевіряємо, чи вже є значення в кеші
        if n in cache:
            return cache[n]
         # рекурсивне обчислення значення
        result = fibonacci(n - 1) + fibonacci(n - 2)
         # зберігаємо результат у кеші
        cache[n] = result
        return result
    # повертаємо внутрішню функцію (замикання)
    return fibonacci

fib = caching_fibonacci()


print(fib(10))
print(fib(15)) 