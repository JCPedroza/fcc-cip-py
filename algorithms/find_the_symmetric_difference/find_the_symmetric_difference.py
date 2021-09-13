from functools import reduce

sym = lambda *args: reduce(lambda acc, cur: acc ^ cur, args)
