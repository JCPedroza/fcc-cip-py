from implement_selection_sort import selection_sort


def test_small_sort():
    assert selection_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
