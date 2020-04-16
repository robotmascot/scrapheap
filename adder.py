#!/usr/bin/python3
import sys

'''Adds contents of lists together.'''


def add(*lists):
    '''Given any same-length lists-of-lists of numbers
    returns a single list-of-list with each
    of the corresponding numbers in the
    given list-of-lists added together.'''
    # tests length
    test_length = [len(r) for r in lists[0]]
    for tested in lists:
        if [len(r) for r in tested] != test_length:
            raise ValueError('Lists are not the same length!')
    new_list = [
        [sum(values) for values in zip(*rows)]
        for rows in zip(*lists)
    ]
    return new_list


def main():
    args = sys.argv[1:]
    if not args:
        print('usage: list_of_lists, list_of_lists, [list_of_lists, ...]')
    else:
        add(args[1], args[2])


if __name__ == "__main__":
    main()
