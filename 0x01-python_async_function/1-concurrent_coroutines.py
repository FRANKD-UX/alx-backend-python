#!/usr/bin/env python3
"""Module for concurrent coroutines.

This module defines a function that spawns wait_random n times with the
specified max_delay and returns the list of all delays.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay in seconds.

    Returns:
        List[float]: List of all delays in ascending order.
    """
    # Create a list of coroutines
    tasks = [wait_random(max_delay) for _ in range(n)]
    
    # Wait for all coroutines to complete
    results = await asyncio.gather(*tasks)
    
    # Return the results in ascending order
    return sorted(results)
