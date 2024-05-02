'''
Text analyzation and profit calculation module
'''

from functools import reduce
import re
from typing import Callable, Generator


def generator_numbers(nums_text: str) -> Generator[float, None, None]:
    '''
    Analyzes text and extracts numbers
    '''
    pattern = r"(^| )(\d+(\.\d+)*)[ \.]"
    for num in re.findall(pattern, nums_text):
        yield float(num[1])

def sum_profit(nums_text: str, func: Callable):
    '''
    Sums profit
    '''
    return reduce((lambda x, y: x + y), func(nums_text))

def main():
    '''
    Main function
    '''
    nums_text = "Загальний дохід працівника складається з декількох частин: \
    1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(nums_text, generator_numbers)
    print(f"Загальний дохід: {total_income}")

if __name__ == "__main__":
    main()
