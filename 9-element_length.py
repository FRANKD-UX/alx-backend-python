#!/usr/bin/env python3
"""
Module for element_length function with type annotations
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples where each tuple contains
    an element from lst and its length

    Args:
        lst: Iterable of sequences

    Returns:
        List of tuples (sequence, length)
    """
    return [(i, len(i)) for i in lst]
