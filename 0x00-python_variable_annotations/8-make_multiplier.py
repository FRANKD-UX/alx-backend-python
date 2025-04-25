#!/usr/bin/env python3
"""
Module for make_multiplier function with type annotations
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by multiplier

    Args:
        multiplier: Factor to multiply by

    Returns:
        Function that takes a float and returns multiplier * float
    """
    def multiply(x: float) -> float:
        return multiplier * x
    return multiply
