#!/usr/bin/env python3
"""script"""
import asyncio
import random


async def async_generator():
    """
    An asynchronous generator that yields random numbers between 0 and 10.

    Yields:
        float: A random number between 0 and 10.

    This coroutine loops 10 times, each time asynchronously waiting 1 second
    before yielding a random number.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
