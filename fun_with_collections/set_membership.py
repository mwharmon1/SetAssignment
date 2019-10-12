"""
Author: Michael Harmon
Date: 10/11/2019
Description: This program will check to see if an element
is in a set.
"""


def in_set(my_set, my_value):
    """
    check for element in set
    :param my_set: set to search
    :param my_value: element to find in set
    :return: true for found, false for not found
    """
    if my_value in my_set:
        return True
    return False


if __name__ == '__main__':
    this_value = 2
    this_set = {1, 2, 3, 4}
    print(in_set(this_set, this_value))
