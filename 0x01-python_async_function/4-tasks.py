#!/usr/bin/env python3
"""Module for using asyncio Tasks.

This module defines a function that spawns task_wait_random n times with
the specified max_delay and returns the list of all delays.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn task_wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn task_wait_random.
        max_delay (int): Maximum delay in seconds.

    Returns:
        List[float]: List of all delays in ascending order.
    """
    # Create a list of tasks
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    
    # Wait for all tasks to complete
    results = await asyncio.gather(*tasks)
    
    # Return the results in ascending order
    return sorted(results)
