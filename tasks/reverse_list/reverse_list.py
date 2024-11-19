def reverse_iterative(lst: list[int]) -> list[int]:
    """
    Reverse the given list and return the reversed list using iteration.
    :param lst: The list to be reversed.
    :return: A new list that is the reverse of the input list.
    """
    reversed_list = []
    for i in range(len(lst) - 1, - 1, - 1):
        reversed_list.append(lst[i])
    return reversed_list


def reverse_inplace_iterative(lst: list[int]) -> None:
    """
    Reverse the given list in place using a two-pointer iterative approach.
    :param lst: The list to be reversed.
    """
    left = 0
    right = len(lst) - 1

    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1


def reverse_inplace(lst: list[int]) -> None:
    """
    Revert list inplace with reverse method
    :param lst: input list
    :return: None
    """
    left, right = 0, len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1


def reverse_reversed(lst: list[int]) -> list[int]:
    """
    Revert list with `reversed`
    :param lst: input list
    :return: reversed list
    """
    return list(reversed(lst))


def reverse_slice(lst: list[int]) -> list[int]:
    """
    Revert list with slicing
    :param lst: input list
    :return: reversed list
    """
    return lst[::-1]
