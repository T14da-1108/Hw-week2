from .uniqueness import union, diff, sym_diff


def test_union() -> None:
    assert union([1, 2, 3], [2, 3, 4]) == {1, 2, 3, 4}
    assert union([], [1, 2, 3]) == {1, 2, 3}
    assert union([1, 2, 3], []) == {1, 2, 3}
    assert union([], []) == set()
    assert union([1, 1, 2], [2, 3, 4]) == {1, 2, 3, 4}


def test_diff() -> None:
    assert diff([1, 2, 3], [2, 3, 4]) == {1}
    assert diff([1, 2, 3], []) == {1, 2, 3}
    assert diff([], [2, 3, 4]) == set()
    assert diff([], []) == set()
    assert diff([1, 1, 2], [2, 3]) == {1}


def test_sym_diff() -> None:
    assert sym_diff([1, 2, 3], [2, 3, 4]) == {1, 4}
    assert sym_diff([1, 2, 3], []) == {1, 2, 3}
    assert sym_diff([], [2, 3, 4]) == {2, 3, 4}
    assert sym_diff([], []) == set()
    assert sym_diff([1, 1, 2], [2, 3]) == {1, 3}
