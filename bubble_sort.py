""" Bubble Sort Sorting Algorithm implementation. """
# Python libs.
import logging
import sys
# Project Files.
import config
# Instantiate logger object.
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
    buble_sort(list_to_sort)
