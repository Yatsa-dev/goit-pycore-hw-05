from typing import Callable, Generator
import sys
from collections import Counter

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

# .........................................................
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

# .......................................................
# task - 3
def parseLogs(line: str) -> dict:
    parts = line.split(' ', 3)
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3].strip()
    }

def openFile(path: str) -> list:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return [parseLogs(line) for line in file]
        
    except FileNotFoundError:
        print(f"Помилка: Файл '{path}' не знайдено.")
        return []
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return []

def filterByLevel(logs: list, level: str) -> list:
    return list(filter(lambda log: log['level'].lower() == level.lower(), logs))

def countLogs(logs: list) -> dict:
    levels = [log['level'] for log in logs]
    return Counter(levels)

def resultLogs(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<17}| {count}")

def main():
    if len(sys.argv) < 2:
        print("Використання: python main.py /шлях/до/logfile.log [рівень_логування]")
        sys.exit(1)

    path = sys.argv[1]
    logs = openFile(path)

    if not logs:
        sys.exit(1)

    logCounts = countLogs(logs)
    resultLogs(logCounts)

    if len(sys.argv) > 2:
        level = sys.argv[2]
        filteredLogs = filterByLevel(logs, level)
        
        print(f"\nДеталі логів для рівня '{level.upper()}':")
        if not filteredLogs:
            print("Записи цього рівня не знайдені.")
        else:
            for log in filteredLogs:
                print(f"{log['date']} {log['time']} - {log['message']}")

if __name__ == "__main__":
    main()