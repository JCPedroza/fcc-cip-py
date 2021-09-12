from functools import reduce
from math import sqrt

is_factor = lambda num, div: num % div == 0

is_early_factor = lambda num: is_factor(num, 2) or is_factor(num, 3)

def is_pivot_factor(num, div):
    return is_factor(num, div) or is_factor(num, div + 2)

def is_prime(num):
    if num < 4: return num in (2, 3)
    if is_early_factor(num): return False

    limit = int(sqrt(num)) + 1
    for div in range(5, limit, 6):
        if is_pivot_factor(num, div): return False

    return True

def factors(num):
    div_range = range(1, int(sqrt(num)) + 1)
    generator = ([div, num//div] for div in div_range if is_factor(num, div))
    factor_list = reduce(list.__add__, generator)
    return set(factor_list)

prime_factors = lambda num: filter(is_prime, factors(num))

largest_prime_factor = lambda num: max(prime_factors(num))
