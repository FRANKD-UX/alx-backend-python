#!/usr/bin/env python3
"""
Module for safely_get_value function with type annotations
"""
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely get a value from a dictionary

    Args:
        dct: A mapping/dictionary
        key: Key to look up in dct
        default: Value to return if key not in dct

    Returns:
        Value in dct[key] if key exists, otherwise default
    """
    if key in dct:
        return dct[key]
    else:
        return default
