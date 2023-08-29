#!/usr/bin/env python3
"""script"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Annotate the below functions parameters and return values
    with the appropriate types

    Args:
        lst (List of strings): list of strings.

    Returns:
        A list of tuples
    """
    return [(i, len(i)) for i in lst]
