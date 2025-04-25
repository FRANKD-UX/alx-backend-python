#!/usr/bin/env python3
"""
Module for to_kv function with type annotations
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with a string and the square of a number

    Args:
        k: String to use as first element of tuple
        v: Integer or float to square for second element

    Returns:
        Tuple where first element is k and second is v squared as a float
    """
    return (k, float(v ** 2))
