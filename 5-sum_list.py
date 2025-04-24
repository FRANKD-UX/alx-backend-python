#!/usr/bin/env python3
"""
Module for sum_list function with type annotations
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sum up a list of floats

    Args:
        input_list: List of floating point numbers

    Returns:
        Sum of all elements as a float
    """
    return sum(input_list)
