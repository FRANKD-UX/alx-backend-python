#!/usr/bin/env python3
"""
Module that measures runtime for parallel async comprehensions.
"""
import asyncio
import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four times in parallel.
    
    Uses asyncio.gather to run four async_comprehension coroutines
    concurrently and measures the total runtime.
    
    Returns:
        Total runtime in seconds.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    
    return end_time - start_time
