from implement_bubble_sort import bubble_sort as bs
from implement_bubble_sort_flag import bubble_sort as bsf
from implement_bubble_sort_flag_while import bubble_sort as bsfw


def test_mini_sort():
    assert bs([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert bsf([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert bsfw([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
