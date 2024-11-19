from operator import index


def get_squares(elements: list[int]) -> list[int]:
    """
    :param elements: list with integer values
    :return: list with squared values
    Use ** operator here (https://docs.python.org/3/reference/expressions.html#the-power-operator)
    """
    return [x ** 2 for x in elements]

# ====================================================================================================


def get_indices_from_one(elements: list[int]) -> list[int]:
    """
    :param elements: list with integer values
    :return: list with indices started from 1
    """
    return [i + 1 for i, in enumerate(elements)]

# ====================================================================================================


def get_max_element_index(elements: list[int]) -> int | None:
    """
    :param elements: list with integer values
    :return: index of maximum element if exists, None otherwise
    """
    return elements.index(max(elements)) if elements else None

# ====================================================================================================


def get_every_second_element(elements: list[int]) -> list[int]:
    """
    :param elements: list with integer values
    :return: list with each second element of list
    """
    return elements[1::2]

# ====================================================================================================


def get_first_three_index(elements: list[int]) -> int | None:
    """
    :param elements: list with integer values
    :return: index of first "3" in the list if exists, None otherwise
    """
    return elements.index(3) if 3 in elements else None

# ====================================================================================================


def get_last_three_index(elements: list[int]) -> int | None:
    """
    :param elements: list with integer values
    :return: index of last "3" in the list if exists, None otherwise
    """
    return len(elements) - 1 - elements[::-1]. index(3) if 3 in elements else None

# ====================================================================================================


def get_sum(elements: list[int]) -> int:
    """
    :param elements: list with integer values
    :return: sum of elements
    Use sum function here (https://docs.python.org/3/library/functions.html#sum)
    """
    return sum(elements)

# ====================================================================================================


def get_min_max(elements: list[int], default: int | None) -> tuple[int | None, int | None]:
    """
    :param elements: list with integer values
    :param default: default value to return if elements are empty
    :return: (min, max) of list elements or (default, default) if elements are empty
    Use max/min functions here (https://docs.python.org/3/library/functions.html#max)
    """
    if elements:
        return (min(elements)), max(elements)
    return default, default

# ====================================================================================================


def get_by_index(elements: list[int], i: int, boundary: int) -> int | None:
    """
    :param elements: list with integer values
    :param i: index of elements to check with
    :param boundary: boundary for check element value
    :return: element at index `i` from `elements` if element greater, then boundary and None otherwise
    """
    if i < len(elements):
        if elements[i] > boundary:
            return elements[i]
    return None
