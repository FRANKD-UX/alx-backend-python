#!/usr/bin/env python3
"""
Module that contains async_comprehension function.
"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using async comprehension.
    
    Uses async comprehension over async_generator to collect 10 random numbers.
    
    Returns:
        List of 10 random float values.
    """
    return [value async for value in async_generator()]
