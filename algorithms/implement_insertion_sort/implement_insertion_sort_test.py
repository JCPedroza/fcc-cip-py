from implement_insertion_sort import insertion_sort as isort


def test_empty_list():
    assert isort([]) == []


def test_one_item():
    assert isort([0]) == [0]


def test_small_sort_():
    assert isort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
