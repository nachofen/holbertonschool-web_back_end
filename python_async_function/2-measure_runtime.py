#!/usr/bin/env python3
"""
This module provides an asynchronous function for waiting on multiple
random delays.
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measures the total execution time for wait_n(n, max_delay)

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int, optional): The maximum delay for each wait_random call

    Returns:
        float: total_time / n
    """
    starting_time = time.time()
    execution = asyncio.run(wait_n(n, max_delay))
    ending_time = time.time()
    total_time = ending_time - starting_time
    return total_time / n
