import typing as tp


def union(list1: tp.List[int], list2: tp.List[int]) -> set[int]:
    """
    Returns the union of two lists as a set.

    :param list1: The first list of integers.
    :param list2: The second list of integers.
    :return: A set containing all unique elements from both lists.
    """


def diff(list1: tp.List[int], list2: tp.List[int]) -> set[int]:
    """
    Returns the difference between two lists as a set
    (elements in list1 but not in list2).

    :param list1: The first list of integers.
    :param list2: The second list of integers.
    :return: A set containing elements that are in list1 but not in list2.
    """


def sym_diff(list1: tp.List[int], list2: tp.List[int]) -> set[int]:
    """
    Returns the symmetric difference between two lists as a set
    (elements in either list1 or list2 but not both).

    :param list1: The first list of integers.
    :param list2: The second list of integers.
    :return: A set containing elements that are in one list but not both.
    """
