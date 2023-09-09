#!/usr/bin/env python3
"""Task0"""

def index_range(page:int, page_size:int):
    starting_index = (page -1) * page_size
    ending_index = starting_index + page_size
    result = (starting_index, ending_index)
    return result

