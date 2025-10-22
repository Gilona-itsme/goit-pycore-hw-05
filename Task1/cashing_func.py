"Реалізуйте функцію caching_fibonacci, яка створює та використовує кеш для зберігання і повторного використання вже обчислених значень чисел Фібоначчі."


# def caching_fibonacci():
#     cache = {}

#     def fibonacci(n):
#         # Перевірка коректності аргументу
#         if not isinstance(n, int):
#             return TypeError("The argument must be an integer.")
#         if n < 0:
#             return ValueError("The argument must be a non-negative number.")
#         # Якщо значення вже є в кеші
#         if n in cache:
#             return cache[n]
#         # Обчислення числа Фібоначчі
#         if n in (0, 1):
#             return n
#         # Рекурсивне обчислення з кешуванням
#         else:
#             cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
#             return cache[n]

#     return fibonacci
# fib = caching_fibonacci()


from functools import cache

@cache
def caching_fibonacci(n):
    if not isinstance(n, int):
        return  TypeError("The argument must be an integer.")
    if n < 0:
        return ValueError("The argument must be a non-negative number.")
    if n in (0, 1):
        return n
    return caching_fibonacci(n - 1) + caching_fibonacci(n - 2)


# Отримуємо функцію fibonacci
fib = caching_fibonacci

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  
print(fib(15)) 
print(fib(0))  
print(fib(1.5))
print(fib(-5))
print(fib("20"))  


             