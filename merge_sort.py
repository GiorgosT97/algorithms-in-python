""" Merge Sort Sorting Algorithm implementation. """
# Python libs.
import logging
import sys
# Project Files.
import config
# Instantiate logger object.
LOGGER = config.get_logger(__name__)


def merge_sort(list_to_sort):
    """
    Function takes as input list to sort and retunrs it
    sorted with merge sort algorithm.
    """
    LOGGER.debug(f'Initial unsorted list: {list_to_sort}')

    LOGGER.debug(f'Sorted list: {list_to_sort}')
    return list_to_sort


def split_list_in_half(list_to_split):
    """
    Function taking a list as input and splits it in half,
    returning the 2 new lists.
    """
    # Find the half len.
    half_len = len(list_to_split)//2
    # Return the lists.
    LOGGER.debug(
        f'Split list: {list_to_split} into: {list_to_split[:half_len]} and \
        {list_to_split[half_len:]}')

    return list_to_split[:half_len], list_to_split[half_len:]


def merge_sorted_list(first_list, second_list):
    """ Merge two 1element lists into one sorted. """
    if first_list[0] > second_list[0]:
        sorted_list = [first_list[0], second_list[0]]
    else:
        sorted_list = [second_list[0], first_list[0]]
    LOGGER.debug(
        f'Merge lists: {first_list} and {second_list} into {sorted_list}')

    return sorted_list


# Run merge sort with arguments.
if __name__ == '__main__':
    try:
        list_to_sort = sys.argv[1]
        try:
            list_to_sort = list(
                map(float, list_to_sort.strip('[]').split(',')))
        except ValueError:
            list_to_sort = [2, 30, 1, 10]
            LOGGER.debug(f"Assuming list is {list_to_sort}")
    except IndexError:
        list_to_sort = [2, 30, 1, 10]
        LOGGER.debug(f"Assuming list is {list_to_sort}")
    merge_sort(list_to_sort)
