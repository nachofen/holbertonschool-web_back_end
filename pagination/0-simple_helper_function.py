#!/usr/bin/env python3
"""Task0"""


def index_range(page: int, page_size: int):
    """ return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters."""
    starting_index = (page - 1) * page_size
    ending_index = starting_index + page_size
    result = (starting_index, ending_index)
    return result
