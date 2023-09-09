#!/usr/bin/env python3
"""
script
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Asynchronous comprehension that generates a list of 10 random floats.
    return: list of 10 random numbers"""
    numbers = [num async for num in async_generator()]
    return numbers
