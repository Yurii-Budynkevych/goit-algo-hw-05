from typing import Callable
import re

STRING = 'Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, \
доповнений додатковими надходженнями 27.45 і 324.00 доларів.'

pattern = r'\b\d+[.,]?\d*\b'

def generator_numbers(text: str):
    numbers = re.findall(pattern, text)
    numbers = [float(num) for num in numbers]
    for number in numbers:
        yield number

def sum_profit(text: str, func: Callable):
    sum = 0
    for i in func(text):
        sum += i
    return sum

total_income = sum_profit(STRING, generator_numbers)
print(f"Загальний дохід: {total_income}")    