#!/usr/bin/env python3
"""
This module measures the runtime of asynchronous comprehensions.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the runtime of asynchronous comprehensions executed concurrently.

    This function creates four asynchronous tasks, each executing the
    'async_comprehension' function concurrently.
    It then waits for all tasks to complete using 'asyncio.gather()'
    and calculates the total runtime.

    Returns:
        float: The total runtime in seconds.
    """
    start = time.time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end = time.time()
    return (end - start)
