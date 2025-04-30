#!/usr/bin/env python3
"""Module for creating asyncio Tasks.

This module defines a function that takes an integer max_delay and
returns an asyncio.Task.
"""

import asyncio
from typing import Any

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create an asyncio.Task for wait_random.

    Args:
        max_delay (int): Maximum delay in seconds.

    Returns:
        asyncio.Task: Task for wait_random with the specified max_delay.
    """
    # Create and return a Task
    return asyncio.create_task(wait_random(max_delay))
