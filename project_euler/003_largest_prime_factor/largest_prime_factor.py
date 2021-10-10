from functools import reduce
from math import sqrt


def is_factor(num: int, div: int) -> bool:
    return num % div == 0


def is_early_factor(num: int) -> bool:
    return is_factor(num, 2) or is_factor(num, 3)


def is_pivot_factor(num: int, div: int) -> bool:
    return is_factor(num, div) or is_factor(num, div + 2)


def is_prime(num: int) -> bool:
    if num < 4:
        return num in (2, 3)
    if is_early_factor(num):
        return False

    limit = int(sqrt(num)) + 1
    for div in range(5, limit, 6):
        if is_pivot_factor(num, div):
            return False

    return True


def factors(num: int) -> set[int]:
    div_range = range(1, int(sqrt(num)) + 1)
    generator = ([div, num//div] for div in div_range if is_factor(num, div))
    factor_list = reduce(list.__add__, generator)
    return set(factor_list)


def prime_factors(num: int) -> set[int]:
    return filter(is_prime, factors(num))


def largest_prime_factor(num):
    return max(prime_factors(num))
