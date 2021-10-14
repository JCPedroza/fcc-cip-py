from implement_bubble_sort import bubble_sort as bs
from implement_bubble_sort_flag import bubble_sort as bsf
from implement_bubble_sort_flag_while import bubble_sort as bsfw


def test_empty_list():
    assert bs([]) == []
    assert bsf([]) == []
    assert bsfw([]) == []


def test_one_item():
    assert bs([0]) == [0]
    assert bs([0]) == [0]
    assert bs([0]) == [0]


def test_five_items():
    assert bs([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert bsf([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert bsfw([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
