"""
Python has a built-in symmetric difference operator for sets, the
caret (^) operator.
"""

from functools import reduce


def sym(*args: set[float]) -> set[float]:
    return reduce(lambda acc, cur: acc ^ cur, args)
