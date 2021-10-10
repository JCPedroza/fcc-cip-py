def num_filter(num: int) -> bool:
    return num % 3 == 0 or num % 5 == 0


def multiples_of_3_and_5(limit: int) -> int:
    return sum(filter(num_filter, range(1, limit)))
