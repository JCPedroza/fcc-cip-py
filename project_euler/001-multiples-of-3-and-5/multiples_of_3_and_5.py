num_filter = lambda num: num % 3 == 0 or num % 5 == 0

multiples_of_3_and_5 = lambda limit: sum(filter(num_filter, range(1, limit)))
