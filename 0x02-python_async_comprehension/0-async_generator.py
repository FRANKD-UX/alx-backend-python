#!/usr/bin/env python3
"""
Module that contains an asynchronous generator function.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine that yields 10 random numbers.
    
    The coroutine loops 10 times, each time asynchronously waiting for 1 second
    and then yielding a random float between 0 and 10.
    
    Returns:
        Generator that yields random float values between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
