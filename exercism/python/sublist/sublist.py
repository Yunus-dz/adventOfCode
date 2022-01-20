"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST, SUPERLIST, EQUAL, UNEQUAL = range(4)


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL

    if len(list_one) == 0 or len(list_one) < len(list_two) and is_sublist(list_two, list_one):
        return SUBLIST

    if len(list_two) == 0 or len(list_one) > len(list_two) and is_sublist(list_one, list_two):
        return SUPERLIST
    return UNEQUAL


def is_sublist(big_list, little_list):
    frames = [
        big_list[i:i + len(little_list)]
        for i in range(len(big_list) - len(little_list) + 1)
    ]
    return little_list in frames


