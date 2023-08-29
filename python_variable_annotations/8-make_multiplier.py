#!/usr/bin/env python3
"""script"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        A function that takes a float and returns the result of multiplication.
    """
    def multiplier_function(x: float) -> float:
        """makes the multiplier

        Args:
            x (float): the float

        Returns:
            the result of x * multiplier
        """
        return x * multiplier

    return multiplier_function
