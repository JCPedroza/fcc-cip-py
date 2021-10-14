from implement_selection_sort import selection_sort as ssort


def test_empty_list():
    assert ssort([]) == []


def test_one_item():
    assert ssort([0]) == [0]


def test_small_sort():
    assert ssort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
