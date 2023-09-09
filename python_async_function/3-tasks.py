#!/usr/bin/env python3
"""
run script
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    This function creates and returns an asyncio.Task that runs
    wait_random(max_delay).

    Args:
        max_delay (int): The maximum delay for the wait_random coroutine.

    Returns:
        asyncio.Task: A Task that runs the wait_random coroutine.
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
