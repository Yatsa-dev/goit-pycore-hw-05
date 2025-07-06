from typing import Callable, Generator

# task - 1
def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        
        if n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        
        return cache[n]

    return fibonacci

fib = caching_fibonacci()

print(f"Fibonacci(10): {fib(10)}")  
print(f"Fibonacci(15): {fib(15)}")  
print(f"Fibonacci(10): {fib(10)}")

# ////////////////////////////////////////////////////////////////////////////////////////////
# task - 2
def generator_numbers(text: str) -> Generator[float, None, None]:
    words = text.split(' ')
    
    for word in words:
        try:
            number = float(word)
            yield number
        except ValueError:
            continue

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    numbers_generator = func(text)
    total = sum(numbers_generator)
    
    return total

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)

print(f"Загальний дохід: {total_income}")