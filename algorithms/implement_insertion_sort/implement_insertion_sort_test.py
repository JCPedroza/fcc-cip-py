from implement_insertion_sort import insertion_sort


def test_small_sort_():
    assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
