#!/usr/bin/env python3
"""
Module with zoom_array function corrected for mypy
"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Repeat each element of a tuple a specified number of times

    Args:
        lst: Tuple of elements
        factor: Number of times to repeat each element

    Returns:
        List with each element of lst repeated factor times
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), 3)
