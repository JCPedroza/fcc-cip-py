is_even= lambda num: num % 2 == 0

next_fibo = lambda num_list: sum(num_list[-2:])

append_next_fibo = lambda num_list: num_list.append(next_fibo(num_list))

def fibo_range(limit):
    fibo_nums = [1, 2]
    while next_fibo(fibo_nums) <= limit: append_next_fibo(fibo_nums)
    return fibo_nums

fibo_even_sum = lambda limit: sum(filter(is_even, fibo_range(limit)))
