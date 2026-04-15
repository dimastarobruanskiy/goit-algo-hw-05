import re
from typing import Callable

#генератор який знаходить усі дійсні числа   
def generate_numbers(text: str):
    numbers = re.findall(r"\d+\.\d+", text)
    for num in numbers:
        yield float(num)

#Повертає суму чисел з тексту
def sum_profit(text: str, func:Callable):
    total = 0
    for number in func(text):
        total += number
    return total

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income=sum_profit(text, generate_numbers)
print(f"Загальний дохід: {total_income:.2f}.")