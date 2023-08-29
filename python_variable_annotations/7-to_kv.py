#!/usr/bin/env python3
"""script"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takes a string and an int or float and returns a tuple

    Args:
        k (str): the string
        v: the int or float

    Return:
        Tuple containg the string k and the square of v
    """
    return k, v * v
