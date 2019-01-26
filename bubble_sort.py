""" Bubble Sort Sorting Algorithm implementation. """
import logging
import config

LOGGER = config.get_logger(__name__)


def buble_sort(list_to_sort):
    """
    Function that takes as an imput a number list 
    and returns it sorted.
    """
    LOGGER.debug(f'Unsorted list: {list_to_sort}')
    unsorted = True
    while unsorted:
        unsorted = False
        for index, num in enumerate(list_to_sort):
            try:
                if num > list_to_sort[index + 1]:
                    unsorted = True
                    list_to_sort[index] = list_to_sort[index + 1]
                    list_to_sort[index + 1] = num
                    LOGGER.debug(
                        f'Smaller {list_to_sort[index]} {list_to_sort[index + 1]}')
            except IndexError:
                continue
            except AttributeError:
                LOGGER.debug(f'List of numbers is not correct.')
                exit()
    LOGGER.debug(f'Sorted list:  {list_to_sort}')
    return list_to_sort


if __name__ == '__main__':
    buble_sort([2, 30, 1, 10])
