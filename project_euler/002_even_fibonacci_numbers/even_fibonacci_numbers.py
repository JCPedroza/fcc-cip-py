def next_fibo(num_list: list[int]) -> int:
    return sum(num_list[-2:])


def fibo_range(limit: int) -> list[int]:
    fibo_nums = [1, 2]

    while next_fibo(fibo_nums) <= limit:
        fibo_nums.append(next_fibo(fibo_nums))

    return fibo_nums


def fibo_even_sum(limit: int) -> int:
    return sum(filter(lambda num: num % 2 == 0, fibo_range(limit)))
