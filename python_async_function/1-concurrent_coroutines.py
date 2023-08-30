#!/usr/bin/env python3
"""
This module provides an asynchronous function for waiting on multiple
random delays.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    An asynchronous coroutine that spawns wait_random n times with the
    specified max_delay

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int, optional): The maximum delay for each wait_random call

    Returns:
        list: A list of all the delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
