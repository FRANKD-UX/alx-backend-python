#!/usr/bin/env python3
"""
Module for safe_first_element function with type annotations
"""
from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely return the first element of a sequence or None

    Args:
        lst: A sequence of elements

    Returns:
        The first element of lst or None if lst is empty
    """
    if lst:
        return lst[0]
    else:
        return None
