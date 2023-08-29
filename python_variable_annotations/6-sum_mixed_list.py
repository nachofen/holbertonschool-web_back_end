#!/usr/bin/env python3
"""script"""
from typing import List, Union


def sum_mixed_list(input_list: List[Union[int, float]]) -> float:
    """calculate the sum of a list of floats or ints
    Args:
        input_list: list of floats or ints to be summed
    Returns:
        float: the sum of the input list
    """
    return sum(input_list)
